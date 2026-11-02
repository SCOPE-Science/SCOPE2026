#!/usr/bin/env python3
"""Exact finite checks for the hill/area dependence theorem on Catalan paths."""
from collections import Counter
from functools import lru_cache
from math import comb

@lru_cache(None)
def dyck(n):
    if n == 0:
        return ('',)
    return tuple('U'+a+'D'+b for i in range(n) for a in dyck(i) for b in dyck(n-1-i))

def stats(s):
    height=0; area=0; hills=0
    for i,ch in enumerate(s):
        if ch=='U':
            area += height
            if height==0 and i+1 < len(s) and s[i+1]=='D': hills+=1
            height+=1
        else: height-=1
        assert height>=0
    assert height==0
    return hills,area

def test():
    checks=0
    for n in range(1,11):
        paths=dyck(n); cn=comb(2*n,n)//(n+1)
        assert len(paths)==cn; checks+=1
        counts=Counter(stats(s) for s in paths)
        sh=sum(h*count for (h,a),count in counts.items())
        sa=sum(a*count for (h,a),count in counts.items())
        sha=sum(h*a*count for (h,a),count in counts.items())
        assert sh==cn; checks+=1
        assert 2*(cn*sha-sh*sa)==-(n-1)*cn*cn;checks+=1
        pairs=[]
        for i in range(n):
            for left in dyck(i):
                for right in dyck(n-1-i):
                    pairs.append((left,right))
        assert len(pairs)==cn;checks+=1
        pair_count=Counter()
        diffs=Counter()
        for a,b in pairs:
            ap=stats(a)[1]+stats(b)[1]
            pair_count[ap]+=1
            diffs[len(a)//2]+=1
        sizebiased=Counter()
        for (h,a),k in counts.items():
            sizebiased[a]+=h*k
        assert pair_count==sizebiased;checks+=1
        # A coupled ordinary path is U A D B and the hill-biased path
        # has area exactly area(A)+area(B).
        for a,b in pairs:
            ordinary='U'+a+'D'+b
            assert stats(ordinary)[1] == stats(a)[1]+stats(b)[1]+len(a)//2
            checks+=1
        assert 2*sum(k*v for k,v in diffs.items())==(n-1)*cn; checks+=1
        # Stochastic domination of size-biased area by uniform area.
        plain=Counter();
        for (h,a),k in counts.items(): plain[a]+=k
        maxarea=max(plain)
        for t in range(maxarea+1):
            assert sum(v for x,v in sizebiased.items() if x>=t)<=sum(v for x,v in plain.items() if x>=t)
            checks+=1
        if n>=2:
            assert sum(v for x,v in sizebiased.items() if x>=1)<sum(v for x,v in plain.items() if x>=1) or any(sum(v for x,v in sizebiased.items() if x>=t)<sum(v for x,v in plain.items() if x>=t) for t in range(maxarea+1))
            checks+=1
        print(f'n={n} Catalan={cn} sum_hills={sh} mixed={sha} total_area={sa} covariance= -{n-1}/2, tested')
    print(f'PASS: {checks} exact assertions')
if __name__=='__main__': test()
