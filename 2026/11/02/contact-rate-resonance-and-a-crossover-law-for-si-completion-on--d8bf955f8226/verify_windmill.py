#!/usr/bin/env python3
"""Reproduce exact SI windmill stage/moment and extreme-value calculations.

No third-party modules. This code tests, but does not substitute for, the proofs.
"""
from fractions import Fraction as Q
from math import factorial, comb, exp, log, sqrt, isclose


def rates(k, beta, gamma):
    return [(k-j)*(beta+j*gamma) for j in range(k)]


def graph_moments(k, beta, gamma, degree=4):
    """Independent state-by-state solution of the full labeled leaf CTMC."""
    total_states=1 << k
    full=total_states-1
    M=[[Q(0) for _ in range(total_states)] for _ in range(degree+1)]
    M[0]=[Q(1) for _ in range(total_states)]
    ordered=sorted(range(full), key=lambda mask:mask.bit_count(), reverse=True)
    for r in range(1,degree+1):
        for mask in ordered:
            j=mask.bit_count()
            step_rate=beta+j*gamma
            jump_rate=(k-j)*step_rate
            assert jump_rate>0
            M[r][mask]=(r*M[r-1][mask]+sum(step_rate*M[r][mask | (1 << i)]
                        for i in range(k) if not (mask & (1 << i))))/jump_rate
    return [M[r][0] for r in range(degree+1)]


def stage_moments(k,beta,gamma,degree=4):
    """Raw moments via cumulants of independently distributed holding times."""
    lam=rates(k,beta,gamma)
    raw=[Q(1)]
    for r in range(1,degree+1):
        raw.append(sum(comb(r-1,l-1)*factorial(l-1)*sum(Q(1,x**l) for x in lam)*raw[r-l]
                      for l in range(1,r+1)))
    return raw


def survival_uniformization(k,beta,gamma,t):
    """Independent CTMC uniformization, no inversion of Laplace transforms."""
    lam=[float(v) for v in rates(k,beta,gamma)]
    nu=max(lam)
    mean=nu*t
    weight=exp(-mean)
    stage=[0.0]*(k+1)
    stage[0]=1.0
    ans=0.0
    max_iter=max(100,int(mean+20*sqrt(mean+1)+50))
    for n in range(max_iter):
        ans+=weight*sum(stage[:-1])
        weight*=mean/(n+1)
        new=[0.0]*(k+1)
        for j in range(k):
            new[j]+=stage[j]*(1-lam[j]/nu)
            new[j+1]+=stage[j]*lam[j]/nu
        new[k]+=stage[k]
        stage=new
    return ans


def h(d):
    if abs(d)<1.e-8:
        return 1-d/2+d*d/6
    return -__import__('math').expm1(-d)/d


def centered_time(k,beta,gamma,m,x=0):
    lam=rates(k,beta,gamma)
    a=min(lam)
    if gamma==beta:
        return (log(m)+log(log(m))+2*log(k-1)+x)/a
    jstar=lam.index(a)
    C=1.0
    for j,other in enumerate(lam):
        if j!=jstar:
            C*=other/(other-a)
    return (log(m)+log(C)+x)/a


def run():
    cases=[(Q(1),Q(0)),(Q(1),Q(1)),(Q(1),Q(2)),(Q(2),Q(1)),(Q(1),Q(3,2)),(Q(3,2),Q(1,2))]
    checks=0
    for k in range(2,8):
        for beta,gamma in cases:
            actual=graph_moments(k,beta,gamma,4)
            predicted=stage_moments(k,beta,gamma,4)
            assert actual==predicted,(k,beta,gamma,actual,predicted)
            checks+=5
            for mask in range(1<<k):
                j=mask.bit_count()
                if j<k:
                    total=sum(beta+gamma*sum(bool(mask&(1<<z)) for z in range(k))
                              for i in range(k) if not mask&(1<<i))
                    assert total==rates(k,beta,gamma)[j]
                    checks+=1
    for k in range(2,10):
        lam=rates(k,Q(1),Q(1)); a=k
        product=Q(1)
        for j in range(1,k-1):
            product*=lam[j]/(lam[j]-a)
        assert product==(k-1)**2
        checks+=1
    for beta,gamma in [(1.0,1.0),(1.0,0.0),(1.0,2.0)]:
        k=2
        for t in (0.1,0.7,1.5,3.0,7.0):
            a=2*beta;b=beta+gamma
            if a==b:
                expected=exp(-a*t)*(1+a*t)
            else:
                expected=(b*exp(-a*t)-a*exp(-b*t))/(b-a)
            actual=survival_uniformization(k,beta,gamma,t)
            assert isclose(expected,actual,rel_tol=1e-9,abs_tol=1e-12)
            checks+=1
    print('Exact independent CTMC moment/cut-rate, product and CDF checks:',checks)
    target=exp(-1.0)
    for k in (2,3,4):
        for gamma in (0.0,1.0,2.0):
            for m in (10**4,10**6,10**8):
                t=centered_time(k,1.0,gamma,m)
                tail=survival_uniformization(k,1.0,gamma,t)
                p=exp(m*__import__('math').log1p(-tail))
                assert 0<p<1
                if m==10**8:print('fixed',k,gamma,m,'limit_CDF',round(p,7),'Gumbel',round(target,7),'diff',round(p-target,7))
                checks+=1
    for k in (2,3,4):
        for c in (-4.0,0.0,4.0):
            d=(k-1)*c/k
            H=(k-1)**2*h(d)
            for m in (10**4,10**6,10**8):
                beta=1.0; gamma=beta*(1+c/log(m))
                a=k*beta
                t=(log(m)+log(log(m))+log(H))/a
                tail=survival_uniformization(k,beta,gamma,t)
                p=exp(m*__import__('math').log1p(-tail))
                assert 0<p<1
                if m==10**8:print('window',k,c,m,'limit_CDF',round(p,7),'Gumbel',round(target,7),'diff',round(p-target,7))
                checks+=1
    print('Total passed calculations:',checks)

if __name__=='__main__':run()
