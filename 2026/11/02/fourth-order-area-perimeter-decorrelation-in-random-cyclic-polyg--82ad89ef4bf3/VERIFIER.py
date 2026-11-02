#!/usr/bin/env python3
"""Independent arithmetic checks for joint area--semiperimeter fluctuations.
Run: python3 VERIFIER.py. Uses the Python standard library only.
These finite checks support, but do not establish, the asymptotic theorem.
"""
from decimal import Decimal, localcontext
from fractions import Fraction
from math import factorial, sin, pi as float_pi

checks = 0
def check(pred, label):
    global checks
    checks += 1
    if not pred:
        raise AssertionError(label)

def arctan(t, prec=100):
    with localcontext() as ctx:
        ctx.prec = prec+10
        x = Decimal(t)
        z = Decimal(1)/x
        zz = z*z
        term = z
        total = Decimal(0)
        k = 0
        while abs(term) > Decimal(10)**(-prec-5):
            total += term/(2*k+1) * (1 if k%2==0 else -1)
            term *= zz
            k += 1
        return +total

with localcontext() as ctx:
    ctx.prec = 90
    PI = +(16*arctan(5)-4*arctan(239))

def rising(n, k):
    v=1
    for a in range(k):v *= n+a
    return v

def power_moment(n,r):
    return Fraction(n*factorial(r),rising(n,r))

def power_cov(n,r,s):
    return Fraction(n*(factorial(r+s)+(n-1)*factorial(r)*factorial(s)), rising(n,r+s)) - power_moment(n,r)*power_moment(n,s)

def kappa(r,s):
    return factorial(r+s)-(1+r*s)*factorial(r)*factorial(s)

check(kappa(3,3)==360,'kappa33')
check(kappa(3,5)==28800,'kappa35')
check(kappa(5,5)==3254400,'kappa55')
check(kappa(5,5)-kappa(3,5)**2//kappa(3,3)==950400,'orthogonal complement')
check(Fraction(9504,32544)==Fraction(33,113),'variance reduction ratio')
for n in (3,4,5,7,10,20,50,100,200,400,800):
    for r,s in ((3,3),(3,5),(5,5)):
        check(power_cov(n,r,s) >= 0, f'nonnegative powers cov {n},{r},{s}')
for n in (200,800,5000):
    for r,s in ((3,3),(3,5),(5,5)):
        approx = float(power_cov(n,r,s)*n**(r+s-1))
        exact = kappa(r,s)
        check(0 < approx < exact, f'moment convergence sign {n},{r},{s}')
        if n==5000:check(abs(approx/exact-1)<.02, f'moment convergence {n},{r},{s}')

def dec_frac(f):
    return Decimal(f.numerator)/Decimal(f.denominator)

def sine_cov(n, kind1, kind2, terms=9):
    with localcontext() as ctx:
        ctx.prec=86
        def series(kind):
            a=(PI if kind=='S' else 2*PI)
            factor=(Decimal(1) if kind=='S' else Decimal('0.5'))
            return [(2*j+1,factor * (-1)**j *a**(2*j+1)/Decimal(factorial(2*j+1))) for j in range(1,terms+1)]
        return +sum(c*d*dec_frac(power_cov(n,r,s)) for r,c in series(kind1) for s,d in series(kind2))

with localcontext() as ctx:
    ctx.prec=86
    const=Decimal(297)/10*PI**4
    beta_const=48*PI**2
    old_diff=None
    for n in (30,60,100,200,400,800):
        vs=sine_cov(n,'S','S')
        va=sine_cov(n,'A','A')
        ca=sine_cov(n,'S','A')
        check(vs>0 and va>0 and ca>0, f'positive variances/covariance n={n}')
        rho=ca/(vs*va).sqrt()
        beta=ca/vs
        check(0<rho<1, f'correlation within (0,1) n={n}')
        delta=Decimal(n)**4*(1-rho)
        bd=Decimal(n)**2*(4-beta)
        check(delta>0 and bd>0,f'positive asymptotic coefficients n={n}')
        if old_diff is not None:
            check(abs(const-delta)<old_diff,f'correlation coefficient converges at n={n}')
        old_diff=abs(const-delta)
        print(f'n={n}: n^4(1-rho)={delta:.10f}; n^2(4-beta)={bd:.10f}')
    check(abs(float(delta/const)-1)<0.055,'n=800 fourth-order coefficient within 5.5%')
    check(abs(float(bd/beta_const)-1)<.02,'n=800 regression correction within 2%')

# Independent, non-moment based numerical integration over the 3-dimensional simplex.
K=180
z=0.0
ES=EA=ESS=EAA=ESA=0.0
for i in range(K):
    u=(i+.5)/K
    for j in range(K):
        v=(j+.5)/K
        ds=(u, (1-u)*v, (1-u)*(1-v))
        ss=sum(sin(float_pi*x) for x in ds)
        aa=.5*sum(sin(2*float_pi*x) for x in ds)
        w=2*(1-u)/(K*K)
        z+=w; ES+=w*ss; EA+=w*aa; ESS+=w*ss**2; EAA+=w*aa**2; ESA+=w*ss*aa
ES/=z; EA/=z; ESS/=z; EAA/=z; ESA/=z
cv_num=ESA-ES*EA
cv_ex=float(sine_cov(3,'S','A'))
check(abs(cv_num-cv_ex)<0.00003, '2D independent midpoint integration n=3 covariance')
print(f'n=3 independent quadrature covariance: {cv_num:.12g}; analytic: {cv_ex:.12g}')
print(f'PASS: {checks} checks; theoretical correlation deficit constant {(float(Decimal(297)/10*PI**4)):.10f}')
