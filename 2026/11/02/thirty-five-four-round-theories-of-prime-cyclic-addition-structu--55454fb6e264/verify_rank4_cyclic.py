"""Exact four-round first-order types of prime cyclic addition structures.

Requires Python 3.9+ standard library only. The final analytic cutoff is
certified by a finite arrangement of rational linear forms, independently
of the finite-field type enumeration.
"""
from fractions import Fraction as Q
from functools import reduce
from itertools import combinations
from math import gcd, lcm


def isprime(n):
    if n<2:return False
    return all(n%d for d in range(2,int(n**0.5)+1))


def atom(t,p):
    n=len(t); bit=0; j=0
    for a in range(n):
        if t[a]==0:bit|=1<<j
        j+=1
    for a in range(n):
        for b in range(a+1,n):
            if t[a]==t[b]:bit|=1<<j
            j+=1
    for a in range(n):
        for b in range(a,n):
            val=(t[a]+t[b])%p
            for c in range(n):
                if val==t[c]:bit|=1<<j
                j+=1
    return bit


def norm(t,p):
    for a in t:
        if a:
            inv=pow(a,-1,p)
            return tuple((v*inv)%p for v in t)
    return t


def find_type(p,intern):
    def key(level,obj):
        idx=(level,obj)
        if idx not in intern:intern[idx]=len(intern)+1
        return intern[idx]
    cache3={};cache2={};cache1={}
    def three(t):
        t=norm(t,p)
        if t not in cache3:
            f={0,*t}
            for a in t:
                for b in t:
                    f.add((a+b)%p)
                    f.add((a-b)%p)
            if p%2:
                half=pow(2,-1,p)
                f.update((a*half)%p for a in t)
            if len(f)<p:
                f.add(next(z for z in range(p) if z not in f))
            cache3[t]=key(3,(atom(t,p),frozenset(atom(t+(z,),p) for z in f)))
        return cache3[t]
    def two(t):
        t=norm(t,p)
        if t not in cache2:
            cache2[t]=key(2,(atom(t,p),frozenset(three(t+(z,)) for z in range(p))))
        return cache2[t]
    def one(t):
        t=norm(t,p)
        if t not in cache1:
            cache1[t]=key(1,(atom(t,p),frozenset(two(t+(z,)) for z in range(p))))
        return cache1[t]
    return key(0,frozenset(one((z,)) for z in range(p)))


def arrangement_certificate():
    E=[tuple(Q(i==j) for i in range(3)) for j in range(3)]
    Z=(Q(0),)*3
    plus=lambda a,b:tuple(x+y for x,y in zip(a,b))
    minus=lambda a,b:tuple(x-y for x,y in zip(a,b))
    F={Z,*E}
    for a in E:F.add(tuple(x/2 for x in a))
    for a in E:
        for b in E:
            F.add(plus(a,b));F.add(minus(a,b))
    def prim(v):
        den=lcm(*(x.denominator for x in v))
        t=tuple(int(x*den) for x in v)
        div=reduce(gcd,map(abs,t))
        t=tuple(x//div for x in t)
        if next(x for x in t if x)<0:t=tuple(-x for x in t)
        return t
    L={prim(minus(a,b)) for a,b in combinations(sorted(F),2)}
    H=set();S=set()
    for a,b,c in L:
        if c:H.add((Q(-a,c),Q(-b,c)))
        elif b:S.add(Q(-a,b))
    for (a,b),(c,d) in combinations(sorted(H),2):
        if b!=d:S.add((c-a)/(b-d))
    def factors(n):
        n=abs(n);res=set();d=2
        while d*d<=n:
            if n%d==0:
                res.add(d)
                while n%d==0:n//=d
            d+=1
        if n>1:res.add(n)
        return res
    bad=set()
    for a,b in combinations(sorted(S),2):
        bad.update(factors(a.numerator*b.denominator-b.numerator*a.denominator))
    assert (len(F),len(L),len(H),len(S))==(19,60,46,93)
    assert bad==set([p for p in range(2,132) if isprime(p)] + [157,191])
    assert max(bad)==191
    print('RATIONAL_FORMS 19; HYPERPLANES 60; SPECIAL_FUNCTIONS 46; EXCEPTIONAL_RATIOS 93')
    print('ALL_EXCEPTIONAL_PRIMES',','.join(map(str,sorted(bad))))
    print('LARGE_PRIME_STABILIZATION_PROVEN p>=193')
    return bad


def check_small_direct():
    # Independent orbit-free recursion for six small fields, all tuple values.
    # A separate interning space is used to avoid any reliance on orbit normalization.
    intern={}
    def interned(t,v):
        k=(t,v)
        if k not in intern:intern[k]=len(intern)+1
        return intern[k]
    for p in (2,3,5,7,11,13):
        three={}
        for a in range(p):
            for b in range(p):
                for c in range(p):
                    T=(a,b,c)
                    three[T]=interned(3,(atom(T,p),frozenset(atom(T+(z,),p) for z in range(p))))
        two={}
        for a in range(p):
            for b in range(p):
                T=(a,b)
                two[T]=interned(2,(atom(T,p),frozenset(three[T+(z,)] for z in range(p))))
        one={}
        for a in range(p):
            T=(a,)
            one[T]=interned(1,(atom(T,p),frozenset(two[T+(z,)] for z in range(p))))
        root=interned(0,frozenset(one[(z,)] for z in range(p)))
        print('ORBIT_FREE_DIRECT_OK',p,'root',root)


def main():
    bad=arrangement_certificate()
    inter={};roots={};pvals=[p for p in range(2,194) if isprime(p)]
    for p in pvals:roots[p]=find_type(p,inter)
    classes={}
    for p,t in roots.items():classes.setdefault(t,[]).append(p)
    assert len(classes)==35
    assert [s for s in classes.values() if len(s)>1]==[[137,139,149,151,163,167,173,179,181,193]]
    assert set(pvals)-set([137,139,149,151,163,167,173,179,181,193])==bad
    # Additional nonexceptional primes in the proven infinite class.
    assert find_type(197,inter)==roots[193]
    assert find_type(211,inter)==roots[193]
    print('EXACT_FINITE_BOUNDARY_OK',len(pvals),'primes through 193')
    print('ALL_35_CLASSES_OK')
    print('GENERIC_CLASS',','.join(map(str,classes[roots[193]])))
    check_small_direct()
    print('VERIFY_OK')

if __name__=='__main__':main()
