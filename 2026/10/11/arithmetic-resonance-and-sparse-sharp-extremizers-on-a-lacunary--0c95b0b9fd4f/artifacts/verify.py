"""Reproducibility checks for a finite-field lacunary Fourier synthesis norm.

All validation of zero-sum fiber multiplicities uses exact finite-field arithmetic.
No finite test is used as an all-field proof.
"""
from collections import defaultdict
import cmath
import math
import random


def field(p, degree=1):
    q=p**degree
    if degree == 1:
        return q, lambda a,b:(a+b)%p, lambda a,b:(a*b)%p, 0, 1
    assert degree==2
    nonsquare=next(d for d in range(2,p) if pow(d,(p-1)//2,p)==p-1)
    def add(a,b):return ((a%p+b%p)%p)+p*(((a//p+b//p)%p))
    def mul(a,b):
        a0,a1=a%p,a//p
        b0,b1=b%p,b//p
        return (a0*b0+nonsquare*a1*b1)%p+p*((a0*b1+a1*b0)%p)
    return q,add,mul,0,1


def check(p, degree=1):
    q,add,mul,z,one=field(p,degree)
    def power(a,n):
        y=one
        for _ in range(n):y=mul(y,a)
        return y
    neg=lambda a: next(b for b in range(q) if add(a,b)==0)
    c=[(a,power(a,3),power(a,4)) for a in range(q)]
    sums=defaultdict(list)
    for a in range(q):
        for b in range(q):
            sums[tuple(add(c[a][j],c[b][j]) for j in range(3))].append((a,b))
    # Characterize every nontrivial collision by its unordered pairs.
    repeated=0
    for key,seq in sums.items():
        unordered={tuple(sorted(ab)) for ab in seq}
        if len(unordered)>1:
            repeated+=1
            assert q%4==1
            assert len(unordered)==2
            aa,bb=next(iter(unordered))
            assert aa!=bb and add(aa,bb)==z
            for u,v in unordered:
                assert u!=v and add(u,v)==z and power(u,4)==power(aa,4)
            assert len(seq)==4
        else:
            assert len(seq) in (1,2)
    assert repeated == ((q-1)//4 if q%4==1 else 0)

    def direct_Q(g):
        return sum(abs(sum(g[a]*g[b] for a,b in pairs))**2 for pairs in sums.values())
    def theoretical_Q(g):
        S=sum(abs(t)**2 for t in g)
        Q=2*S*S-sum(abs(t)**4 for t in g)
        if q%4==1:
            seen=set()
            for a in range(1,q):
                if a in seen: continue
                orbit={b for b in range(1,q) if power(b,4)==power(a,4)}
                assert len(orbit)==4
                seen.update(orbit)
                neg_a=neg(a)
                j=next(b for b in orbit if b not in (a,neg_a))
                U=g[a]*g[neg_a]
                V=g[j]*g[neg(j)]
                Q+=8*(U*V.conjugate()).real
        return Q
    rng=random.Random(2500+p+degree)
    for _ in range(5):
        g=[complex(rng.randrange(-3,4),rng.randrange(-3,4)) for a in range(q)]
        got=direct_Q(g)
        theory=theoretical_Q(g)
        assert abs(got-theory)<=2e-9*max(1,abs(got))
        S=sum(abs(a)**2 for a in g)
        assert got<= (9/4 if q%4==1 else 2-1/q)*S*S+1e-8*S*S
    if q%4==1:
        orbit={a for a in range(1,q) if power(a,4)==1}
        assert len(orbit)==4
        g=[0j]*q
        for a in orbit:g[a]=1+0j
        assert abs(direct_Q(g)-36)<1e-9
        assert abs(direct_Q(g)/16-9/4)<1e-9
        # Two opposite pairs with unequal phases reduce the strict value.
        a=next(iter(orbit))
        g[a]*=1j
        assert direct_Q(g)<36-1e-9
    else:
        g=[1+0j]*q
        assert abs(direct_Q(g)-(2*q*q-q))<1e-9
    return len(sums),repeated


def direct_fourier(p):
    q,add,mul,z,one=field(p)
    c=[(t,pow(t,3,p),pow(t,4,p)) for t in range(q)]
    if q%4==1:
        orbit={t for t in range(1,q) if pow(t,4,q)==1}
        f=[int(t in orbit) for t in range(q)]
        expect=2.25
    else:
        f=[1]*q
        expect=2-1/q
    S=sum(abs(x)**2 for x in f)
    tot=0
    for a in range(q):
        for b in range(q):
            for d in range(q):
                val=sum(f[t]*cmath.exp(2j*math.pi*((a*x+b*y+d*z)%q)/q) for t,(x,y,z) in enumerate(c))
                tot+=abs(val)**4
    ratio=tot/(q**3*S*S)
    assert abs(ratio-expect)<1e-10,(p,ratio,expect)
    return ratio

if __name__=='__main__':
    checks=[]
    for p in [5,7,11,13,17,19,23]:
        checks.append((p,1,*check(p)))
    for p in [5,7]:
        checks.append((p,2,*check(p,2)))
    for p in [5,7]:
        direct_fourier(p)
    print('VERIFY_OK field_cases=',len(checks),'full_pair_fiber_cases=',len(checks),'direct_fourier_cases=2', 'data=',checks)
