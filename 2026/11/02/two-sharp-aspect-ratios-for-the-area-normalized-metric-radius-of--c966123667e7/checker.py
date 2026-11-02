"""Independent rational Voronoi tests for flat Klein-bottle metric radius.

The exact infinite statement has an analytic proof; these checks are finite diagnostics.
Requires only Python 3's standard library.
"""
from fractions import Fraction as F
from itertools import product
from math import isclose, sqrt


def analytic_eccentricity_sq(a, b, v):
    """Formula in the theorem; all inputs are positive rationals."""
    residue = (2 * v) % b
    delta = min(residue, b - residue)
    B = b - delta
    t = min(delta, a * a / B)
    return (a * a + B * B + (1 + B * B / (a * a)) * t * t) / 4


def squared_distance_from_deck(a,b,v,x,y):
    """Independent finite deck-image minimization, with an ample exact window."""
    return min(
        min((x-2*k*a)**2+(y-v-l*b)**2,
            (x-(2*k+1)*a)**2+(y+v-l*b)**2)
        for k,l in product(range(-3,4),repeat=2))


def voronoi_eccentricity_sq(a,b,v,window=2):
    """Enumerate exact rational vertices of a finite deck Voronoi diagram."""
    p = []
    for k,l in product(range(-window,window+1),repeat=2):
        if k or l:
            p.append((2*k*a,l*b))
        p.append(((2*k+1)*a,l*b-2*v))
    p = list(set(p))
    inequalities = [(dx,dy,(dx*dx+dy*dy)/2) for dx,dy in p]
    vertices = set()
    for i,(ax,ay,ac) in enumerate(inequalities):
        for bx,by,bc in inequalities[i+1:]:
            det=ax*by-ay*bx
            if det == 0: continue
            x=(ac*by-ay*bc)/det
            y=(ax*bc-ac*bx)/det
            if all(dx*x+dy*y<=c for dx,dy,c in inequalities):
                vertices.add((x,y))
    assert vertices, (a,b,v)
    return max(x*x+y*y for x,y in vertices),len(vertices)


def radius(a,b):
    return a*a/b+b/4 if 2*a<=b else a/2+b*b/(8*a)


def main():
    cases=[
        (F(1,5),F(1),F(0)),
        (F(1,5),F(1),F(1,8)),
        (F(1,5),F(1),F(1,4)),
        (F(1,3),F(1),F(1,10)),
        (F(1,3),F(1),F(1,4)),
        (F(1,2),F(1),F(1,4)),
        (F(2,3),F(1),F(1,8)),
        (F(4,5),F(1),F(1,4)),
        (F(1),F(1),F(1,10)),
        (F(3,2),F(1),F(1,4)),
        (F(2),F(3),F(2,7)),
    ]
    for a,b,v in cases:
        sq,n=voronoi_eccentricity_sq(a,b,v,2)
        assert sq==analytic_eccentricity_sq(a,b,v), (a,b,v,sq,analytic_eccentricity_sq(a,b,v))
        assert n>=3
    print('EXACT_INDEPENDENT_DECK_VORONOI_VERTEX_CASES_PASSED',len(cases))

    for a,b in [(F(1,5),F(1)),(F(1,4),F(1)),(F(1,2),F(1)),
                (F(3,4),F(1)),(F(5,4),F(1)),(F(2),F(1))]:
        vals=[analytic_eccentricity_sq(a,b,F(i,40)*b) for i in range(11)]
        assert all(vals[j]>vals[j+1] for j in range(10)), (a,b,vals)
        assert vals[-1]==radius(a,b)**2, (a,b,vals[-1],radius(a,b)**2)
        assert vals[0]==(a*a+b*b)/4
    print('EXACT_MONOTONE_ECCENTRICITY_AND_END_POINT_CASES_PASSED',6)

    for a,b,v,x,y in [(F(1,3),F(1),F(1,5),F(1,7),F(2,3)),
                         (F(3,2),F(2),F(1,4),F(3,5),F(3,7)),
                         (F(5,4),F(1),F(1,7),F(7,11),F(5,9))]:
        even_x=min(abs(x-2*k*a) for k in range(-3,4))
        odd_x=min(abs(x-(2*k+1)*a) for k in range(-3,4))
        even_y=min(abs(y-v-l*b) for l in range(-3,4))
        odd_y=min(abs(y+v-l*b) for l in range(-3,4))
        assert squared_distance_from_deck(a,b,v,x,y)==min(even_x**2+even_y**2,odd_x**2+odd_y**2)
    print('EXACT_EVEN_ODD_DECK_DISTANCE_DECOMPOSITION_PASSED')

    # Exact derivative factorisations, and nonisometry of the two sharp shapes.
    s1=1/(2*sqrt(3)); s2=sqrt(3)/2
    q1=(s1*s1+0.25)**2/s1
    q2=(4*s2*s2+1)**2/(64*s2**3)
    q=2/(3*sqrt(3))
    assert isclose(q1,q,rel_tol=1e-13)
    assert isclose(q2,q,rel_tol=1e-13)
    assert s1<.5<s2 and not isclose(s1,s2)
    for s in [0.05,0.2,0.25,0.4,0.5,0.7,0.99,1,2,10]:
        q_test=float(radius(F.from_float(s),F(1))**2 / F.from_float(s))
        assert q_test>q, (s,q_test,q)
    print('TWO_EQUAL_SHARP_AREA_NORMALIZED_OPTIMA_PASSED')
    print('ALL_CHECKS_PASSED')

if __name__=='__main__': main()
