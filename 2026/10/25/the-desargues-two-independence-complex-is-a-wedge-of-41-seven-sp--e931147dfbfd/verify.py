#!/usr/bin/env python3
"""Exact finite calculation of a higher-independence homotopy type.

Only Python's standard library is needed. No cached data or external files.
Face sets use bit masks. All boundary coefficients are integers.
"""
from collections import Counter, defaultdict, deque
from itertools import combinations
import json

N = 20
ADJ = [0] * N
EDGES = set()
for i in range(10):
    for u, v in ((i, (i + 1) % 10), (i, i + 10), (i + 10, (i + 3) % 10 + 10)):
        u, v = sorted((u, v))
        EDGES.add((u, v))
for u, v in EDGES:
    ADJ[u] |= 1 << v
    ADJ[v] |= 1 << u
assert len(EDGES) == 30 and all(a.bit_count() == 3 for a in ADJ)
assert all((ADJ[v] & ADJ[u]) == 0 for u, v in EDGES) # triangle-free

# Test A: every vertex in the induced graph has degree <= 1.
def face_test_a(mask):
    s = mask
    while s:
        b = s & -s
        s ^= b
        if (ADJ[b.bit_length()-1] & mask).bit_count() > 1:
            return False
    return True

# Test B: no three-set consisting of one vertex and two neighbors.
FORBIDDEN = set()
for v in range(N):
    nbr = [i for i in range(N) if (ADJ[v] >> i) & 1]
    for a, b in combinations(nbr, 2):
        FORBIDDEN.add((1 << v) | (1 << a) | (1 << b))
assert len(FORBIDDEN) == 60

FACES = []
for s in range(1 << N):
    ok_a = face_test_a(s)
    ok_b = not any((s & t) == t for t in FORBIDDEN)
    assert ok_a == ok_b, ('face tests disagree', s)
    if ok_a:
        FACES.append(s)
FSET = set(FACES)
assert len(FACES) == 62049
fvector = dict(sorted(Counter(s.bit_count()-1 for s in FACES if s).items()))
assert sum(((-1)**d)*v for d,v in fvector.items())-1 == -41

# Sequential elementary matching using ascending vertex pivot.
UNPAIRED = set(FACES)
PAIRS = []
for v in range(N):
    bit = 1 << v
    stage = []
    for s in sorted(UNPAIRED):
        if (s & bit) == 0 and (s | bit) in UNPAIRED:
            stage.append((s, s | bit))
    for a, b in stage:
        UNPAIRED.remove(a)
        UNPAIRED.remove(b)
    PAIRS.extend(stage)
assert 2*len(PAIRS)+len(UNPAIRED)==len(FACES)
assert len(PAIRS)==31001
assert Counter(s.bit_count()-1 for s in UNPAIRED)=={6: 3, 7: 44}
assert (0, 1) in PAIRS

# Global acyclicity of the matched Hasse graph, not merely pivot acyclicity.
INDEX = {s: i for i, s in enumerate(FACES)}
MATCHED = {(a,b) for a,b in PAIRS}
OUT = [[] for _ in FACES]
DEG = [0] * len(FACES)
cover_count = 0
for b in FACES:
    if not b:
        continue
    ib = INDEX[b]
    t = b
    while t:
        bit = t & -t
        t ^= bit
        a = b ^ bit
        ia = INDEX[a]
        if (a,b) in MATCHED:
            OUT[ia].append(ib)
            DEG[ib] += 1
        else:
            OUT[ib].append(ia)
            DEG[ia] += 1
        cover_count += 1
queue = deque(i for i,d in enumerate(DEG) if d==0)
visited = 0
while queue:
    i = queue.popleft()
    visited += 1
    for j in OUT[i]:
        DEG[j] -= 1
        if DEG[j] == 0:
            queue.append(j)
assert visited==len(FACES), (visited, len(FACES))

LOWER_TO_UPPER = {a:b for a,b in PAIRS}
UPPER_TO_LOWER = {b:a for a,b in PAIRS}
CRIT6 = sorted(s for s in UNPAIRED if s.bit_count()==7)
CRIT7 = sorted(s for s in UNPAIRED if s.bit_count()==8)

def faces_with_sign(s):
    sign = 1
    remainder = s
    while remainder:
        bit = remainder & -remainder
        yield s ^ bit, sign
        sign = -sign
        remainder ^= bit

def incidence(upper, lower):
    removed = upper ^ lower
    assert removed and not (removed & (removed-1))
    return -1 if ((upper & (removed-1)).bit_count() % 2) else 1

# Algebraic Morse projection of each dimension-6 simplex to critical 6-cells.
CACHE = {}
ACTIVE = set()
def projection(s):
    if s in CACHE:
        return CACHE[s]
    assert s.bit_count() == 7
    assert s not in ACTIVE, ('gradient cycle',s)
    ACTIVE.add(s)
    if s in UNPAIRED:
        out = {s: 1}
    elif s in UPPER_TO_LOWER:
        out = {}
    else:
        t = LOWER_TO_UPPER[s]
        assert t.bit_count()==8
        pivot = incidence(t,s)
        raw = defaultdict(int)
        for a,sign in faces_with_sign(t):
            if a==s:
                continue
            for target,coef in projection(a).items():
                raw[target] -= pivot*sign*coef
        out = {a:v for a,v in raw.items() if v!=0}
    ACTIVE.remove(s)
    CACHE[s] = out
    return out

# Each row lists the coefficients of the Morse boundary of a critical 7-cell.
BOUNDARY_ROWS = []
for b in CRIT7:
    ans = defaultdict(int)
    for a,sign in faces_with_sign(b):
        for target,coef in projection(a).items():
            ans[target] += sign*coef
    BOUNDARY_ROWS.append([ans[a] for a in CRIT6])

def det3(rows):
    (a,b,c),(d,e,f),(g,h,i)=rows
    return a*(e*i-f*h)-b*(d*i-f*g)+c*(d*h-e*g)
unit_minor = next(((i,j,k,det3([BOUNDARY_ROWS[t] for t in (i,j,k)]))
                   for i,j,k in combinations(range(len(CRIT7)),3)
                   if abs(det3([BOUNDARY_ROWS[t] for t in (i,j,k)]))==1),None)
assert unit_minor is not None
assert len(CRIT6)==3 and len(CRIT7)==44
print(json.dumps({
 'verification':'VERIFY_OK',
 'graph':'GP(10,3)', 'vertices':N,'edges':len(EDGES),
 'total_vertex_subsets_checked':1 << N,
 'forbidden_induced_three_vertex_paths':len(FORBIDDEN),
 'faces_including_empty':len(FACES),'f_vector':fvector,
 'matched_pairs_in_augmented_complex':len(PAIRS),
 'directed_hasse_incidence_count':cover_count,
 'hasse_vertices_acyclic':visited,
 'critical_cells_augmented':{'dim_6':len(CRIT6),'dim_7':len(CRIT7)},
 'critical_6_masks':CRIT6,'critical_7_masks':CRIT7,
 'morse_boundary_rows':BOUNDARY_ROWS,
 'unit_minor_rows_zero_based_and_determinant':unit_minor,
 'projection_states':len(CACHE),
 'conclusion':'Ind_2(GP(10,3)) is homotopy equivalent to a wedge of 41 seven-spheres.'
},sort_keys=True,indent=2))
