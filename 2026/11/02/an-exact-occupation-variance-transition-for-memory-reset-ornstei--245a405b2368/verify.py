"""Reproduce mathematical diagnostics for time-integrated memory-reset OU motion.

Run: pip install -r requirements.txt && python verify.py
These finite checks do not substitute for the analytic proof in RESULT.md.
"""
from fractions import Fraction
import math
import numpy as np
import mpmath as mp

mp.mp.dps = 45
count=0

def check(test, label):
    global count
    count+=1
    if not test:
        raise AssertionError(label)

def y_exact(t, mu, r, D):
    b=mp.mpf(mu)+r
    v=mp.mpf(D)/mu
    p=2*mp.mpf(r)/b
    z=b*t
    if p==1:
        return (2*v/b)*(t*(mp.log(z)+mp.euler+mp.e1(z)-1)+(1-mp.exp(-z))/b)
    return (2*v*t/(b*(p-1)))*(mp.hyp1f1(1-p,2,-z)-1)

# 1. Exact rational coefficient identities for the singular ODE.
# y(t)=sum a_n*t**n; a_0=a_1=0; a_2=v.
for mu,r,D in [(Fraction(1),Fraction(1,2),Fraction(1)),
               (Fraction(1),Fraction(1),Fraction(2)),
               (Fraction(1),Fraction(3),Fraction(1)),
               (Fraction(3,2),Fraction(7,3),Fraction(5,4))]:
    b=mu+r;v=D/mu
    a=[Fraction(0),Fraction(0),v]
    for n in range(2,71):
        a.append((2*r-b*n)*a[n]/(n*(n+1)))
    check(a[2]==v,'quadratic coefficient')
    for n in range(1,70):
        lhs=(n+2)*(n+1)*a[n+2]+(b*(n+1)-2*r)*a[n+1]
        check(lhs==0,f'Taylor coefficient {n}')

# 2. Exact formula independently satisfies the second-order ODE.
for mu,r,D in [(1,0.25,1),(1,0.5,1),(1,1,1),(1,3,1),(2,1,3),(3,10,1)]:
    for t in [mp.mpf('0.015'),mp.mpf('0.1'),mp.mpf('0.7'),mp.mpf('2'),mp.mpf('6')]:
        f=lambda z:y_exact(z,mu,r,D)
        e=mp.diff(f,t,2)+(mu+r)*mp.diff(f,t)-2*r*f(t)/t-2*mp.mpf(D)/mu
        check(abs(e)<mp.mpf('1e-29'),f'ODE residual {mu},{r},{t}: {e}')
        check(f(t)>0,'variance positive')

# 3. Exact transform via numerical quadrature, independently of ODE tests.
for mu,r,D,s in [(1,mp.mpf('0.5'),1,2),(1,1,1,3),(1,3,1,4)]:
    b=mp.mpf(mu)+r;p=2*r/b;v=mp.mpf(D)/mu
    target=2*v/b/s**2*mp.log(1+b/s) if p==1 else 2*v/(b*(p-1)*s**2)*((1+b/s)**(p-1)-1)
    observed=mp.quad(lambda t:mp.exp(-s*t)*y_exact(t,mu,r,D),[mp.mpf('0.000001'),mp.mpf('0.1'),1,4,10,mp.inf])
    check(abs(observed-target)/target<mp.mpf('1e-9'),'Laplace transform')

# 4. Large-time rates at deliberately separated scales.
for mu,r,D in [(1,mp.mpf('0.3'),1),(1,1,1),(1,3,1)]:
    b=mp.mpf(mu)+r;p=2*r/b;v=mp.mpf(D)/mu; t=mp.mpf('10000000')
    a=y_exact(t,mu,r,D)/t**2
    if r<mu: ref=2*v/(mu-r)/t
    elif r==mu:ref=v/mu*(mp.log(2*mu*t)+mp.euler-1)/t
    else:ref=2*v*b**(p-2)/((p-1)*mp.gamma(p+1))*t**(p-2)
    check(abs(a/ref-1)<mp.mpf('0.02'),f'asymptotic constant {r}')

# 5. Independently generate trajectories with resets copying a prior sample.
# Discretization is approximate; compare only within a deliberately wide MC error band.
rng=np.random.default_rng(20261031)
for mu,r,D in [(1,0.5,1),(1,1,1),(1,3,1)]:
    v=D/mu;T=8.0;dt=0.005;nstep=round(T/dt);n=4500
    history=np.zeros((n,nstep+1))
    history[:,0]=rng.normal(0,math.sqrt(v),n)
    cumulative=np.zeros(n)
    a=math.exp(-mu*dt)
    sigma=math.sqrt(v*(1-a*a))
    for k in range(1,nstep+1):
        prev=history[:,k-1]
        jump=rng.random(n)<r*dt
        past=history[np.arange(n),rng.integers(0,k,size=n)]
        prev=np.where(jump,past,prev)
        new=a*prev+sigma*rng.normal(size=n)
        history[:,k]=new
        cumulative+=dt*new
    empirical=float(np.mean((cumulative/T)**2))
    analytic=float(y_exact(mp.mpf(T),mu,r,D)/T**2)
    check(abs(empirical/analytic-1)<0.09,'independent path simulation')
    print(f'Path diagnostic r={r}: empirical={empirical:.9f}, analytic={analytic:.9f}, ratio={empirical/analytic:.5f}')

print(f'PASS: {count} finite exact-rational, analytic and simulation assertions')
