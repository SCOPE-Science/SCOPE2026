"""Exact finite simplicial Morse certificate for the scale-three Čech complex of Q_5.

Requires Python >=3.9 and sympy. Run: python3 checker.py
"""
from itertools import combinations
from collections import Counter, deque
from functools import lru_cache
from sympy import zeros
from sympy.polys.domains import ZZ
from sympy.matrices.normalforms import smith_normal_form

N = 32
facets = []
for x in range(N):
    for i in range(5):
        y = x ^ (1 << i)
        if x < y:
            facets.append(tuple(sorted({x, y} | {x ^ (1 << j) for j in range(5)}
                                       | {y ^ (1 << j) for j in range(5)})))
assert len(facets) == 80 and all(len(f) == 10 for f in facets)

faces = set()
for f in facets:
    for size in range(1, len(f) + 1):
        for c in combinations(f, size):
            faces.add(sum(1 << x for x in c))
assert len(faces) == 54416
assert [sum(s.bit_count() == d + 1 for s in faces) for d in range(10)] == [32,400,2560,8320,14592,14752,9280,3600,800,80]

remaining = faces.copy()
pairs = []
for v in range(N):
    bit = 1 << v
    current = [(f, f | bit) for f in remaining if not f & bit and (f | bit) in remaining]
    for a, b in current:
        assert a in remaining and b in remaining and b == (a | bit)
        remaining.remove(a)
        remaining.remove(b)
    pairs.extend(current)
assert len(pairs) == 27134
assert Counter(f.bit_count() - 1 for f in remaining) == {0: 1, 3: 18, 4: 129}

# Acyclicity on the entire Hasse diagram (not merely sampled gradient paths).
matched_pairs = set(pairs)
indeg = {f: 0 for f in faces}
successors = {f: [] for f in faces}
for hi in faces:
    if hi.bit_count() <= 1:
        continue
    bits = hi
    while bits:
        t = bits & -bits
        bits -= t
        lo = hi ^ t
        if (lo, hi) in matched_pairs:
            src, dst = lo, hi
        else:
            src, dst = hi, lo
        successors[src].append(dst)
        indeg[dst] += 1
queue = deque(f for f, v in indeg.items() if v == 0)
visited = 0
while queue:
    f = queue.popleft()
    visited += 1
    for g in successors[f]:
        indeg[g] -= 1
        if indeg[g] == 0:
            queue.append(g)
assert visited == len(faces), (visited, len(faces))
del indeg, successors, matched_pairs, queue

critical3 = sorted(f for f in remaining if f.bit_count() == 4)
critical4 = sorted(f for f in remaining if f.bit_count() == 5)
ix = {f: k for k, f in enumerate(critical3)}
low3 = {a: b for a, b in pairs if a.bit_count() == 4}
high3 = {b for a, b in pairs if b.bit_count() == 4}

def boundary(f):
    b, sign = f, 1
    while b:
        bit = b & -b
        b ^= bit
        yield f ^ bit, sign
        sign = -sign

@lru_cache(maxsize=None)
def reduction(f):
    if f in ix:
        return {ix[f]: 1}
    if f in high3:
        return {}
    assert f in low3
    u = low3[f]
    pairing_sign = next(s for t, s in boundary(u) if t == f)
    ans = {}
    for t, s in boundary(u):
        if t == f:
            continue
        for j, coeff in reduction(t).items():
            ans[j] = ans.get(j, 0) - pairing_sign * s * coeff
    return {k: v for k, v in ans.items() if v}

M = zeros(18, 129)
for col, f in enumerate(critical4):
    for t, s in boundary(f):
        for j, c in reduction(t).items():
            M[j, col] += s * c
nz = [(i, j, int(M[i, j])) for i in range(M.rows) for j in range(M.cols) if M[i,j] != 0]
assert len(nz) == 54
assert all(abs(v) == 1 for _, _, v in nz)
D = smith_normal_form(M, domain=ZZ)
factors = [abs(int(D[i,i])) for i in range(min(D.shape)) if D[i,i]]
assert factors == [1] * 9
assert M.rank() == 9
print('f_vector=', [sum(s.bit_count() == d + 1 for s in faces) for d in range(10)])
print('matched_pairs=', len(pairs), 'critical_0_3_4=', (1,18,129))
print('full_hasse_acyclic_nodes=', visited)
print('critical_boundary_shape=', M.shape, 'nonzero_entries=', len(nz), 'smith_factors=', factors)
print('integral_homotopy_type= wedge(9,S3) + wedge(120,S4)')
# Full translation Lefschetz characters from fixed oriented simplices.
from math import comb

def fixed_trace(t):
    if not t:
        return sum((-1)**(f.bit_count()-1) for f in faces) - 1
    pairs_of_vertices=[]
    for v in range(N):
        if v < (v ^ t):
            pairs_of_vertices.append((1 << v) | (1 << (v ^ t)))
    total=-1  # reduced chain augmentation
    for f in faces:
        if all((f & p) in (0,p) for p in pairs_of_vertices):
            assert f.bit_count() % 2 == 0
            total += (-1) ** (f.bit_count() // 2 - 1)
    return total

all_trace={t:fixed_trace(t) for t in range(N)}
L=[all_trace[(1<<w)-1] for w in range(6)]
assert all(all_trace[t]==L[t.bit_count()] for t in range(N))
assert L==[111,31,-17,-9,-1,-1]

def inner_product_character(s):
    x=sum((-1 if (s & t).bit_count()%2 else 1)*all_trace[t] for t in range(N))
    assert x%N==0
    return x//N
virtual={s:inner_product_character(s) for s in range(N)}
weight_profile=[virtual[(1<<w)-1] for w in range(6)]
assert weight_profile==[0,6,6,3,-1,-4]
assert all(virtual[s]==weight_profile[s.bit_count()] for s in range(N))
# In the virtual difference H4-H3, every negative multiplicity
# forces that many copies in H3. Here the lower bound equals b3.
min_h3=sum(max(0,-virtual[s]) for s in range(N))
assert min_h3==9
h3={s:max(0,-virtual[s]) for s in range(N)}
h4={s:max(0,virtual[s]) for s in range(N)}
assert sum(h3.values())==9 and sum(h4.values())==120
assert [h3[(1<<w)-1] for w in range(6)]==[0,0,0,0,1,4]
assert [h4[(1<<w)-1] for w in range(6)]==[0,6,6,3,0,0]
tr3=[sum(m * (-1 if (s & t).bit_count()%2 else 1) for s,m in h3.items()) for t in range(N)]
tr4=[sum(m * (-1 if (s & t).bit_count()%2 else 1) for s,m in h4.items()) for t in range(N)]
assert all(tr4[t]-tr3[t]==all_trace[t] for t in range(N))
assert [tr3[(1<<w)-1] for w in range(6)]==[9,-7,5,-3,1,1]
assert [tr4[(1<<w)-1] for w in range(6)]==[120,24,-12,-12,0,0]
print('reduced Lefschetz by translation weight=',L)
print('virtual Fourier multiplicities by character weight=',weight_profile)
print('H3 Fourier multiplicities by character weight=',[h3[(1<<w)-1] for w in range(6)])
print('H4 Fourier multiplicities by character weight=',[h4[(1<<w)-1] for w in range(6)])
print('HYPERCUBE5_CECH3_TRANSLATION_CHARACTER_EXACT_OK')
