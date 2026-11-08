"""Finite exact checks for induced claw/path covariance identities.
Requires Python 3 standard library only. Run: python verify.py
"""
from fractions import Fraction as F
from itertools import combinations, permutations
from math import comb

EDGES4 = tuple(combinations(range(4), 2))
STARS = {frozenset(tuple(sorted((c,j))) for j in range(4) if j != c)
         for c in range(4)}
P4_REP = frozenset(((0,1),(1,2),(2,3)))
PATHS = {frozenset(tuple(sorted((a[u], a[v]))) for u,v in P4_REP)
         for a in permutations(range(4))}
assert len(STARS)==4 and len(PATHS)==12

# Subset Fourier coefficients: 4-label induced graphlet indicator in basis Y_e=X_e-p.
def coeff(patterns, edges, p):
    k=len(edges)
    return sum(((-1)**(k-len(edges & H))) * p**(3-len(edges & H)) *
               (1-p)**(3-k+len(edges & H)) for H in patterns)

def inner(v,p):
    edges=tuple(combinations(range(v),2))
    total=F(0)
    for k in range(1,len(edges)+1):
        for tt in combinations(edges,k):
            T=frozenset(tt)
            if len({vtx for e in T for vtx in e}) != v: continue
            total += coeff(STARS,T,p)*coeff(PATHS,T,p)*(p*(1-p))**k
    return total

def shape(v,p):
    if v==2: return 12*p**5*(1-p)**5*(2*p-1)**2
    if v==3: return -6*p**4*(1-p)**5*(2*p-1)*(8*p*p-4*p+1)
    if v==4: return 24*p**4*(1-p)**5*(6*p**3-6*p*p+3*p-1)
    raise ValueError

def formula(n,p):
    return (comb(n,2)*comb(n-2,2)**2*shape(2,p)
          + comb(n,3)*(n-3)**2*shape(3,p)
          + comb(n,4)*shape(4,p))

# The inner polynomials have degree at most 12 (conservative).
# Checking on thirteen distinct rational values certifies their identity.
checks=0
for v in (2,3,4):
    for i in range(13):
        p=F(i,12)
        assert inner(v,p)==shape(v,p), (v,p,inner(v,p),shape(v,p))
        checks+=1

# Independent direct enumeration of all graphs G on n vertices for small n.
# Each graph has weight p^m(1-p)^(M-m), not derived from the projection formula.
def graphlet_numbers(n,mask,edges,quads):
    adjacency=[[0]*n for _ in range(n)]
    for i,(u,v) in enumerate(edges):
        if mask>>i&1: adjacency[u][v]=adjacency[v][u]=1
    claws=paths=0
    for q in quads:
        deg=[sum(adjacency[u][v] for v in q if v!=u) for u in q]
        if sorted(deg)==[1,1,1,3]: claws+=1
        if sorted(deg)==[1,1,2,2]: paths+=1
    return claws,paths

def brute(n,p):
    edges=list(combinations(range(n),2))
    quads=list(combinations(range(n),4))
    N=len(edges)
    eA=eB=eAB=F(0)
    w=[p**k*(1-p)**(N-k) for k in range(N+1)]
    for bits in range(1<<N):
        a,b=graphlet_numbers(n,bits,edges,quads)
        prob=w[bits.bit_count()]
        eA+=a*prob;eB+=b*prob;eAB+=a*b*prob
    return eAB-eA*eB

for n in (4,5,6):
    for p in (F(1,3),F(1,2),F(2,3)):
        observed=brute(n,p)
        assert observed==formula(n,p),(n,p,observed,formula(n,p))
        checks+=1

for n in range(4,30):
    assert formula(n,F(1,2)) == -F(3,256)*comb(n,4)
    checks+=1
print('PASS:',checks,'exact certificate assertions; exhaustive graphs n=4,5,6 at three densities; polynomial interpolation checks')
