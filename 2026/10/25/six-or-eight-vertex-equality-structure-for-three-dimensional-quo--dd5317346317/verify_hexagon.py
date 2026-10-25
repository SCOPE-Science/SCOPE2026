"""Exact rational checks for a hexagonal quotient equality construction.

Requires Python 3 standard library only. All claims of infinite scope are proved
in the accompanying mathematical text; this code checks rational certificates.
"""
from fractions import Fraction as Q

R = [
    (Q(2,3), -Q(1,3)),
    (Q(1,3), Q(1,3)),
    (-Q(1,3), Q(2,3)),
    (-Q(2,3), Q(1,3)),
    (-Q(1,3), -Q(1,3)),
    (Q(1,3), -Q(2,3)),
]
QGRAD = [(2, 1), (1, 2), (-1, 1), (-2, -1), (-1, -2), (1, -1)]
FGRAD = [(0, 0), (-1, 1), (1, 2), (0, 0), (-1, 1), (1, 2)]
FVERT = [0, 0, 1, 0, 0, -1]

def dot(a,b): return sum(x*y for x,y in zip(a,b))
def signed_area(poly):
    return sum(x*poly[(i+1)%len(poly)][1] - y*poly[(i+1)%len(poly)][0]
               for i,(x,y) in enumerate(poly))/2

def cone_certificate(t):
    # A fan-linear function is convex iff each linear gradient is maximal
    # on its fan cone; it suffices to check the two rays per cone.
    outcomes = []
    for sign in (-1,1):
        gradients = [tuple(Q(g[k]) + sign*t*Q(f[k]) for k in range(2))
                     for g,f in zip(QGRAD,FGRAD)]
        slacks = [dot(tuple(gradients[i][k]-gradients[j][k] for k in range(2)), R[v])
                  for i in range(6) for v in (i,(i+1)%6) for j in range(6)]
        outcomes.append(min(slacks))
    return outcomes

assert signed_area(R) == 1
assert all(R[(i+3)%6] == tuple(-a for a in R[i]) for i in range(3))
assert all(dot(QGRAD[i], R[i]) == dot(QGRAD[i], R[(i+1)%6]) == 1
           for i in range(6))
assert all(dot(FGRAD[i], R[i]) == FVERT[i]
           and dot(FGRAD[i], R[(i+1)%6]) == FVERT[(i+1)%6]
           for i in range(6))
assert all(cone_certificate(Q(t)) == [Q(0),Q(0)] for t in (-1,0,1))
assert all(x>=0 for x in cone_certificate(Q(1,2)))
assert any(x<0 for x in cone_certificate(Q(3,2)))
assert any(x<0 for x in cone_certificate(Q(-3,2)))
# The three linear forms are integer-valued; finite check of their
# possible values -1,0,1 proves there is no nonzero integer vector with q<2.
for a in (-1,0,1):
    for b in (-1,0,1):
        u,v = Q(2*a-b,3),Q(2*b-a,3)
        if u.denominator==v.denominator==1 and abs(u-v)<=1:
            assert (u,v)==(0,0)
# For t=1/2 the six equatorial lifts are not coplanar: values on
# two independent rays vanish while the value on a third does not.
assert FVERT[0]==FVERT[1]==0 and FVERT[2]==1
print('PASS: area=1; lattice packing; all cone gradients; sharp |t|<=1; nonplanar equator')
