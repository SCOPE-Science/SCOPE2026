"""Independent elementary algebra and numeric checks for the four-symbol random-map theorem."""
from fractions import Fraction as Q
from math import log
import sympy as s

y,b1,b2=s.symbols('y b1 b2', real=True)
k1=(b2-2)/(2*(b2-b1));k2=(2-b1)/(2*(b2-b1))
r1=b1+4*(2-b1)*y;r2=b2+4*(2-b2)*y
assert s.simplify(k1*r1+k2*r2-1)==0
assert s.simplify(s.integrate(r1,(y,0,s.Rational(1,2)))-1)==0
assert s.simplify(s.integrate(r2,(y,0,s.Rational(1,2)))-1)==0
for aa,bb in [(Q(1,2),Q(7,2)),(Q(1,4),Q(13,5)),(Q(9,5),Q(11,5))]:
    a=float(aa); b=float(bb)
    ww=(b-2)/(b-a)
    def J(z):
        if abs(z-2)<1e-12:return log(2)
        def F(t):return .5*t*t*log(t)-.25*t*t
        return (F(4-z)-F(z))/(4*(2-z))
    lam=ww*J(a)+(1-ww)*J(b)
    assert log(2)<lam<2*log(2)-.5
    # Midpoint quadrature for conditional entropy and exact entropy balance.
    N=200000
    hh=0.
    for j in range(N):
        u=(j+.5)/(2*N)
        pp=(b-2)/(2*(b-a))*(a+4*(2-a)*u)
        hh+=-pp*log(pp)-(1-pp)*log(1-pp)
    hh/=N
    H=-ww*log(ww)-(1-ww)*log(1-ww)
    assert abs(lam-(log(2)+H-hh))<1e-9, (a,b,lam,hh)
    print('b1,b2,lam',a,b,lam,'mean conditional entropy',hh)
print('VERIFY_OK')
