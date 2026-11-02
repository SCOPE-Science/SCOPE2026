"""Exact and asymptotic verification for asynchronous binary majority on odd bicliques.

Run with Python 3, optional SciPy for the large-population numerical checks.
"""
from math import comb, sqrt
from fractions import Fraction
from functools import lru_cache
from itertools import combinations


def formula(a, b, i, j):
    assert a % 2 and b % 2 and 0 <= i <= a and 0 <= j <= b
    ua, vb = a // 2, b // 2
    if i > ua and j > vb:
        return Fraction(1)
    if i <= ua and j <= vb:
        return Fraction(0)
    if i <= ua and j > vb:
        return 1 - formula(a, b, a-i, b-j)
    k = b-j
    r = i-ua
    s = vb+1-j
    t = r+s-1
    num = sum(comb(k, l)*comb(i, t-l) for l in range(max(s,t-i,0), min(k,t)+1))
    return Fraction(num,comb(i+k,t))


def recurrence(a,b):
    ua, vb = a//2,b//2
    @lru_cache(None)
    def prob(i,j):
        if i > ua and j > vb: return Fraction(1)
        if i <= ua and j <= vb: return Fraction(0)
        if i > ua and j <= vb:
            return (i*prob(i-1,j)+(b-j)*prob(i,j+1))/(i+b-j)
        return ((a-i)*prob(i+1,j)+j*prob(i,j-1))/(a-i+j)
    return prob


# Distinct verifier: enumerate every critical first-update A/B order, not formulas.
def enumerate_first_update_orders(a,b,i,j):
    ua, vb = a//2, b//2
    if i > ua and j > vb: return Fraction(1)
    if i <= ua and j <= vb: return Fraction(0)
    if i <= ua and j > vb: return 1-enumerate_first_update_orders(a,b,a-i,b-j)
    n_A,n_B=i,b-j
    wins=0
    for aset in combinations(range(n_A+n_B),n_A):
        aset=set(aset)
        ca=cb=0
        for event in range(n_A+n_B):
            if event in aset:
                ca+=1
                if i-ca <= ua: break
            else:
                cb+=1
                if j+cb > vb:
                    wins+=1
                    break
    return Fraction(wins,comb(n_A+n_B,n_A))


cases=0; small_orders=0
for a in (1,3,5,7,9,11):
    for b in (1,3,5,7,9,11):
        dp=recurrence(a,b)
        for i in range(a+1):
            for j in range(b+1):
                p=formula(a,b,i,j)
                assert p == dp(i,j), (a,b,i,j,p,dp(i,j))
                cases+=1
                if a<=5 and b<=5:
                    assert p == enumerate_first_update_orders(a,b,i,j),(a,b,i,j)
                    small_orders+=1

fair=0
for m in range(1,80,2):
    for i in range(m//2+1,m+1):
        assert formula(m,m,i,m-i)==Fraction(1,2)
        fair+=1

print('EXACT_CASES',cases,'ORDER_ENUMERATIONS',small_orders,'FAIRNESS_CHECKS',fair)

try:
    from scipy.stats import hypergeom, norm
except ImportError:
    print('SCIPY_UNAVAILABLE - numerical asymptotic checks skipped')
else:
    lam=.3;x=.7;c=1.5
    target=norm.cdf(c*sqrt(lam*(1-lam))/sqrt(x*(2*x-1)))
    for N in (801,2001,5001,10001,20001,50001):
        a=round(lam*N); a+= (a%2==0)
        b=N-a
        if b%2==0: b+=1
        n=a+b
        i=round(x*a)
        y=1-x+c/sqrt(n)
        j=round(y*b)
        assert i>a//2 and j<b//2
        k=b-j;r=i-a//2;s=(b+1)//2-j;t=r+s-1
        p=hypergeom.sf(s-1,i+k,k,t)
        print('CRITICAL',n,'plus_P',round(p,8),'limit',round(target,8),'discrepancy',round(p-target,8))

    for lam,x,y in ((.1,.8,.25),(.2,.72,.18),(.3,.65,.36)):
        for N in (5001,20001):
            a=round(lam*N);a+=(a%2==0); b=N-a
            if b%2==0:b+=1
            i=round(a*x);j=round(b*y)
            k=b-j;r=i-a//2;s=(b+1)//2-j;t=r+s-1
            p=hypergeom.sf(s-1,i+k,k,t)
            print('PHASE',a+b,'local',round(i/a+j/b-1,6),'global_plus',round((i+j)/(a+b),6),'P_plus',round(p,9))
