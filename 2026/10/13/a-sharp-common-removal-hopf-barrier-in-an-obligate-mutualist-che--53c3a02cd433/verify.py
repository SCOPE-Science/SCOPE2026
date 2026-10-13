"""Exact rational symbolic checks for the symmetric obligate-mutualist chemostat.

Run with Python 3 and SymPy. The global theorems require the accompanying
analytic proof; this script verifies their stated algebraic inputs and the
nondegenerate Hopf example.
"""
import sympy as sp

S, x, x1, x2, K = sp.symbols('S x x1 x2 K', real=True)
D, d, Sin, L = sp.Rational(1), sp.Rational(5), sp.Rational(11), sp.Rational(19)
K0 = sp.Rational(3, 5)
m = 100 * (1 + K)

def grow(s, z):
    return m * s * z / ((K + s) * (L + z))

F3 = sp.Matrix([
    D*(Sin-S)-x1*grow(S,x2)-x2*grow(S,x1),
    x1*(grow(S,x2)-d),
    x2*(grow(S,x1)-d)
])
pars = {S: 1, x1: 1, x2: 1, K: K0}
assert all(sp.simplify(v.subs(pars)) == 0 for v in F3)
J3 = sp.simplify(F3.jacobian([S,x1,x2]).subs(pars))
anti = sp.Matrix([0, 1, -1]); assert J3*anti == -sp.Rational(19,4)*anti

f = grow(S,x)
P = sp.Matrix([D*(Sin-S)-2*x*f, x*(f-d)])
A = sp.simplify(P.jacobian([S,x]).subs({S:1,x:1,K:K0}))
assert A == sp.Matrix([[-sp.Rational(19,4),-sp.Rational(39,2)],
                       [sp.Rational(15,8),sp.Rational(19,4)]])
assert sp.trace(A) == 0 and A.det() == 14
assert sp.simplify(sp.trace(P.jacobian([S,x])).subs({S:1,x:1}) +
                   D + 2*d*K/(1+K) - d*sp.Rational(19,20)) == 0
assert sp.simplify(sp.diff(sp.trace(P.jacobian([S,x])).subs({S:1,x:1}),K).subs(K,K0)
                   + sp.Rational(125,32)) == 0

# Transform the *full nonlinear* symmetric-plane vector field into
# U'=-omega*V+F(U,V), V'=omega*U+G(U,V).
U,V = sp.symbols('U V',real=True)
omega=sp.sqrt(14)
M=sp.Matrix([[1,0],[-sp.Rational(19,78),2*omega/39]])
uv0=sp.Matrix([1,1])+M*sp.Matrix([U,V]); assert sp.simplify(M.det())!=0
X=sp.simplify(M.inv()*P.subs({S:uv0[0],x:uv0[1],K:K0},simultaneous=True))
Q=sp.simplify(X[0]+omega*V)
R=sp.simplify(X[1]-omega*U)
assert all(sp.simplify(sp.diff(z,k).subs({U:0,V:0}))==0
           for z in (Q,R) for k in (U,V))

def deriv(expr, a,b):
    return sp.simplify(sp.diff(expr,U,a,V,b).subs({U:0,V:0}))

cub = (deriv(Q,3,0)+deriv(Q,1,2)+deriv(R,2,1)+deriv(R,0,3))/16
quad = (deriv(Q,1,1)*(deriv(Q,2,0)+deriv(Q,0,2))
        -deriv(R,1,1)*(deriv(R,2,0)+deriv(R,0,2))
        -deriv(Q,2,0)*deriv(R,2,0)
        +deriv(Q,0,2)*deriv(R,0,2))/(16*omega)
l1=sp.simplify(cub+quad)
assert l1 == -sp.Rational(40879,532480), l1

# The fold scalar derivative vanishes exactly at q and has positive curvature.
y,a,Delta,Kf,Lf,mf,df = sp.symbols('y a Delta Kf Lf mf df',positive=True)
H=df*Kf*(Lf+y)/(a*y-df*Lf)+2*df*y/Delta
assert sp.simplify(sp.diff(H,y)+df*Kf*(a+df)*Lf/(a*y-df*Lf)**2-2*df/Delta)==0
assert sp.simplify(sp.diff(H,y,2)-2*a*df*Kf*(a+df)*Lf/(a*y-df*Lf)**3)==0
print('VERIFY_OK')
