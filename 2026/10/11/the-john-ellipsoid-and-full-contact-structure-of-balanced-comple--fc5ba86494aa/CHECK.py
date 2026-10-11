#!/usr/bin/env python3
"""Exact arithmetic tests for the maximal inscribed ellipsoid of balanced complete-multipartite stable-set polytopes.

Standard-library only. The proof for arbitrary sizes is in RESULT.md;
finite parameter tests here independently replay tangency and John-moment identities.
"""
from fractions import Fraction as F
from itertools import product
from math import isqrt

class Q:
    """a+b*sqrt(q), represented exactly, for rational square q>0."""
    __slots__=('a','b','q')
    def __init__(self,a=0,b=0,q=1):
        self.a,self.b,self.q=F(a),F(b),F(q)
    def _co(self,other):
        if isinstance(other,Q):
            assert other.q==self.q
            return other
        return Q(other,0,self.q)
    def __add__(self,x):
        x=self._co(x);return Q(self.a+x.a,self.b+x.b,self.q)
    __radd__=__add__
    def __neg__(self):return Q(-self.a,-self.b,self.q)
    def __sub__(self,x):return self+-self._co(x)
    def __rsub__(self,x):return self._co(x)+-self
    def __mul__(self,x):
        x=self._co(x)
        return Q(self.a*x.a+self.q*self.b*x.b,self.a*x.b+self.b*x.a,self.q)
    __rmul__=__mul__
    def __truediv__(self,x):
        x=self._co(x); den=x.a*x.a-self.q*x.b*x.b
        assert den!=0
        return self*Q(x.a/den,-x.b/den,self.q)
    def __rtruediv__(self,x):return self._co(x)/self
    def __eq__(self,x):
        x=self._co(x)
        return self.a==x.a and self.b==x.b
    def __repr__(self):return f'Q({self.a},{self.b};{self.q})'

def check(a,r):
    n=a*r
    sq=F(r*(a-1)+1,a)
    nr,dr=isqrt(sq.numerator),isqrt(sq.denominator)
    z=Q(F(nr,dr),0,sq) if nr*nr==sq.numerator and dr*dr==sq.denominator else Q(0,1,sq)
    one=Q(1,0,sq)
    t=one/(r+z); h=1-r*t
    u=z/(r*(r+z)*(z+1))
    v=one/(r*(r+z))
    w=z/(r*(r+z)*(r+z))
    alpha=r/(r+z)
    gamma=r*z/(a**(r-1)*(r+z))
    Sig=[]
    for i in range(n):
        row=[]
        for j in range(n):
            same=i//a==j//a
            x=u*((int(i==j)-F(1,a)) if same else 0)
            x=x+v*((F(1,a) if same else 0)-F(1,n))+w*F(1,n)
            row.append(x)
        Sig.append(row)
    for i in range(n):
        assert Sig[i][i]==t*t,('coordinate contact',a,r,i)
    ct=0
    for choice in product(range(a),repeat=r):
        indices=[j*a+choice[j] for j in range(r)]
        val=sum((Sig[i][j] for i in indices for j in indices), Q(0,0,sq))
        assert val==h*h,('clique contact',a,r,choice)
        ct+=1
    # Sum of the contact displacement vectors is zero.
    assert alpha/t==gamma*a**(r-1)/h
    # Inverse covariance identity: sum of positive weighted facet-normal outer products.
    mat=[]
    for i in range(n):
        row=[]
        for j in range(n):
            pair_count=(a**(r-1) if i==j else a**(r-2) if i//a!=j//a else 0)
            row.append((alpha/(t*t) if i==j else 0)+gamma*pair_count/(h*h))
        mat.append(row)
    for i in range(n):
        for j in range(n):
            val=sum((Sig[i][k]*mat[k][j] for k in range(n)),Q(0,0,sq))
            assert val==(1 if i==j else 0),('John covariance',a,r,i,j,val)
    assert n*alpha+(a**r)*gamma==n
    return n,ct

def main():
    cases=0;coord=0;clique=0
    for a in range(1,5):
        for r in range(1,5):
            d,c=check(a,r);cases+=1;coord+=d;clique+=c
    print('EXACT_PASS cases=',cases,'coordinate facet contacts=',coord,
          'transversal facet contacts=',clique,'all first/second John moments')
if __name__=='__main__': main()
