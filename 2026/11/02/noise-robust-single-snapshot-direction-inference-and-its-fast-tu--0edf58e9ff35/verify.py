"""Reproducible numerical and symbolic checks for orientation inference in a confined run-and-tumble system.

Requires Python 3, NumPy, SciPy, SymPy.  Numerical tests supplement the analytic theorem.
"""
from __future__ import annotations
import math
import numpy as np
from scipy.integrate import quad
from scipy.special import beta as beta_func, erf, ndtr, digamma
import sympy as sp

ASSERTIONS = 0

def check(condition, note):
    global ASSERTIONS
    ASSERTIONS += 1
    if not condition:
        raise AssertionError(note)

def univar_success(beta, delta):
    # Integrate against the beta law of t=Z^2, not the raw signed density.
    if delta == 0:
        # Equivalent to Gamma(beta+1/2)/(beta sqrt(pi)Gamma(beta)):
        m = math.exp(math.lgamma(beta+0.5)-math.lgamma(beta+1)-.5*math.log(math.pi))
        return .5*(1+m)
    B = beta_func(.5,beta)
    def f(t):
        return .5*math.sqrt(t)*erf(math.sqrt(t)/(math.sqrt(2)*delta))/B
    ans,err=quad(f,0.,1.,weight='alg',wvar=(-.5,beta-1),epsabs=2e-11,epsrel=2e-11,limit=250)
    return .5+ans

def univar_success_alt(beta,delta):
    # Alternative integration by parts and Gaussian smoothing expression.
    if delta==0:
        return univar_success(beta,0)
    B = beta_func(.5,beta)
    # Weighted quadrature with the 1/sqrt(t) endpoint factor outside the kernel.
    q,_=quad(lambda t: math.exp(-t/(2*delta*delta))/2,0,1,weight='alg',wvar=(-.5,beta),epsabs=2e-11,epsrel=2e-11)
    return .5 + q/(beta*B*math.sqrt(2*math.pi)*delta)

def posterior_mean(beta,delta,x):
    if delta==0: return x
    # Symmetric latent density with Gaussian observation; normalization cancels.
    def num(z): return z*(1-z*z)**(beta-1)*math.exp(-.5*((x-z)/delta)**2)
    def den(z): return (1-z*z)**(beta-1)*math.exp(-.5*((x-z)/delta)**2)
    # Endpoint-singular adaptive integrator.
    numerator=quad(num,-1,1,points=[-.999999,0,.999999],epsabs=1e-10,epsrel=1e-10,limit=400)[0]
    denominator=quad(den,-1,1,points=[-.999999,0,.999999],epsabs=1e-10,epsrel=1e-10,limit=400)[0]
    return numerator/denominator

