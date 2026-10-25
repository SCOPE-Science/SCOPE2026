from sympy import symbols, Rational, exp, sqrt, simplify, factor, diff
from mpmath import mp
mp.dps=50
c,T,w,u=symbols('c T w u', real=True)
P=(T*T+w*w)**2+(8*c-4)*T*T-(8*c+12)*w*w+16*c*c+16*c+12
s=symbols('s',real=True)
k=16*c+8
sminus=4*c+6-2*sqrt(8*c+6)
splus=4*c+6+2*sqrt(8*c+6)
X=(s-sminus)*(splus-s)/k
Y=s-X
assert simplify(P.subs({T*T:X,w*w:Y}))==0
assert simplify(Y-(s*s+(8*c-4)*s+16*c*c+16*c+12)/k)==0
assert simplify(X.subs(s,4*c+6)-(4*c+3)/(2*c+1))==0
assert simplify(Y.subs(s,2-4*c)-(4*c+1)/(2*c+1))==0
assert simplify(X.subs(s,2-4*c)-(1-4*c-8*c*c)/(2*c+1))==0
assert simplify(P.subs(w,0)-(T*T+4*c-2)**2-(32*c+8))==0
for cv,tv,wv in [(Rational(1,4),Rational(1,2),Rational(3,2)),(1,2,3),(Rational(1,10),Rational(3,2),Rational(5,4))]:
    f=lambda x: (x*x+mp.mpf(cv))*mp.exp(-x*x/2)
    numeric=mp.quad(lambda x:f(x+mp.mpf(tv)/2)*f(x-mp.mpf(tv)/2)*mp.cos(mp.mpf(wv)*x),[-mp.inf,0,mp.inf])
    exact=mp.sqrt(mp.pi)*mp.exp(-(mp.mpf(tv)**2+mp.mpf(wv)**2)/4)*mp.mpf(str(P.subs({c:cv,T:tv,w:wv})))/16
    assert abs(numeric-exact)<mp.mpf('1e-40'),(cv,tv,wv,numeric,exact)
for cv in [mp.mpf('0.01'),mp.mpf('0.1'),mp.mpf('0.25'),mp.mpf('1'),mp.mpf('100')]:
    disc=mp.sqrt(8*cv+6)
    lower=4*cv+6-2*disc
    upper=4*cv+6+2*disc
    maxdelay=mp.sqrt((4*cv+3)/(2*cv+1))
    for frac in [mp.mpf('0.01'),mp.mpf('0.25'),mp.mpf('0.5'),mp.mpf('0.75'),mp.mpf('0.99')]:
        sv=lower+(upper-lower)*frac
        xv=(sv-lower)*(upper-sv)/(16*cv+8)
        yv=sv-xv
        assert xv>0 and yv>0 and abs(xv+yv-sv)<mp.mpf('1e-40')
        t=mp.sqrt(xv); ww=mp.sqrt(yv)
        pp=(t*t+ww*ww)**2+(8*cv-4)*t*t-(8*cv+12)*ww*ww+16*cv*cv+16*cv+12
        assert abs(pp)<mp.mpf('1e-35')
        assert t<=maxdelay+mp.mpf('1e-40')
print('PASS: exact symbolic zero-curve, sharp delay and Doppler fold identities; 3 high-precision direct integrations; 25 high-precision zero points.')
