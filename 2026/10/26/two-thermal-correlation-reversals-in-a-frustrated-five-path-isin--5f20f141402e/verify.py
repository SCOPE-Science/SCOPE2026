"""Exact checks for an equilibrium Ising multipath correlation theorem.

Standard-library only. All root counts follow from exact integer/rational
arithmetic and Descartes' rule, not from floating-point root finding.
"""
from fractions import Fraction
from itertools import product
from math import comb

LENGTHS = (2, 3, 4, 9, 10)
SIGNS = (-1, 1, 1, -1, -1)
Q_TERMS = {18: 1, 16: 1, 14: 1, 13: -1, 12: 1, 10: 1,
           8: 1, 6: 1, 5: -1, 3: -1, 1: -1, 0: 1}
R_EXPECTED = (1, 17, 136, 679, 2365, 6082, 11909, 18017,
              21088, 18820, 12267, 5145, 630, -805, -614,
              -195, -15, 10, 4)

def plus(a, b):
    v = [0] * max(len(a), len(b))
    for i, c in enumerate(a): v[i] += c
    for i, c in enumerate(b): v[i] += c
    return v

def mult(a, b):
    v = [0] * (len(a) + len(b) - 1)
    for i, x in enumerate(a):
        for j, y in enumerate(b): v[i+j] += x*y
    return v

def scale(a, c): return [c*x for x in a]

def monomial(l, c):
    ans = [0] * (l+1)
    ans[0], ans[l] = 1, c
    return ans

def calc_numerator():
    p, m = [1], [1]
    for l,sgn in zip(LENGTHS,SIGNS):
        p = mult(p, monomial(l,sgn))
        m = mult(m, monomial(l,-sgn))
    return plus(p,scale(m,-1))

q = [Q_TERMS.get(k,0) for k in range(19)]
numer = calc_numerator()
# Product factor: -2 t^2(1-t^2)^2(1+t^2+t^4)Q(t).
a = mult(mult([1,0,-1],[1,0,-1]),[1,0,1,0,1])
expected = mult([0,0,-2],mult(a,q))
assert numer == expected, 'symbolic factorization failed'

# Root count of Q on (0,1): z=t/(1-t) maps this interval onto z>0.
# Calculate transformed coefficients without symbolic algebra packages.
r = [sum(q[k] * comb(18-k,j-k) for k in range(j+1)) for j in range(19)]
assert tuple(r) == R_EXPECTED
nonzero = [1 if c>0 else -1 for c in r if c]
changes = sum(a!=b for a,b in zip(nonzero,nonzero[1:]))
assert changes == 2, f'Descartes only gives {changes} roots'

# Two strict signs force at least two distinct roots in the open interval.
def eval_poly(a,t):
    v=Fraction(0)
    for c in a[::-1]: v=v*t+c
    return v

sign_table=[]
for t,sgn in [(Fraction(7,10),-1),(Fraction(3,4),1),(Fraction(4,5),-1)]:
    v=eval_poly(numer,t)
    assert v*sgn > 0
    sign_table.append((str(t),sgn))
assert r[0]>0 and r[-1]>0

# Exact finite-state comparison with independent Ising configuration sums
# on a smaller three-branch network (not used to prove the general theorem).
def exact_graph_correlation(lens,signs,t):
    edges=[]; next_v=2
    for l,sgn in zip(lens,signs):
        path=[0]+list(range(next_v,next_v+l-1))+[1]
        next_v+=l-1
        for j,(u,v) in enumerate(zip(path,path[1:])):
            edges.append((u,v,sgn if j==0 else 1))
    z, num = Fraction(0),Fraction(0)
    for spins in product((-1,1),repeat=next_v):
        weight=Fraction(1)
        for u,v,sgn in edges:
            weight *= 1 + sgn*t*spins[u]*spins[v]
        z+=weight
        num+=weight*spins[0]*spins[1]
    return num/z

def independent_path_formula(lens,signs,t):
    plusweight=Fraction(1); minusweight=Fraction(1)
    for l,s in zip(lens,signs):
        plusweight *= 1+s*t**l
        minusweight *= 1-s*t**l
    return (plusweight-minusweight)/(plusweight+minusweight)

checks=3
for lens,sgns in [((2,3,4),(-1,1,1)),((2,2,3),(1,-1,-1))]:
    for t in [Fraction(1,3),Fraction(3,4)]:
        assert exact_graph_correlation(lens,sgns,t)==independent_path_formula(lens,sgns,t)
        checks+=1

# No claim of exactly two roots for this variable-length family, only >=2.
# At t=3/4 the long negative paths only weaken if they are lengthened.
for d in range(9,16):
    for e in range(max(d+1,10),19):
        assert independent_path_formula((2,3,4,d,e),SIGNS,Fraction(3,4)) > 0
        checks+=1

# Distinct solutions are bracketed in (7/10,3/4) and (3/4,4/5);
# coefficient sign-variation proves that these exhaust (0,1).
print('PASS: exact factorization; 2 Descartes variations; 2 separated roots;')
print('      finite-graph enumeration; family positivity; %d supplemental assertions.'%checks)
print('signs',sign_table)
