#!/usr/bin/env python3
"""Exact independent checks of subsequence embedding multiplicities.

No external libraries, tables, or stored mathematical results are used.
"""
from collections import Counter, defaultdict
from itertools import product
from math import comb


def embedding_counts(host):
    """Count all index-increasing embeddings by dynamic programming on positions."""
    dp={'':1}
    for a in host:
        for t,c in list(dp.items()):
            dp[t+a]=dp.get(t+a,0)+c
    dp.pop('')
    return dp


def weakdesc(word):
    return sum(a>=b for a,b in zip(word,word[1:]))


def predicted_n(q,m,d):
    return sum((-1)**i * comb(m+1,i) * (comb(q*(d+1-i),m) if q*(d+1-i)>=m else 0)
               for i in range(d+1))


def check():
    cases=0; targets=0; histogram_entries=0; zero_checks=0
    for q in (2,3,4,5):
        for k in range(1,8):
            n=q*k
            if n>14:
                continue
            host=''.join(map(str,range(q)))*k
            actual=embedding_counts(host)
            observed=defaultdict(Counter)
            for u, multiplicity in actual.items():
                m=len(u); d=weakdesc(u)
                expected=comb(k+m-1-d,m) if d<=k-1 else 0
                assert expected==multiplicity, (q,k,u,multiplicity,expected)
                observed[m][multiplicity]+=1
                targets+=1
            for m in range(1,n+1):
                predicted=Counter()
                for d in range(m):
                    number=predicted_n(q,m,d)
                    assert number>=0
                    if d<=k-1:
                        mult=comb(k+m-1-d,m)
                        predicted[mult]+=number
                    else:
                        zero_checks+=1
                assert predicted==observed[m],(q,k,m,predicted,observed[m])
                assert sum(mult*count for mult,count in predicted.items())==comb(n,m)
                histogram_entries+=len(predicted)
            cases+=1
    # All d between the sharp endpoints are realizable; test analytically predicted
    # nonzero class counts for additional much larger exact parameter ranges.
    formal_checks=0
    for q in range(2,11):
        for k in range(1,20):
            for m in range(1,min(q*k,40)+1):
                dmin=(m-1)//q
                dmax=min(k-1,m-1)
                for d in range(m):
                    positive = predicted_n(q,m,d)>0
                    assert positive==(dmin<=d<=m-1),(q,k,m,d)
                    if d<=k-1:
                        formal_checks+=1
                assert sum(predicted_n(q,m,d)*comb(k+m-1-d,m) for d in range(dmax+1))==comb(q*k,m)
    print('VERIFY_OK literal_hosts=',cases,'distinct_targets=',targets,'histogram_bins=',histogram_entries,
          'absent_degree_checks=',zero_checks,'formal_positive_coefficients=',formal_checks)
    for q,k in [(2,3),(3,3),(4,2)]:
        print('PROFILE',q,k,'m=2',dict(Counter(embedding_counts(''.join(map(str,range(q)))*k)[u] for u in productmap(q,2))))


def productmap(q,m):
    for x in product(map(str,range(q)), repeat=m):
        yield ''.join(x)

if __name__ == '__main__':
    check()
