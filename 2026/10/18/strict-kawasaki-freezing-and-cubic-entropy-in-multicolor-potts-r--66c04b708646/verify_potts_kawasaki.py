#!/usr/bin/env python3
"""Reproducible checks for strict exchange-blocking in cyclic q-color Potts chains."""
import itertools
from collections import Counter
from functools import lru_cache

@lru_cache(None)
def power_sums(q, nmax):
    # Newton sums for x^3-x^2-(q-1)x-(q-1)(q-2)u and x^3-x^2+x+(q-2)u.
    import sympy as sp
    u=sp.Symbol('u')
    out=[]
    for b,c in [(-(q-1),-(q-1)*(q-2)*u),(1,(q-2)*u)]:
        ps=[sp.Integer(3),sp.Integer(1),sp.Integer(1)-2*b]
        ps.append(sp.expand(ps[2]-b*ps[1]-3*c))
        for n in range(4,nmax+1):
            ps.append(sp.expand(ps[n-1]-b*ps[n-2]-c*ps[n-3]))
        out.append(ps)
    return [sp.expand(out[0][n]+(q-1)*out[1][n]) for n in range(nmax+1)]

def direct_blocked(word):
    n=len(word)
    H=lambda s:sum(int(s[i]!=s[(i+1)%n]) for i in range(n))
    initial=H(word)
    for i in range(n):
        j=(i+1)%n
        if word[i]==word[j]:continue
        w=list(word);w[i],w[j]=w[j],w[i]
        if H(w)<=initial:return False
    return True

def locally_blocked(word):
    n=len(word)
    for i in range(n):
        a,b,c,d=(word[(i-1)%n],word[i],word[(i+1)%n],word[(i+2)%n])
        if b!=c and int(a!=c)+int(b!=d)-int(a!=b)-int(c!=d)<=0:
            return False
    return True

def singletons(word):
    n=len(word)
    return sum(word[(i-1)%n]!=word[i] and word[(i+1)%n]!=word[i] for i in range(n))

def domain_characterization(word):
    n=len(word)
    if len(set(word))==1:return True
    for i in range(n):
        if word[i]!=word[(i-1)%n] and word[i]!=word[(i+1)%n]:
            if word[(i-1)%n]==word[(i+1)%n]:return False
            if word[(i-2)%n]!=word[(i-1)%n]:return False
            if word[(i+2)%n]!=word[(i+1)%n]:return False
    return True

def run():
    import sympy as sp
    u=sp.Symbol('u')
    count=0
    for q, maximum in [(2,11),(3,10),(4,8)]:
        preds=power_sums(q,maximum)
        for n in range(3,maximum+1):
            actual=Counter()
            for w in itertools.product(range(q),repeat=n):
                a=direct_blocked(w);b=locally_blocked(w);c=domain_characterization(w)
                assert a==b==c,(q,n,w,a,b,c)
                if a:actual[singletons(w)]+=1
                count+=1
            pred=sp.Poly(preds[n],u)
            got=Counter({int(ex[0]):int(co) for ex,co in pred.terms()})
            assert actual==got,(q,n,actual,got)
            print('pass',q,n,'blocked',sum(actual.values()),'by singletons',dict(sorted(actual.items())))
    print('PASS',count,'independent Hamiltonian configurations with local and domain comparisons, exact polynomial equalities')
if __name__=='__main__':run()
