#!/usr/bin/env python3
from itertools import product


def reductions(w):
    out=set()
    n=len(w)
    for p in range(1,n//2+1):
        for i in range(0,n-2*p+1):
            if w[i:i+p]==w[i+p:i+2*p]:
                out.add(w[:i]+w[i+p:])
    return out


def match_records(w):
    # One record for each maximal run of matches w[t]=w[t+p]
    # whose match length is at least p. Each record is (p,a,b),
    # with [a,b] inclusive in the match sequence.
    n=len(w)
    rec=[]
    for p in range(1,n):
        m=[w[t]==w[t+p] for t in range(n-p)]
        t=0
        while t<len(m):
            if not m[t]:
                t+=1
                continue
            a=t
            while t+1<len(m) and m[t+1]:
                t+=1
            b=t
            if b-a+1>=p:
                rec.append((p,a,b))
            t+=1
    return rec


def min_period(s):
    L=len(s)
    for d in range(1,L+1):
        if all(s[t]==s[t+d] for t in range(L-d)):
            return d
    raise AssertionError


def standard_runs(w):
    n=len(w)
    runs=[]
    for a in range(n):
        for b in range(a+1,n):
            s=w[a:b+1]
            d=min_period(s)
            L=b-a+1
            if L<2*d:
                continue
            left=(a>0 and w[a-1]==w[a-1+d])
            right=(b+1<n and w[b+1]==w[b+1-d])
            if not left and not right:
                runs.append((a,b,d))
    return runs


def distinct_square_factors(w):
    ans=set()
    n=len(w)
    for p in range(1,n//2+1):
        for i in range(n-2*p+1):
            if w[i:i+p]==w[i+p:i+2*p]:
                ans.add(w[i:i+2*p])
    return ans


def check_word(w):
    rec=match_records(w)
    assert len(reductions(w))==len(rec)
    runs=standard_runs(w)
    runset=set(runs)
    for p,a,b in rec:
        # The p-periodic factor corresponding to the match run is w[a:b+p+1].
        d=min_period(w[a:b+p+1])
        assert p%d==0
        assert (a,b+p,d) in runset
    bound=sum((b-a+1)//(2*d) for a,b,d in runs)
    assert len(rec)<=bound
    return len(rec)


def census(q,maxn):
    maxima=[]
    total=0
    alphabet='0123456789'[:q]
    for n in range(1,maxn+1):
        best=0
        for x in product(alphabet, repeat=n):
            w=''.join(x)
            best=max(best,check_word(w))
            total+=1
        maxima.append(best)
    return total,maxima

btotal,bmax=census(2,11)
ttotal,tmax=census(3,7)
assert btotal==4094
assert ttotal==3279
assert bmax==[0,1,1,2,2,3,4,5,5,6,7]
assert tmax==[0,1,1,2,2,3,4]

# Distinct square factors and distinct square-reduction outputs are different invariants.
w='00100'
assert len(reductions(w))==2
assert distinct_square_factors(w)=={'00'}

print('VERIFY_OK binary_words=4094 ternary_words=3279 '
      'binary_max=0,1,1,2,2,3,4,5,5,6,7 '
      'ternary_max=0,1,1,2,2,3,4 witness=00100:reductions2:squares1')
