"""Independent exact-arithmetic checks for the central cuboctahedron section formula.
Requires only the Python standard library. Finite checks do not prove the theorem."""
from fractions import Fraction as F
from itertools import product, permutations
from math import gcd
V=sorted({tuple(p) for x,y in product((-1,1),repeat=2) for p in permutations((0,x,y))})
E=[(V[i],V[j]) for i in range(12) for j in range(i) if sum((V[i][k]-V[j][k])**2 for k in range(3))==2]
assert len(V)==12 and len(E)==24

def hull_area_projected(a,b,c,level=0):
    points=set()
    for p,q in E:
        x=a*p[0]+b*p[1]+c*p[2]-level
        y=a*q[0]+b*q[1]+c*q[2]-level
        if x==0: points.add((F(p[1]),F(p[2])))
        if y==0: points.add((F(q[1]),F(q[2])))
        if x*y<0:
            points.add((F(y*p[1]-x*q[1],y-x),F(y*p[2]-x*q[2],y-x)))
    pts=sorted(points)
    def det(o,p,q):return (p[0]-o[0])*(q[1]-o[1])-(p[1]-o[1])*(q[0]-o[0])
    lower=[]
    for p in pts:
        while len(lower)>=2 and det(lower[-2],lower[-1],p)<=0:lower.pop()
        lower.append(p)
    upper=[]
    for p in reversed(pts):
        while len(upper)>=2 and det(upper[-2],upper[-1],p)<=0:upper.pop()
        upper.append(p)
    h=lower[:-1]+upper[:-1]
    area=sum(h[i][0]*h[(i+1)%len(h)][1]-h[i][1]*h[(i+1)%len(h)][0] for i in range(len(h)))/2
    # dA_plane = ||u||/a * d(y,z), so return A/||u||.
    return area/F(a), len(h)

n=0
for a in range(1,19):
    for b in range(a+1):
        for c in range(b+1):
            if gcd(gcd(a,b),c)>1: continue
            val,nv=hull_area_projected(a,b,c)
            if a==b==c:
                assert val==F(3,a)
            else:
                expected=F(2*(2*a*a+2*a*b-b*b-3*c*c),(a+b)*(a*a-c*c))
                assert val==expected,(a,b,c,val,expected)
            n+=1
print('CUBOCTAHEDRON_SECTION_FORMULA_OK cases='+str(n)+' vertices=12 edges=24')

for i in range(81):
    h=F(i,40)
    val,nv=hull_area_projected(1,1,1,h)
    expected=(h*h-12*h+24)/8
    assert val==expected,(h,val,expected)
print('DIAGONAL_AFFINE_PROFILE_OK rational_offsets=81')
