"""Exact arithmetic checks for the symmetric truncation difference-body identity.
Run with Python 3.10 or newer. No external packages are required.
This is a finite algebraic check; the analytic proof covers every real parameter.
"""
from fractions import Fraction as F
from itertools import permutations, product

V=((1,1,1),(1,-1,-1),(-1,1,-1),(-1,-1,1))
G=((1,1,0),(1,-1,0),(1,0,1),(1,0,-1),(0,1,1),(0,1,-1))

def edge_points(t):
    return {tuple((1-t)*F(V[i][k])+t*F(V[j][k])
                  for k in range(3))
            for i in range(4) for j in range(4) if i!=j}

def diff_points(p):
    return {tuple(x[k]-y[k] for k in range(3)) for x in p for y in p}

def candidate_vertices(a):
    return {tuple(signs[k]*q[k] for k in range(3))
            for q in set(permutations((F(2),F(2)*a,F(0))))
            for signs in product((-1,1),repeat=3)}

def support(points,n):
    return max(sum(x[k]*n[k] for k in range(3)) for x in points)

for t in (F(0),F(1,16),F(1,8),F(1,4),F(1,3),F(7,16),F(1,2)):
    a=1-2*t
    P=edge_points(t)
    D=diff_points(P)
    H=candidate_vertices(a)
    assert H <= D,(t,"missing intersection vertices",H-D)
    assert all(max(map(abs,x))<=2 and sum(map(abs,x))<=2+2*a for x in D)
    for n in ((1,0,0),(0,1,0),(0,0,1)):
        assert support(D,n)==2
    for n in product((-1,1),repeat=3):
        assert support(D,n)==2+2*a
    print("parameter",str(t),"D-points",len(D),"C-vertices",len(H),"facet/support tests PASS")

# At t=1/4, a generator representation gives the entire 24-vertex polytope.
Z={tuple(sum(F(s[j])*F(G[j][k],2) for j in range(6)) for k in range(3))
   for s in product((-1,1),repeat=6)}
H=candidate_vertices(F(1,2))
assert H <= Z
assert all(max(map(abs,x))<=2 and sum(map(abs,x))<=3 for x in Z)
print("exact 6-segment zonotope representation PASS")

# A diagonal facet is a hexagon whose three opposite-vertex pair-sums
# agree exactly when 4a=2. Check linear coefficient identities.
def polygon(a):
    return ((F(2),2*a,F(0)),(F(2),F(0),2*a),(2*a,F(0),F(2)),
            (F(0),2*a,F(2)),(F(0),F(2),2*a),(2*a,F(2),F(0)))
for a in (F(1,5),F(1,2),F(4,5)):
    q=polygon(a)
    sums=[tuple(q[i][k]+q[i+3][k] for k in range(3)) for i in range(3)]
    assert (len(set(sums))==1)==(a==F(1,2))
print("hexagon central-symmetry condition PASS")
print("ALL CHECKS PASS")
