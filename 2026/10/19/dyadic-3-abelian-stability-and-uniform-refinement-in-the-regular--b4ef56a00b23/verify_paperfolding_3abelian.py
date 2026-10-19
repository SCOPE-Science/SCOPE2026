#!/usr/bin/env python3
"""Finite exact signature certificate and independent direct word checks.

For the regular paperfolding word f, f(2t)=t mod 2 and f(2t+1)=f(t).
The finite symbolic recurrence covers every factor position, not just a prefix.
"""
from collections import Counter, defaultdict
from itertools import product


def f_recurrence(n):
    while n % 2:
        n //= 2
    return (n // 2) % 2


def f_odd_part(n):
    n += 1
    while n % 2 == 0:
        n //= 2
    return int(n % 4 == 3)


def triplet(a, b, c):
    return (a << 2) + (b << 1) + c


def q(e, b):
    """The four length-3 patterns starting at offsets 0,1,2,3 of a 4-block."""
    return ((0, e, 1), (e, 1, b), (1, b, 0), (b, 0, 1-e))


def symbolic_signature(k, delta, x, y, p, e, r):
    """Complete 1-,2-,3-gram signature for start 4j+r, j=2s+e.

    x=f(s), y=f(s+2**(k-3)-1), p=s mod 2;
    delta=number of ones in the length-2**(k-3) factor at s minus
    2**(k-4). All inputs are integral and k>=4.
    """
    m = 1 << (k-2)
    c3 = [0]*8
    for ee, b in product(range(2), repeat=2):
        count = m//4 + (delta if (ee,b)==(1,1) else
                        (-delta if (ee,b)==(1,0) else 0))
        for a0,a1,a2 in q(ee,b):
            c3[triplet(a0,a1,a2)] += count

    first = p if e==0 else x
    last  = y if e==0 else p
    leading=q(e,first)
    trailing=q(1-e,last)
    removed=(
      (trailing[2],trailing[3]) if r==0 else
      (leading[0],trailing[3]) if r==1 else
      (leading[0],leading[1]) if r==2 else
      (leading[1],leading[2])
    )
    for a0,a1,a2 in removed:
        c3[triplet(a0,a1,a2)] -= 1

    suffix=(
      (1,last) if r==0 else (last,0) if r==1
      else (0,e) if r==2 else (e,1)
    )
    c2 = [c3[2*t]+c3[2*t+1]+int(t==2*suffix[0]+suffix[1])
          for t in range(4)]
    c1 = [c2[0]+c2[1]+int(suffix[1]==0),
          c2[2]+c2[3]+int(suffix[1]==1)]
    assert sum(c3)==(1<<k)-2
    assert sum(c2)==(1<<k)-1
    assert sum(c1)==(1<<k)
    return tuple(c1+c2+c3)


def next_states(T):
    return {(d,p,y,0) for d,x,y,p in T} | {(d,x,p,1) for d,x,y,p in T}


def signatures_at(k,T):
    assert k>=4
    return {symbolic_signature(k,d,x,y,p,e,r)
            for (d,x,y,p) in T for e in (0,1) for r in range(4)}


def raw_signatures(sequence, n, analytic=None):
    c1=[0]*2
    c2=[0]*4
    c3=[0]*8
    for t in range(n): c1[sequence[t]]+=1
    for t in range(n-1): c2[2*sequence[t]+sequence[t+1]]+=1
    for t in range(n-2):c3[triplet(*sequence[t:t+3])]+=1
    seen=set()
    factors=set()
    N=len(sequence)
    half=1<<(n.bit_length()-4) # n=2**k, half=2**(k-3)
    for i in range(N-n+1):
        full=tuple(c1+c2+c3)
        seen.add(full)
        factors.add(sequence[i:i+n])
        if analytic is not None and i < min(N-n+1,4*n+40):
            j,r=divmod(i,4)
            s,e=divmod(j,2)
            delta=sum(sequence[s:s+half])-half//2
            expect=symbolic_signature(n.bit_length()-1,delta,
                           sequence[s],sequence[s+half-1],s%2,e,r)
            assert full==expect,(n,i,full,expect)
        if i==N-n: break
        c1[sequence[i]]-=1
        c1[sequence[i+n]]+=1
        c2[2*sequence[i]+sequence[i+1]]-=1
        c2[2*sequence[i+n-1]+sequence[i+n]]+=1
        c3[triplet(*sequence[i:i+3])]-=1
        c3[triplet(*sequence[i+n-2:i+n+1])]+=1
    return seen,len(factors)


def main():
    prefix=bytes(f_recurrence(i) for i in range(32768))
    assert all(prefix[i]==f_odd_part(i) for i in range(len(prefix)))
    witness={}
    for s in range(12):
        x,y=prefix[s:s+2]
        witness.setdefault((x+y-1,x,y,s%2),s)
    assert len(witness)==8
    print('T1_witnesses', sorted(witness.items()))
    T=set(witness)
    for h in range(1,9):
        if h>=2: T=next_states(T)
        k=h+3
        assert len(T)=={1:8,2:16,3:20}.get(h,24)
        assert all(-1<=d<=1 for d,x,y,p in T)
        A=signatures_at(k,T)
        expected=32 if k==4 else 36
        assert len(A)==expected,(k,len(A))
        smaller=defaultdict(set)
        for sig in A: smaller[sig[:6]].add(sig[6:])
        assert len(smaller)==12
        split=Counter(len(v) for v in smaller.values())
        assert split==(Counter({1:2,3:10}) if k==4 else Counter({3:12})),(k,split)
        weights=Counter(sig[1]-(1<<(k-1)) for sig in A)
        assert weights==(Counter({-1:10,0:12,1:10}) if k==4
                          else Counter({-1:12,0:12,1:12})),(k,weights)
        print('symbolic',k,'T',len(T),'3_abelian',len(A),
              '2_abelian',len(smaller),'split',sorted(split.items()),
              'weight_groups',sorted(weights.items()))
        if k<=10:
            raw,fac_count=raw_signatures(prefix,1<<k,A)
            assert fac_count==4*(1<<k),(k,fac_count)
            assert raw==A,(k,len(raw),len(A),len(raw.symmetric_difference(A)))
            print('direct',k,'length',1<<k,'distinct_factors',fac_count,
                  'all_3_abelian_signatures_equal',True)
    assert len(T)==24
    print('VERIFY_OK symbolic_exact=all_k_ge_4 raw_complete_k_4_through_10')

if __name__=='__main__':main()
