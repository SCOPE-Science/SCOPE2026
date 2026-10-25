"""Exact and numerical checks for rooted triangle avoidance in Bernoulli random graphs."""
from fractions import Fraction
from itertools import combinations
from math import comb, log, log1p, exp, lgamma, sqrt


def weights(n, p):
    q = 1-p
    return [Fraction(comb(n-1,d))*p**d*q**(n-1-d+comb(d,2)) for d in range(n)]

def exhaustive(n, p):
    edges = list(combinations(range(n), 2))
    out = [Fraction(0) for _ in range(n)]
    for mask in range(1 << len(edges)):
        e = {edges[k] for k in range(len(edges)) if (mask >> k) & 1}
        nei = {j for j in range(1,n) if (0,j) in e}
        if all((min(a,b),max(a,b)) not in e for a,b in combinations(nei,2)):
            out[len(nei)] += p**len(e)*(1-p)**(len(edges)-len(e))
    return out

def logsumexp(xs):
    m=max(xs)
    return m+log(sum(exp(x-m) for x in xs))

def dist_log(n,p):
    q=1-p
    ls=[lgamma(n)-lgamma(d+1)-lgamma(n-d)+d*log(p)+(n-1-d+d*(d-1)/2)*log(q) for d in range(n)]
    z=logsumexp(ls)
    return ls,z, max(range(n),key=ls.__getitem__)

def W(x):
    # Positive Lambert inverse by monotone Newton iteration.
    y = log1p(x)
    for _ in range(100):
        ey = exp(y)
        yn = y - (y*ey-x)/(ey*(1+y))
        if abs(yn-y) <= 1e-14 * (1+abs(yn)):
            return yn
        y = yn
    raise AssertionError("Lambert iteration did not converge")

def main():
    checks=0
    for n in range(3,7):
        for p in [Fraction(1,3),Fraction(2,5)]:
            ws=weights(n,p)
            ex=exhaustive(n,p)
            assert ws==ex, (n,p,ws,ex)
            checks+=n
            q=1-p
            for d in range(n-1):
                assert ws[d+1]/ws[d] == Fraction(n-1-d,d+1)*p*q**(d-1)
                checks+=1
            for d in range(n-2):
                assert ws[d+1]/ws[d] > ws[d+2]/ws[d+1]
                checks+=1
    for alpha in [.30,.50,.70]:
        for n in [200,1000,10000,100000]:
            c=1.35;p=c*n**(-alpha)
            ls,z,m=dist_log(n,p)
            dstar=W((n-1)*p*p)/p
            assert abs(m-dstar) / dstar < .3, (alpha,n,m,dstar)
            checks+=1
            if alpha==.5 and n>=1000:
                x=W(c*c)/c
                rate=c-x-c*x*x/2
                assert abs(z/sqrt(n)+rate)<.15,(n,z/sqrt(n),rate)
                checks+=1
    print('VERIFIED', checks, 'exact and asymptotic assertions')

if __name__=='__main__': main()
