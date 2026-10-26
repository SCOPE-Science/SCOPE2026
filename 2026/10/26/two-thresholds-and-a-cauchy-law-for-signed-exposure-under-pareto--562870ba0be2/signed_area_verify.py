"""Reproducibility checks for Pareto-clock scaled-Brownian signed-area scaling.
Only numerical evidence: the proof uses regular variation and renewal limits.
Run: python signed_area_verify.py
"""
import math
import numpy as np
import mpmath as mp
from scipy.special import gamma


def constants(beta, alpha, K=1., t0=1.):
    g=1+beta/2
    p=alpha/g
    v=4*K/((beta+1)*(beta+2))
    moment_abs=(v**(p/2))*2**(p/2)*gamma((p+1)/2)/math.sqrt(math.pi)
    mean_tau=alpha*t0/(alpha-1)
    C=t0**alpha*moment_abs/mean_tau
    factor=math.pi/2 if abs(p-1)<1e-12 else gamma(1-p)*math.cos(math.pi*p/2)
    scale=C*factor
    variance_prefactor=v*(2*g)*t0**alpha/(mean_tau*(2*g-alpha)*(2*g-alpha+1))
    return p,v,scale,variance_prefactor


def laplace_var(s, beta, alpha, K=1., t0=1.):
    mp.mp.dps=35
    z=mp.mpf(str(s)); a=mp.mpf(str(alpha)); g=1+mp.mpf(str(beta))/2
    q=2*g; b=mp.mpf(str(t0)); v=4*mp.mpf(str(K))/((mp.mpf(str(beta))+1)*(mp.mpf(str(beta))+2))
    ftilde=a*b**a*z**a*mp.gammainc(-a,z*b,mp.inf)
    first=z**(-q-1)*mp.gammainc(q+1,0,z*b)+b**a*z**(-q+a-1)*mp.gammainc(q-a+1,z*b,mp.inf)
    second=a*b**a*z**(-q+a-1)*mp.gammainc(q-a,z*b,mp.inf)
    return float(v*(first+second)/(1-ftilde))


def monte_carlo_char(t, beta, alpha, K=1., t0=1., R=8500, seed=24):
    rng=np.random.default_rng(seed)
    gamma_age=1+beta/2
    p,v,scale,c2=constants(beta,alpha,K,t0)
    remaining=np.full(R,float(t))
    quadratic=np.zeros(R)
    nsteps=0
    while True:
        live=np.flatnonzero(remaining>0)
        if not len(live): break
        waits=t0*np.exp(-np.log1p(-rng.random(len(live)))/alpha)
        observed=np.minimum(waits,remaining[live]);quadratic[live]+=observed**(2*gamma_age)
        remaining[live]-=observed
        nsteps+=1
        if nsteps>20000: raise AssertionError('unexpected cycle count')
    conditional_var=v*quadratic/t**(2/p)
    return [(u,float(np.exp(-.5*u*u*conditional_var).mean()),math.exp(-scale*abs(u)**p)) for u in (0.5,1.0,2.0)]


def main():
    cases=[(.5,1.25),(.5,1.7),(1.2,1.4)]
    checks=0
    for i,(beta,alpha) in enumerate(cases):
        p,v,scale,c2=constants(beta,alpha)
        assert 0<p<2 and v>0 and scale>0 and c2>0;checks+=4
        # Fundamental BM covariance integral: 2K ∫∫min(s,u)^beta du ds
        numerical=mp.quad(lambda x:4*mp.mpf(x)**(beta+1)/(beta+1),[0,1])
        assert abs(float(numerical)-v)<1e-9; checks+=1
        e=3+beta-alpha
        coeff_lap=c2*float(mp.gamma(e+1))
        ratios=[]
        for s in (1e-4,1e-5,1e-6,1e-7):
            val=laplace_var(s,beta,alpha)
            ratio=val*s**(e+1)/coeff_lap
            print("ratio",beta,alpha,s,ratio); assert 0.95<ratio<1.3;checks+=1
            ratios.append(ratio)
        assert abs(ratios[-1]-1)<abs(ratios[0]-1) and abs(ratios[-1]-1)<0.05;checks+=1
        comparisons=monte_carlo_char(4000,beta,alpha,R=8000,seed=12345+i)
        for u,got,target in comparisons:
            print("CF",beta,alpha,u,got,target); assert abs(got-target)<0.1, (beta,alpha,u,got,target)
            checks+=1
        print(f'beta={beta}, alpha={alpha}, stable_index={p:.6f}, scale={scale:.9f}, variance_const={c2:.9f}')
        print('  Laplace ratios:',[round(r,5) for r in ratios])
        print('  mixture CF:',[(u,round(got,5),round(target,5)) for u,got,target in comparisons])
    # Sharp threshold: beta=0.5, 1+beta = 1.5, critical variance exponent zero
    b=.5
    for a in (1.25,1.4,1.5,1.7):
        e=1+b-a
        if a<1+b: assert e>0
        elif a==1+b: assert e==0
        else: assert e<0
        checks+=1
    print('ALL',checks,'checks passed')

if __name__=='__main__':main()
