"""Independent exact moment checks for the two-shell sphere fourth-moment theorem."""
from itertools import product
import sympy as s
X,Y,Z=s.symbols('X Y Z',real=True)
coords=s.Matrix([X,Y,Z])

def moment(p):
    """Normalized S^2 integral of an exact polynomial."""
    out=s.S(0)
    for powers,v in s.Poly(s.expand(p),X,Y,Z).terms():
        if any(e%2 for e in powers):
            continue
        out+=v*s.prod(s.factorial2(e-1) for e in powers)/s.factorial2(sum(powers)+1)
    return s.simplify(out)

def check(A,u):
    assert A==A.T and s.trace(A)==0
    q=(coords.T*A*coords)[0]
    l=(coords.T*u)[0]
    uu=(u.T*u)[0]
    T=s.trace(A*A)
    m=(u.T*A*A*u)[0]
    assert moment(l*l)==uu/3
    assert moment(q*q)==2*T/15
    assert moment(l**4)==uu**2/5
    assert moment(q**4)==4*T**2/105
    assert moment(l*l*q*q)==(2*uu*T+8*m)/105
    assert moment(l**3*q)==0
    assert moment(l*q**3)==0
    v=moment((l+q)**4)
    r=uu/3+2*T/15
    deficit=s.Rational(375,112)*r*r-v
    cert=s.Rational(192,35)*(uu/3-s.Rational(15,32)*r)**2+s.Rational(16,35)*(s.Rational(2,3)*uu*T-m)
    assert s.simplify(deficit-cert)==0
    return 8

count=0
for a,b,c in product(range(-2,3),repeat=3):
    # A is trace-free, may be non-diagonal and has non-coaxial u.
    A=s.Matrix([[a,b,c],[b,-a,1],[c,1,0]])
    u=s.Matrix([1,b+1,c-1])
    count+=check(A,u)
assert count==1000
z=s.symbols('z', real=True)
P1=s.sqrt(3)*z
P2=s.sqrt(5)*(3*z*z-1)/2
E=lambda p:s.simplify(s.integrate(s.expand(p),(z,-1,1))/2)
assert E(P1*P1)==E(P2*P2)==1
assert E(P1*P2)==0
assert E(P1**4)==s.Rational(9,5)
assert E(P2**4)==s.Rational(15,7)
assert E(P1**2*P2**2)==s.Rational(11,7)
t=s.symbols('t')
F=s.expand(E(P1**4)*t*t+6*E(P1**2*P2**2)*t*(1-t)+E(P2**4)*(1-t)**2)
assert s.factor(F-(s.Rational(375,112)-s.Rational(192,35)*(t-s.Rational(15,32))**2))==0
assert F.subs(t,s.Rational(15,32))==s.Rational(375,112)
print('PASS:',count+8,'exact moment and optimization assertions')
