import sympy as sp
from fractions import Fraction

x=sp.symbols("x")
z=sp.symbols("z")
d=sp.CRootOf(8*z**3-4*z**2-4*z+1,1)
q=sp.Rational(1,2)+d-2*d**2
a=1+2*d
b=(2+8*d-8*d**2)/7
c=(2-6*d-8*d**2)/7

# Seventh-root identities and upper-certificate identity.
assert sp.simplify(8*d**3-4*d**2-4*d+1)==0
assert sp.simplify((1+2*d)*(q+d)-(1+d))==0

P=sp.expand(1+a*x+b*(2*x**2-1)+c*(16*x**5-20*x**3+5*x))
Q=(sp.Rational(32,7)*(1+d)*(1-4*d)*x**2
   +sp.Rational(16,7)*(8*d**2-1)*x
   +sp.Rational(8,7)*d*(10*d+3))
K=sp.QQ.algebraic_field(d)
Pp=sp.Poly(P,x,domain=K)
Fp=sp.Poly((x+1)*(x+q)**2*Q,x,domain=K)
assert Pp == Fp
# Exact contact conditions follow from the factorization: x=-1 is a root and x=-q is a double root.
assert Pp.eval(-1)==0
assert Pp.eval(-K.from_sympy(q))==0
assert Pp.diff().eval(-K.from_sympy(q))==0

A=sp.Rational(32,7)*(1+d)*(1-4*d)
B=sp.Rational(16,7)*(8*d**2-1)
C=sp.Rational(8,7)*d*(10*d+3)
assert sp.simplify(B**2-4*A*C-sp.Rational(256,49)*(232*d**2+100*d-34))==0

# Rational part of the rigorous bound d < 223/1000.
y=Fraction(11,49)
taylor=y-y**3/Fraction(6,1)+y**5/Fraction(120,1)
assert taylor < Fraction(223,1000)
assert 232*Fraction(223,1000)**2+100*Fraction(223,1000)-34 == Fraction(-20359,125000)

# Stress sample; not used as proof.
import math
av=float(sp.N(a,30)); bv=float(sp.N(b,30)); cv=float(sp.N(c,30))
mn=10.0
for j in range(20001):
    t=2*math.pi*j/20001
    v=1+av*math.cos(t)+bv*math.cos(2*t)+cv*math.cos(5*t)
    mn=min(mn,v)
assert mn > -1e-10
print("VERIFY_OK exact_contacts=3 factorization=1 discriminant=negative sample_points=20001")
