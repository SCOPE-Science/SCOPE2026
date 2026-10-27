"""Exact finite checks for rooted triangle birth times in a two-parent recursive graph."""
from fractions import Fraction
from itertools import product
from math import factorial, comb, log


def birth_prob(q):
    return Fraction(2*q-1, q*q)


def analytic_moments(n):
    # Arrival s belongs to {2,...,n}; q=s-1 existing vertices.
    dmean = {1: Fraction(0)}
    dsecond = {1: Fraction(0)}
    py = {2: Fraction(0)}
    for s in range(2, n+1):
        q = s-1
        mu = dmean[s-1]
        m2 = dsecond[s-1]
        py[s] = 2*mu/Fraction(q*q)
        p = birth_prob(q)
        dmean[s] = mu+p
        dsecond[s] = m2+2*p*mu+p
    pair = {}
    for s in range(2,n+1):
        for t in range(s+1,n+1):
            q, r = s-1, t-1
            mu = dmean[s-1]
            m2 = dsecond[s-1]
            future = sum((birth_prob(u-1) for u in range(s+1,t)), Fraction(0))
            pair[(s,t)] = 4*(m2+mu+mu*future)/Fraction(q*q*r*r)
    return dmean, py, pair


def exhaustive(n):
    d_total = Fraction(0)
    y_count = [0]*(n+1)
    pair_count = {(s,t):0 for s in range(2,n+1) for t in range(s+1,n+1)}
    choices = [list(product(range(1,s),repeat=2)) for s in range(2,n+1)]
    count = 0
    for sequence in product(*choices):
        root_neighbors = {2}
        ys = [0]*(n+1)
        for s, parents in enumerate(sequence,start=2):
            if s == 2:
                continue
            p1,p2 = parents
            ys[s] = int(1 in parents and ((p1 in root_neighbors and p1 != 1) or (p2 in root_neighbors and p2 != 1)))
            if 1 in parents:
                root_neighbors.add(s)
        d_total += len(root_neighbors)
        for s in range(2,n+1):
            y_count[s]+=ys[s]
            for t in range(s+1,n+1):
                pair_count[(s,t)]+=ys[s]*ys[t]
        count+=1
    dn, py, pair=analytic_moments(n)
    assert count==factorial(n-1)**2
    assert d_total/count==dn[n]
    for s in range(2,n+1):
        assert Fraction(y_count[s],count)==py[s], (s,y_count[s], count,py[s])
    for k,v in pair_count.items():
        assert Fraction(v,count)==pair[k], (k,v,count,pair[k])
    return count, (n-1)+comb(n-1,2)


def small_window(n, cutoff):
    # Two exact recursions for the probability of any post-cutoff rooted triangle.
    # DP tracks root degree and whether a triangle has appeared after cutoff.
    dp = {(0,False): Fraction(1)}
    for t in range(2,n+1):
        q=t-1
        nd={}
        for (d,hit),w in dp.items():
            outcomes=[(d,False, Fraction((q-1)**2,q*q)),
                      (d+1,False,Fraction(2*q-1-2*d,q*q)),
                      (d+1,True,Fraction(2*d,q*q))]
            for d2,y,p in outcomes:
                if p==0:continue
                key=(d2,hit or (y and t>cutoff))
                nd[key]=nd.get(key,Fraction(0))+w*p
        dp=nd
        assert sum(dp.values(),Fraction(0))==1
    return sum((v for (d,h),v in dp.items() if h),Fraction(0))


def check_windows():
    for n in range(3,11):
        d,py,pair=analytic_moments(n)
        for N in range(2,n):
            ans=small_window(n,N)
            e=sum((py[t] for t in range(N+1,n+1)),Fraction(0))
            b=sum((pair[(s,t)] for s in range(N+1,n+1) for t in range(s+1,n+1)),Fraction(0))
            assert e-b <= ans <= e, (n,N,ans,e,b)

if __name__=='__main__':
    count, tests=exhaustive(6)
    check_windows()
    print('EXACT_BIRTH_ENUMERATION_PASS',count,'configurations;',tests,'moment comparisons')
    print('EXACT_WINDOW_BONFERRONI_PASS',sum(range(1,9)),'windows')
    for N in (100,1000,10000):
        # An asymptotic diagnostic for expected late triangles, NOT a proof of tail probability.
        from scipy.special import polygamma, digamma
        # Exact E[Z_N] computed by summing a convergent positive series to a large cutoff;
        # omitted positive terms are bounded analytically in the manuscript.
        import numpy as np
        q=np.arange(N,2000001,dtype=np.float64)
        mu=2*(digamma(q)+0.5772156649015328606) - (np.pi**2/6-polygamma(1,q))
        approx=float(np.sum(2*mu/q**2))
        leading=(4*log(N)+4+4*0.5772156649015328606-2*np.pi**2/6)/N
        print('TAIL_EXPECTATION_DIAGNOSTIC',N,round(approx,8),round(leading,8),'lower_bound_due_to_truncation')
    print('VERIFY_OK')
