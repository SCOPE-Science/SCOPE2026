#!/usr/bin/env python3
"""Exact small-order checks for binary collisions under deleted DFT samples.

Requires Python 3 and SymPy; calculations use integer polynomial arithmetic.
"""
from itertools import product
from sympy import Poly, Symbol, cyclotomic_poly, divisors, factorint

X=Symbol('X')

def minimum_formula(n,d):
    return (n//d)*(2**len(factorint(d)))

def remainders(n):
    """Vectors for evaluation at one primitive root of each divisor order."""
    table={}
    for d in divisors(n):
        poly=Poly(cyclotomic_poly(d,X),X,domain='ZZ')
        deg=poly.degree()
        accum=[]
        for j in range(n):
            rem=Poly(X**j,X,domain='ZZ').rem(poly)
            accum.append(tuple(int(rem.nth(t)) for t in range(deg)))
        table[int(d)]=accum
    return table

def min_collision(n,missing,tab):
    seen=None; count=0
    # Exhaustive ternary differences cover all pairs of binary words.
    for word in product((-1,0,1),repeat=n):
        s=sum(c!=0 for c in word)
        if not s or seen is not None and s>seen: continue
        good=True
        for d,terms in tab.items():
            if d==missing:continue
            acc=[0]*len(terms[0])
            for c,vec in zip(word,terms):
                if c:
                    for z,v in enumerate(vec):acc[z]+=c*v
            if any(acc):good=False;break
        if good:
            if seen is None or s<seen:
                seen=s;count=0
            if s==seen:count+=1
    return seen,count

def check_construction(n,d,tab):
    factors=factorint(n); h=[0]*n
    for j in range(n):
        val=1
        for p,a in factors.items():
            b=0; temp=d
            while temp%p==0:
                b+=1;temp//=p
            if b:
                r=j%(p**b)
                if r==0: val*=1
                elif r==p**(b-1):val*=-1
                else:val=0
        h[j]=val
    assert sum(x!=0 for x in h)==minimum_formula(n,d),(n,d,'construction size')
    for e,terms in tab.items():
        acc=[0]*len(terms[0])
        for c,vec in zip(h,terms):
            for z,v in enumerate(vec):acc[z]+=c*v
        assert (not any(acc))==(e!=d),(n,d,e,'spectrum')

if __name__=='__main__':
    tests=0
    for n in (2,3,4,5,6,7,8,9,10):
        T=remainders(n)
        for d in sorted(T):
            got,number=min_collision(n,d,T)
            exp=minimum_formula(n,d)
            assert got==exp,(n,d,got,exp)
            assert number>0
            check_construction(n,d,T)
            print(f'N={n:2} d={d:2} minimal_diff={got:2} minimizers={number}')
            tests+=1
    for n in (12,15,18,20,24,30,36,45,60,72):
        T=remainders(n)
        for d in sorted(T):
            check_construction(n,d,T)
            tests+=1
    print(f'PASS: {tests} exact primitive-shell checks, including exhaustive ternary differences for N <= 10.')
