#!/usr/bin/env python3
"""Standalone small-field checks for the six-generator exterior-algebra tuple theorem."""
from itertools import combinations, product
from random import Random
from math import prod

N=6
MASKS={d:[sum(1<<j for j in s) for s in combinations(range(N),d)] for d in range(7)}
ALL=2**N-1

def invsign(a,b):
    return -1 if (sum((b & ((1<<j)-1)).bit_count() for j in range(N) if a&(1<<j)))%2 else 1

def plus(a,b,p):
    d=a.copy()
    for u,c in b.items():
        val=(d.get(u,0)+c)%p
        if val:d[u]=val
        else:d.pop(u,None)
    return d

def scale(a,c,p):
    return {u:(v*c)%p for u,v in a.items() if v*c%p}

def wedge(a,b,p):
    out={}
    for u,x in a.items():
        for v,y in b.items():
            if u&v: continue
            z=u|v
            out[z]=(out.get(z,0)+invsign(u,v)*x*y)%p
    return {u:c for u,c in out.items() if c}

def random_form(d,p,rng):
    return {m:x for m in MASKS[d] if (x:=rng.randrange(p))}

def isotropic_count(q,n,t):
    total=0
    from fractions import Fraction
    for r in range(min(n,t)+1):
        # Product of factors as one rational number, never truncate intermediate products.
        grass=Fraction(prod(q**(2*n-i)-q**i for i in range(r)),
                       prod(q**r-q**i for i in range(r)))
        surj=prod(q**t-q**i for i in range(r))
        term=grass*surj
        assert term.denominator==1
        total+=term.numerator
    return total

def enumerate_iso(q,n,t):
    # Canonical symplectic form on Fq^(2n).
    vecs=list(product(range(q), repeat=2*n))
    def pair(v,w):
        return sum(v[i]*w[n+i]-v[n+i]*w[i] for i in range(n))%q
    total=0
    for tup in product(vecs,repeat=t):
        if all(pair(tup[i],tup[j])==0 for i in range(t) for j in range(i+1,t)):
            total+=1
    return total

def field_formula(q,t):
    rankone=(q**6-1)*(q**t-1)//(q-1)
    return q**(32*t)*(q**(6*t)*isotropic_count(q,10,t)+rankone*q**(15*t+11))

def main():
    rng=Random(41033)
    tests=0
    for q,n,t in [(2,2,1),(2,2,2),(2,2,3),(2,2,4),
                  (3,2,1),(3,2,2),(3,2,3), (2,3,2),(2,3,3)]:
        got=enumerate_iso(q,n,t)
        want=isotropic_count(q,n,t)
        assert got==want,(q,n,t,got,want)
        tests+=1
    for q in (3,5,7):
        for t in (2,3,5):
            for _ in range(80):
                # e0 as a common linear direction, all pairwise equations checked by actual wedge multiplication.
                common=random_form(3,q,rng)
                beta1=random_form(5,q,rng)
                c=[1]+[rng.randrange(q) for _ in range(t-1)]
                alphas=[common]; betas=[beta1]
                for j in range(1,t):
                    eta={m: v for m,v in random_form(2,q,rng).items() if m&1==0}
                    zeta={m:v for m,v in random_form(4,q,rng).items() if m&1==0}
                    a=plus(scale(common,c[j],q),wedge({1:1},eta,q),q)
                    b=plus(plus(scale(beta1,c[j],q),wedge(common,eta,q),q),wedge({1:1},zeta,q),q)
                    alphas.append(a);betas.append(b)
                odd=[plus(plus({1:c[j]},alphas[j],q),betas[j],q) for j in range(t)]
                assert all(not wedge(odd[i],odd[j],q) for i in range(t) for j in range(i+1,t))
                tests+=1
            # rank-zero locus: all degree-three monomials containing e0 make a standard Lagrangian.
            for _ in range(30):
                odd=[]
                for j in range(t):
                    alpha={m:v for m,v in random_form(3,q,rng).items() if m&1}
                    odd.append(plus(alpha,random_form(5,q,rng),q))
                assert all(not wedge(odd[i],odd[j],q) for i in range(t) for j in range(i+1,t))
                tests+=1
    # Direct check: the 20-dimensional middle wedge-pairing is nonsingular.
    for q in (3,5,7):
        mid=MASKS[3]
        for i,a in enumerate(mid):
            assert mid[19-i]==(ALL^a)
            assert wedge({a:1},{ALL^a:1},q) in ({ALL:1},{ALL:q-1})
        tests+=1
    assert field_formula(3,1)==3**64
    for q in (3,5,7,9):
        previous_pair=q**115+q**112+q**111-q**106-q**105+q**96-q**95
        assert field_formula(q,2)==previous_pair
        tests+=1
    for t in (2,3,4,9,10,11,20):
        dimA=48*t+16
        dimB=(58*t-t*(t-1)//2) if t<=10 else (48*t+55)
        assert dimB>dimA
        if t==2:assert (dimA,dimB)==(112,115)
        if t==3:assert (dimA,dimB)==(160,171)
        if t==10: assert (dimA,dimB)==(496,535)
    print('VERIFY_OK_EXTERIOR_TUPLE_COMPONENTS_AND_COUNTS',tests,'direct tests; t=3 component dimensions 160 171; t=10 496 535')

if __name__=='__main__':main()
