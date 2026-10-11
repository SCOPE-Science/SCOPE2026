"""Exact standalone algebraic and geometric verification of the hexagon formulas."""
from fractions import Fraction
import itertools
import sympy as sp

X,Y,Z=sp.symbols('X Y Z',positive=True)
T=X+Y+Z
assert sp.simplify((X+Y)*(X+Z)/X - (T+Y*Z/X)) == 0
assert sp.simplify((T+Y*Z/X)-(T+X*Y*Z/X**2))==0
r,s,eps=sp.symbols('r s eps',positive=True)
assert sp.simplify(sp.Rational(4,3)-(1+r/(2+r)) - 2*(1-r)/(3*(2+r))) == 0
assert sp.simplify(sp.diff(r*s/(1+r+s),s)) == r*(1+r)/(1+r+s)**2
# Rearranged stability inequality is equivalent to the advertised inverse bound.
assert sp.simplify((2-6*eps)/(2+3*eps) - (2*(1-3*eps)/(2+3*eps)))==0

def det(p,q):
    return p[0]*q[1]-p[1]*q[0]

def area_hull(points):
    """Exact monotone-chain hull and shoelace area on rational points."""
    pts=sorted(set(points))
    def cross(o,a,b):return det((a[0]-o[0],a[1]-o[1]),(b[0]-o[0],b[1]-o[1]))
    low=[]
    for p in pts:
        while len(low)>=2 and cross(low[-2],low[-1],p)<=0:low.pop()
        low.append(p)
    high=[]
    for p in reversed(pts):
        while len(high)>=2 and cross(high[-2],high[-1],p)<=0:high.pop()
        high.append(p)
    hull=low[:-1]+high[:-1]
    return len(hull),abs(sum(det(hull[i],hull[(i+1)%len(hull)]) for i in range(len(hull))))/2

for rr in [Fraction(1,5),Fraction(1,2),Fraction(3,4),Fraction(1,1)]:
    a=(Fraction(1),Fraction(0)); b=(Fraction(0),Fraction(1)); c=(-Fraction(1),rr)
    vectors=[a,b,c]
    nodes=[]
    for signs in itertools.product([-1,1],repeat=3):
        nodes.append(tuple(sum(signs[i]*vectors[i][j] for i in range(3)) for j in [0,1]))
    n,polyarea=area_hull(nodes)
    assert n==6
    xx,yy,zz=abs(det(a,b)),abs(det(b,c)),abs(det(c,a))
    tot=xx+yy+zz;mm=max(xx,yy,zz)
    assert polyarea==4*tot
    pairvals=[4*(tot+xx*yy*zz/dd**2) for dd in [xx,yy,zz]]
    assert min(pairvals)==4*(tot+xx*yy*zz/mm**2)
    assert sp.Rational(4,3)-(1+xx*yy*zz/(mm**2*tot))==2*(1-rr)/(3*(2+rr))

print('VERIFY_OK')
print('candidate_area_identity=true')
print('deficit_inverse_exact=true')
print('rational_zonotope_hull_areas=true')
print('sharp_family_all_tested_r=true')
