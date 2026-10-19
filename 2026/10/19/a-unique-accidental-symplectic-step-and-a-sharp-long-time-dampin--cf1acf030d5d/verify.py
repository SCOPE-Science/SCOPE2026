"""Reproduce exact sign certificates and direct-step checks for the Gaussian RBF-RK2 harmonic-oscillator calculation.

Only Python standard library is needed. The infinite-parameter claims require
and are proved by the convexity argument in RESULT.md; this code supplies
exact-rational endpoint certificates and independent numerical sanity checks.
"""
from fractions import Fraction as F
from math import exp, log1p, sqrt, factorial, isclose
import random

checks = 0

def verify(condition, label):
    global checks
    assert condition, label
    checks += 1


def exp_minus_enclosure(t):
    """Exact rational enclosure for exp(-t), 0<=t<=1, via alternating series."""
    verify(0 <= t <= 1, 'exponential enclosure domain')
    term = F(1)
    total = term
    lower = None
    for k in range(1, 41):
        term *= -t / k
        total += term
        if k == 39:
            lower = total
    upper = total
    verify(lower <= upper, 'alternating-order')
    return lower, upper


def exact_interval_signs(s, kind):
    lq, uq = exp_minus_enclosure(2*s/9)
    lq2, uq2 = exp_minus_enclosure(4*s/9)
    if kind == 'H':
        base, c1, c2 = 4*s-15, F(6), F(9)
    else:
        base, c1, c2 = 8*s-15, 6-4*s/3, 9-4*s
    verify(c1 >= 0 and c2 >= 0, 'positive exponential coefficients')
    return base+c1*lq+c2*lq2, base+c1*uq+c2*uq2

D = 10**12
sroot_lo = F(1577421180854, D)
sroot_hi = F(1577421180856, D)
sdamp_lo = F(1026544029217, D)
sdamp_hi = F(1026544029219, D)
for kind, lo, hi in [('H',sroot_lo,sroot_hi),('K',sdamp_lo,sdamp_hi)]:
    low = exact_interval_signs(lo,kind)
    high = exact_interval_signs(hi,kind)
    verify(low[1] < 0,kind+' strict negative at lower rational endpoint')
    verify(high[0] > 0,kind+' strict positive at upper rational endpoint')


def H(s):
    return 4*s-15+6*exp(-2*s/9)+9*exp(-4*s/9)


def Hp(s):
    return 4-(4/3)*exp(-2*s/9)-4*exp(-4*s/9)


def Q(s):
    return 1+s*H(s)/16


def stage(omega,h,z):
    def az(v):return (-omega*v[1], omega*v[0])
    y=az(z)
    a=exp(-2*(omega*h)**2/9)
    v=(a*z[0]+(2*h/3)*y[0],a*z[1]+(2*h/3)*y[1])
    y2=az(v)
    return (z[0]+h*(y[0]/4+3*y2[0]/4),z[1]+h*(y[1]/4+3*y2[1]/4))


def closed(omega,h,z):
    x=omega*h
    a=1-x*x/2
    b=x*(1+3*exp(-2*x*x/9))/4
    return (a*z[0]-b*z[1],b*z[0]+a*z[1])

rng = random.Random(20261016)
for _ in range(750):
    w=10**rng.uniform(-1,1)
    h=10**rng.uniform(-2,.4)
    z=(rng.uniform(-2,2),rng.uniform(-2,2))
    if z == (0,0):continue
    a=stage(w,h,z)
    b=closed(w,h,z)
    verify(isclose(a[0],b[0],rel_tol=1e-11,abs_tol=1e-10) and isclose(a[1],b[1],rel_tol=1e-11,abs_tol=1e-10),'direct-stage and analytic map')
    en=(a[0]**2+a[1]**2)/(z[0]**2+z[1]**2)
    verify(isclose(en,Q((w*h)**2),rel_tol=1e-10,abs_tol=1e-10),'energy factor')

sstar=(float(sroot_lo)+float(sroot_hi))/2
sdamp=(float(sdamp_lo)+float(sdamp_hi))/2
verify(abs(H(sstar)) < 2e-11,'root residual')
verify(abs(H(sdamp)+sdamp*Hp(sdamp))< 2e-11,'damping stationarity')
verify(0<sdamp<sstar,'ordering')
verify(Q(sdamp)<1 and abs(Q(sstar)-1)<2e-11,'damping and exact energy at exceptional step')
verify(Q(sstar/2)<1 and Q(2*sstar)>1,'sharp stability phase')
for omega in [0.1, 1.0, 3.2, 10.0]:
    h=sqrt(sstar)/omega
    p=closed(omega,h,(1.0,0.0))
    verify(isclose(p[0]**2+p[1]**2,1,rel_tol=1e-11,abs_tol=1e-11),'exceptional rotation')

for h in [0.2,0.1,0.05,0.025]:
    omega=1.0
    tau=1.25
    n=int(tau*h**(-4))
    x=(omega*h)**2
    log_energy=n*log1p(x*H(x)/16)
    theoretical=-tau*omega**4/12
    verify(abs(log_energy-theoretical)<0.15*h*h, 'long-time asymptotic scaling')

print('PASS; checks:',checks)
print('certified s_star in',sroot_lo,sroot_hi)
print('certified s_damp in',sdamp_lo,sdamp_hi)
print('oscillatory cutoff sqrt(s_star) approx:',sqrt(sstar))
print('single-step minimum energy factor approx:',Q(sdamp))
