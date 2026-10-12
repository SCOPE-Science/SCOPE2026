import sympy as sp

x,y,z,t,lam,b,m = sp.symbols('x y z t lam b m')
I=sp.I

def q(L, X=x, Y=y, Z=z):
    return sp.expand(Y**2 + X*Z + L*X**2)

# Additive one-parameter subgroup U_t.
Xp=x
Yp=y+t*x
Zp=z-2*t*y-t**2*x
assert sp.expand(q(lam,Xp,Yp,Zp)-q(lam)) == 0

# Order-four lift of the reflection lambda -> m+1-lambda.
M=m+1
Xp=x
Yp=I*y
Zp=-M*x-z
assert sp.expand(q(lam,Xp,Yp,Zp) + q(M-lam)) == 0

U=sp.Matrix([[1,0,0],[t,1,0],[-t**2,-2*t,1]])
R=sp.Matrix([[1,0,0],[0,I,0],[-M,0,-1]])
D=sp.diag(1,-1,1)
assert sp.simplify(R**2-D) == sp.zeros(3)
assert sp.simplify(R**4-sp.eye(3)) == sp.zeros(3)
Ui=sp.Matrix([[1,0,0],[I*t,1,0],[-(I*t)**2,-2*I*t,1]])
assert sp.simplify(R*U*R.inv()-Ui) == sp.zeros(3)

# The pencil span <q_0,x^2> has a unique singular member: x^2.
Qmat=sp.Matrix([[lam,0,sp.Rational(1,2)],[0,1,0],[sp.Rational(1,2),0,0]])
assert sp.factor(Qmat.det()) == -sp.Rational(1,4)

# General triangular pullback after the unique rank-one member forces x' = a x.
a,c,e,f,g=sp.symbols('a c e f g', nonzero=True)
Xg=a*x
Yg=b*x+c*y
Zg=e*x+f*y+g*z
expr=sp.Poly(sp.expand(q(lam,Xg,Yg,Zg)),x,y,z)
assert expr.coeff_monomial(y**2) == c**2
assert expr.coeff_monomial(x*z) == a*g
assert expr.coeff_monomial(x*y) == a*f+2*b*c
assert expr.coeff_monomial(x**2) == b**2+a*e+a**2*lam

# Under c^2=ag and af+2bc=0, the induced parameter map is affine.
A=a*g
phi=sp.factor((b**2+a*e+a**2*lam)/A)
assert sp.diff(phi,lam,2) == 0

# Centered second moment of {1,...,m}; nonzero for m>=2.
j=sp.symbols('j', integer=True, positive=True)
center=(m+1)/2
moment=sp.simplify(sp.summation((j-center)**2,(j,1,m)))
assert sp.factor(moment - m*(m**2-1)/12) == 0

# Classification after projective scaling a=1.
# identity on parameters: c=+/-1 gives U_b R^0 or U_b R^2
Ub=sp.Matrix([[1,0,0],[b,1,0],[-b**2,-2*b,1]])
Rid=sp.Matrix([[1,0,0],[0,I,0],[-M,0,-1]])
T_id_plus=sp.Matrix([[1,0,0],[b,1,0],[-b**2,-2*b,1]])
T_id_minus=sp.Matrix([[1,0,0],[b,-1,0],[-b**2,2*b,1]])
assert T_id_plus == Ub
assert sp.simplify(T_id_minus-Ub*(Rid**2)) == sp.zeros(3)
# reflection on parameters: c=+/-i gives U_b R or U_b R^3
T_ref_plus=sp.Matrix([[1,0,0],[b,I,0],[-b**2-M,-2*I*b,-1]])
T_ref_minus=sp.Matrix([[1,0,0],[b,-I,0],[-b**2-M,2*I*b,-1]])
assert sp.simplify(T_ref_plus-Ub*Rid) == sp.zeros(3)
assert sp.simplify(T_ref_minus-Ub*(Rid**3)) == sp.zeros(3)

# Infinitesimal generator gives the linear Jacobian syzygy.
qgen=q(lam)
delta=sp.expand(x*sp.diff(qgen,y)-2*y*sp.diff(qgen,z))
assert delta == 0

# Concrete finite-set check for several m values: only identity/reflection affine symmetries.
from itertools import permutations
for mm in range(2,9):
    S=list(range(1,mm+1))
    aff=[]
    for p in permutations(S):
        u=sp.Rational(p[1]-p[0],1) if mm>=2 else 1
        v=p[0]-u*S[0]
        if all(u*S[k]+v==p[k] for k in range(mm)):
            aff.append((u,v))
    assert set(aff)=={(sp.Integer(1),sp.Integer(0)),(sp.Integer(-1),sp.Integer(mm+1))}

print('VERIFY_OK')
