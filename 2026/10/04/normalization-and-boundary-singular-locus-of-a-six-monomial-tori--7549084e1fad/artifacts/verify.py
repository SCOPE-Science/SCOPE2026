#!/usr/bin/env python3
from math import gcd
A=[(0,0),(0,5),(1,2),(1,3),(5,0),(5,5)]
# Convex hull is the 5-by-5 square; normalized area is 2!*25=50.
verts={(0,0),(0,5),(5,0),(5,5)}
assert verts.issubset(A)
assert all(0<=a<=5 and 0<=b<=5 for a,b in A)
assert 2*25==50
# The exponent differences generate Z^2: (0,1) and (1,2) have determinant -1.
v=(A[3][0]-A[2][0],A[3][1]-A[2][1])
w=A[2]
assert v==(0,1)
assert v[0]*w[1]-v[1]*w[0]==-1
# Dense-torus inverse: y=z3/z2 and x=z2^3/(z0*z3^2).
def lincomb(cs):
    return (sum(c*a for c,(a,b) in zip(cs,A)),sum(c*b for c,(a,b) in zip(cs,A)))
assert lincomb([0,0,-1,1,0,0])==(0,1)
assert lincomb([-1,0,3,-2,0,0])==(1,0)
# Facet supports are exactly the endpoint monomials on the four square edges.
facets={
'x=0':{0,1}, 'x=5':{4,5}, 'y=0':{0,4}, 'y=5':{1,5}
}
for name,inds in facets.items():
    if name=='x=0': got={i for i,(a,b) in enumerate(A) if a==0}
    elif name=='x=5': got={i for i,(a,b) in enumerate(A) if a==5}
    elif name=='y=0': got={i for i,(a,b) in enumerate(A) if b==0}
    else: got={i for i,(a,b) in enumerate(A) if b==5}
    assert got==inds,(name,got)
# Along every facet, the two surviving exponent vectors differ by lattice length five,
# hence the boundary restriction is [u:v] -> [u^5:v^5].
for inds in facets.values():
    i,j=sorted(inds); dx=abs(A[i][0]-A[j][0]); dy=abs(A[i][1]-A[j][1])
    assert gcd(dx,dy)==5
# Homogenized sections on P1xP1 all have bidegree (5,5).
# entries are exponents (X0,X1,Y0,Y1)
sections=[(5,0,5,0),(5,0,0,5),(4,1,3,2),(4,1,2,3),(0,5,5,0),(0,5,0,5)]
assert all(e[0]+e[1]==5 and e[2]+e[3]==5 for e in sections)
print('VERIFY_OK')
