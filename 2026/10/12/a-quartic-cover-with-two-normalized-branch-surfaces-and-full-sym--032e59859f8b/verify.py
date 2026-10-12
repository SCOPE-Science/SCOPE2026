"""Exact symbolic checks for the finite quartic cover and its branch divisor.

Requires Python 3 and SymPy; run: python bs_cover_verify.py.
This verifies polynomial identities and rational parameterizations, not a
computational substitute for the irreducibility or monodromy arguments.
"""
import sympy as sp

x, y, z, u, v, w, t, X = sp.symbols('x y z u v w t X')
F = (y, y*z-x**2, z**2+y*x**2+y**2*z+x**3)
J = sp.factor(sp.det(sp.Matrix(F).jacobian((x,y,z))))
assert J == x*(4*z+4*y*y+3*x*y)

# Two quadratic relations are monic with coprime leading terms.
f = x**2 + sp.Rational(1,2)*u**2*x - u*t + v
g = (t**2 + (2*u**2-u**3/4)*t +
     (u**4/8-u**3-v)*x + u**2*v/4-u*v-w)
G = sp.groebner((f,g),x,t,order='grlex',domain=sp.QQ.frac_field(u,v,w))
assert len(G.polys) == 2
assert all(G.reduce(h)[1] == 0 for h in (f,g))
assert sp.expand(f.subs({u:y,v:F[1],t:z+y*x/2})) == 0
assert sp.expand(g.subs({u:y,v:F[1],w:F[2],t:z+y*x/2})) == 0

basis = [sp.Integer(1),x,t,x*t]
def multiply_by(h):
    cols=[]
    for b in basis:
        rem=sp.Poly(sp.expand(G.reduce(h*b)[1]),x,t)
        cols.append([rem.coeff_monomial(c) for c in basis])
    return sp.Matrix(4,4,lambda i,j:cols[j][i])
T = sp.Matrix(4,4,lambda i,j:sp.trace(multiply_by(basis[i]*basis[j])))

B1 = v**2 + u**3*v-u**2*w
C = sp.Rational(3,16)*u**5-u**4+sp.Rational(3,16)*u**2*v-u*v
D = sp.Rational(9,64)*u**4-u**3-v
H = (w-C)**2+sp.Rational(3,4)*u**2*D*(w-C)+(u**3+v)*D**2
assert sp.expand(T.det()-256*B1*H) == 0

# The ordinary quartic after inverting u has an extra u^4 chart factor.
q=X**4 + u**2*X**3+2*(v+u**3)*X**2+B1
assert sp.expand(q.subs({X:x,u:F[0],v:F[1],w:F[2]})) == 0
assert sp.expand(sp.discriminant(q,X)-256*u**4*B1*H) == 0

# Normalizations: R1 parametrizes the pinch point B1; R2 parametrizes H.
assert sp.expand(B1.subs({v:u*z,w:z**2+u**2*z})) == 0
W=sp.symbols('W')
assert sp.expand(B1.subs(w,W+u*v)-(v**2-u**2*W)) == 0
z2=-u**2-sp.Rational(3,4)*u*x
v2=sp.expand(u*z2-x**2)
w2=sp.expand(z2**2+u*x**2+u**2*z2+x**3)
assert sp.expand(H.subs({v:v2,w:w2})) == 0
quadratic=x**2+sp.Rational(3,4)*u**2*x+u**3+v
rem=sp.Poly(sp.expand(sp.rem(w2,quadratic,x)),x)
assert sp.expand(rem.coeff_monomial(x)-D) == 0
assert sp.expand(rem.coeff_monomial(1)-C) == 0
assert sp.factor((sp.Rational(3,4)*u**2)**2-4*(u**3+v)) != 0

# Independent exact Jacobian checks at smooth points of each ramification divisor.
Jac=sp.Matrix(F).jacobian((x,y,z))
for point in ((0,1,0),(1,1,sp.Rational(-7,4))):
    sub=dict(zip((x,y,z),point))
    A=Jac.subs(sub)
    assert A.rank()==2
    normal=sp.Matrix([sp.diff(J,var) for var in (x,y,z)])
    kernel=A.nullspace()[0]
    assert normal.dot(kernel).subs(sub) != 0

print('VERIFY_OK')
print('Trace discriminant = 256 * B1 * H; both ramification parameterizations checked.')
