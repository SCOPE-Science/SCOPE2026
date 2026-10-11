"""Exact-arithmetic face-slice checks for a one-parameter family of cube sections.

The argument establishing the formula and inequalities is analytic; this script
independently reconstructs sample polygon sections from cube edges.
"""
from fractions import Fraction as F
from itertools import product, combinations


def det(a, b, c):
    return (b[0]-a[0])*(c[1]-a[1])-(b[1]-a[1])*(c[0]-a[0])


def convex_hull(points):
    pts=sorted(set(points))
    if len(pts)<3:
        return []
    lo=[]
    for q in pts:
        while len(lo)>1 and det(lo[-2],lo[-1],q)<=0:
            lo.pop()
        lo.append(q)
    hi=[]
    for q in pts[::-1]:
        while len(hi)>1 and det(hi[-2],hi[-1],q)<=0:
            hi.pop()
        hi.append(q)
    return lo[:-1]+hi[:-1]


def area_coefficient(weights, level):
    """A polygon area is this rational coefficient times ||weights||."""
    w=tuple(map(F,weights)); t=F(level)
    assert any(x!=0 for x in w)
    points=set()
    for k in range(3):
        others=[i for i in range(3) if i!=k]
        for a,b in product((-1,1),repeat=2):
            p=[F(0)]*3; p[others[0]]=F(a);p[others[1]]=F(b)
            lo=list(p);hi=list(p);lo[k]=F(-1);hi[k]=F(1)
            vlo=sum(w[i]*lo[i] for i in range(3))
            vhi=sum(w[i]*hi[i] for i in range(3))
            if vlo==t: points.add(tuple(lo))
            if vhi==t: points.add(tuple(hi))
            if (vlo-t)*(vhi-t)<0:
                lam=(t-vlo)/(vhi-vlo)
                points.add(tuple(lo[i]+lam*(hi[i]-lo[i]) for i in range(3)))
    axis=next(i for i,v in enumerate(w) if v!=0)
    free=[j for j in range(3) if j!=axis]
    hull=convex_hull((p[free[0]],p[free[1]]) for p in points)
    if not hull: return F(0)
    shoelace=sum(hull[i][0]*hull[(i+1)%len(hull)][1]-hull[i][1]*hull[(i+1)%len(hull)][0] for i in range(len(hull)))
    return abs(shoelace)/(2*abs(w[axis]))


def actual_coeffs(s):
    w=(F(1),F(1),F(1),F(1),F(s))
    coef_special=F(0);coef_regular=F(0)
    for i,j in combinations(range(5),2):
        remaining=[k for k in range(5) if k not in (i,j)]
        for ei,ej in product((-1,1),repeat=2):
            lev=-ei*w[i]-ej*w[j]
            k=area_coefficient([w[z] for z in remaining],lev)
            if 4 in (i,j): coef_regular+=k
            else: coef_special+=k
    return coef_special,coef_regular


def formula_coeffs(s):
    s=F(s)
    if s<=2:
        return 6*(8-s),4*(8-s*s)
    if s<=4:
        return 12*(8-(4-s)**2/2)/s,4*(4-s)**2
    return 96/s,F(0)


def main():
    test=[F(0),F(1,8),F(1,3),F(1,2),F(2,3),F(3,4),F(1),F(5,4),F(3,2),F(2),F(9,4),F(5,2),F(3),F(7,2),F(4),F(5),F(10),F(100)]
    for s in test:
        got=actual_coeffs(s)
        want=formula_coeffs(s)
        assert got==want, (s,got,want)
    print('EXACT_RIDGE_FACE_SLICES_OK',len(test))
    # Sliced-cube contributions are nonnegative and the identity at endpoints is exact.
    assert formula_coeffs(F(0))==(48,32)
    assert formula_coeffs(F(1))==(42,28)
    assert formula_coeffs(F(2))==(36,16)
    assert formula_coeffs(F(4))==(24,0)
    print('EXACT_ENDPOINTS_OK')

if __name__=='__main__':
    main()
