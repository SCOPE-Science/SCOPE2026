#!/usr/bin/env python3
"""Standalone finite-size checks for escape-rate variance in q-ary Markov holes.
No external dependencies. This checks examples, not the infinite-family proof.
"""
from itertools import product
from math import log, exp, isclose


def periods(word):
    n = len(word)
    return tuple(p for p in range(1, n) if word[:-p] == word[p:])


def corr(word, z):
    return 1.0 + sum(z ** p for p in periods(word))


def escape(word, q):
    n = len(word)
    h = q ** (-n)
    lo, hi = 1.0 - 2.0*h, 1.0
    assert lo > 0.0 and n >= 3
    def f(lam):
        return (1.0 - lam) * (lam ** (n-1)) * corr(word, 1.0/(q*lam)) - h
    assert f(lo) >= -1e-12 and f(hi) <= 0.0, (word,q, f(lo))
    for _ in range(65):
        mid = (lo+hi)/2
        if f(mid)>0:
            lo=mid
        else:
            hi=mid
    return -log((lo+hi)/2)


def count_avoid(word, q, length):
    n = len(word)
    count = 0
    for digits in product(range(q), repeat=length):
        if all(tuple(digits[k:k+n]) != word for k in range(length-n+1)):
            count += 1
    return count


def predicted_counts(word,q,limit):
    n=len(word)
    c = [0]*(limit+1)
    c[0]=1
    for p in periods(word):
        c[p]=1
    # [ (1-qz)C + z^n ] A = C
    den=[0]*(max(n,len(c)-1)+1)
    for i,coeff in enumerate(c):
        if coeff:
            den[i] += coeff
            if i+1<len(den):
                den[i+1] -= q*coeff
    den[n]+=1
    a=[0]*(limit+1)
    for i in range(limit+1):
        a[i]=(c[i] if i<len(c) else 0)-sum(den[k]*a[i-k] for k in range(1,min(i,len(den)-1)+1))
    return a


def mobius(n):
    x=n; p=2; num=0
    while p*p<=x:
        if x%p==0:
            x//=p;num+=1
            if x%p==0:
                return 0
            while x%p==0: x//=p
        p+=1
    if x>1:num+=1
    return -1 if num%2 else 1


def primitive(q,p):
    return sum(mobius(d)*q**(p//d) for d in range(1,p+1) if p%d==0)


def constant(q,nterms=60):
    return sum(primitive(q,p)*q**(-2*p) for p in range(1,nterms+1))


def check():
    for q,n in [(2,3),(2,4),(2,5),(2,6),(2,7),(2,8),(2,9),(3,3),(3,4),(3,5),(4,3),(4,4)]:
        words=list(product(range(q),repeat=n))
        ys=[escape(w,q)*q**n for w in words]
        var=sum((y-sum(ys)/len(ys))**2 for y in ys)/len(ys)
        assert var>=0
        if q==2 and n<=5:
            for w in words:
                actual=[count_avoid(w,q,m) for m in range(n,n+3)]
                pred=predicted_counts(w,q,n+2)
                assert actual==pred[n:n+3], (w,actual,pred)
        # Approximation is globally O(nq^-n), with a bounded q-dependent prefactor.
        worst=max(abs(y-1/corr(w,1/q)) for y,w in zip(ys,words))
        assert worst<8*n*q**(-n), (q,n,worst)
        if q==2 and n==9:
            assert 0.72<q**n*var<0.85,(q,n,var)
    # The primitive-count formula and Möbius rearrangement give same constant.
    K2=constant(2)
    K2_alt=sum(mobius(d)*2/(2**(2*d)-2) for d in range(1,41))
    assert abs(K2-K2_alt)<1e-12
    assert abs(K2-0.8232956899365094)<1e-11, K2
    for q in range(2,6):
        for p in range(1,8):
            assert 0<primitive(q,p)<=q**p
    print('VERIFY_OK; K_2=%.15f' % K2)

if __name__=='__main__':
    check()
