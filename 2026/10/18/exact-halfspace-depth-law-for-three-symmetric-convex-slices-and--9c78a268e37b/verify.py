"""Exact-rational finite tests for a three-slice halfspace-depth identity.

This checks geometric integration identities at selected directions and cuts.
It is not an exhaustive verification over all directions or a proof of the theorem.
"""
from fractions import Fraction as Q
from itertools import product

def polygon_area(poly):
    if not poly:
        return Q(0)
    return abs(sum(x*y1-y*x1 for (x,y),(x1,y1) in zip(poly,poly[1:]+poly[:1])))/2

def tail_area(poly, nx, ny, threshold):
    if not poly:
        return Q(0)
    side=lambda p: nx*p[0]+ny*p[1]-threshold
    out=[]
    for p,q in zip(poly,poly[1:]+poly[:1]):
        a,b=side(p),side(q)
        if a>=0:
            out.append(p)
        if (a<0 and b>0) or (a>0 and b<0):
            out.append(((b*p[0]-a*q[0])/(b-a),(b*p[1]-a*q[1])/(b-a)))
        elif a<0 and b==0:
            out.append(q)
    return polygon_area(out)

def rect(x,y):
    return [(-Q(x),-Q(y)),(Q(x),-Q(y)),(Q(x),Q(y)),(-Q(x),Q(y))]

cases=[
    (rect(Q(1,2),Q(1,2)),[(Q(-2),Q(-1)),(Q(1),Q(-2)),(Q(2),Q(1)),(Q(-1),Q(2))],rect(1,1)),
    (rect(2,Q(1,2)),[(Q(-2),Q(0)),(Q(0),Q(-2)),(Q(2),Q(0)),(Q(0),Q(2))],rect(Q(1,2),2)),
    (rect(2,2),rect(1,2),rect(Q(1,2),Q(1,2))),
]
checks=0
for p0,p1,p2 in cases:
    a,b,c=map(polygon_area,(p0,p1,p2))
    for nx,ny in product(range(-3,4),repeat=2):
        if (nx,ny)==(0,0):
            continue
        for cut in [Q(-8),Q(-3),Q(-1),Q(-1,2),Q(0),Q(1,2),Q(1),Q(3),Q(8)]:
            f0=tail_area(p0,Q(nx),Q(ny),cut)
            f1=tail_area(p1,Q(nx),Q(ny),Q(0))
            f2=tail_area(p2,Q(nx),Q(ny),-cut)
            f2positive=tail_area(p2,Q(nx),Q(ny),cut)
            assert 2*f1==b
            assert f2+f2positive==c
            assert f0+f1+f2==b/2+c+f0-f2positive
            checks+=3

# A nonnested pair with equal area has a strictly positive cap-volume discrepancy.
p0,p1,p2=cases[1]
a,c=polygon_area(p0),polygon_area(p2)
assert a==c==4
assert tail_area(p0,Q(1),Q(0),Q(1))==1
assert tail_area(p2,Q(1),Q(0),Q(1))==0
checks+=3

# The nested classes have explicit limiting halfspace witnesses for the
# middle-center depth, while the large outer center supplies the other bound.
for p0,p1,p2 in (cases[0],cases[2]):
    a,b,c=map(polygon_area,(p0,p1,p2))
    f_early=tail_area(p0,Q(1),Q(0),Q(-30))+b/2+tail_area(p2,Q(1),Q(0),Q(30))
    f_late=tail_area(p0,Q(1),Q(0),Q(30))+b/2+tail_area(p2,Q(1),Q(0),Q(-30))
    assert f_early==b/2+a and f_late==b/2+c
    checks+=2

# Check the sharp quarter infimum for nested homothetic stacks in d=2.
for n in range(1,30):
    a=Q(1,n*n)
    depth=(Q(2)+a)/(Q(8)+a)
    assert depth>Q(1,4)
    checks+=1
# Sharp one-third family, using L=n^2 and the rational threshold t=1/n.
for n in (2,3,5,7,11,17,31):
    L=Q(n*n)
    left=rect(L,1/L)
    right=rect(1/L,L)
    assert polygon_area(left)==polygon_area(right)==4
    threshold=Q(1,n)
    cap_difference=tail_area(left,Q(1),Q(0),threshold)-tail_area(right,Q(1),Q(0),threshold)
    assert cap_difference==2-Q(2,n**3)
    assert (Q(6)-cap_difference)/12==Q(1,3)+Q(1,6*n**3)
    checks+=4
print(f'VERIFY_OK exact_rational_assertions={checks} cases={len(cases)}')
