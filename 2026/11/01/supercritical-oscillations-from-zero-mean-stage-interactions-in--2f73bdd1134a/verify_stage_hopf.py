"""Symbolic and finite checks for a two-stage, two-species Hopf theorem.

Requires Python 3 and SymPy. This checks algebraic identities; the
infinite-parameter theorem rests on the analytical inequalities and Hopf
argument stated in RESULT.md.
"""
import sympy as sp

u, d, tau = sp.symbols('u d tau', real=True)
z = sp.Symbol('z')
w = 2*d + 2 + tau
H = sp.Matrix([[-1, -1], [-1, -1]])
M = sp.Matrix([[w/2, -u-w/2], [u-w/2, w/2]])
R = sp.Matrix([[2+u-d, d], [d, 2-u-d]])
ones = sp.ones(2, 1)
assert sp.simplify(sum(M)) == 0
b = H*ones + M*ones
assert sp.simplify(b-sp.Matrix([-u-2, u-2])) == sp.zeros(2, 1)
J_plus = sp.simplify(R+H+M+sp.diag(*b))
J_minus = sp.simplify(R+H-M+sp.diag(*b))
assert sp.simplify(J_plus-sp.Matrix([[tau/2, -u-2-tau/2],
                                     [u-2-tau/2, tau/2]])) == sp.zeros(2)
assert sp.simplify(J_minus-sp.Matrix([[-2*d-2-tau/2, 2*d+u+tau/2],
                                      [2*d-u+tau/2, -2*d-2-tau/2]])) == sp.zeros(2)
p_plus = sp.factor(J_plus.charpoly(z).as_expr())
p_minus = sp.factor(J_minus.charpoly(z).as_expr())
assert sp.simplify(p_plus-(z**2-tau*z+u**2-4-2*tau)) == 0
assert sp.simplify(p_minus-(z**2+(4*d+4+tau)*z+(8*d+4+2*tau+u**2))) == 0

# Derive the nonlinear restriction to the species-exchange fixed plane.
x, y = sp.symbols('x y', real=True)
v = sp.Matrix([x, y])
F = sp.simplify(R*v+sp.diag(x, y)*(H+M)*v)
assert F.subs({x: 1, y: 1}) == sp.zeros(2, 1)
assert sp.simplify(F.jacobian((x,y)).subs({x:1,y:1})-J_plus) == sp.zeros(2)
X, Y = sp.symbols('X Y', real=True)
F0 = [sp.expand(q.subs({x:1+X,y:1+Y,tau:0})) for q in F]
assert sp.simplify(F0[0]-(-(u+2)*Y+d*X**2-(d+u+2)*X*Y)) == 0
assert sp.simplify(F0[1]-((u-2)*X+(u-d-2)*X*Y+d*Y**2)) == 0

# Canonical planar Hopf variables, with frequency Omega and s = Omega/(u+2).
A, B = u+2, u-2
omega = sp.sqrt(A*B)
s = omega/A
h, k = sp.symbols('h k', real=True)
Q = sp.expand(F0[0].subs({X:h, Y:s*k}) + omega*k)
P = sp.expand(F0[1].subs({X:h,Y:s*k})/s-omega*h)
fxx = sp.diff(Q,h,2).subs({h:0,k:0})
fxy = sp.diff(Q,h,k).subs({h:0,k:0})
fyy = sp.diff(Q,k,2).subs({h:0,k:0})
gxx = sp.diff(P,h,2).subs({h:0,k:0})
gxy = sp.diff(P,h,k).subs({h:0,k:0})
gyy = sp.diff(P,k,2).subs({h:0,k:0})
# Quadratic-only Poincare-Lyapunov coefficient with canonical
# linearization h'=-Omega k, k'=Omega h.
l1 = (fxy*(fxx+fyy)-gxy*(gxx+gyy)-fxx*gxx+fyy*gyy)/(16*omega)
assert sp.simplify(l1 + d*u/(4*(u+2))) == 0

# Check the full four-dimensional Jacobian block decomposition.
a,b1,c,e=sp.symbols('a b1 c e',real=True)
v1=sp.Matrix([a,b1]); v2=sp.Matrix([c,e])
F4 = sp.Matrix.vstack(R*v1+sp.diag(a,b1)*(H*v1+M*v2),
                      R*v2+sp.diag(c,e)*(H*v2+M*v1))
J4=sp.simplify(F4.jacobian((a,b1,c,e)).subs({a:1,b1:1,c:1,e:1}))
assert sp.simplify(J4-sp.Matrix.vstack(sp.Matrix.hstack(J_plus-M,M),
                                      sp.Matrix.hstack(M,J_plus-M)))==sp.zeros(4)
assert sp.factor(J4.charpoly(z).as_expr()-p_plus*p_minus)==0

# Exact positive-parameter sample: (u,d,w)=(3,6,14).
assert R.subs({u:3,d:6}) == sp.Matrix([[-1,6],[6,-7]])
assert M.subs({u:3,d:6,tau:0}) == sp.Matrix([[7,-10],[-4,7]])
assert sp.factor(p_plus.subs({u:3,d:6,tau:0})) == z*z+5
assert sp.factor(p_minus.subs({u:3,d:6,tau:0})) == z*z+28*z+61
assert sp.simplify(l1.subs({u:3,d:6})+sp.Rational(9,10))==0

for uu,dd in [(sp.Rational(5,2), 5), (3, 6), (4, 8), (7, 10)]:
    assert dd>uu+2
    for tt in [sp.Rational(-1,2), sp.Rational(-1,10), 0,
               sp.Rational(1,10), sp.Rational(1,2)]:
        ww=2*dd+2+tt
        assert ww>0
        jp=J_plus.subs({u:uu,d:dd,tau:tt})
        jm=J_minus.subs({u:uu,d:dd,tau:tt})
        assert sp.trace(jm)<0 and jm.det()>0
        if tt<0: assert sp.trace(jp)<0 and jp.det()>0
        if tt>0: assert sp.trace(jp)>0
        if tt==0: assert sp.trace(jp)==0 and jp.det()>0
print('PASS: symbolic identities, full Jacobian, exact Hopf coefficient, and 20 rational cases')
