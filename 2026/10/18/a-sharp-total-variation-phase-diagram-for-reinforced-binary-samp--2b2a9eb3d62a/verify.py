"""Standalone finite checks for a beta-binomial/binomial comparison.

Only uses the Python 3 standard library. Finite tests corroborate, not prove,
the analytic infinite-parameter result.
"""
from fractions import Fraction
from math import comb, erf, exp, lgamma, log, pi, sqrt


def exact_pmf(n, a, b):
    """Beta-binomial rational masses at integer alpha=a,b."""
    den = 1
    for j in range(n):
        den *= a + b + j
    ans = []
    for k in range(n + 1):
        u = v = 1
        for j in range(k):
            u *= a + j
        for j in range(n-k):
            v *= b + j
        ans.append(Fraction(comb(n, k) * u * v, den))
    return ans


def exact_bin(n, a, b):
    A=a+b
    return [Fraction(comb(n,k)*a**k*b**(n-k),A**n) for k in range(n+1)]


def pmfs(n,p,A):
    a,b=A*p,A*(1-p)
    def lb(k):
        return lgamma(n+1)-lgamma(k+1)-lgamma(n-k+1)+k*log(p)+(n-k)*log(1-p)
    def lx(k):
        return (lgamma(n+1)-lgamma(k+1)-lgamma(n-k+1)
                +lgamma(a+k)-lgamma(a)+lgamma(b+n-k)-lgamma(b)
                -lgamma(A+n)+lgamma(A))
    return [exp(lb(k)) for k in range(n+1)], [exp(lx(k)) for k in range(n+1)]


def gaussian_tv(r):
    if r <= 0:
        return 0.
    if r == float('inf'):
        return 1.
    h=log(1+r)/r
    a=sqrt((1+r)*h)
    b=sqrt(h)
    Phi=lambda x: (1+erf(x/sqrt(2)))/2
    return 2*(Phi(a)-Phi(b))


def main():
    exact_checks=0
    for n in range(2, 12):
        for a in (1,2,3,5,11):
            for b in (1,2,4,9):
                bb=exact_pmf(n,a,b)
                bi=exact_bin(n,a,b)
                assert sum(bb)==sum(bi)==1
                ratio=[bb[k]/bi[k] for k in range(n+1)]
                assert ratio[0]>1 and ratio[-1]>1
                assert all(ratio[k+2]*ratio[k]>ratio[k+1]**2
                           for k in range(n-1))
                bad=[k for k in range(n+1) if bb[k]<bi[k]]
                assert bad and bad==list(range(bad[0],bad[-1]+1))
                tv=sum(abs(x-y) for x,y in zip(bb,bi))/2
                assert tv==sum(bi[k]-bb[k] for k in bad)
                exact_checks+=1
    expected=exp(-.5)/sqrt(2*pi)
    numeric=[]
    for p in (.23,.37,.7):
        for ratio in (.25,1.0,3.):
            for n in (300,900):
                b,x=pmfs(n,p,n/ratio)
                tv=sum(abs(t-s) for t,s in zip(x,b))/2
                target=gaussian_tv(ratio)
                numeric.append((p,ratio,n,tv,target))
                assert abs(tv-target)<0.025, (p,ratio,n,tv,target)
        for n in (300,900):
            A=n*n
            b,x=pmfs(n,p,A)
            tv=sum(abs(t-s) for t,s in zip(x,b))/2
            ratio=tv*n
            numeric.append((p,'small',n,ratio,expected))
            assert abs(ratio-expected)<.014,(p,n,ratio,expected)
    print('Exact rational sign-interval and likelihood-ratio comparisons:', exact_checks)
    print('Numerical asymptotic checks:',len(numeric))
    print('Universal small-reinforcement constant:',round(expected,12))
    print('Sample numeric results:')
    for row in numeric[:5]+numeric[-4:]:
        print(row)
    print('PASS')


if __name__=='__main__':
    main()
