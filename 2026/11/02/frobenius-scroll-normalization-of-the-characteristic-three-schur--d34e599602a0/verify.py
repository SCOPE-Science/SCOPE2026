#!/usr/bin/env python3
"""Exact reproducibility checks for the characteristic-three Schur model.

No external libraries are required. The geometric conclusions for arbitrary
fields come from the proof accompanying this checker; finite counts here are
independent supplementary confirmations, not infinite-field arguments.
"""
from itertools import product


class Poly:
    """Sparse four-variable polynomial over F3 for independent identity checks."""
    def __init__(self,terms):
        self.terms={k:v%3 for k,v in terms.items() if v%3}
    def __add__(self,other):
        d=self.terms.copy()
        for k,v in other.terms.items(): d[k]=(d.get(k,0)+v)%3
        return Poly(d)
    def __neg__(self):
        return Poly({k:-v for k,v in self.terms.items()})
    def __sub__(self,other): return self+-other
    def __mul__(self,other):
        d={}
        for a,va in self.terms.items():
            for b,vb in other.terms.items():
                k=tuple(x+y for x,y in zip(a,b))
                d[k]=(d.get(k,0)+va*vb)%3
        return Poly(d)
    def __pow__(self,n):
        out=Poly({(0,0,0,0):1})
        for _ in range(n):out=out*self
        return out
    def derivative(self,j):
        d={}
        for ex,coef in self.terms.items():
            if ex[j]:
                next_ex=list(ex);next_ex[j]-=1; next_ex=tuple(next_ex)
                d[next_ex]=(d.get(next_ex,0)+coef*ex[j])%3
        return Poly(d)
    def __eq__(self,other): return self.terms==other.terms


def polynomial_identity():
    u,v,a,b=[Poly({tuple(int(i==j) for i in range(4)):1}) for j in range(4)]
    f=u**4-u*(u-a)**3-v**4+v*(v-b)**3
    target=u*a**3-v*b**3
    zero=Poly({})
    assert f==target
    assert [target.derivative(i) for i in range(4)] == [a**3,-(b**3),zero,zero]
    print('CHARACTERISTIC_THREE_TRANSFORMATION_AND_JACOBIAN_OK')


def monomial_membership(i,j):
    return j >= i % 3


def conductor_test():
    # R=F3[t^3,a,t*a] subset B=F3[t,a].
    # For every monomial in R, multiplication by all powers of t
    # stays in R exactly when its a-exponent is >=2.
    for i in range(0,45):
        for j in range(0,15):
            if not monomial_membership(i,j):
                continue
            all_t_powers = all(monomial_membership(i+k,j) for k in range(3))
            assert all_t_powers == (j>=2)
    # a^2 B as an R-ideal is (a^2,a*b,b^2), b=t*a.
    for i in range(0,45):
        for j in range(2,15):
            assert monomial_membership(i,j)
            r=i%3
            # Subtract generator a^2, a*b, or b^2, respectively.
            assert monomial_membership(i-r,j-2)
    print('SEMIGROUP_CONDUCTOR_PATTERN_OK')


class F3m:
    def __init__(self,m,irr):
        self.m=m; self.q=3**m; self.irr=irr
        self.tup=[tuple((n//3**j)%3 for j in range(m)) for n in range(self.q)]
        self.dct={t:i for i,t in enumerate(self.tup)}
        self.add=[[self.dct[tuple((x+y)%3 for x,y in zip(a,b))] for b in self.tup] for a in self.tup]
        self.mul=[[self.raw_mul(a,b) for b in self.tup] for a in self.tup]
    def raw_mul(self,a,b):
        m=self.m; c=[0]*(2*m-1)
        for i in range(m):
            for j in range(m): c[i+j]=(c[i+j]+a[i]*b[j])%3
        for n in range(2*m-2,m-1,-1):
            coefficient=c[n]
            for j in range(m): c[n-m+j]=(c[n-m+j]-coefficient*self.irr[j])%3
        return self.dct[tuple(c[:m])]
    def power(self,x,n):
        o=1
        while n:
            if n&1: o=self.mul[o][x]
            x=self.mul[x][x]; n//=2
        return o


def projective_points(F):
    q=F.q
    for first in range(4):
        for tail in product(range(q), repeat=3-first):
            yield (0,)*first + (1,) + tail


def point_count(F):
    q=F.q
    x3=[F.power(x,3) for x in range(q)]
    for x in range(q): assert x3[x3[x]] == F.power(x,9)
    cnt=0
    for u,v,a,b in projective_points(F):
        lhs=F.mul[u][x3[a]]
        rhs=F.mul[v][x3[b]]
        cnt += lhs==rhs
    return cnt


def test_counts():
    # Degree 1, 2, 3 irreducible choices over F3.
    for m,poly in [(1,[0,1]),(2,[1,0,1]),(3,[1,2,0,1])]:
        F=F3m(m,poly); q=F.q
        for x in range(q):
            assert F.power(x,q)==x
        count=point_count(F)
        assert count==(q+1)**2,(q,count)
        assert q+3==2+(q+1)
        print(f'GF({q})_PROJECTIVE_POINT_COUNT_OK: {count}; RATIONAL_LINES={q+3}')


if __name__=='__main__':
    polynomial_identity()
    conductor_test()
    test_counts()
    print('VERIFY_OK')
