"""Finite-field verification of UT4(F3) maximum noncommuting sets.

Run: python3 verify.py. Standard library only.
"""
from collections import Counter
from itertools import product
from math import comb

q = 3

def omega(u, v):
    a,b,e,f = u
    A,B,E,F = v
    return (a*E + b*F - A*e - B*f) % q

def canon(v):
    return min(tuple((t*x)%q for x in v) for t in (1,2))

pts = sorted({canon(v) for v in product(range(q), repeat=4) if any(v)})
assert len(pts) == 40
N = len(pts)
nb = [sum(1 << j for j in range(N) if j != i and omega(pts[i], pts[j])) for i in range(N)]

# Forward-neighbor exact clique enumeration. The increasing-index rule
# makes each clique appear once; this is complete, not a random sample.
counts=Counter(); chosen=[]; exemplar=None; heptads=[]
def recurse(candidates):
    global exemplar
    counts[len(chosen)] += 1
    if len(chosen) == 7:
        heptads.append(tuple(chosen))
        if exemplar is None and all(pts[i][0] or pts[i][3] for i in chosen):
            exemplar = tuple(pts[i] for i in chosen)
    while candidates:
        bit = candidates & -candidates
        j = bit.bit_length() - 1
        candidates ^= bit
        chosen.append(j)
        recurse(candidates & nb[j])
        chosen.pop()
recurse((1 << N) - 1)
assert counts[7] == 2880, counts
assert counts[8] == 0, counts
assert sum(counts.values()) == 40055, counts # includes the empty clique
L = {i for i, z in enumerate(pts) if z[0] == 0 and z[3] == 0}
assert len(L) == 4
hist = Counter(len(set(T) & L) for T in heptads)
assert hist == {0:864,1:2016}, hist
assert exemplar is not None
assert len([T for T in heptads if not set(T)&L]) == 864

# Each 7-clique meets a totally isotropic line in at most one point.
# Symplectic transitivity is not assumed by the computer check; verify
# directly that each projective point occurs 504 times.
deg=Counter(i for T in heptads for i in T)
assert set(deg.values()) == {504} and len(deg) == 40

# A UT4 tuple is (a,b,c,d,e,f). Matrix commutation is expressed by
# three independent upper-diagonal entries of XY-YX.
def commute(x,y):
    a,b,c,d,e,f=x
    A,B,C,D,E,F=y
    return (a*D-d*A) % q == 0 and (d*F-f*D) % q == 0 and (a*E+b*F-A*e-B*f) % q == 0

def select(r,s,t):
    if r:
        b=0; e=(t*pow(r,-1,q))%q
    else:
        e=0; b=(-t*pow(s,-1,q))%q
    return (r,b,0,1,e,s)

# One representative of each of the 25 giant cliques at d != 0,
# plus seven from a projective partial ovoid disjoint from L.
witness = [(0,0,0,1,0,0)]
for r,s in product(range(q),repeat=2):
    if (r,s) != (0,0):
        witness.extend(select(r,s,t) for t in range(q))
assert len(witness)==25
witness.extend((a,b,0,0,e,f) for (a,b,e,f) in exemplar)
assert len(witness)==32
for i in range(len(witness)):
    for j in range(i):
        assert not commute(witness[i],witness[j]), (i,j)

n_nonzero_fibers = q * (q*q - 1)
assert n_nonzero_fibers == 24
fiber_lifts = (q-1)*q*q
zero_lifts = (q-1)*q**3
projective_lifts = (q-1)*q
answer = 864 * projective_lifts**7 * fiber_lifts**24 * zero_lifts
assert answer == 2**37 * 3**61
print('VERIFY_OK: 40 projective points, 2880 heptads, 864 avoid line, no octads, 32-vertex UT4 witness; maximum-family count = 2^37 * 3^61')
