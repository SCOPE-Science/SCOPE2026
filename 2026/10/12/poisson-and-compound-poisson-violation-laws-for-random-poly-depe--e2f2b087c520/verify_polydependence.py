#!/usr/bin/env python3
"""Standalone finite checks for random two-relation poly-dependence violations."""
from collections import Counter
from math import comb, exp


def pgf_key_coefficients(q):
    """Unweighted one-key coefficient list over all pairs of q-bit fibers."""
    hist=Counter()
    for x in range(1<<q):
        for y in range(1<<q):
            m=x.bit_count()
            k=y.bit_count()
            w=m*k-(x&y).bit_count()
            hist[w]+=1
    return hist


def conv(h,k):
    r=Counter()
    for i,a in h.items():
        for j,b in k.items():r[i+j]+=a*b
    return r


def direct_hist(q):
    words=1<<(q*q)
    result=Counter()
    for x in range(words):
        for y in range(words):
            w=0
            for a in range(q):
                xx=(x>>(q*a))&((1<<q)-1)
                yy=(y>>(q*a))&((1<<q)-1)
                w+=xx.bit_count()*yy.bit_count()-(xx&yy).bit_count()
            result[w]+=1
    return result


def single_key_pgf(q,p,r,t):
    # Stable binomial-mass recursion avoids huge intermediate binomial coefficients.
    weight=(1-p)**q
    answer=0.
    for m in range(q+1):
        factor=(1-r+r*t**(m-1))**m if m else 1.
        answer += weight*factor*(1-r+r*t**m)**(q-m)
        if m<q: weight *= (q-m)/(m+1)*p/(1-p)
    return answer


def satisfaction_prob(q,p,r):
    Ax=(1-p)**q
    Ay=(1-r)**q
    agreement=q*p*r*(1-p)**(q-1)*(1-r)**(q-1)
    return (Ax+Ay-Ax*Ay+agreement)**q


def run():
    for q in (1,2,3):
        one=pgf_key_coefficients(q)
        via=Counter({0:1})
        for _ in range(q):via=conv(via,one)
        direct=direct_hist(q)
        assert direct==via,(q,direct,via)
        assert sum(direct.values())==2**(2*q*q)
        total_zero=(2**(q+1)-1+q)**q
        assert direct[0]==total_zero,(q,direct[0],total_zero)
        expected=sum(w*c for w,c in direct.items())
        assert expected==2**(2*q*q)*q*q*(q-1)/4,(q,expected)
        print('EXHAUSTIVE',q,'pair_relations',2**(2*q*q),'satisfying',total_zero,'support',len(direct))
    for q in range(1,15):
        for p,r in ((.05,.07),(.13,.24),(.5,.5),(.9,.3)):
            assert abs(single_key_pgf(q,p,r,0.)**q-satisfaction_prob(q,p,r))<3e-13
            assert abs(single_key_pgf(q,p,r,1.)-1.)<3e-13
    print('BERNOULLI_EXACT_OK',56)
    for q in (500,2000,8000):
        a,b=.9,1.3
        # Only tests numeric convergence, not a substitute for proof.
        t=.4
        asym1=exp(b*(exp(a*(t-1))-1))
        est1=single_key_pgf(q,a/q,b/q**2,t)**q
        asym2=exp(a*b*(t-1))
        est2=single_key_pgf(q,a/q**1.5,b/q**1.5,t)**q
        print('LIMIT_CHECK',q,'compound_abs_error',round(abs(est1-asym1),6),'poisson_abs_error',round(abs(est2-asym2),6))
        assert abs(est1-asym1)<(20/q)**.5
        assert abs(est2-asym2)<(20/q)**.5
    print('VERIFY_OK')
if __name__=='__main__':run()
