"""Reproduce finite-degree calculations for the two-channel attention-limited incidence map.

The infinite-cutoff and all-parameter conclusions are proved analytically
in RESULT.md; finite computations are corroboration, not those proofs.
"""
from math import exp, log, log1p, isclose


def reproduction(L, tau, alpha, r, lam):
    assert L >= 1 and 2 < tau < 3 and 0 <= alpha <= 1
    assert 0 <= lam <= 1 and 0 <= r < 1/(1+lam)
    numer = denom = 0.0
    for d in range(1, L+1):
        edge_weight = d**(1-tau)
        v = d**(1-alpha)
        numer += edge_weight*d*(-log1p(-r/v)-log1p(-lam*r/v))
        denom += edge_weight
    return numer/denom


def component(L, tau, alpha, z):
    return reproduction(L,tau,alpha,z,0.0)


def bisect(f,lo,hi,steps=100):
    assert f(lo) < 0 and f(hi) > 0
    for _ in range(steps):
        m=(lo+hi)/2
        if f(m)>0:hi=m
        else:lo=m
    return (lo+hi)/2


def critical_r(L,tau,alpha,lam):
    high=(1-1e-11)/(1+lam)
    return bisect(lambda r:reproduction(L,tau,alpha,r,lam)-1,0.0,high)


def direct_incidence(L,tau,alpha,r,lam,theta_s,theta_d):
    denom=0.0
    output_s=output_d=0.0
    for d in range(1,L+1):
        w=d**(1-tau)
        denom+=w
        p=r/d**(1-alpha); q=lam*p
        output_s+=w*(1-exp(d*(theta_s*log1p(-p)+theta_d*log1p(-q))))
        output_d+=w*(1-exp(d*(theta_s*log1p(-q)+theta_d*log1p(-p))))
    return output_s/denom,output_d/denom


def run():
    L,tau,alpha,r,lam=19,2.5,0.6,0.25,0.35
    h=1e-7
    f_ss=direct_incidence(L,tau,alpha,r,lam,h,0)[0]/h
    f_sd=direct_incidence(L,tau,alpha,r,lam,0,h)[0]/h
    f_ds=direct_incidence(L,tau,alpha,r,lam,h,0)[1]/h
    assert abs(f_ss-component(L,tau,alpha,r)) < 2e-5
    assert abs(f_sd-component(L,tau,alpha,lam*r)) < 2e-5
    assert abs(f_ds-component(L,tau,alpha,lam*r)) < 2e-5

    # At degree-one cutoff and equal leakage, the threshold solves 2[-log(1-r)]=1.
    assert abs(critical_r(1,2.5,0,1)-(1-exp(-0.5))) < 1e-10
    last=0
    for L in [1,2,4,8,16,64,256,1024]:
        root=critical_r(L,2.5,0,0.5)
        assert 0<root<2/3 and root>last
        assert abs(reproduction(L,2.5,0,root,0.5)-1)<1e-12
        last=root
    print('Strict finite-cutoff ordering at zero recommendation mediation: PASS')

    for L in [1,2,8,64,1024]:
        a=component(L,2.5,0,0.5)
        assert 0.5<a<=log(2)+1e-14 and log(2)<1
        lc=bisect(lambda ell:component(L,2.5,0,ell/2) -(1-a),0,1)
        assert 0<lc<1
        assert a+component(L,2.5,0,lc/2)>1-1e-12
        assert a+component(L,2.5,0,(lc+1)/4)>1
        print('L=',L,'A(1/2)=',round(a,12),'leakage onset=',round(lc,12))
    assert abs(bisect(lambda ell:component(1,2.5,0,ell/2) -(1-component(1,2.5,0,0.5)),0,1)-(2-4/exp(1)))<1e-11

    from math import fsum
    zeta_15=fsum(d**-1.5 for d in range(1,1000000)) + 2/(1000000**0.5) # Euler-Maclaurin coarse bound O(1e-9)
    # Alpha critical = 1/2 when tau=5/2. Limiting critical prefactor ~= zeta(3/2)/(1+lam).
    lim_log=zeta_15/1.5
    lim_power=.5*zeta_15/1.5
    for L in [128,2048,32768]:
        crit_log=critical_r(L,2.5,.5,.5)
        crit_pow=critical_r(L,2.5,1,.5)
        print('L=',L, 'rcrit(alpha=.5)*log L=',round(crit_log*log(L),10),
              'rcrit(alpha=1)*sqrt(L)=',round(crit_pow*L**.5,10))
    assert abs(critical_r(32768,2.5,1,.5)*(32768**.5)-lim_power)<0.01
    print('Finite-difference Jacobian, thresholds, coupling, scaling: PASS')

if __name__=='__main__':
    run()
