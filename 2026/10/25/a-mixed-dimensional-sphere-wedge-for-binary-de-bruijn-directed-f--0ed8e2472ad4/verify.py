#!/usr/bin/env python3
"""Standalone exact verification of directed-forest topology on the binary de Bruijn digraph.
Run as: python3 verify.py (from the directory containing certificate.json).
Uses only the Python standard library, exact integer and rational arithmetic.
"""
import collections
import itertools
import json
from fractions import Fraction
from pathlib import Path

WORDS = list(itertools.product((0, 1), repeat=3))
W2I = {w: i for i, w in enumerate(WORDS)}
ARCS = [(W2I[w], W2I[w[1:] + (b,)]) for w in WORDS for b in (0, 1)
        if w != w[1:] + (b,)]
M = len(ARCS)

def is_forest(s):
    parents = {}
    for i, (a, b) in enumerate(ARCS):
        if s & (1 << i):
            if b in parents:
                return False
            parents[b] = a
    for v in parents:
        cur, seen = v, set()
        while cur in parents:
            if cur in seen:
                return False
            seen.add(cur)
            cur = parents[cur]
    return True

def input_choice_faces():
    by_target = [[] for _ in WORDS]
    for i, (a, b) in enumerate(ARCS):
        by_target[b].append(i)
    masks = set()
    for selected in itertools.product(*[(None,) + tuple(opts) for opts in by_target]):
        mask = sum((1 << e for e in selected if e is not None), 0)
        if mask and is_forest(mask):
            masks.add(mask)
    return masks

def boundary(s, faces):
    bits = [i for i in range(M) if s & (1 << i)]
    return {s ^ (1 << i): (-1 if j & 1 else 1)
            for j, i in enumerate(bits) if s ^ (1 << i) in faces}

def sign_perm(values):
    return -1 if sum(values[i] > values[j]
                     for i in range(len(values))
                     for j in range(i+1, len(values))) % 2 else 1

faces = {x for x in range(1, 1 << M) if is_forest(x)}
assert len(WORDS) == 8 and M == 14
assert faces == input_choice_faces(), 'independent incoming-edge enumeration failed'
by_dim = {d: sorted(x for x in faces if x.bit_count() == d+1) for d in range(7)}
assert [len(by_dim[d]) for d in range(7)] == [14,84,280,560,672,448,128]
facets = [x for x in faces if not any((x | (1 << i)) in faces
                                     for i in range(M) if not x & (1 << i))]
assert collections.Counter(x.bit_count() for x in facets) == {7:128,6:4}

# Lexicographic pivot matching. Pair each still-unmatched nonempty face
# with the still-unmatched face obtained by adding the current arc.
paired = set()
pairs = []
for i in range(M):
    for x in sorted(faces):
        y = x | (1 << i)
        if not (x & (1 << i)) and x not in paired and y in faces and y not in paired:
            paired.update((x,y))
            pairs.append((x,y))
critical = sorted(faces - paired)
assert len(pairs) == 1091 and len(critical) == 4
assert [(hex(c),c.bit_count()-1) for c in critical] == [
  ('0x1',0),('0x2cd2',6),('0x32cc',6),('0x348a',5)]

# Recompute all certificate data, rather than trusting the recorded list.
cert = json.loads(Path(__file__).with_name('certificate.json').read_text(encoding='utf-8'))
assert cert['arcs_0_based'] == [list(a) for a in ARCS]
assert cert['face_masks'] == sorted(faces)
assert cert['matching_pairs'] == [list(z) for z in pairs]
assert cert['critical_masks'] == critical
assert cert['facet_masks'] == sorted(facets)

# Reverse matched Hasse edges and orient all other edges upward. The
# resulting finite directed graph is acyclic iff the Morse matching is acyclic.
pair_set = set(pairs)
out = collections.defaultdict(list)
indeg = {x:0 for x in faces}
incidences = 0
for up in faces:
    for i in range(M):
        if up & (1 << i):
            lo = up ^ (1 << i)
            if lo not in faces:
                continue
            src,dst = (up,lo) if (lo,up) in pair_set else (lo,up)
            out[src].append(dst)
            indeg[dst] += 1
            incidences += 1
q = collections.deque(x for x in faces if indeg[x] == 0)
visited = 0
while q:
    x = q.popleft();visited += 1
    for y in out[x]:
        indeg[y] -= 1
        if indeg[y] == 0:
            q.append(y)
assert incidences == 10192 and visited == len(faces)

