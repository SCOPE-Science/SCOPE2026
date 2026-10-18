"""Exact symbolic check for the diameter formulas of complementary chainlink sections.

Requires Python 3 and SymPy. All coefficients and comparisons are rational.
The test proves the vertex census and all 15 diameter comparisons for each
section simultaneously for every integer m >= 3; it is not a finite sample.
"""
from itertools import combinations
import sympy as S

m = S.symbols('m', integer=True, positive=True)

LOW = [
 (0, 3*m/2, m/2),
 (0, m-1, m+1),
 (m+2, 0, m-2),
 ((m-1)/2, 0, (3*m+1)/2),
 ((3*m+2)/2, (m-2)/2, 0),
 (m, m, 0),
]
HIGH = [
 (2*m+2, m, m+1),
 (2*m+2, (3*m+1)/2, (m+1)/2),
 (m+3, 2*m, m),
 (m/2+1, 2*m, 3*m/2+2),
 (3*m/2+2, m/2, 2*m+1),
 (m, m+2, 2*m+1),
]

def eq(x, y):
    return S.simplify(x-y) == 0

def inequalities(t):
    # The coordinates are (x,y,t-x-y); the result is A*x+B*y<=C.
    return [(-1,0,0), (1,0,2*m+2), (0,-1,0), (0,1,2*m),
            (1,1,t), (-1,-1,2*m+1-t),
            (1,-1,m+2), (1,2,t+m), (-2,-1,m+1-t)]

def affine_slope(expr):
    expr = S.expand(expr)
    assert S.diff(expr,m,2) == 0
    return S.diff(expr,m)

def certify(t, expected, diameter_squared, witness_pairs):
    I=inequalities(t)
    accepted=set()
    intersections=0
    for (i,(a,b,c)),(j,(d,e,f)) in combinations(enumerate(I),2):
        det=a*e-b*d
        if det == 0:
            continue
        intersections += 1
        x=S.cancel((c*e-b*f)/det)
        y=S.cancel((a*f-c*d)/det)
        z=S.cancel(t-x-y)
        residual=[S.expand(u*x+v*y-w) for u,v,w in I]
        feasible_all=all(v.subs(m,3)<=0 and affine_slope(v)<=0
                         for v in residual)
        if feasible_all:
            accepted.add(tuple(map(S.expand,(x,y,z))))
        else:
            # Every excluded line intersection violates one inequality
            # strictly for the entire parameter half-line m>=3.
            assert any(v.subs(m,3)>0 and affine_slope(v)>=0
                       for v in residual), (t,i,j,residual)
    E={tuple(map(S.expand,p)) for p in expected}
    assert accepted==E, (t,accepted-E,E-accepted)
    assert len(E)==6
    # Check the full all-pairs squared diameter analytically.
    for p,q in combinations(expected,2):
        dsq=S.expand(sum((p[k]-q[k])**2 for k in range(3)))
        gap=S.Poly(S.expand((diameter_squared-dsq).subs(m,m+3)), m)
        assert all(c>=0 for c in gap.all_coeffs()),(t,p,q,gap)
    for i,j in witness_pairs:
        p,q=expected[i-1],expected[j-1]
        dsq=S.expand(sum((p[k]-q[k])**2 for k in range(3)))
        assert eq(dsq,diameter_squared),(t,i,j,dsq)
    print('t =',t,':',len(E),'vertices,',intersections,
          'line intersections classified, 15 global distance bounds proved')

certify(2*m,LOW,7*m*m/2+5*m+2,[(1,5),(2,5)])
certify(4*m+3,HIGH,7*m*m/2+11*m/2+S.Rational(7,2),[(2,4)])
assert S.expand((7*m*m/2+11*m/2+S.Rational(7,2))-(7*m*m/2+5*m+2))==(m+3)/2
assert S.limit(S.sqrt(7*m*m/2+11*m/2+S.Rational(7,2))-
               S.sqrt(7*m*m/2+5*m+2),m,S.oo)==1/(2*S.sqrt(14))
print('All infinite-parameter diameter, gap and limit assertions passed.')
