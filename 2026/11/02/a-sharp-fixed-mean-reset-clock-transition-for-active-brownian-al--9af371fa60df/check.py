"""Independent finite diagnostic checks for the renewal-clock alignment theorem.

Analytic proof, not these tests, establishes universal optimality.
Requires Python 3, numpy, scipy, sympy.
"""
import math
import numpy as np
from scipy.integrate import quad, solve_ivp
from scipy.optimize import brentq
from sympy import symbols, exp, integrate, simplify, diff

checks = 0

def check(cond, msg="assertion"):
    global checks
    if not cond:
        raise AssertionError(msg)
    checks += 1

def F(t, k, g, v=1.0):
    if k == g:
        return v*t*math.exp(-k*t)
    return v*(math.exp(-g*t)-math.exp(-k*t))/(k-g)

def G(t, k, g, v=1.0):
    if k == g:
        return v*(-math.expm1(-k*t)-k*t*math.exp(-k*t))/(k*k)
    return v*((-math.expm1(-g*t))/g-(-math.expm1(-k*t))/k)/(k-g)

def tmax(k,g):
    return 1.0/k if k == g else math.log(k/g)/(k-g)

def tau(k,g):
    t0=tmax(k,g)
    h=lambda t:t*F(t,k,g)-G(t,k,g)
    return brentq(h, t0, max(20.0/min(k,g),t0*40), xtol=2e-14)

def envelope(m,k,g):
    t=tau(k,g)
    return F(t,k,g) if m<=t else G(m,k,g)/m

# Formal differentiation, used only for the model identities (not for the concave-envelope proof).
t,k,g,symv=symbols('t k g v', positive=True)
fform=symv*(exp(-g*t)-exp(-k*t))/(k-g)
gform=symv*((1-exp(-g*t))/g-(1-exp(-k*t))/k)/(k-g)
check(simplify(diff(gform,t)-fform)==0, 'integrated reward derivative')
check(simplify(diff(t*fform-gform,t)-t*diff(fform,t))==0, 'tangency derivative')
check(simplify(integrate(fform,(t,0,t))-gform)==0,'symbolic reward integration')

cases=[(0.1,1),(0.5,1),(1,1),(2,1),(10,1),(1,3),(3,1),(4,4)]
rng=np.random.default_rng(20240911)
for kk,gg in cases:
    critical=tau(kk,gg)
    check(critical>tmax(kk,gg),'critical time after peak')
    check(abs(critical*F(critical,kk,gg)-G(critical,kk,gg))<2e-10,'tangent')
    check(abs(F(critical,kk,gg)-G(critical,kk,gg)/critical)<1e-10,'value match')
    # Independent two-component moment evolution, without substituting the closed form.
    grid=np.linspace(0,3*critical,13)
    evolution=solve_ivp(lambda z,y:[-gg*y[0], -kk*y[1]+y[0]],
                        (0,float(grid[-1])), [1.0,0.0], t_eval=grid,
                        rtol=2e-12,atol=2e-13)
    check(evolution.success,'moment ODE solvability')
    for xx,ex in zip(grid,evolution.y[1]):
        check(abs(ex-F(float(xx),kk,gg))<2e-10,'independent moment ODE')
    for x in np.linspace(0.02, 6*critical, 30):
        check(F(critical,kk,gg)+1e-12>=G(x,kk,gg)/x,'global normalized reward bound')
        check(abs(quad(lambda z:F(z,kk,gg),0,x,epsabs=1e-10)[0]-G(x,kk,gg))<1e-9,'direct quadrature')
    for _ in range(200):
        n=int(rng.integers(2,8))
        vals=np.exp(rng.uniform(-4,3,n))*critical
        w=rng.dirichlet(np.ones(n))
        m=float(np.dot(w,vals))
        payoff=float(np.dot(w,[G(x,kk,gg) for x in vals]))/m
        check(payoff<=envelope(m,kk,gg)+2e-11,'arbitrary discrete clock upper bound')
    for m in [0.1*critical,0.5*critical,0.9*critical]:
        vals=[]
        for eps in [m/20,m/100,m/1000,m/10000]:
            p=(m-eps)/(critical-eps)
            reward=((1-p)*G(eps,kk,gg)+p*G(critical,kk,gg))/m
            vals.append(reward)
            check(reward < F(critical,kk,gg),'nonattainment for positive waiting times')
        check(abs(vals[-1]-envelope(m,kk,gg))<2e-4*max(1,F(critical,kk,gg)),'bursty sharp limit')
    for rr in [0.03,0.2,1,3,10]:
        poisson=rr*quad(lambda z:math.exp(-rr*z)*G(z,kk,gg),0,400/rr,epsabs=1e-11)[0]*rr
        # E[G(T)]/E[T] = r^2 integral exp(-rt) G(t) dt
        direct=rr/((rr+kk)*(rr+gg))
        check(abs(poisson-direct)<1e-9,'Poisson consistency')
    rstar=math.sqrt(kk*gg)
    poiss_best=rstar/((rstar+kk)*(rstar+gg))
    check(F(critical,kk,gg)>poiss_best,'sharp deterministic versus best Poisson')

root=tau(1,1)
check(abs(math.exp(root)-(1+root+root*root))<1e-11,'resonant transcendental root')
check(abs(root-1.7932821329008575)<1e-11,'resonant critical time')
check(abs(F(root,1,1)-0.2984256075256264)<1e-11,'resonant optimal alignment')
print(f'{checks} finite/symbolic diagnostic assertions passed')
print(f'resonant critical time: {root:.15f}')
print(f'best renewal: {F(root,1,1):.15f}; best Poisson: {0.25:.15f}')
