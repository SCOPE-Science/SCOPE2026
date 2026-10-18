"""Exact checks for the Cartier stratification of a genus-three family over F_13.

Run: python3 verify.py. Uses the Python standard library only.
The symbolic proof is in RESULT.md; this program recomputes its finite identities.
"""

from collections import defaultdict
from itertools import product

P = 13


def add_poly(a, b):
    out = [0] * max(len(a), len(b))
    for i, c in enumerate(a):
        out[i] = (out[i] + c) % P
    for i, c in enumerate(b):
        out[i] = (out[i] + c) % P
    while out and out[-1] == 0:
        out.pop()
    return out


def multiply(a, b):
    out = [0] * (len(a) + len(b) - 1)
    for i, x in enumerate(a):
        for j, y in enumerate(b):
            out[i+j] = (out[i+j] + x*y) % P
    return out


# A bivariate polynomial is a dict (power_of_x, power_of_t) -> coefficient.
def bi_multiply(a, b):
    out = defaultdict(int)
    for (i, j), x in a.items():
        for (k, ell), y in b.items():
            out[(i+k, j+ell)] = (out[(i+k, j+ell)] + x*y) % P
    return {k: v for k, v in out.items() if v}


f = {(7, 0): 1, (4, 0): P-1, (4, 1): P-1, (1, 1): 1}
g = {(0, 0): 1}
for _ in range(6):
    g = bi_multiply(g, f)


def at_x_degree(n):
    z = [0] * 7
    for (i,j), c in g.items():
        if i == n:
            z[j] = c
    return z


H1, H2, H3 = (at_x_degree(k) for k in (12, 24, 36))
A = [1, 5, 1]
B = [P-4, 4, 1]
C = [1, P-6, 1]
D = [3, P-1, 1]
assert H1 == [0,0,0,0] + [(2*c) % P for c in A]
assert H3[:3] == [(2*c) % P for c in A]
assert all(x == 0 for x in H3[3:])
assert H2 == multiply(multiply(B,C),D)


def fm(x,y):
    a,b=x; c,d=y
    return ((a*c + 2*b*d)%P, (a*d+b*c)%P)


def fa(x,y):
    return ((x[0]+y[0])%P, (x[1]+y[1])%P)


def fpow(x,n):
    z = (1,0)
    while n:
        if n&1: z=fm(z,x)
        x=fm(x,x)
        n //= 2
    return z


def eval_poly(poly, t):
    v=(0,0)
    for c in reversed(poly):
        v=fa(fm(v,t),(c,0))
    return v


zero=(0,0)
roots={}
for key,poly in [('A',A),('B',B),('C',C),('D',D)]:
    roots[key] = {t for t in product(range(P),repeat=2) if eval_poly(poly,t)==zero}
    assert len(roots[key])==2
    assert not any(t[1]==0 for t in roots[key])
    assert all(t != (0,0) and t != (1,0) for t in roots[key])
for i,u in enumerate(roots):
    for j,v in enumerate(roots):
        if i<j: assert not roots[u] & roots[v]

assert fpow((0,1),2)==(2,0)
assert all(fpow(t,168)==(1,0) for t in product(range(P),repeat=2) if t!=zero)
counts={1:0,2:0,3:0}
strata={1:set(),2:set(),3:set()}
for t in product(range(P),repeat=2):
    if t in (zero,(1,0)): continue
    rank=sum(eval_poly(h,t)!=zero for h in (H1,H2,H3))
    assert rank in counts
    counts[rank]+=1
    strata[rank].add(t)
assert counts == {1:2,2:6,3:159}
assert strata[1]==roots['A']
assert strata[2]==roots['B'] | roots['C'] | roots['D']
assert all((t,0) not in strata[1] | strata[2] for t in range(P) if t not in (0,1))

# These are parameter involution orbits, not claims of a complete curve-isomorphism census.
special = strata[1] | strata[2]
orbits = set()
for t in special:
    inverse=fpow(t,167)
    assert inverse in special
    orbits.add(frozenset((t,inverse)))
assert len(orbits)==4 and all(len(o)==2 for o in orbits)
assert len({o for o in orbits if next(iter(o)) in strata[1]}) == 1
assert len({o for o in orbits if next(iter(o)) in strata[2]}) == 3
print('VERIFIED: Cartier coefficients, quadratic factorizations, field roots,')
print('          2 p-rank-1, 6 p-rank-2, 159 ordinary geometric parameters')
print('          over F_169 (with t not 0,1), and four inversion orbits.')
