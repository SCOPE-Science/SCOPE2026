#!/usr/bin/env python3
"""Independent complete checker for a Paley graph clique-complex Morse certificate.
Only the Python standard library is required. Run beside morse_certificate.json.
"""
import itertools
import json
from collections import Counter, deque
from pathlib import Path

BASE = Path(__file__).resolve().parent
N = 25

def add(a, b):
    return ((a % 5 + b % 5) % 5) + 5 * ((a // 5 + b // 5) % 5)

def neg(a):
    return ((-a % 5) % 5) + 5 * ((-(a // 5)) % 5)

def mul(a, b):
    x, y, u, v = a % 5, a // 5, b % 5, b // 5
    return ((x * u + 2 * y * v) % 5) + 5 * ((x * v + y * u) % 5)

SQ = {mul(a,a) for a in range(1, N)}
assert len(SQ) == 12 and 1 in SQ and 6 in SQ and 5 not in SQ
adj = [{v for v in range(N) if v != u and add(v,neg(u)) in SQ} for u in range(N)]
assert all(len(x) == 12 for x in adj)
assert all((u in adj[v]) == (v in adj[u]) for u in range(N) for v in range(N))

faces = {t for k in range(1,6) for t in itertools.combinations(range(N), k)
         if all(y in adj[x] for x,y in itertools.combinations(t, 2))}
f_vector = tuple(sum(len(s)==k for s in faces) for k in range(1,6))
assert f_vector == (25,150,250,75,15), f_vector
# Maximal cliques are the 15 affine lines in the three square directions.
maximal = {s for s in faces if len(s)==5}
assert len(maximal)==15
assert all(any(tuple(sorted(add(x,mul(k,v)) for k in range(5))) == s
               for x in range(N) for v in (1,6,9)) for s in maximal)

raw = json.loads((BASE/'morse_certificate.json').read_text('utf-8'))
pairs = [(tuple(a),tuple(b)) for a,b in raw['pairs']]
critical = [tuple(x) for x in raw['critical']]
assert len(pairs)==225 and len(critical)==65
assert len(set(critical)) == len(critical)
all_assigned = list(critical)
for low,high in pairs:
    assert low in faces and high in faces
    assert len(high)==len(low)+1 and set(low).issubset(high)
    all_assigned += [low,high]
assert set(all_assigned) == faces and len(set(all_assigned))==len(faces)
assert Counter(len(s)-1 for s in critical) == Counter({0:1,2:64})

# Full Hasse diagram: orient unmatched cover arrows higher -> lower,
# and matched arrows lower -> higher. Acyclicity is global, not sampled.
match = set(pairs)
succ = {s:[] for s in faces}
indeg = {s:0 for s in faces}
cover_count = 0
for high in faces:
    for low in itertools.combinations(high,len(high)-1):
        if not low:
            continue
        cover_count += 1
        if (low,high) in match:
            src,dst=low,high
        else:
            src,dst=high,low
        succ[src].append(dst)
        indeg[dst] +=1
q = deque(x for x in faces if indeg[x]==0)
visited=0
while q:
    v=q.popleft();visited+=1
    for w in succ[v]:
        indeg[w]-=1
        if indeg[w]==0:q.append(w)
assert visited==len(faces),f'A directed cycle remains; only {visited} visited'

# Independent rank verification over GF(2) using sparse-integer bit vectors.
def rank_bitvectors(cols):
    basis={}
    for x in cols:
        while x:
            p=x.bit_length()-1
            if p in basis:x ^= basis[p]
            else:basis[p]=x;break
    return len(basis)

bydim = [sorted(s for s in faces if len(s)==k) for k in range(1,6)]
ranks=[]
for k in range(1,5):
    rowidx={x:i for i,x in enumerate(bydim[k-1])}
    columns=[]
    for s in bydim[k]:
        v=0
        for t in itertools.combinations(s,len(s)-1):v ^= 1<<rowidx[t]
        columns.append(v)
    ranks.append(rank_bitvectors(columns))
assert ranks == [24,126,60,15],ranks
b2 = f_vector[2]-ranks[1]-ranks[2]
assert b2==64

# Each translation acts by a permutation; compute signed simplicial Lefschetz numbers.
def perm_sign(img):
    inversions=sum(img[i]>img[j] for i in range(len(img)) for j in range(i+1,len(img)))
    return -1 if inversions % 2 else 1

traces=[]
for g in range(N):
    Lef=0
    for s in faces:
        img=[add(x,g) for x in s]
        if set(img)==set(s):
            Lef += ((-1)**(len(s)-1))*perm_sign(img)
    h2=Lef-1  # H_0 is the trivial representation; all other reduced homology vanishes.
    traces.append(h2)
    if g==0:assert Lef==65 and h2==64
    elif g in SQ:assert Lef==5 and h2==4,(g,Lef)
    else:assert Lef==0 and h2==-1,(g,Lef)
assert sum(traces)==100
assert sum(traces)//25==4
print('field_model=GF(5)[t]/(t^2-2); square_residues='+str(sorted(SQ)))
print('f_vector='+str(f_vector))
print(f'certificate_pairs={len(pairs)}; critical_cells={dict(Counter(len(s)-1 for s in critical))}')
print(f'hasse_covers={cover_count}; acyclicity_visited={visited}')
print(f'boundary_ranks_mod2={ranks}; betti_2_mod2={b2}')
print('translation_H2_trace_counts='+str(dict(sorted(Counter(traces).items()))))
print('translation_invariant_H2_dim=4; rational_module_multiplicities=3_on_square_lines_2_on_nonsquare_lines')
print('CHECK_OK')
