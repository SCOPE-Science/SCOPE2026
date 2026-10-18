#!/usr/bin/env python3
"""Reproduce exact Gaussian two-column condition-test probabilities and asymptotics."""
import math
import numpy as np
from scipy.integrate import quad
from scipy.special import betainc, betaln


def constants(kappa, tau):
    assert kappa > tau > 1
    K, T = kappa*kappa, tau*tau
    I = math.log((K+T)/(2*kappa*tau))
    pref = (K+T)/(K-T)*math.sqrt((K+T)*(T-1)/(4*math.pi*T*(K-1)))
    return I, pref


def exact_prob(kappa, tau, s):
    assert s >= 2 and kappa > tau > 1
    K, T = kappa*kappa, tau*tau
    # Condition h(x)<1 is equivalent to a quadratic in x.
    w2 = T + 2 + 1/T
    # (1+(K-1)x)^2 - K*w2*x*(1-x) < 0.
    aa=(K-1)**2+K*w2
    bb=2*(K-1)-K*w2
    disc=bb*bb-4*aa
    lo=(-bb-math.sqrt(disc))/(2*aa)
    hi=(-bb+math.sqrt(disc))/(2*aa)
    logB=betaln(s/2,s/2)
    def density(x):
        h=(1+(K-1)*x)**2/(K*w2*x*(1-x))
        if h>=1: return 0.0
        # regularized incomplete beta with R=V/(V+Z^2)
        return math.exp((s/2-1)*(math.log(x)+math.log1p(-x))-logB)*betainc(0.5,(s-1)/2,1-h)
    return quad(density,lo,hi,epsabs=1e-15,epsrel=2e-10,limit=250)[0]


def empirical_prob(kappa,tau,s,N=180000,seed=121):
    rng=np.random.default_rng(seed)
    # Bartlett decomposition, sampled in bounded chunks.
    wins=0
    for m in range(0,N,20000):
        size=min(20000,N-m)
        u=rng.chisquare(s,size)
        v=rng.chisquare(s-1,size)
        z=rng.standard_normal(size)
        a=kappa*kappa*u
        d=v+z*z
        delta=(a-d)**2+4*kappa*kappa*u*z*z
        eigenratio=(a+d+np.sqrt(delta))/(a+d-np.sqrt(delta))
        wins+=np.count_nonzero(eigenratio<=tau*tau)
    return wins/N


def importance_prefactor(kappa,tau,s,N=180000,seed=88):
    # Sampling from the exact tilted 2x2 Gaussian distribution C*.
    rng=np.random.default_rng(seed)
    K,T=kappa*kappa,tau*tau
    D=2*K/(K+T)
    A=T*D
    eta=(T-K)/(4*K*T)
    weights=[]
    for m in range(0,N,12000):
        size=min(12000,N-m)
        u=rng.chisquare(s,size)
        v=rng.chisquare(s-1,size)
        z=rng.standard_normal(size)
        ca=A*u/s
        cd=D*(v+z*z)/s
        cab=math.sqrt(A*D)*np.sqrt(u)*z/s
        det=ca*cd-cab*cab
        ratio=(ca+cd)**2/det
        acceptable=ratio<=(tau+1/tau)**2
        h=ca-T*cd
        # tilted likelihood ratio exp(-s I)*exp(-s eta H), hence rescale
        weights.append(np.exp(-s*eta*h)*acceptable)
    return np.concatenate(weights).mean()*math.sqrt(s)


def main():
    number=0
    for kappa,tau in [(2,1.5),(3,2),(4,2)]:
        I,C=constants(kappa,tau)
        assert I>0 and C>0
        K,T=kappa*kappa,tau*tau
        A=2*K*T/(K+T)
        D=2*K/(K+T)
        assert abs(A/T-D)<1e-12
        eta=(T-K)/(4*K*T)
        sigma=2*T*D
        c=(T+1)/(A-D)
        C_from_tilt=1/(abs(eta)*sigma*math.sqrt(2*math.pi)*math.sqrt(1+2*abs(eta)*c*A*D))
        assert abs(C-C_from_tilt)<1e-11
        number+=4
        vals=[]
        for s in [10,20,50,100,200]:
            p=exact_prob(kappa,tau,s)
            assert 0<p<1
            vals.append(p)
            number+=1
        assert all(vals[j]>vals[j+1] for j in range(len(vals)-1))
        number+=1
        pred= C*math.exp(-100*I)/10
        print('parameters',kappa,tau,'rate',round(I,12),'prefactor',round(C,12),
              'exact_p100',format(vals[3],'.12g'),'leading_p100',format(pred,'.12g'))
    for kappa,tau,s in [(2,1.5,8),(3,2,10),(4,2,10)]:
        exact=exact_prob(kappa,tau,s)
        mc=empirical_prob(kappa,tau,s)
        err=math.sqrt(max(exact*(1-exact),.001)/180000)
        assert abs(mc-exact)<6*err+0.0001,(kappa,tau,s,mc,exact,err)
        print('direct Gaussian',kappa,tau,s,'Monte Carlo',mc,'exact',exact)
        number+=1
    for kappa,tau,s in [(2,1.5,300),(3,2,300),(4,2,300)]:
        I,C=constants(kappa,tau)
        sampled=importance_prefactor(kappa,tau,s)
        assert abs(sampled/C-1)<.12,(kappa,tau,s,sampled,C)
        print('tilted prefactor',kappa,tau,s,'empirical',sampled,'theory',C)
        number+=1
    print('PASS:',number,'deterministic, quadrature, Gaussian-sampling and importance checks')


if __name__=='__main__':
    main()