def main():
    # Symbolically check the stationary Fokker-Planck flux cancellation.
    z,b=sp.symbols('z b', real=True, positive=True)
    p=(1-z*z)**(b-1)
    pp=p*(1+z)/2
    pm=p*(1-z)/2
    residual=-sp.diff((1-z)*pp,z)+b*(pm-pp)
    check(sp.simplify(residual)==0,'plus-state Fokker-Planck equation')
    residual2=-sp.diff((-1-z)*pm,z)+b*(pp-pm)
    check(sp.simplify(residual2)==0,'minus-state Fokker-Planck equation')
    check(sp.simplify((pp-pm)/p-z)==0,'conditional drift identity')
    # Exact beta moment relations.
    for n in range(1,8):
        moment=sp.prod(2*j-1 for j in range(1,n+1))/sp.prod(2*b+2*j-1 for j in range(1,n+1))
        lhs=sp.gamma(n+sp.Rational(1,2))*sp.gamma(b+sp.Rational(1,2))/(sp.gamma(sp.Rational(1,2))*sp.gamma(n+b+sp.Rational(1,2)))
        check(sp.simplify(sp.expand_func(lhs)-moment)==0,f'even moment n={n}')
    # Orthogonal 2D directional code:
    physical={'E':(1,1),'N':(1,-1),'W':(-1,-1),'S':(-1,1)}
    for theta in np.linspace(-math.pi,math.pi,721,endpoint=False):
        x,y=math.cos(theta),math.sin(theta)
        inferred=physical[max(physical,key=lambda name:(1+physical[name][0]*(x+y))*(1+physical[name][1]*(x-y)))]
        direct=(1 if x+y>0 else -1,1 if x-y>0 else -1)
        check(inferred==direct,f'orthogonal map theta={theta}')
    # The beta-Gaussian integral and independent integration-by-parts formula agree.
    bs=[.25,.5,1.,1.5,3.,8.,15.]
    ds=[.08,.3,.7,1.3,4.]
    for beta in bs:
        former=1.
        for delta in [0]+ds:
            p1=univar_success(beta,delta)
            p2=univar_success_alt(beta,delta)
            check(abs(p1-p2)<1.4e-9,f'integral representations beta={beta} delta={delta}: {p1},{p2}')
            check(.5<p1<1.,f'nontrivial accuracy beta={beta} delta={delta}')
            check(p1<former+1e-11,f'noise monotonicity beta={beta} delta={delta}')
            former=p1
    for d in [0,.05,.3,1.]:
        probs=[univar_success(b,d) for b in bs]
        check(all(x>y for x,y in zip(probs,probs[1:])),f'rate monotonicity delta={d}')
    # The athermal entropy identity is compared to direct beta integration.
    for beta in [.2,.5,1.,2.,5.,10.]:
        val=digamma(beta+1)-digamma(beta+.5) # 2D mutual info in nats
        check(val>0,'mutual information positive')
        if abs(beta-1)<1e-8:
            check(abs(val-(2*math.log(2)-1))<1e-13,'beta=1 exact mutual information')
        # Numerical integration with beta weights on t=Z^2.
        def entropy(z):
            v=(1+z)/2
            return 0. if v<=0. or v>=1. else -v*math.log(v)-(1-v)*math.log(1-v)
        B=beta_func(.5,beta)
        E,_=quad(lambda t:entropy(math.sqrt(t)),0,1,weight='alg',wvar=(-.5,beta-1),epsabs=2e-11,epsrel=2e-11)
        check(abs((math.log(2)-E/B)*2-val)<3e-9,f'entropy beta={beta}')
    # Fixed thermal strength: the fast-tumbling exponent changes from 1/sqrt(beta) to 1/beta.
    for delta in [.25,.8,2.]:
        for beta in [100,300,1000]:
            val=univar_success(beta,delta)-.5
            leading=1/((2*beta+1)*math.sqrt(2*math.pi)*delta)
            check(abs(val-leading)<1.5/(beta*beta*delta**3),f'fixed-noise asymptotic beta={beta} delta={delta}')
    # Crossover: sqrt(beta)*(success - 1/2) -> 1/[2sqrt(pi(1+lambda^2))].
    for lam in [0.,.3,1.,3.]:
        for beta in [50,150,500]:
            p=univar_success(beta,lam/math.sqrt(2*beta))
            rhs=1/(2*math.sqrt(math.pi*(1+lam*lam)))
            check(abs(math.sqrt(beta)*(p-.5)-rhs)<.012,f'crossover beta={beta} lambda={lam}')
    # Direct stationary sampling with a known beta-conditional heading law.
    rng=np.random.default_rng(17429)
    for beta,delta in [(.4,0.),(1.,.3),(3.,.5),(10.,1.)]:
        count=180_000
        U=rng.beta(beta,beta,size=(count,2))*2-1
        S=(rng.random((count,2)) < (1+U)/2).astype(np.int8)*2-1
        observed=U+rng.normal(scale=delta,size=(count,2))
        predicted=np.where(observed>=0,1,-1)
        empirical=(predicted==S).all(axis=1).mean()
        theoretical=univar_success(beta,delta)**2
        check(abs(empirical-theoretical)<.009,f'Monte Carlo beta={beta} delta={delta} {empirical=} {theoretical=}')
    print(f'PASS {ASSERTIONS} reproducible analytic/numerical diagnostics')

if __name__=='__main__':main()
