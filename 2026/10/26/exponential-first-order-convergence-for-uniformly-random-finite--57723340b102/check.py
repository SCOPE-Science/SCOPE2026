"""Finite exact checks for uniform labeled total preorders and their block words.

Run with: python weak_order_checker.py
"""
from collections import Counter
from math import comb, factorial, log
from itertools import product

def exhaustive_counts(n):
    counts=Counter()
    for k in range(1,n+1):
        for levels in product(range(k), repeat=n):
            if set(levels)!=set(range(k)):
                continue
            sizes=tuple(levels.count(i) for i in range(k))
            counts[sizes]+=1
    return counts

def weighted_compositions(n):
    counts=Counter()
    def visit(rem, seq, weight):
        if not rem:
            counts[tuple(seq)]+=weight
            return
        for s in range(1,rem+1):
            visit(rem-s, seq+[s], weight*comb(rem,s))
    visit(n, [], 1)
    return counts

def recurrence(n):
    a=[1]
    for j in range(1,n+1):
        a.append(sum(comb(j,s)*a[j-s] for s in range(1,j+1)))
    return a

def verify():
    vals=recurrence(7)
    assert vals == [1,1,3,13,75,541,4683,47293], vals
    for n in range(1,8):
        direct=exhaustive_counts(n)
        via=weighted_compositions(n)
        assert direct==via,(n,direct-via)
        assert sum(direct.values())==vals[n]
        first1=sum(c for seq,c in direct.items() if seq[0]==1)
        assert first1==n*vals[n-1]
        last2=sum(c for seq,c in direct.items() if seq[-1]==2)
        assert last2==comb(n,2)*vals[n-2] if n>=2 else last2==0
        both=sum(c for seq,c in direct.items() if len(seq)>=2 and seq[0]==1 and seq[-1]==2)
        expected=n*comb(n-1,2)*vals[n-3] if n>=3 else 0
        assert both==expected,(n,both,expected)
        print('N',n,'TOTAL',vals[n],'FIRST_SINGLETON',first1,'LAST_TWO',last2,'BOTH',both)
    rho=log(2)
    assert abs(sum(rho**s/factorial(s) for s in range(1,30))-1)<1e-12
    for n in (4,5,6,7):
        ratios=(n*vals[n-1]/vals[n],)
        print('FIRST_SINGLETON_PROB',n,*ratios,'LIMIT',rho)
    print('TOTAL_PREORDER_BLOCK_WORD_CHECK_OK')

if __name__=='__main__':
    verify()
