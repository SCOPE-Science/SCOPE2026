"""Independent algebraic and numerical checks for regular-polygon center depth.
Run: python verify.py  (requires sympy, mpmath, scipy)."""
import math
from fractions import Fraction
import mpmath as mp
import sympy as sp
from scipy.integrate import quad

# Exactly integrate the fourth-order convolution coefficient.
u, v = sp.symbols('u v', real=True)
q = lambda t: t*t-sp.Rational(1,3)
integrand = q(u)*q(v)
exact = sp.integrate(sp.integrate(integrand, (v,-1,u-sp.Rational(1,2))),
                     (u,-sp.Rational(1,2),sp.Rational(1,2)))
exact += sp.integrate(sp.integrate(integrand,
                                  (v,u-sp.Rational(3,2),u-sp.Rational(1,2))),
                      (u,sp.Rational(1,2),1))
assert sp.simplify(exact+sp.Rational(5,96)) == 0, exact

mp.mp.dps = 65

def depth_closed(n):
    if n%2==0: return mp.mpf('0.5'),mp.mpf('0.25')
    if n == 3:
        J = (2-mp.log(3))/4
    else:
        a=mp.pi/n; h=mp.tan(a); b=mp.tan(a/2); c=mp.tan(3*a/2)
        def H(k,x): return x/k - (1+k*k)/(k*k)*mp.log(1+k*x)
        J=(H(b,h)-H(b,-b)-H(c,h)+H(c,b)+2*h*b)/(4*h*h)
    eps=(-1)**((n-3)//2)
    return mp.mpf('0.5')+eps*(1-4*J)/(2*n),J

def depth_integral(n):
    a=math.pi/n; h=math.tan(a)
    def f(t): return 1/(math.cos(t)**2)
    def integral(c,x,y):
        return quad(lambda t:f(t)*math.tan(t-c),x,y,epsabs=1e-12,epsrel=1e-12)[0]
    J=(integral(a/2,-a/2,a)-integral(3*a/2,a/2,a)
       +2*h*math.tan(a/2))/(4*h*h)
    eps=(-1)**((n-3)//2)
    return .5+eps*(1-4*J)/(2*n),J

for n in (3,5,7,9,11,13,17,21,51):
    d,j=depth_closed(n)
    di,ji=depth_integral(n)
    assert abs(float(d)-di)<4e-11,(n,d,di)
    assert abs(float(j)-ji)<4e-11,(n,j,ji)
    assert j < mp.mpf('0.25'),(n,j)
    expected=(-1)**((n-3)//2)
    assert expected*(d-mp.mpf('0.5'))>0,(n,d)
    if n == 3:
        assert abs(d-(mp.mpf(1)/3+mp.log(3)/6))<mp.mpf('1e-55')
    print('n',n,'J',mp.nstr(j,18),'depth',mp.nstr(d,18))

# Check the exact discrete phase-count identity for every odd 3 <= n <= 43
# on samples safely away from transition boundaries.
for n in range(3,44,2):
    a=math.pi/n; eps=(-1)**((n-3)//2)
    for k in range(-190,191):
        z=2*a*k/200
        if min(abs(abs(z)-a/2),abs(abs(z)-3*a/2))<1e-10:continue
        observed=sum(math.cos(z+2*math.pi*j/n)<0 for j in range(n))
        predicted=(n+eps)//2-eps*int(a/2<abs(z)<3*a/2)
        assert observed==predicted,(n,z,observed,predicted)

# Exact area inequality for uniform central rectangles, checked on rational grid
# but its infinite-range proof is supplied in RESULT.md.
def plus(z):return max(0.,z)
for i in range(1,100):
    for j in range(1,100):
        s=i/100.; t=j/100.; a=s+t; b=abs(s-t)
        K=(plus(a-.5)**2-plus(b-.5)**2-plus(a-1.5)**2)/2
        assert K < s*t+1e-12,(s,t,K,s*t)

# Independent numeric angular-convolution check, with no elementary primitive.
def J_convolution(n):
    a=math.pi/n; h=math.tan(a)
    def density(z):
        return quad(lambda x:1/(math.cos(x)**2*math.cos(x-z)**2),z-a,a,
                    epsabs=1e-10,epsrel=1e-10)[0]/(4*h*h)
    return quad(density,a/2,3*a/2,epsabs=1e-10,epsrel=1e-10)[0]
for n in (3,5,7,9):
    _,j=depth_closed(n)
    assert abs(J_convolution(n)-float(j))<2e-10,(n,j)

# Asymptotic coefficient, tested without claiming that finite tests prove the limit.
coef=5*mp.pi**4/192
for n in (31,51,101,201):
    d,_=depth_closed(n)
    scaled=(-1)**((n-3)//2)*(d-mp.mpf('0.5'))*n**5
    assert abs(scaled/coef-1)<max(.05,2000/n**2),(n,scaled,coef)
    print('asymptotic n',n,'n^5 signed-deficit',mp.nstr(scaled,15))
print('PASS: exact convolution coefficient, phase counts, independent quadrature and limits')
