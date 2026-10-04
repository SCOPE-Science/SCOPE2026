import sympy as sp

x,y,z,w = sp.symbols('x y z w', real=True)
a,b,c,alpha,eps,beta,xi = sp.symbols('a b c alpha eps beta xi', nonzero=True, real=True)
F = z + alpha*sp.sin(z)
G = beta + 3*xi*w**2
X = sp.Matrix([
    a*y,
    -x + y*(b*F + c*G),
    eps - y**2,
    y,
])
I = w - x/a
gradI = sp.Matrix([sp.diff(I,q) for q in (x,y,z,w)])
assert sp.simplify((gradI.T*X)[0]) == 0

K = sp.symbols('K', real=True)
subs_w = x/a + K
XK = sp.Matrix([
    sp.simplify(X[0].subs(w,subs_w)),
    sp.simplify(X[1].subs(w,subs_w)),
    sp.simplify(X[2].subs(w,subs_w)),
    sp.Integer(0),
])
assert XK[3] == 0
J = XK.jacobian((x,y,z,K))
assert all(sp.simplify(J[3,j]) == 0 for j in range(4))

# For an equilibrium, xdot=0 and a!=0 imply y=0. Then zdot=eps,
# so eps>0 excludes every equilibrium.
assert sp.simplify(X[2].subs(y,0)) == eps

aval = sp.Rational(1,20)
def leaf_value(pt):
    xv,yv,zv,wv = map(sp.Rational, pt)
    return sp.simplify(wv - xv/aval)
assert leaf_value(('0.1','0','0','0')) == -2
assert leaf_value(('0.1','0.2','0.3','0')) == -2

print('VERIFY_OK')
