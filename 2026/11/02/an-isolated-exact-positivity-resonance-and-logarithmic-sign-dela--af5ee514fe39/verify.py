"""Exact symbolic certificates and high-precision checks for five-step BDFL scalar decay."""
from fractions import Fraction
from math import comb
import sympy as sp
import mpmath as mp

x, r = sp.symbols('x r', real=True)
k = sp.sqrt(5)
a4=(45+14*k)/44
a3=-k/2
a2=(25+9*k)/88
a1=-(10-3*k)/22
a0=(13-5*k)/88
b=5*(7-k)/44
F=sp.expand((1+b*r)*x**5-a4*x**4-a3*x**3-a2*x**2-a1*x-a0)
q=1/(1+r)
r0=k
q0=sp.simplify(q.subs(r,r0))
assert sp.simplify(q0-(k-1)/4)==0
assert sp.simplify(F.subs({x:q0,r:r0}))==0
resid=sp.factor(sp.cancel(F.subs(x,q)),extension=k)
expect=sp.factor(r**2*(k-3)*(7-k)*(r-k)*(r**2+(5+3*k)/2)/(176*(1+r)**5),extension=k)
# original factor equivalent via (k-3)=(sqrt5-3), not (sqrt5-3)?
assert sp.simplify(resid-expect)==0, (resid,expect)
Q=sp.div(sp.Poly(F.subs(r,r0),x,extension=k),sp.Poly(x-q0,x,extension=k))[0].as_expr()
Q=sp.simplify(Q/sp.LC(sp.Poly(Q,x)))
Q_expected=x**4+(-69+3*k)*x**3/131+(217-55*k)*x**2/262+(-74+26*k)*x/131+(37-13*k)/262
assert sp.simplify(Q-Q_expected)==0

# Rational enclosure 2236067977/10^9 < sqrt(5) < 2236067978/10^9.
lo=sp.Rational(2236067977,10**9)
hi=sp.Rational(2236067978,10**9)
assert lo**2<5<hi**2

def bounds_in_qsqrt5(expr):
    expr=sp.expand(sp.simplify(expr))
    bb=sp.expand(expr).coeff(k)
    aa=sp.simplify(expr-bb*k)
    assert aa.is_Rational and bb.is_Rational,(expr,aa,bb)
    if bb>=0:return aa+bb*lo,aa+bb*hi
    return aa+bb*hi,aa+bb*lo

def norm_squared(expr):
    v=sp.expand(expr)
    return sp.simplify(sp.expand(sp.re(v))**2+sp.expand(sp.im(v))**2)

def upper_abs_below(expr,bound):
    _,up=bounds_in_qsqrt5(norm_squared(expr))
    return up<sp.Rational(bound)**2

def lower_abs_above(expr,bound):
    low,_=bounds_in_qsqrt5(norm_squared(expr))
    return low>sp.Rational(bound)**2

centers=[sp.Rational(-23,2000)+sp.I*sp.Rational(623,1250),
         sp.Rational(2493,10000)+sp.I*sp.Rational(2443,10000)]
eps=sp.Rational(1,4000)
# Guaranteed modulus and angle bands follow from the disk radii,
# using squared rational bounds for the two centers.
for center,lower,upper in zip(centers,[sp.Rational(498,1000),sp.Rational(348,1000)],
                                   [sp.Rational(499,1000),sp.Rational(350,1000)]):
    norm2=sp.simplify(norm_squared(center))
    assert norm2>(lower+eps)**2
    assert norm2<(upper-eps)**2
assert abs(centers[0].as_real_imag()[0])+eps < sp.Rational(3,100)*(centers[0].as_real_imag()[1]-eps)
for center in centers:
    assert upper_abs_below(Q.subs(x,center),sp.Rational(1,100000))
    assert lower_abs_above(sp.diff(Q,x).subs(x,center),sp.Rational(1,8))
    for j in (2,3,4):
        assert upper_abs_below(sp.diff(Q,x,j).subs(x,center)/sp.factorial(j),10)
    # Rouche: |Q(c)| + sum_{j>=2}|Q^(j)(c)|eps^j/j! < eps|Q'(c)|.
    assert sp.Rational(1,100000)+10*sum(eps**j for j in (2,3,4)) < eps/8
# Each of four disjoint conjugate disks contains exactly one zero of Q.

# Reproducible high-precision recurrence comparisons (not a replacement for the proof).
mp.mp.dps=170
kk=mp.sqrt(5)
A=[(45+14*kk)/44,-kk/2,(25+9*kk)/88,-(10-3*kk)/22,(13-5*kk)/88]
B=5*(7-kk)/44

def trajectory(rr,count):
    qq=1/(1+rr)
    values=[qq**j for j in range(5)]
    for n in range(5,count):
        values.append(mp.fsum(A[j]*values[-j-1] for j in range(5))/(1+B*rr))
    return values

res=trajectory(kk,90)
assert max(abs(res[n]-((kk-1)/4)**n) for n in range(90))<mp.mpf('1e-145')
for rr in [mp.mpf('2.0'),mp.mpf('2.1'),kk-mp.mpf('0.001'),kk+mp.mpf('0.001'),mp.mpf('2.4')]:
    ys=trajectory(rr,150)
    assert any(v<0 for v in ys[5:]),rr
    assert any(v>0 for v in ys[5:]),rr
    for n in range(5,150):
        exact=mp.fsum(A[j]*ys[n-j-1] for j in range(5))/(1+B*rr)
        assert abs(ys[n]-exact)<mp.mpf('1e-130')
rootz=mp.polyroots([1,mp.mpf(str(sp.N(Q_expected.coeff(x,3),70))),mp.mpf(str(sp.N(Q_expected.coeff(x,2),70))),mp.mpf(str(sp.N(Q_expected.coeff(x,1),70))),mp.mpf(str(sp.N(Q_expected.coeff(x,0),70)))],maxsteps=300,error=False)
positive=sorted([z for z in rootz if mp.im(z)>0],key=lambda z:abs(z),reverse=True)
rho=abs(positive[0]);t=(kk-1)/4
rate=1/mp.log(rho/t)
for p in [2,3,4,6,8]:
    for sign in (-1,1):
        rr=kk+sign*mp.power(10,-p)
        ys=trajectory(rr,160)
        first=next((n for n,y in enumerate(ys) if y<0),None)
        assert first is not None
        print('delta',sign,p,'first-negative',first,'leading-approx',mp.nstr(rate*p*mp.log(10),9))
print('PASS: algebraic identity, four Rouche disks, spectral ordering, exact resonance, high-precision recurrence')
print('rho=',mp.nstr(rho,25),'t=',mp.nstr(t,25),'log reciprocal=',mp.nstr(rate,25))
