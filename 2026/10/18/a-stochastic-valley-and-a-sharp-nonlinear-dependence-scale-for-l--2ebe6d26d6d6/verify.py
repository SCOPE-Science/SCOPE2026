"""Exact finite checks for leaf-count/marked-degree laws in uniform labeled trees.

All finite assertions use integer arithmetic or fractions.  Limiting proofs are in RESULT.md.
"""
from collections import Counter, defaultdict
from fractions import Fraction as F
from itertools import product
from math import comb, factorial

CHECKS=0

def check(a,b,msg):
    global CHECKS
    assert a==b, (msg,a,b)
    CHECKS+=1

def stirling2(t,k):
    s=[[0]*(t+1) for _ in range(t+1)]
    s[0][0]=1
    for a in range(1,t+1):
        for b in range(1,a+1):
            s[a][b]=b*s[a-1][b]+s[a-1][b-1]
    return s[t][k] if 0<=k<=t else 0

def empty_law(q,t):
    return {e:F(comb(q,e)*factorial(q-e)*stirling2(t,q-e),q**t)
            for e in range(q+1) if q-e<=t}

def conditional_law(n,k):
    m=n-2
    q=n-1
    raw=empty_law(q,m-k)
    return {e+(1 if k==0 else 0):p for e,p in raw.items()}

def cond_mean_formula(n,k):
    m=n-2
    q=n-1
    return (1 if k==0 else 0)+q*F(q-1,q)**(m-k)

def degree_prob(n,k):
    return F(comb(n-2,k)*(n-1)**(n-2-k),n**(n-2))

def total_leaf_var(n):
    m=n-2
    p=F(n-1,n)**m
    p2=F(n-2,n)**m
    return n*p*(1-p)+n*(n-1)*(p2-p*p)

def corr_ratio(n):
    m=n-2
    gbar=n*F(n-1,n)**m
    vg=sum((degree_prob(n,k)*(cond_mean_formula(n,k)-gbar)**2
            for k in range(m+1)),F(0))
    return vg/total_leaf_var(n)

def tail(law,h):
    return sum((p for x,p in law.items() if x>=h),F(0))

for n in range(4,20):
    m=n-2
    q=n-1
    laws=[conditional_law(n,k) for k in range(m+1)]
    for k,law in enumerate(laws):
        check(sum(law.values()),F(1),(n,k,'normalization'))
        check(sum((x*p for x,p in law.items()),F(0)),cond_mean_formula(n,k),
              (n,k,'conditional mean'))
    for h in range(n+1):
        check(tail(laws[0],h)>=tail(laws[1],h),True,(n,h,'leaf vs degree 2'))
        for k in range(1,m):
            check(tail(laws[k+1],h)>=tail(laws[k],h),True,(n,k,h,'higher degree'))
    check(any(tail(laws[0],h)>tail(laws[1],h) for h in range(n+1)),True,
          (n,'strict first comparison'))
    for k in range(1,m):
        check(any(tail(laws[k+1],h)>tail(laws[k],h) for h in range(n+1)),True,
              (n,k,'strict later comparison'))
    check(sum((degree_prob(n,k) for k in range(m+1)),F(0)),F(1),
          (n,'degree normalization'))
    EXL=sum((degree_prob(n,k)*cond_mean_formula(n,k) for k in range(m+1)),F(0))
    EDL=sum((degree_prob(n,k)*(k+1)*cond_mean_formula(n,k)
             for k in range(m+1)),F(0))
    check(EXL,n*F(n-1,n)**m,(n,'leaf mean'))
    check(EDL,F(2*(n-1),n)*EXL,(n,'zero covariance'))
    check(corr_ratio(n)>0,True,(n,'nonlinear dependence'))

for n in range(4,9):
    freq=defaultdict(Counter)
    m=n-2
    for word in product(range(n),repeat=m):
        k=word.count(0)
        leaves=sum((x not in word) for x in range(n))
        freq[k][leaves]+=1
    for k in range(m+1):
        den=sum(freq[k].values())
        check(F(den,n**m),degree_prob(n,k),(n,k,'exhaustive weight'))
        actual={leaf:F(count,den) for leaf,count in freq[k].items()}
        expected={leaf:p for leaf,p in conditional_law(n,k).items() if p}
        check(actual,expected,(n,k,'exhaustive distribution'))

print('PASS:',CHECKS,'exact assertions; exhaustive Prüfer arrays for n=4,...,8.')
for n in [10,25,50,100,200,500,1000]:
    # Floating approximations here are illustrative only; not evidence for a limit.
    print('n=',n,' n*eta^2=',round(n*float(corr_ratio(n)),9))
