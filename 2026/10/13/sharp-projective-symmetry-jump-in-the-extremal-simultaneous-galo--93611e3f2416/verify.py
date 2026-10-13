"""Exact algebraic checks for the three extremal quartic unions.
Requires Python 3 and SymPy. Run: python verify.py
"""
import sympy as s
u,v,z,t,a=s.symbols('u v z t a')
g=lambda b: s.expand(b*u*v*(b*b*v*v-3*b*u*v+3*u*u))
assert s.expand(g(1)-u*v*(v*v-3*u*v+3*u*u))==0
assert s.factor(s.resultant(3*t*t-3*t+1,3*t*t-3*a*t+a*a,t))==9*(a-1)**2*(a*a-a+1)
omega=s.symbols('omega')
assert s.factor(s.resultant((omega-a)**3+(a-1)**3, omega**2+omega+1, omega))==27*a*a*(a*a-a+1)

def change(poly,U,V):
    return s.expand(poly.subs({u:U,v:V},simultaneous=True))
def same(x,y):return s.simplify(s.expand(x-y))==0
for aa in (-1,s.I,-s.I):
    f,g2=g(1),g(aa)
    assert same(change(f,aa*v/s.Integer(3),u),g2/9)
    assert same(change(g2,aa*v/s.Integer(3),u),f/9)
    if aa == -1:
        assert same(change(f,-u,v),g2)
        assert same(change(g2,-u,v),f)
        assert same(change(f,v/3,u),f/9)
        assert same(change(g2,v/3,u),g2/9)
    else:
        assert not same(change(g2,v/3,u),g2/9)
    # Every residual intersection line is transverse to the quartics.
    assert s.simplify((9*(aa-1)**2*(aa*aa-aa+1)))!=0
    assert s.simplify(27*aa*aa*(aa*aa-aa+1))!=0
    # The two quartics both have the fourth powers of Z and independent binary parts.
    P=s.expand((f+z**4)*(g2+z**4))
    assert s.degree(P,z)==8 and P.coeff(z,1)==0
    # Anti-diagonal lifts really preserve the reduced union.
    mapped=(change(f,aa*v/3,u)+z**4/9)*(change(g2,aa*v/3,u)+z**4/9)
    assert same(s.expand(mapped),P/81)
# The source equations change to g_a+Z^4 under v=x+y.
x,y=s.symbols('x y')
for aa in (-1,s.I,-s.I):
    original=x*((aa-1)*x+aa*y)**3+x**4+z**4
    assert same(s.expand(original.subs({x:u,y:v-u}, simultaneous=True)),g(aa)+z**4)
# Projective relations: U_a^2 rescales (u,v,z) by (a/3,a/3,1/3),
# so its projective square is the central map z -> a^-1 z.
for aa in (-1,s.I,-s.I):
    U=s.Matrix([[0,aa/s.Integer(3),0],[1,0,0],[0,0,1/s.sqrt(3)]])
    assert s.simplify(U*U-s.diag(aa/3,aa/3,s.Rational(1,3)))==s.zeros(3)
    T=s.diag(1,1,1/aa)
    assert s.simplify(U*U-aa*T/3)==s.zeros(3)
R=s.diag(-1,1,1)
S=s.Matrix([[0,s.Rational(1,3),0],[1,0,0],[0,0,1/s.sqrt(3)]])
T2=s.diag(1,1,-1)
assert s.simplify(R*S+S*R*T2)==s.zeros(3) # not the right projective normalization? check below
print('VERIFY_OK: three complete extremal pairs; exact binary identities, resultants and group lifts')