# Compute the integral Morse differential by Gaussian cancellation of the
# matched codimension-one pairs (all pivots are ±1).
low_to_up = dict(pairs)
def morse_boundary(s):
    chain = boundary(s,faces)
    rounds = 0
    while True:
        active = [x for x,c in chain.items() if c and x in low_to_up]
        if not active:
            break
        lo = min(active)
        up = low_to_up[lo]
        bd = boundary(up,faces)
        coeff = chain[lo]
        pivot = bd[lo]
        assert abs(pivot) == 1 and coeff % pivot == 0
        for x,c in bd.items():
            z = chain.get(x,0) - (coeff // pivot)*c
            if z:
                chain[x]=z
            else:
                chain.pop(x,None)
        rounds += 1
        assert rounds < len(faces)
    return chain,rounds
morse = [(s,morse_boundary(s)) for s in critical if s.bit_count()==7]
assert len(morse) == 2
assert all(r==({},7) for s,r in morse), morse

# Entire ordinary simplicial chain complex: independent rank check over F2.
def mod2_rank(d):
    if d == 0:
        return 0
    rows = {s:j for j,s in enumerate(by_dim[d-1])}
    pivots = {}
    for s in by_dim[d]:
        col = 0
        for j in range(M):
            if s & (1 << j):
                col ^= 1 << rows[s ^ (1 << j)]
        while col:
            p = col.bit_length()-1
            if p in pivots:
                col ^= pivots[p]
            else:
                pivots[p] = col
                break
    return len(pivots)
ranks = [0] + [mod2_rank(d) for d in range(1,7)]
assert ranks == [0,13,71,209,351,321,126]
betti = [len(by_dim[d])-ranks[d]-(ranks[d+1] if d<6 else 0)
         -(1 if d==0 else 0) for d in range(7)]
assert betti == [0,0,0,0,0,1,2]

# Exact C2 symmetry on top homology. A basis of integral 6-cycles is
# constructed by fraction-free-in-output rational column elimination.
upper = by_dim[6]
rows = {s:i for i,s in enumerate(by_dim[5])}
basis,comb_basis,cycles,free = {},{},{},[]
for j,fac in enumerate(upper):
    v = {rows[lo]:Fraction(c) for lo,c in boundary(fac,faces).items()}
    combination = {j:Fraction(1)}
    while v:
        pivot=max(v)
        if pivot not in basis:
            inv = 1/v[pivot]
            basis[pivot] = {x:c*inv for x,c in v.items()}
            comb_basis[pivot] = {x:c*inv for x,c in combination.items()}
            break
        factor=v[pivot]
        for x,c in basis[pivot].items():
            k=v.get(x,0)-factor*c
            if k:v[x]=k
            else:v.pop(x,None)
        for x,c in comb_basis[pivot].items():
            k=combination.get(x,0)-factor*c
            if k:combination[x]=k
            else:combination.pop(x,None)
    else:
        cycles[j]=combination
        free.append(j)
assert free == [90,106] and len(basis)==126
assert all(a.denominator == 1 and abs(a)==1 for cyc in cycles.values() for a in cyc.values())
assert [len(cycles[j]) for j in free] == [8,8]
flip = {v:W2I[tuple(1-b for b in w)] for v,w in enumerate(WORDS)}
arcperm = [ARCS.index((flip[a],flip[b])) for a,b in ARCS]
upper_id = {s:j for j,s in enumerate(upper)}
column_action = []
for freej in free:
    transformed = {}
    for j,c in cycles[freej].items():
        mask=upper[j]
        im=[arcperm[i] for i in range(M) if mask & (1 << i)]
        k=upper_id[sum(1<<i for i in im)]
        transformed[k]=transformed.get(k,0)+c*sign_perm(im)
    column_action.append([transformed.get(j,0) for j in free])
assert column_action == [[0,1],[1,0]], column_action

# Signed Lefschetz number from fixed simplices determines remaining H5.
chain_traces = []
for d in range(7):
    trace=0
    for s in by_dim[d]:
        image=[arcperm[i] for i in range(M) if s & (1 << i)]
        if sum(1<<i for i in image)==s:
            trace += sign_perm(image)
    chain_traces.append(trace)
assert chain_traces == [0,-6,0,12,0,-8,0]
reduced_lefschetz=sum((-1)**d * trace for d,trace in enumerate(chain_traces))-1
assert reduced_lefschetz == 1
# trace H6=0, hence -trace H5+trace H6=1 implies trace H5=-1.
assert 0 - (-1) == reduced_lefschetz

print('VERIFY_OK')
print('arc_count=14; faces=2186; facets_by_size={6:4,7:128}')
print('f_vector='+str([len(by_dim[d]) for d in range(7)]))
print('matching_pairs=1091; critical=(1 dimension 0,1 dimension 5,2 dimension 6)')
print('gradient_incidence_DAG_nodes=2186; edges=10192; exact_Morse_d6=(0,0)')
print('mod2_boundary_ranks='+str(ranks))
print('top_H6_flip_matrix_columns='+str(column_action))
print('reduced_Lefschetz=1; trace_H5=-1; trace_H6=0')
