#!/usr/bin/env python3
"""Exact checks of signed-permutation point-excess / rationality cycle enumerators.
No external libraries required."""
from fractions import Fraction
from itertools import permutations, product
from collections import Counter
from math import factorial, comb

# Laurent polynomials in z, coefficients rational.
def add(a,b):
    r=a.copy()
    for e,c in b.items():
        r[e]=r.get(e, Fraction(0))+c
        if not r[e]: del r[e]
    return r

def scale(a,c):
    return {e:v*c for e,v in a.items() if v*c}

def mul(a,b):
    c={}
    for e,x in a.items():
        for f,y in b.items(): c[e+f]=c.get(e+f,Fraction(0))+x*y
    return {e:v for e,v in c.items() if v}

def power(a,n):
    r={0:Fraction(1)}
    for _ in range(n): r=mul(r,a)
    return r

def a_coeff(n):
    # [u^n] e^((z-1)u) / sqrt(1-2u)
    out={}
    for k in range(n+1):
        c=Fraction(comb(2*(n-k),n-k),2**(n-k)*factorial(k))
        out=add(out,scale(power({1:1,0:-1},k),c))
    return out

def exact_rational_counts(n):
    term=a_coeff(n)
    if n>=2: term=add(term,scale({e-2:v for e,v in a_coeff(n-2).items()},Fraction(1,2)))
    if n>=3: term=add(term,{e-1:v for e,v in a_coeff(n-3).items()})
    return scale(term,factorial(n))

def exact_all_counts(n):
    term={}
    for k in range(n+1):
        term=add(term,scale(power({1:1,-1:1,0:-2},k),Fraction(2**(n-k),factorial(k))))
    term=add(term,scale(power({1:1,-1:-1},n),Fraction(1,factorial(n))))
    return scale(term,Fraction(factorial(n),2))

def classify(p,neg):
    n=len(p); seen=set(); cyc=[]
    for i in range(n):
        if i in seen: continue
        cur=i; ln=0; parity=0
        while cur not in seen:
            seen.add(cur); ln+=1; parity^=neg[cur]; cur=p[cur]
        cyc.append((ln,parity))
    negative=sorted(ln for ln,sgn in cyc if sgn)
    s=sum((1 if neg[i]==0 else -1) for i in range(n) if p[i]==i)
    isrational=negative in ([],[1,1],[1,2])
    return s,isrational

def exhaustive(n):
    h=Counter(); r=Counter()
    for p in permutations(range(n)):
        for prefix in product((0,1),repeat=n-1):
            neg=prefix+(sum(prefix)%2,)
            s,ok=classify(p,neg)
            h[s]+=1
            if ok:r[s]+=1
    return dict(h),dict(r)

def odd_doublefact(k):
    v=1
    for x in range(1,k+1,2):v*=x
    return v

for n in range(4,8):
    h,r=exhaustive(n)
    eh=exact_all_counts(n); er=exact_rational_counts(n)
    assert h==eh,(n,'all',h,eh)
    assert r==er,(n,'rat',r,er)
    assert sum(h.values())==2**(n-1)*factorial(n)
    assert sum(r.values())==(comb(n,2)*odd_doublefact(2*n-5)
                               +2*n*comb(n-1,2)*odd_doublefact(2*n-7)
                               +odd_doublefact(2*n-1))
    assert min(r)==-2
    assert r[-2]==factorial(n)*Fraction(1,2)*sum(
        Fraction((-1)**k, factorial(k))
        *Fraction(comb(2*(n-2-k),n-2-k),2**(n-2-k))
        for k in range(n-1))
    print(n,'total',sum(h.values()),'rational',sum(r.values()),'rational_min_mass',r[-2], 'rational_hist',sorted(r.items()))
print('VERIFY_OK')
