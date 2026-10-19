#!/usr/bin/env python3
"""Finite verification of exact constant-letter complement spectra.
No external dependencies. Run: python3 verify.py
"""
from itertools import product, combinations
from math import comb


def complement_count(w, k, a=0):
    positions = [i for i, c in enumerate(w) if c == a]
    if len(positions) < k:
        return 0
    return len({tuple(c for i, c in enumerate(w) if i not in I)
                for subset in combinations(positions, k)
                for I in (set(subset),)})


def truncated_product(lengths, k):
    dp = [1] + [0] * k
    for x in lengths:
        nd = [0] * (k + 1)
        for i, val in enumerate(dp):
            for j in range(min(x, k-i) + 1):
                nd[i+j] += val
        dp = nd
    return dp[k]


def exact_formula(n, k):
    best = 0
    winners = []
    for r in range(1, min((n+1)//2, n-k+1)+1):
        m=n-r+1
        t,s=divmod(m,r)
        val=truncated_product([t]*(r-s)+[t+1]*s,k)
        if val>best:
            best=val
            winners=[r]
        elif val==best:
            winners.append(r)
    return best, winners


def triple_formula(n):
    assert n>=3
    if n == 3:return 1
    if n == 5:return 2
    if n == 7:return 5
    if n%2:
        return comb((n+1)//2,3)
    r=n//2
    return (comb(r,3) if r>=3 else 0)+r-1


def run_lengths(w, a=0):
    out=[];run=0
    for c in w:
        if c==a:run+=1
        elif run:
            out.append(run)
            run=0
    if run:out.append(run)
    return out


def main():
    total=0
    # Independently enumerate actual deletion embeddings, not just run profiles.
    for q,max_n in [(2,12),(3,8)]:
        for n in range(1,max_n+1):
            maxima=[0]*(n+1)
            for w in product(range(q),repeat=n):
                runs=run_lengths(w)
                for k in range(1,sum(runs)+1):
                    val=complement_count(w,k)
                    assert val==truncated_product(runs,k),(q,n,w,k,val,runs)
                    if val>maxima[k]:maxima[k]=val
                total+=1
            for k in range(1,n+1):
                expect,_=exact_formula(n,k)
                assert maxima[k]==expect,(q,n,k,maxima[k],expect)
    for n in range(3,251):
        assert exact_formula(n,3)[0]==triple_formula(n),n
    print('VERIFY_OK',f'words={total}', 'alphabet_cases=2,3', 'max_n=12,8', 'triple_n<=250')

if __name__=='__main__':main()
