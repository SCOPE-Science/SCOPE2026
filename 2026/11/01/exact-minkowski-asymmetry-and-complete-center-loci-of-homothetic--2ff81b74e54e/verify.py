"""Independent finite-polytope tests for the homothetic-frustum Minkowski-asymmetry formula.

The universal proof uses vertex-free convex containment; this checker tests exact
rational inclusions and independent linear programs on three unequal base types.
"""
from fractions import Fraction as F
from itertools import product
from scipy.optimize import linprog


def dot(x, y):
    return sum(a*b for a,b in zip(x,y))


def families():
    tri = [(F(0),F(0)),(F(3),F(0)),(F(0),F(2))]
    tri_facets = [((F(-1),F(0)),F(0)),((F(0),F(-1)),F(0)),((F(1,3),F(1,2)),F(1))]
    square = list(product([F(-1),F(1)],repeat=2))
    sq_facets = [((F(1),F(0)),F(1)),((F(-1),F(0)),F(1)),((F(0),F(1)),F(1)),((F(0),F(-1)),F(1))]
    prod_vertices = [(x,y,z) for (x,y),z in product(tri,[F(-1),F(1)])]
    prod_facets = [((u[0],u[1],F(0)),h) for (u,h) in tri_facets] + [((F(0),F(0),F(e)),F(1)) for e in [-1,1]]
    return [
        ('asymmetric_triangle',tri,tri_facets,F(2),[(F(1),F(2,3))]),
        ('centrally_symmetric_square',square,sq_facets,F(1),[(F(0),F(0))]),
        ('triangle_times_segment',prod_vertices,prod_facets,F(2),[(F(1),F(2,3),F(-1,3)),(F(1),F(2,3),F(0)),(F(1),F(2,3),F(1,3))]),
    ]


def check_exact(base, facets, s, centers, t):
    m=len(base[0]); k=1-t; lam=s+k
    vertices=[(*v,F(0)) for v in base] + [(*(t*x for x in v),F(1)) for v in base]
    ambient_facets=[((*u,k*h),h) for u,h in facets]
    ambient_facets += [((*(F(0) for _ in range(m)),F(-1)),F(0)),((*(F(0) for _ in range(m)),F(1)),F(1))]
    for mid in centers:
        q=tuple((s+1)/(lam+1)*coord for coord in mid)
        c=(*q,F(1)/(lam+1))
        w=tuple((lam+1)*z for z in c)
        for v in vertices:
            reflected=tuple(wi-vi for wi,vi in zip(w,v))
            for a,h in ambient_facets:
                assert dot(a,reflected)<=lam*h, (t,mid,v,a)
        # The source base's containment certificate must also hold exactly.
        for v in base:
            for u,h in facets:
                assert dot(u, tuple((s+1)*mi-vi for mi,vi in zip(mid,v)))<=s*h
    return vertices,ambient_facets


def solve_lp(vertices,facets):
    # Independently minimize lambda over all possible centers using the full
    # V-to-H facet containment constraints, without imposing axial symmetry.
    A=[];rhs=[];m=len(vertices[0]);
    for a,h in facets:
        for v in vertices:
            A.append([float(q) for q in a]+[-float(h)])
            rhs.append(float(dot(a,v)))
    res=linprog([0.]*m+[1.],A_ub=A,b_ub=rhs,
                bounds=[(None,None)]*m+[(1.,None)],method='highs')
    assert res.success,res.message
    return res.x[-1]


def main():
    n=0
    for name,base,facets,s,centers in families():
        for t in [F(0),F(1,5),F(1,2),F(4,5),F(1)]:
            vertices,ambient_facets=check_exact(base,facets,s,centers,t)
            result=solve_lp(vertices,ambient_facets)
            expected=float(s+1-t)
            assert abs(result-expected)<2e-8,(name,t,result,expected)
            n+=1
    print('EXACT_RATIONAL_VERTEX_FACET_REFLECTION_INCLUSIONS_PASSED')
    print('INDEPENDENT_UNRESTRICTED_LP_OPTIMA_PASSED',n)
    print('NONUNIQUE_MINKOWSKI_CENTER_FAMILY_ENDPOINTS_PASSED')
    print('PYRAMID_AND_PRISM_BOUNDARIES_PASSED')
    print('ALL_CHECKS_PASSED')

if __name__=='__main__':
    main()
