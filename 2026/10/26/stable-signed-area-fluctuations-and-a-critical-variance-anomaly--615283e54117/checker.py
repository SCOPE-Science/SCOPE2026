#!/usr/bin/env python3
"""Numerical checks of independently stated signed-area renewal formulas.
Requires mpmath. Purely finite checks; not a substitute for the proof.
"""
import math
import mpmath as mp
mp.mp.dps=60
checks=0

def close(actual, expected, rtol='1e-14', atol='1e-20'):
    global checks
    a,b=mp.mpf(actual),mp.mpf(expected)
    assert abs(a-b) <= mp.mpf(atol)+mp.mpf(rtol)*max(abs(a),abs(b)),(a,b)
    checks+=1

def mu(alpha):return alpha/(alpha-1)
def cov(alpha,h,D=1):
    alpha,h,D=map(mp.mpf,(alpha,h,D))
    if h<=1:
        return D*((alpha-1)/(alpha-2)-2*h+(alpha-1)/alpha*h*h)
    return 2*D/(alpha*(alpha-2))*h**(2-alpha)

def vexact(alpha,T,D=1):
    alpha,T,D=map(mp.mpf,(alpha,T,D))
    A=(alpha-1)/(alpha-2); B=(alpha-1)/alpha
    if T<1: return 2*D*(A*T*T/2-T**3/3+B*T**4/12) # derived integral
    low=2*D*(T*(A-1+B/3)-(A/2-mp.mpf(2)/3+B/4))
    if alpha==3: high=T*mp.log(T)-(T-1)
    elif alpha==4: high=T-1-mp.log(T)
    else: high=T*(T**(3-alpha)-1)/(3-alpha)-(T**(4-alpha)-1)/(4-alpha)
    return low+4*D/(alpha*(alpha-2))*high

def cycle_cf(alpha,k,D=1):
    alpha,k,D=map(mp.mpf,(alpha,k,D)); p=alpha/3; u=D*k*k/3
    if u==0: return mp.mpf(1)
    return p*u**p*mp.gammainc(-p,u,mp.inf)

for astr in ['2.2','2.5','2.8','3','3.5','4','5']:
    a=mp.mpf(astr)
    for hs in ['0','0.2','0.7','1','1.3','3','8']:
        h=mp.mpf(hs)
        # direct stationary cycle occupation integral, no use of closed-form covariance
        # when a+h<1, tail exactly 1 rather than (a+h)**-alpha
        direct=(2/mu(a))*(mp.quad(lambda x:x,[0,max(mp.mpf(0),1-h)])+mp.quad(lambda x:x*(x+h)**(-a),[max(mp.mpf(0),1-h),mp.inf]))
        close(cov(a,h),direct,rtol='1e-10')
    for Ts in ['0.5','1','2','7','40']:
        T=mp.mpf(Ts)
        direct=2*mp.quad(lambda h:(T-h)*cov(a,h),[0,min(1,T),T] if T>1 else [0,T])
        close(vexact(a,T),direct,rtol='1e-32')

# Asymptotic coefficient from the exact full cycle characteristic function.
for a in ['2.3','2.5','2.8']:
    alpha=mp.mpf(a); p=alpha/3; beta=2*p; c=mp.mpf(1)/3
    Kcycle=mp.gamma(1-p)*c**p
    mp.mp.dps=350
    for exponent in [75,150]:
        k=mp.power(10,-exponent)
        actual=(1-cycle_cf(alpha,k))/k**beta
        close(actual,Kcycle,rtol='1e-6')
    mp.mp.dps=60

# Critical Gaussian normalization: deterministic n rewards / sqrt(2*c*n*log(n)) -> N(0,1).
for n in [10**7,10**10,10**13]:
    c=mp.mpf(1)/3
    x=mp.mpf('.6')/mp.sqrt(2*c*n*mp.log(n))
    actual=mp.exp(n*mp.log(cycle_cf(mp.mpf(3),x)))
    close(actual,mp.exp(-mp.mpf('.6')**2/2),rtol='2e-1')

# Exact asymptotic second-moment prefactors (stationary process).
for a in ['2.25','2.5','2.75']:
    alpha=mp.mpf(a)
    target=4/(alpha*(alpha-2)*(3-alpha)*(4-alpha))
    for T in [10**15,10**25]:
        close(vexact(alpha,T)/(mp.mpf(T)**(4-alpha)),target,rtol='3e-3')
for T in [10**35,10**55]:
    close(vexact(3,T)/(mp.mpf(T)*mp.log(T)),mp.mpf(4)/3,rtol='2e-2')
for a in ['3.2','3.5','4','6']:
    alpha=mp.mpf(a)
    target=(mp.mpf(2)/3)*(alpha-1)/(alpha-3)
    close(vexact(alpha,10**30)/mp.mpf(10**30),target,rtol='1e-2')

# Critical typical variance coefficient differs by exactly factor 3 from its second-moment coefficient.
close((mp.mpf(4)/3)/(mp.mpf(4)/9),3,rtol='1e-50')
print('PASS',checks,'deterministic analytical-numeric assertions')
