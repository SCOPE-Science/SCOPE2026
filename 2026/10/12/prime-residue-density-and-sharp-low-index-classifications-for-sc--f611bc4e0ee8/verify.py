"""Exact reproducibility checks for a prime-power Schemmel abundance theorem.
No conclusions about infinite sets are drawn from the enumeration.
"""
from fractions import Fraction
from functools import lru_cache

@lru_cache(None)
def factor(n):
    t=n; fac={}; d=2
    while d*d<=t:
        if t%d==0:
            a=0
            while t%d==0:t//=d;a+=1
            fac[d]=a
        d=3 if d==2 else d+2
    if t>1:fac[t]=fac.get(t,0)+1
    return fac

def primes_le(n):
    return [k for k in range(2,n+1) if len(factor(k))==1 and list(factor(k).values())==[1]]

@lru_cache(None)
def L(m,n):
    if n==0:return 0
    if n==1:return 1
    out=1
    for p,a in factor(n).items():
        if p<=m:return 0
        out*=p**(a-1)*(p-m)
    return out

@lru_cache(None)
def D(m,n):
    if n==1 or n==0:return 0  # terminal continuation, not the standalone value D_m(1)
    y=L(m,n)
    return y+D(m,y)

def cm(m):
    z=Fraction(1)
    for q in primes_le(2*m):
        if q>m:z*=Fraction(q-m,q)
    return z

def check():
    lemmas=0; dichotomies=0; lowm=0; primes=primes_le(290)
    for m in range(2,15,2):
        c=cm(m)
        for u in range(1,800):
            if all(q>m for q in factor(u)):
                v=L(m,u)
                assert v*v*c.denominator**2 >= c.numerator**2*u, (m,u,c,v)
                lemmas+=1
        for p in primes:
            if p<=m:continue
            u=p-m
            qsmall=any(q<=m for q in factor(u))
            for a in range(1,4):
                n=p**a
                if qsmall:
                    assert D(m,n)==n//p*(p-m),(m,p,a,D(m,n))
                    dichotomies+=1
                elif u>=m and c*c*u>4*m*m:
                    assert D(m,n)>n,(m,p,a,D(m,n))
                    dichotomies+=1
    for p in primes:
        for a in range(1,5):
            v=D(2,p**a)
            assert (v>p**a)==(p>=7),(p,a,v)
            assert (v<p**a)==(p<7),(p,a,v)
            lowm+=1
            v=D(4,p**a)
            truth=(p>=17 and p%3==2)
            assert (v>p**a)==truth,(p,a,v)
            assert (v<p**a)==(not truth),(p,a,v)
            lowm+=1
    assert cm(2)==Fraction(1,3)
    assert cm(4)==Fraction(3,35)
    assert cm(6)==Fraction(5,77)
    return 'FINITE_CHECKS_OK growth_lemma_instances=%d prime_power_dichotomies=%d small_m_classifications=%d rational_c2=%s rational_c4=%s rational_c6=%s'%(lemmas,dichotomies,lowm,cm(2),cm(4),cm(6))

if __name__=='__main__':print(check())
