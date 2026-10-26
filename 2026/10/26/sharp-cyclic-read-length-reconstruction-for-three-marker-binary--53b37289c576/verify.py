#!/usr/bin/env python3
"""Exact small-case verification of cyclic ternary-marker read-length laws.
No libraries beyond Python's standard library are required.
"""
from collections import Counter, defaultdict
from itertools import combinations
from math import comb
from fractions import Fraction as Q

def rotations(w):
    return (w[i:]+w[:i] for i in range(len(w)))

def necklace(w):
    return min(rotations(w))

def spectrum(w, k):
    n = len(w)
    assert 1 <= k <= n
    wrap = w+w
    return tuple(sorted(wrap[i:i+k] for i in range(n)))

def gaps(w):
    ii = [i for i, b in enumerate(w) if b == '1']
    assert len(ii) == 3
    n = len(w)
    return tuple((ii[(j+1)%3]-ii[j]-1) % n for j in range(3))

def threshold(g):
    a,b,c = sorted(g)
    n = a+b+c+3
    if n <= 4:
        return 1
    if a == b == c:
        return a+1
    if a == b:
        return a+1 if c == a+1 else a+2
    if b == c:
        return b+1
    return n-c

def predicted_count(n,k):
    # Independent closed-form distribution. Valid for n >= 5.
    m=n-3
    D=max(0, (k-2)//2-max(0,2*k-n-2))
    small=sum(1 for a in range((m-1)//3+1)
              if (a+1 if m==3*a+1 else a+2)==k)
    large=sum(1 for b in range(m//3+1,m//2+1) if b+1==k)
    equal=int(m%3==0 and k==m//3+1)
    return 2*D+small+large+equal

def run():
    raw_words=0; necklaces=0; tested_spectra=0
    for n in range(3,29):
        all_w = []
        for sites in combinations(range(n),3):
            w=''.join('1' if i in sites else '0' for i in range(n))
            all_w.append(w)
        raw_words+=len(all_w)
        ww=sorted({necklace(w) for w in all_w})
        necklaces+=len(ww)
        preds={w:threshold(gaps(w)) for w in ww}
        actual={w:None for w in ww}
        for k in range(1,n+1):
            groups=defaultdict(list)
            for w in ww:
                groups[spectrum(w,k)].append(w)
                tested_spectra+=1
            for gs in groups.values():
                if len(gs)==1 and actual[gs[0]] is None:
                    actual[gs[0]]=k
        assert actual==preds, (n,[(w,actual[w],preds[w])
                                     for w in ww if actual[w]!=preds[w]])
        if n>=5:
            counts=Counter(preds.values())
            assert all(counts[k]==predicted_count(n,k) for k in range(1,n+1)),(n,counts)
            assert len(ww)==(comb(n-1,2)+2*int(n%3==0))//3
            if n>=6:
                assert max(preds.values())==2*n//3
                expected_max=4 if n%3==1 and n>=10 else 2
                assert counts[2*n//3]==expected_max,(n,counts)
        print('n=%d necklaces=%d max_threshold=%d' %(n,len(ww),max(preds.values())))
    # Exact integration of the two polynomial pieces of the limiting CDF.
    def integral_poly(powers, lo, hi):
        return sum(v*(hi**(i+1)-lo**(i+1))/Q(i+1)
                   for i,v in powers.items())
    a=Q(0); b=Q(1,2); c=Q(2,3)
    e=integral_poly({0:Q(1),2:Q(-3)},a,b)+integral_poly({0:Q(4),1:Q(-12),2:Q(9)},b,c)
    e2=2*(integral_poly({1:Q(1),3:Q(-3)},a,b)+integral_poly({1:Q(4),2:Q(-12),3:Q(9)},b,c))
    assert e==Q(7,18) and e2-e*e==Q(13,648),(e,e2-e*e)
    print('PASS limit_mean=%s limit_variance=%s' %(e,e2-e*e))
    print('PASS raw_weight_three_words=%d necklaces=%d spectra=%d'
          %(raw_words,necklaces,tested_spectra))

if __name__ == '__main__':
    run()
