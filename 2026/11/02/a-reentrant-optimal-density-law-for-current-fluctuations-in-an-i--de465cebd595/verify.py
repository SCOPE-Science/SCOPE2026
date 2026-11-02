"""Exact algebraic checks for the active-lattice current-noise density theorem.

Run with Python 3 and SymPy: python verify.py
These are reproducibility checks; the analytic sign arguments are in RESULT.md.
"""
import sympy as s

x,p,t=s.symbols('x p t',real=True)
A=x*(1-x)*(2+p*(1-x))
H=2-p*(1-x)*(2*x-1)
N=s.expand(2*H*s.diff(A,x)-A*s.diff(H,x))
assert s.factor(N-(8*p**2*x**4-23*p**2*x**3+24*p**2*x**2-11*p**2*x+2*p**2-8*p*x**3+30*p*x**2-30*p*x+8*p-16*x+8))==0

def transformed(poly, left, right, degree):
    newx=(left+right*t)/(1+t)
    return s.Poly(s.cancel((1+t)**degree*poly.subs(x,newx)),t)

whole=transformed(N,0,1,4)
whole_expected=[2*(p+2)**2,-(p+2)*(3*p-8),3*p*(p-4),-2*(3*p+8),-8]
assert all(s.simplify(whole.nth(i)-whole_expected[i])==0 for i in range(5))

low=transformed(N,0,s.Rational(1,2),4)
low_expected=[2*(p+2)**2,(p+2)*(5*p+24)/2,3*(p**2+7*p+16)/2,(5*p**2+8*p+64)/8,p*(p-4)/8]
assert all(s.simplify(low.nth(i)-low_expected[i])==0 for i in range(5))

high=transformed(N,s.Rational(3,4),1,4)
high_expected=[(p-16)*(5*p+16)/64,(15*p**2-232*p-1280)/64,3*(p**2-22*p-192)/16,-(3*p+56)/2,-8]
assert all(s.simplify(high.nth(i)-high_expected[i])==0 for i in range(5))

mid_der=transformed(-s.diff(N,x),s.Rational(1,2),s.Rational(3,4),3)
mid_expected=[(p**2+24*p+64)/4,3*(3*p+16),3*(3*p**2+8*p+256)/16,(5*p**2-24*p+256)/16]
assert all(s.simplify(mid_der.nth(i)-mid_expected[i])==0 for i in range(4))

# The positive coefficients of low and mid_der, negative coefficients
# of high on 4<p<16, and Descartes' sign rule for whole on 0<p<=4
# establish exact root uniqueness; sampled roots are not that proof.
assert s.factor(s.resultant(N,s.diff(N,p),p)) == -4*x**2*(x-1)**4*(8*x**2-7*x+2)*(16*x**2+40*x-23)
xt=s.sqrt(3)-s.Rational(5,4)
pt=s.Rational(64,99)+s.Rational(16,33)*s.sqrt(3)
assert s.simplify(N.subs({x:xt,p:pt}))==0
assert s.simplify(s.diff(N,p).subs({x:xt,p:pt}))==0
assert s.factor(N.subs(x,s.Rational(1,2)))==p*(p-4)/8
assert s.factor(N.subs(x,s.Rational(3,4)))==(p-16)*(5*p+16)/64
assert s.diff(N,x).subs({x:s.Rational(3,4),p:16})==-72
assert s.diff(N,p).subs({x:s.Rational(3,4),p:16})==s.Rational(3,2)
assert s.simplify(-s.diff(N,p).subs({x:s.Rational(1,2),p:0})/s.diff(N,x).subs({x:s.Rational(1,2),p:0}))==-s.Rational(1,32)
assert s.simplify(-s.diff(N,p).subs({x:s.Rational(1,2),p:4})/s.diff(N,x).subs({x:s.Rational(1,2),p:4}))==s.Rational(1,88)
assert s.simplify(A.subs({x:s.Rational(3,4),p:16}))==s.Rational(9,8)

# Independent high-precision root and normalization checks at several parameters.
import mpmath as mp
mp.mp.dps=65
for q in ['0.01','1','1.4862468561950113','4','9','15','15.99']:
    qq=mp.mpf(q)
    poly=s.Poly(N.subs(p,s.Rational(q)),x)
    bisection_lo,bisection_hi=mp.mpf('0'),mp.mpf('1')
    def f(z):
        return 8*qq**2*z**4-23*qq**2*z**3+24*qq**2*z**2-11*qq**2*z+2*qq**2-8*qq*z**3+30*qq*z**2-30*qq*z+8*qq-16*z+8
    for _ in range(230):
        middle=(bisection_lo+bisection_hi)/2
        if f(middle)>0: bisection_lo=middle
        else: bisection_hi=middle
    z=(bisection_lo+bisection_hi)/2
    assert abs(f(z))<mp.mpf('1e-55')
    assert z>0 and z<1
    assert f(z-mp.mpf('0.00001'))>0 if z>mp.mpf('0.00001') else True
    assert f(z+mp.mpf('0.00001'))<0 if z<1-mp.mpf('0.00001') else True
    sigma=2*z*(1-z)
    delta=2-qq*(1-z)*(2*z-1)
    late_from_source=sigma*(2+qq*(1-z))/(2*mp.sqrt(mp.pi)*mp.sqrt(delta))
    late_target=z*(1-z)*(2+qq*(1-z))/(mp.sqrt(mp.pi)*mp.sqrt(delta))
    assert abs(late_from_source-late_target)<mp.mpf('1e-56')
print('PASS: 10 exact polynomial/normalization identities, uniqueness certificates, turnpoint, edge, and 7 high-precision cases')
