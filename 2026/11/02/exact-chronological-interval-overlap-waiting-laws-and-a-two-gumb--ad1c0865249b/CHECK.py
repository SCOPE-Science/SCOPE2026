"""Exact independently reproducible checks for chronological colour-interval coverage.

No numerical computation in this script substitutes for the all-size proof.
Run with Python 3: python CHECK.py
"""
from fractions import Fraction
from itertools import product, combinations
from math import factorial, comb


def stirling2(n, k):
    if k > n or k < 0:
        return 0
    dp = [0]*(k+1)
    dp[0] = 1
    for i in range(1,n+1):
        nxt=[0]*(k+1)
        for j in range(1,min(k,i)+1):
            nxt[j]=j*dp[j]+dp[j-1]
        dp=nxt
    return dp[k]


def direct_overlap(word, m):
    if len(set(word)) < m:
        return False
    first = [word.index(j) for j in range(m)]
    last = [len(word)-1-word[::-1].index(j) for j in range(m)]
    return max(first) <= min(last)


def structural_overlap(word, m):
    seen=set()
    tau=None
    for i,x in enumerate(word):
        seen.add(x)
        if len(seen)==m:
            tau=i
            break
    if tau is None:
        return False
    return all(j in word[tau+1:] for j in range(m) if j!=word[tau])


def uniform_count(m, n):
    if n<m:
        return 0
    out=0
    for t in range(m,n+1):
        prefix=factorial(m)*stirling2(t-1,m-1)
        suffix=sum((-1)**r*comb(m-1,r)*(m-r)**(n-t)
                    for r in range(m))
        out +=prefix*suffix
    return out


def nonuniform_cdf(weights, n):
    m=len(weights)
    total=sum(weights)
    p=tuple(Fraction(w,total) for w in weights)
    out=Fraction()
    for l in range(m):
        other=[i for i in range(m) if i!=l]
        for t in range(1,n+1):
            a=Fraction()
            b=Fraction()
            for r in range(m):
                for ss in combinations(other,r):
                    a += (-1)**r*(1-p[l]-sum(p[i] for i in ss))**(t-1)
                    b += (-1)**r*(1-sum(p[i] for i in ss))**(n-t)
            out +=p[l]*a*b
    return out


checks=0
for m in (2,3,4):
    max_n={2:9,3:9,4:8}[m]
    for n in range(m,max_n+1):
        count=0
        for word in product(range(m),repeat=n):
            overlap=direct_overlap(word,m)
            assert overlap == structural_overlap(word,m),(m,n,word)
            checks +=1
            count +=overlap
        assert count==uniform_count(m,n),(m,n,count,uniform_count(m,n))
        checks +=1

# General nonuniform exact CDF, independently enumerate weighted words.
for weights,maxn in [((1,2),8),((1,2,3),8),((1,1,2,3),7)]:
    m=len(weights)
    p=[Fraction(w,sum(weights)) for w in weights]
    for n in range(m,maxn+1):
        total=Fraction()
        for word in product(range(m),repeat=n):
            if direct_overlap(word,m):
                prob=Fraction(1)
                for j in word: prob *= p[j]
                total +=prob
        pred=nonuniform_cdf(weights,n)
        assert total==pred,(weights,n,total,pred)
        checks+=1

# Check the exact first two moments for the complete-overlap hitting time
# via the independent geometric variables, using the exact success rates.
for m in range(2,20):
    rates=list(range(1,m+1))+list(range(1,m))
    mu=sum((Fraction(m,j) for j in rates),Fraction())
    var=sum((Fraction(m*(m-j),j*j) for j in rates),Fraction())
    H=sum((Fraction(1,j) for j in range(1,m+1)),Fraction())
    H2=sum((Fraction(1,j*j) for j in range(1,m+1)),Fraction())
    assert mu==2*m*H-1
    assert var==2*m*m*H2-2*m*H
    checks+=2

# Check minimum possible hitting time and its probability.
for m in range(2,30):
    n=2*m-1
    assert uniform_count(m,n)==factorial(m)*factorial(m-1)
    checks+=1
print(f'PASS: {checks} independent exact finite assertions')
