#!/usr/bin/env python3
"""Exact independent rank-interleaving checks for the conditional runs/KS comparison."""
from collections import Counter, defaultdict
from itertools import combinations
from fractions import Fraction
from functools import lru_cache


def brute(a, b):
    n = a+b
    out=defaultdict(Counter)
    for subset in combinations(range(n), a):
        selected=set(subset)
        run=0; last=None; score=0; maximum=0
        for k in range(n):
            symbol = k in selected
            if symbol != last: run+=1
            score += b if symbol else -a
            maximum = max(maximum, abs(score))
            last = symbol
        assert score == 0
        out[run][maximum] += 1
    return out


def dynamic(a,b):
    # Every path to state has exact count; explicitly propagate the maximum.
    states={(0,0,0,0,0):1} # i, j, last(0 initial/1 plus/2 minus), runs, max
    for _ in range(a+b):
        nxt=defaultdict(int)
        for (i,j,last,r,m),count in states.items():
            if i<a:
                ii=i+1; jj=j; newmax=max(m,abs(b*ii-a*jj))
                nxt[(ii,jj,1,r+(last!=1),newmax)] +=count
            if j<b:
                ii=i; jj=j+1; newmax=max(m,abs(b*ii-a*jj))
                nxt[(ii,jj,2,r+(last!=2),newmax)] +=count
        states=nxt
    out=defaultdict(Counter)
    for (i,j,last,r,m),count in states.items():
        assert (i,j)==(a,b)
        out[r][m]+=count
    return out


def violations(table):
    rows=[]
    for r in sorted(table):
        if r+1 not in table: continue
        left,right=table[r],table[r+1]
        den1,den2=sum(left.values()),sum(right.values())
        for t in sorted(set(left)|set(right)):
            c1=sum(v for k,v in left.items() if k>=t)
            c2=sum(v for k,v in right.items() if k>=t)
            if c2*den1>c1*den2:
                rows.append((r,t,c1,den1,c2,den2))
    return rows


def formula(a):
    b=2*a-1
    r3=Counter();r4=Counter()
    for i in range(1,a):r3[b*max(i,a-i)]+=1
    for j in range(1,b):r3[a*max(j,b-j)]+=1
    for i in range(1,a):
        for j in range(1,b):
            r4[max(b*i,abs(b*i-a*j),a*(b-j))]+=1
            r4[max(a*j,abs(b*i-a*j),b*(a-i))]+=1
    th=(a-1)*b
    P3=Fraction(sum(v for m,v in r3.items() if m>=th),sum(r3.values()))
    P4=Fraction(sum(v for m,v in r4.items() if m>=th),sum(r4.values()))
    assert P3==Fraction(4,3*(a-1)),(a,P3)
    assert P4==Fraction(3*a-4,2*(a-1)**2),(a,P4)
    assert P4-P3==Fraction(a-4,6*(a-1)**2)
    return P3,P4


def run():
    ncases=0; ncomp=0; all_fail=[]
    for n in range(2,15):
        local=[]
        for a in range(1,n//2+1):
            b=n-a
            tab=brute(a,b)
            alt=dynamic(a,b)
            assert tab==alt,(a,b)
            assert sum(sum(c.values()) for c in tab.values())==len(list(combinations(range(n),a)))
            fs=violations(tab)
            if fs:local.append((a,b,fs))
            ncases+=1
            ncomp+=sum((len(tab[r])+len(tab[r+1])) for r in tab if r+1 in tab)
        if n<=13: assert not local,(n,local)
        if n==14:
            assert len(local)==1 and local[0][0:2]==(5,9),local
            assert (3,36,4,12,22,64) in local[0][2],local
            all_fail=local
        print(f'n={n}: exact two-algorithm checks for {n//2} label splits passed, failing cases={len(local)}')
    for a in range(5,45):
        formula(a)
    assert formula(5)==(Fraction(1,3),Fraction(11,32))
    print(f'PASS: {ncases} finite-size splits, {ncomp} conditional comparison supports, 40 closed-form family instances.')
    print(f'FIRST: {all_fail}')
if __name__=='__main__':run()
