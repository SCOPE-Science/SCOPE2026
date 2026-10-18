#!/usr/bin/env python3
"""Exact finite enumeration for affine groups of two types of chain rings.

No external dependencies. Output consists of verified mathematical equalities.
"""
from collections import Counter
from cmath import exp, pi
from itertools import product

class ChainRing:
    def __init__(self, p, n, kind):
        assert p in (2,3,5) and n>=1 and kind in ('poly','integer')
        self.p,self.n,self.kind=p,n,kind
        self.zero = (0,)*n if kind=='poly' else 0
        self.one = (1,)+(0,)*(n-1) if kind=='poly' else 1
        self.E=list(product(range(p),repeat=n)) if kind=='poly' else list(range(p**n))
        self.U=[x for x in self.E if self.const(x)!=0]
    def const(self,a): return a[0] if self.kind=='poly' else a%self.p
    def add(self,a,b):
        return tuple((x+y)%self.p for x,y in zip(a,b)) if self.kind=='poly' else (a+b)%(self.p**self.n)
    def neg(self,a):
        return tuple((-x)%self.p for x in a) if self.kind=='poly' else (-a)%(self.p**self.n)
    def sub(self,a,b): return self.add(a,self.neg(b))
    def mul(self,a,b):
        if self.kind=='integer': return (a*b)%(self.p**self.n)
        return tuple(sum(a[j]*b[i-j] for j in range(i+1))%self.p for i in range(self.n))
    def val(self,a):
        if self.kind=='poly':
            return next((i for i,c in enumerate(a) if c),self.n)
        if a==0:return self.n
        i=0
        while a%self.p==0:
            i+=1;a//=self.p
        return i
    def uniform(self,h):
        if self.kind=='poly':return (0,)*h+(1,)+(0,)*(self.n-h-1)
        return self.p**h
    def conj(self,a,u,b,v):
        # (b,v)(a,u)(b,v)^{-1}=(v*a+(1-u)*b,u)
        return self.add(self.mul(v,a),self.mul(self.sub(self.one,u),b)),u
    def group(self):return list(product(self.E,self.U))

def check_ramanujan(R):
    # Evaluate the induced-character orbit sum using a genuinely generating
    # additive character, independently of the valuation sum formula.
    for z in R.E:
        h=R.val(z)
        if h==R.n:continue
        m=R.n-h
        orb={R.mul(u,z) for u in R.U}
        for a in R.E:
            av=R.val(a)
            expect=(R.p-1)*R.p**(m-1) if av>=m else (-R.p**(m-1) if av==m-1 else 0)
            def chi(x):
                if R.kind=='integer':
                    return exp(2j*pi*x/(R.p**R.n))
                if R.p==4:
                    trace=x[-1]^R.fm(x[-1],x[-1])
                    assert trace in (0,1)
                    return (-1)**trace
                return exp(2j*pi*x[-1]/R.p)
            actual=sum(chi(R.mul(a,w)) for w in orb)
            assert abs(actual-expect)<1.e-6,(R.kind,R.p,R.n,z,a,actual,expect)

def test_ring(R):
    q=R.p;n=R.n
    G=R.group();S=len(G);U=len(R.U)
    assert S==(q-1)*q**(2*n-1)
    # Direct brute-force conjugation by all elements, counting all orbits once.
    unseen=set(G); sizes=[]; types=[]
    while unseen:
        a,u=next(iter(unseen));k=R.val(R.sub(R.one,u));h=R.val(a)
        orbit={R.conj(a,u,b,v) for b,v in G}
        assert orbit<=unseen
        unseen.difference_update(orbit)
        assert len(orbit)==(q**(n-k) if h>=k else (q-1)*q**(n-h-1))
        sizes.append(len(orbit));types.append((k,min(h,k)))
    assert len(sizes)==U+(q**n-1)//(q-1)
    # All classes can be produced by the predicted explicit representatives.
    expected=[]
    for u in R.U:
        k=R.val(R.sub(R.one,u))
        expected.append((R.zero,u))
        expected.extend((R.uniform(h),u) for h in range(k))
    assert len(expected)==len(sizes)
    assert {R.conj(a,u,b,v) for a,u in expected for b,v in G}==set(G)
    assert len({(R.val(R.sub(R.one,u)), h) for (a,u),h in zip(expected,[0]*len(expected))})>=1
    # Centralizer formula, checked element-by-element (not derived from orbit sizes).
    for a,u in G:
        h=R.val(a);k=R.val(R.sub(R.one,u))
        C=sum(R.mul(R.sub(R.one,v),a)==R.mul(R.sub(R.one,u),b) for b,v in G)
        assert C==(U*q**k if h>=k else q**(n+h))
    # Orbit sizes in the dual additive group; for either ring the parameter z
    # indexes additive characters via a generating additive character of R.
    unseen=set(R.E);degrees=[]
    while unseen:
        z=next(iter(unseen))
        orbit={R.mul(u,z) for u in R.U}
        unseen.difference_update(orbit)
        stab=U//len(orbit)
        degrees.extend([len(orbit)]*stab)
    expected_degrees=[1]*U
    for h in range(n):expected_degrees += [(q-1)*q**(n-1-h)]*(q**h)
    assert Counter(degrees)==Counter(expected_degrees)
    assert sum(d*d for d in degrees)==S
    assert len(degrees)==len(sizes)
    assert sum(sizes)==S
    commute=sum(sum(R.mul(R.sub(R.one,v),a)==R.mul(R.sub(R.one,u),b) for b,v in G) for a,u in G)
    assert commute==S*len(sizes)
    check_ramanujan(R)
    print(f'PASS kind={R.kind} q={q} n={n} order={S} classes={len(sizes)} sizes={sorted(Counter(sizes).items())} degrees={sorted(Counter(degrees).items())}')

class F4PolynomialRing(ChainRing):
    def __init__(self,n):
        self.p,self.n,self.kind=4,n,'poly'
        self.zero=(0,)*n
        self.one=(1,)+(0,)*(n-1)
        self.E=list(product(range(4),repeat=n))
        self.U=[x for x in self.E if self.const(x)!=0]
    @staticmethod
    def fm(a,b):
        x=0
        for i in range(2):
            for j in range(2):
                if (a>>i)&1 and (b>>j)&1:x^=1<<(i+j)
        if x&4:x^=7 # X^2+X+1
        return x
    def add(self,a,b):return tuple(x^y for x,y in zip(a,b))
    def neg(self,a):return a
    def mul(self,a,b):
        return tuple(self._sum(self.fm(a[j],b[i-j]) for j in range(i+1)) for i in range(self.n))
    @staticmethod
    def _sum(L):
        x=0
        for v in L:x^=v
        return x

if __name__=='__main__':
    for p,n in [(2,1),(2,2),(2,3),(3,1),(3,2),(5,1)]:
        for kind in ('poly','integer'):
            test_ring(ChainRing(p,n,kind))
    for n in (1,2):test_ring(F4PolynomialRing(n))
    print('ALL EXACT ENUMERATION TESTS PASSED')
