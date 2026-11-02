#!/usr/bin/env python3
"""Standalone exact small-case checks of entropy-word counting for conjugate power partitions."""
from math import comb

def count_via_words(m, q, cap):
    stack=[(1, 0, 0, 0)]
    values=set(); words=0; groups={}
    while stack:
        n, k, t, depth=stack.pop()
        if n>cap: continue
        words+=1;values.add(n)
        groups[(k,t)]=groups.get((k,t),0)+1
        stack.append((n*q, k,t+1,depth+1))
        stack.append((n+(m-1)*m**k, k+1,t,depth+1))
    return values,words,groups

def count_direct(m,q,cap):
    vals=set()
    # Each candidate specified by a nonincreasing sequence of exponents for
    # counts of rows of length >= m**i, ending at a positive power of q.
    for t in range(1): pass
    for t in range(30):
        if q**t>cap: break
        def go(i,last,area):
            # At tail i we can terminate: multiplicity of m**i is q**last
            vals.add(area+m**i*q**last)
            for nxt in range(last+1):
                step=m**i*(q**last-q**nxt)
                if area+step+m**(i+1)*q**nxt>cap:continue
                go(i+1,nxt,area+step)
        go(0,t,0)
    return {n for n in vals if n<=cap}

for m,q,cap in [(2,3,500),(3,2,500),(4,4,2000),(3,6,10000),(2,11,10000),(5,5,10000)]:
    vals,words,groups=count_via_words(m,q,cap)
    # independent direct partition generation; duplicate-free words expected
    direct=count_direct(m,q,cap)
    assert vals==direct,(m,q, sorted(vals^direct)[:20])
    assert len(vals)<=words
    K=T=0
    while m**(K+1)<=cap:K+=1
    while q**(T+1)<=cap:T+=1
    upper=comb(K+T+2,K+1)-1
    assert words<=upper
    for (k,t),x in groups.items():
        assert x<=comb(k+t,k)
    print(f'PASS m={m} q={q} cap={cap} distinct={len(vals)} words={words} bound={upper} K={K} T={T}')
print('VERIFY_OK')
