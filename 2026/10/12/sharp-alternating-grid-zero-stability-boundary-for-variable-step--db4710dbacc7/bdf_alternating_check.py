"""Exact symbolic checks for alternating-step BDF parasitic multipliers.

Requires SymPy. Execute: python bdf_alternating_check.py
"""
import sympy as S

r, z = S.symbols('r z', positive=True)
x = S.Symbol('x')

def step_matrix(order, steps):
    assert len(steps) == order
    nodes = [S.Integer(0)]
    for h in steps:
        nodes.append(S.factor(nodes[-1] - h))
    w = []
    for j, tj in enumerate(nodes):
        basis = S.prod((z - nodes[k])/(tj-nodes[k])
                       for k in range(order+1) if k != j)
        w.append(S.factor(S.diff(basis,z).subs(z,0)))
    advance = [-w[j]/w[0] for j in range(1, order+1)]
    assert S.cancel(sum(advance) - 1) == 0
    # Differences d_n=y_n-y_(n-1) of the zero-equation solution.
    row = [-sum(advance[j:]) for j in range(1,order)]
    M = S.zeros(order-1)
    for j, q in enumerate(row): M[0,j] = S.factor(q)
    for j in range(1,order-1): M[j,j-1] = 1
    return M

def char(order):
    a = step_matrix(order, [r if i%2==0 else S.Integer(1) for i in range(order)])
    b = step_matrix(order, [S.Integer(1) if i%2==0 else r for i in range(order)])
    return S.Poly(S.cancel((b*a).charpoly(x).as_expr()),x)

def pos(expr):
    num, den = map(S.expand,S.fraction(S.cancel(expr)))
    # Strict positivity follows when both numerator and denominator
    # have nonnegative coefficients and nonzero constant/power terms.
    assert all(k >= 0 for k in S.Poly(num,r).coeffs())
    assert all(k >= 0 for k in S.Poly(den,r).coeffs())
    assert num != 0 and den != 0

# BDF2 monodromy is scalar.
P2 = char(2)
assert S.cancel(P2.as_expr().subs(x,0) + r/((1+2*r)*(r+2))) == 0

# BDF3 quadratic Schur inequalities.
P3 = char(3)
a,b = [S.factor(k) for k in P3.all_coeffs()[1:]]
for e in [1-b,1+a+b,1-a+b]: pos(e)

# BDF4 cubic Schur inequalities.
P4 = char(4)
a,b,c = [S.factor(k) for k in P4.all_coeffs()[1:]]
for e in [1-c,1+c,1+a+b+c,1-a+b-c,1-b+a*c-c*c]: pos(e)

# BDF5 quartic Schur reduction: the transformed cubic has
# parameters a,b,c and is Schur stable precisely when its four
# strict Jury inequalities hold, together with |e|<1.
P5 = char(5)
A,B,C,E = [S.factor(k) for k in P5.all_coeffs()[1:]]
assert S.factor(E) == 4*r*(r+1)**2*(r+2)*(2*r+1)/((4*r**3+30*r**2+63*r+40)*(40*r**3+63*r**2+30*r+4))
pos(1-E*E)
a = S.factor((A-E*C)/(1-E*E))
b = S.factor((B-E*B)/(1-E*E))
c = S.factor((C-E*A)/(1-E*E))
for expr in [1+c,1-c,1+a+b+c,1-b+a*c-c*c]: pos(expr)
H=4*r**6-8*r**5-83*r**4-143*r**3-83*r**2-8*r+4
D=160*r**6+1460*r**5+4566*r**4+6541*r**3+4566*r**2+1460*r+160
assert S.cancel(1-a+b-c+32*H/D) == 0
assert S.cancel(P5.as_expr().subs(x,-1)+32*H/((4*r**3+30*r**2+63*r+40)*(40*r**3+63*r**2+30*r+4))) == 0
assert S.factor(r**6*H.subs(r,1/r)-H) == 0
assert S.gcd(H,S.together(S.diff(P5.as_expr(),x).subs(x,-1)).as_numer_denom()[0]) == 1
# Exactly two positive roots: Descartes permits at most two, while
# H(0)>0, H(1)<0 and the leading coefficient is positive.
assert H.subs(r,0)>0 and H.subs(r,1)<0 and S.LC(S.Poly(H,r))>0
roots=[u for u in S.nroots(H,n=40,maxsteps=1000) if abs(S.im(u)) < S.Rational(1,10)**30 and S.re(u)>0]
assert len(roots)==2
lo,hi=sorted([float(S.re(u)) for u in roots])
assert abs(lo*hi-1)<1e-10
assert .1590<lo<.1591 and 6.288<hi<6.289
# Independent exact-rational checks by reconstructing the full
# recurrence and comparing characteristic polynomial coefficients.
for order in (2,3,4,5):
    for rat in (S.Rational(1,17),S.Rational(1,3),S.Integer(1),S.Rational(7,2),S.Integer(11)):
        M = step_matrix(order,[rat if j%2==0 else S.Integer(1) for j in range(order)])
        N = step_matrix(order,[S.Integer(1) if j%2==0 else rat for j in range(order)])
        expected = [S.factor(k.subs(r,rat)) for k in char(order).all_coeffs()]
        actual = [S.factor(k) for k in (N*M).charpoly(x).all_coeffs()]
        assert expected==actual
print('VERIFY_OK', 'r_minus=',lo,'r_plus=',hi)
