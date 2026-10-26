#!/usr/bin/env python3
"""Exact checks of random-mapping cyclic-core conditional laws; stdlib only."""
from fractions import Fraction
from itertools import product
from collections import Counter
from math import factorial, sqrt, log


def unsigned_stirling(n):
    a = [[0]*(n+1) for _ in range(n+1)]
    a[0][0] = 1
    for r in range(1,n+1):
        for k in range(1,r+1):
            a[r][k] = a[r-1][k-1]+(r-1)*a[r-1][k]
    return a


def symmetric_reciprocals(n):
    # e[j](1,1/2,...,1/(n-1)), where index 'n' is the cyclic count.
    e=[Fraction(1)]+[Fraction(0)]*n
    ans={1:e[:2]}
    for c in range(2,n+1):
        x=Fraction(1,c-1)
        for j in range(c-1,0,-1):
            e[j]+=x*e[j-1]
        ans[c]=e[:c+1]
    return ans


def ck_of_function(f):
    n=len(f)
    cyclic=set()
    components=set()
    for start in range(n):
        seen={}
        p=start
        t=0
        while p not in seen:
            seen[p]=t
            t+=1
            p=f[p]
        cyc=[v for v,i in seen.items() if i>=seen[p]]
        cyclic.update(cyc)
        components.add(min(cyc))
    return len(cyclic),len(components)


def main():
    checks=0
    for n in range(1,6):
        actual=Counter(ck_of_function(f) for f in product(range(n),repeat=n))
        s=unsigned_stirling(n)
        for c in range(1,n+1):
            forest_count=c*n**(n-c-1) if c<n else 1
            # c*n^(n-c-1) is integral for c<n; n=c is treated separately.
            if c<n: assert forest_count == int(forest_count)
            for k in range(1,c+1):
                expected=(factorial(n)//factorial(n-c))*int(forest_count)*s[c][k]//factorial(c)
                # recompute without intermediate divisibility assumption
                expected2=(factorial(n)*int(forest_count)*s[c][k])//(factorial(c)*factorial(n-c))
                assert expected==expected2, (n,c,k,'counts')
                assert actual[c,k]==expected,(n,c,k,actual[c,k],expected)
                checks+=2
        assert sum(actual.values())==n**n
        checks+=1
    for n in range(2,51):
        s=unsigned_stirling(n)
        e=symmetric_reciprocals(n)
        for c in range(1,n+1):
            for k in range(1,c+1):
                assert e[c][k-1]==Fraction(s[c][k],factorial(c-1))
                checks+=1
        for k in range(1,n+1):
            ratios=[]
            for c in range(k,n):
                p=Fraction(n-c,n)
                ratio=p*(1+Fraction(e[c][k-2],c*e[c][k-1])) if k>1 else p
                # brute exact normalized consecutive weight ratios
                q_c=Fraction(factorial(n),factorial(n-c)*n**c)
                q_cp1=Fraction(factorial(n),factorial(n-c-1)*n**(c+1))
                assert ratio == q_cp1*e[c+1][k-1]/(q_c*e[c][k-1])
                if ratios:
                    assert ratios[-1]>ratio,(n,k,c,ratios[-1],ratio)
                    checks+=1
                ratios.append(ratio)
                checks+=1
    # numerically inspect predicted mode at increasingly large n.
    for n,k in [(1000,2),(10000,2),(100000,2),(100000,3),(100000,4)]:
        e=[0.0]*k;e[0]=1.0
        q=1.0
        weights=[]
        for c in range(1,n+1):
            if c>1:
                q*=1-(c-1)/n
                v=1/(c-1)
                for j in range(min(k-1,c-1),0,-1):e[j]+=v*e[j-1]
            if c>=k:weights.append((q*e[k-1],c))
            if c>5000 and q<1e-100:break
        mode=max(weights)[1]
        assert abs(mode-sqrt(2*(k-1)*n/log(n)))/sqrt(2*(k-1)*n/log(n))<0.2,(n,k,mode)
        checks+=1
    print('PASS',checks,'exact/analytic-identity assertions plus numerical mode smoke checks')

if __name__=='__main__':main()
