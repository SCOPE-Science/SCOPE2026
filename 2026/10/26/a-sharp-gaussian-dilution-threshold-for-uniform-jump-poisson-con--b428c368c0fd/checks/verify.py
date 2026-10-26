#!/usr/bin/env python3
"""Finite reproducibility checks for a uniform-mark Poisson sub-gamma phase law."""
from fractions import Fraction as F
from math import factorial

checks = 0

def check(cond, msg):
    global checks
    if not cond:
        raise AssertionError(msg)
    checks += 1


def uniform_mark_moment(k):
    return F(2**(k+1) - 1, k + 1)

# H(t) = sum_{n>=0} [2 E J^(n+3)/(E J^2 (n+3)!)] t^n.
# Its first coefficients follow from the independent beta(1,2) canonical factor.
coeff = [F(2)*uniform_mark_moment(n+3)/(uniform_mark_moment(2)*factorial(n+3))
         for n in range(115)]
for n in range(115):
    check(coeff[n] == F(6*(2**(n+4)-1),7*factorial(n+4)),f'coefficient {n}')

h0=coeff[0];h1=coeff[1];hsecond=2*coeff[2]
wcrit=h1/(h0*h0)
gp=(hsecond*h0-2*h1*h1)/(h0**3)
check(h0==F(15,28),'H0')
check(h1==F(31,140),'Hprime0')
check(hsecond==F(3,20),'Hsecond0')
check(wcrit==F(868,1125),'threshold')
check(gp==F(-9716,84375),'gprime at origin')
check(uniform_mark_moment(2)*(1-wcrit)/wcrit==F(257,372),'sigma-to-rate cutoff')
check(-1/gp==F(84375,9716),'optimizer slope')
check(-wcrit*h0*h0/(2*gp)==F(523125,544096),'excess scale coefficient')

# Confirm the two polynomial pieces of h(t) and their matching derivatives.
for k in range(81):
    u=F(k,80)
    hlow=u*u-3*u+F(7,3)
    # Integral of (j-u)^2 for 1<=j<=2, no normalization.
    hintegral=((2-u)**3-(1-u)**3)/3
    check(hlow==hintegral,'piecewise integrated-tail identity')
    # The negative curvature numerator of log(h) is increasing up to 1.
    numer=-2*u*u+6*u-F(13,3)
    check(numer<=-F(1,3),'strict log-concavity on [0,1]')
check(F(1,3)==(2-F(1))**3/3,'piecewise continuity')

# The power series avoids cancellation for small arguments.
def H(x):
    return sum(float(a)*x**n for n,a in enumerate(coeff[:105]))
def Hp(x):
    return sum(n*float(a)*x**(n-1) for n,a in enumerate(coeff[1:105],1))
def g(x):
    v=H(x)
    return Hp(x)/(v*v)
def phi(x,w):
    v=H(x)
    return w*v/(1+w*x*v)

samples=[k/20 for k in range(0,281)]
for u,v in zip(samples,samples[1:]):
    check(g(v)<g(u),f'calculated strict g decrease {u},{v}')
check(abs(g(0)-float(wcrit))<1e-13,'critical slope from series')

def bisect(w):
    left,right=0.0,15.0
    check(g(left)>w and g(right)<w,f'root bracket {w}')
    for _ in range(75):
        mid=(left+right)/2
        if g(mid)>w: left=mid
        else: right=mid
    return (left+right)/2

for w in [0.08,0.2,0.5,0.7,0.74,0.76]:
    x=bisect(w)
    check(x>0,'positive root')
    check(abs(g(x)-w)<2e-11,'stationarity')
    check(phi(x,w)>w*float(h0),'strict interior gain')
    check(phi(max(0,x/2),w)<phi(x,w),'left of optimum')
    check(phi(x*1.5,w)<phi(x,w),'right of optimum')
for w in [float(wcrit),0.9,1.0]:
    for x in samples[1:]:
        check(phi(x,w)<w*float(h0)+2e-13,'local regime')

# A direct check of the original cumulant generating function.
from math import exp
for lam in [0.125,1.0,2.5]:
    for sig2 in [0.0,0.1,3.0]:
        V=sig2+lam*float(uniform_mark_moment(2))
        w=lam*float(uniform_mark_moment(2))/V
        for t in [0.1,0.25,0.4,0.8]:
            # E e^(tJ) over J uniform [1,2].
            mj=(exp(2*t)-exp(t))/t
            K=sig2*t*t/2+lam*(mj-1-t*float(uniform_mark_moment(1)))
            reconstructed=V*t*t/2*(1+w*t*H(t))
            check(abs(K-reconstructed)<5e-12,'MGF factorization')

# The critical asymptotic slope/excess agree with small-parameter roots.
for delta in [0.003,0.001,0.0003]:
    w=float(wcrit)-delta
    root=bisect(w)
    slope=float(-1/gp)
    improvement=phi(root,w)-w*float(h0)
    check(abs(root/delta-slope)<0.25,'critical optimizer asymptotic')
    check(abs(improvement/(delta*delta)-float(F(523125,544096)))<0.06,
          'quadratic excess asymptotic')
print(f'PASS: {checks} finite and exact checks')
print(f'w_crit={wcrit}; sigma_squared_over_lambda_crit=257/372')
print(f'gprime(0)={gp}; critical optimizer slope=84375/9716')
print(f'excess-scale coefficient=523125/544096')
print('Finite tests do not certify the global log-concavity or all-parameter claims; the analytic proof does.')
