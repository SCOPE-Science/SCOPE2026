#!/usr/bin/env python3
"""Exact checks for the quartic tangent-discriminant identity and rational contact counts.

Uses the standard Python library; SymPy is optional for the symbolic checks.
This is a finite test suite, not a proof for all finite fields.
"""
from collections import Counter

try:
    import sympy as S
except ImportError:
    S = None


def symbolic():
    if S is None:
        print('SYMBOLIC_CHECK_SKIPPED_SYMPY_NOT_INSTALLED')
        return
    u, v, w, k, x, y = S.symbols('u v w k x y')
    delta = u*w**3 + v**3*w-k*u*v*w**2-k*v**4-u**3*v
    aa = w**3-k*v*w**2-u*u*v
    bb = -2*u*v*v
    cc = -u*w*w-v**3
    assert S.expand(bb**2-4*aa*cc-4*w**2*delta)==0
    aa2 = v*v*w-u**3-k*v**3
    bb2 = 2*u*u*w
    cc2 = -u*w*w-v**3
    assert S.expand(bb2**2-4*aa2*cc2-4*v**2*delta)==0
    d = delta.subs(w, 1)
    assert S.expand(S.diff(d,u).subs(k,(1-3*u*u*v)/v)- (1-(1-3*u*u*v)-3*u*u*v))==0
    # Eliminate the parameter from the quartic equation using the first partial.
    assert S.factor(d.subs(k,(1-3*u*u*v)/v)) == u*u*v*(2*u+3*v**3)
    xx = -S.Rational(1,3)/v**2
    kv = S.Rational(7,6)/v
    assert S.rem(S.together(xx**7+kv*xx**3-1).as_numer_denom()[0],81*v**7+2,v)==0
    assert S.rem(S.together(7*xx**6+3*kv*xx**2).as_numer_denom()[0],81*v**7+2,v)==0
    print('SYMBOLIC_TWO_CHART_DISCRIMINANTS_AND_MULTIPLE_ROOT_IDENTITIES_PASS')


class Field:
    def __init__(self,p,ext=1,non_square=None):
        self.p,self.ext=p,ext
        self.q=p**ext
        if ext==2:
            self.ns = non_square
            assert pow(self.ns,(p-1)//2,p)==p-1
    def add(self,a,b):
        p=self.p
        if self.ext==1:return (a+b)%p
        return (a%p+b%p)%p + p*((a//p+b//p)%p)
    def neg(self,a):
        if self.ext==1:return (-a)%self.p
        return self.add(0, self.q-a) if False else ((-a%self.p)+self.p*((-(a//self.p))%self.p))
    def sub(self,a,b):return self.add(a,self.neg(b))
    def mul(self,a,b):
        p=self.p
        if self.ext==1:return a*b%p
        a0,a1=a%p,a//p
        b0,b1=b%p,b//p
        return (a0*b0+self.ns*a1*b1)%p + p*((a0*b1+a1*b0)%p)
    def power(self,a,n):
        result=1
        while n:
            if n&1:result=self.mul(result,a)
            a=self.mul(a,a)
            n//=2
        return result
    def inv(self,a):
        assert a!=0
        return self.power(a,self.q-2)
    def project(self,vec):
        for value in vec:
            if value:
                i=self.inv(value)
                return tuple(self.mul(z,i) for z in vec)
        return None
    def points(self):
        return [(1,u,v) for u in range(self.q) for v in range(self.q)]+[(0,1,u) for u in range(self.q)]+[(0,0,1)]


def test_field(p,ext=1,ns=None):
    F=Field(p,ext,ns)
    q=F.q
    points=F.points()
    assert len(points)==q*q+q+1
    add,mul,sub,powr=F.add,F.mul,F.sub,F.power
    def poly(T,k):return sub(add(powr(T,7),mul(k,powr(T,3))),1)
    good=[k for k in range(q) if all(poly(T,k)!=0 for T in range(q))]
    assert good
    def delta(U,V,W,k):
        return sub(sub(add(mul(U,powr(W,3)),mul(powr(V,3),W)),mul(k,mul(U,mul(V,powr(W,2))))),add(mul(k,powr(V,4)),mul(powr(U,3),V)))
    def phi(P,k):
        x,y,z=P
        a=sub(sub(mul(powr(x,2),y),powr(z,3)),mul(k,mul(powr(x,2),z)))
        b=sub(mul(powr(y,2),z),powr(x,3))
        c=add(sub(mul(x,powr(z,2)),powr(y,3)),mul(k,powr(x,3)))
        return F.project((a,b,c))
    for k in good:
        multiplicities=Counter(phi(P,k) for P in points)
        assert None not in multiplicities,('singular Fq point',p,ext,k)
        assert set(multiplicities.values()) <= {1,2}
        n1=sum(1 for m in multiplicities.values() if m==1)
        n2=sum(1 for m in multiplicities.values() if m==2)
        discriminant_points=sum(delta(*L,k)==0 for L in points)
        assert n1==discriminant_points,('quartic/count',p,ext,k,n1,discriminant_points)
        assert n2==(q*q+q+1-n1)//2
        assert n2==q*q+q+1-len(multiplicities)
    print(f'GF({q})_ALL_{len(good)}_GOOD_PARAMETERS_QUARTIC_TANGENCY_AND_BITANGENTS_PASS')


if __name__=='__main__':
    symbolic()
    for p in (3,5,7,11,13,17,19,23,29,31,37,41,43):
        test_field(p)
    for p,ns in ((3,2),(5,2),(7,3)):
        test_field(p,2,ns)
    print('PLANE_FILLING_TANGENT_DISCRIMINANT_VERIFIER_PASS')
