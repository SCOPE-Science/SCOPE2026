"""Independent numerical checks for a stationary mean-reverting diffusion with proportional Poisson contractions.
Uses an embedded variance recursion and direct conditional-age quadrature; no external data.
"""
import math
import numpy as np
from scipy.integrate import quad
from scipy.special import gammaln

def run(seed=20261014):
    rng = np.random.default_rng(seed)
    kappa,D,r,a = 1.0,1.0,1.2,0.35
    alpha=r/(2*kappa)
    n=180000
    u=0.4
    data=np.empty(n)
    for i in range(n):
        w=rng.random()**(1/alpha) # exp(-2 kappa * exponential reset age)
        u=1-(1-a*a*u)*w
        data[i]=u
    # Compare the stationary variance moments with exact generator recursion
    m=1.0
    for degree in range(1,7):
        m*=degree/(degree+alpha*(1-a**(2*degree)))
        empirical=float(np.mean(data**degree))
        assert abs(empirical-m)<0.013, (degree,empirical,m)
    # Independent exact series for K = E[(1-a^2 U)^(-alpha)]
    mm=1.0; c=1.0; K=1.0
    for j in range(1,120):
        mm*=j/(j+alpha*(1-a**(2*j)))
        c*=(alpha+j-1)/j*a*a
        K+=c*mm
    Kmc=float(np.mean((1-a*a*data)**(-alpha)))
    assert abs(K-Kmc)<0.002, (K,Kmc)
    # Direct conditional-age integration to obtain the exact density on exponential scale.
    # q = x^2/(2D/kappa), exact density divided by the stationary OU Gaussian core.
    # Deterministic quadrature, with a random pre-reset variance sample.
    sample=data[::1200]
    def scaled_density(q, U):
        H=1-a*a*U
        upper=q*H
        def integrand(z):
            t=z/q
            if t>=1: return 0.0
            return z**(alpha-1)*(1-t)**(-.5)*math.exp(-z/(1-t))
        integral=quad(integrand,0,upper,epsabs=1.e-10,epsrel=1.e-10,limit=160)[0]
        return alpha*(q*H)**(-alpha)*integral
    result=[]
    predicted=math.gamma(alpha+1)*K
    for q in [8., 20., 45., 90.]:
        value=float(np.mean([scaled_density(q,u) for u in sample]))
        normalized=value*q**alpha
        result.append((q,normalized,predicted,normalized/predicted))
    assert abs(result[-1][-1]-1)<0.025
    assert result[0][-1]<result[1][-1]<result[2][-1]<result[3][-1] < 1.001
    # Kummer-Moyal stationary approximation instead has polynomial tails.
    s=0.15; lam=1.0
    approx_tail_exponent=2*(kappa+lam)/(lam*s)+2
    assert approx_tail_exponent>0
    print('parameters',dict(kappa=kappa,D=D,r=r,a=a,alpha=alpha))
    print('moment recurrence degrees 1..6 checked, MC size',n)
    print('K_series',K,'K_MC',Kmc,'coefficient',predicted)
    print('q, exact_density_to_OU_core_times_q^alpha, limit, ratio:')
    for row in result:print(' '.join(f'{x:.10g}' for x in row))
    print('approximate diffusive power-law density exponent',approx_tail_exponent)
    print('ALL CHECKS PASSED')

if __name__=='__main__':run()
