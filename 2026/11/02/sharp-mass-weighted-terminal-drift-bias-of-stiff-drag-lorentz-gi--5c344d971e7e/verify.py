#!/usr/bin/env python3
"""Reproduce the sharp stiff-GIRK forced-fixed-point bias computations.

Uses only Python's standard library. This finite checker supplements, but does
not replace, the analytic half-plane functional-calculus proof.
"""
from fractions import Fraction as F
from math import sqrt
from random import Random


def poly_mul(a, b):
    c = [F(0)] * (len(a) + len(b) - 1)
    for i, x in enumerate(a):
        for j, y in enumerate(b):
            c[i + j] += x*y
    return c


def poly_sub(a, b):
    return [(a[i] if i < len(a) else 0) - (b[i] if i < len(b) else 0)
            for i in range(max(len(a), len(b)))]


# D^2-N^2 = z(2z-1)(2z^2-3z+2),
# and -2(1-z)D - (2z-1)(2z^2-3z+2) = -z
D=[F(1), F(-2), F(2)]
N=[F(1),F(-1)]
L=poly_mul([F(0),F(-1),F(2)], [F(2),F(-3),F(2)])
assert poly_sub(poly_mul(D,D),poly_mul(N,N)) == L
# Correct ratio-minus-one numerator computed without cancellation of z.
assert poly_sub(poly_mul([F(-2),F(2)],D),poly_mul([F(-1),F(2)],[F(2),F(-3),F(2)])) == [F(0),F(-1),F(0),F(0)]


class Q:
    def __init__(self, re=0, im=0):
        self.a = F(re); self.b = F(im)
    def __add__(self, other):
        other=co(other); return Q(self.a+other.a,self.b+other.b)
    __radd__=__add__
    def __neg__(self): return Q(-self.a,-self.b)
    def __sub__(self, other): return self+(-co(other))
    def __rsub__(self, other): return co(other)-self
    def __mul__(self, other):
        other=co(other)
        return Q(self.a*other.a-self.b*other.b,self.a*other.b+self.b*other.a)
    __rmul__=__mul__
    def __truediv__(self, other):
        other=co(other); d=other.a**2+other.b**2
        assert d != 0
        return Q((self.a*other.a+self.b*other.b)/d, (self.b*other.a-self.a*other.b)/d)
    def __eq__(self, other):
        other=co(other); return self.a==other.a and self.b==other.b
    def conj(self): return Q(self.a,-self.b)
    def __repr__(self): return f'({self.a}+{self.b}i)'

def co(z): return z if isinstance(z,Q) else Q(z)

def ident(n): return [[Q(int(i==j)) for j in range(n)] for i in range(n)]

def mul(A,B):
    return [[sum((A[i][k]*B[k][j] for k in range(len(B))), Q()) for j in range(len(B[0]))]
            for i in range(len(A))]

def matadd(A,B): return [[A[i][j]+B[i][j] for j in range(len(A[0]))] for i in range(len(A))]

def scale(A,s): return [[s*x for x in row] for row in A]

def matinv(A):
    n=len(A); W=[list(row)+list(Irow) for row,Irow in zip(A,ident(n))]
    for k in range(n):
        p=next(j for j in range(k,n) if W[j][k] != Q())
        W[p],W[k]=W[k],W[p]
        v=W[k][k]
        W[k]=[x/v for x in W[k]]
        for j in range(n):
            if j!=k:
                c=W[j][k]
                W[j]=[x-c*y for x,y in zip(W[j],W[k])]
    return [row[n:] for row in W]

def matminus(A,B): return matadd(A,scale(B,-1))

def qnorm2(w,eps):
    e=sum(eps)
    # This is the exact relative kinetic energy metric at gas density one.
    diag=sum((e_i*(v.conj()*v).a for e_i,v in zip(eps,w)),F(0))
    mean=sum((e_i*v for e_i,v in zip(eps,w)),Q())
    return diag-(mean.conj()*mean).a/(1+e)


def check_case(eps,alpha,omega,h):
    n=len(eps); I=ident(n)
    d=[Q(-a,o) for a,o in zip(alpha,omega)]
    M=[[Q(int(i==j)+eps[j])*d[j] for j in range(n)] for i in range(n)]
    Z=scale(M,h)
    Z2=mul(Z,Z)
    R=mul(matinv(matadd(matminus(I,scale(Z,2)),scale(Z2,2))),matminus(I,Z))
    v=[[Q(F(1,j+1), F((-1)**j,j+2))] for j in range(n)]
    a=scale(mul(M,v),-1)
    W=scale(mul(matinv(matminus(I,mul(R,R))),mul(R,a)),2*h)
    delta=matminus(W,v)
    P=mul(matminus(scale(Z,2),I),matadd(matminus(scale(Z2,2),scale(Z,3)),scale(I,2)))
    delta_formula=scale(mul(matinv(P),mul(Z,v)),-1)
    assert delta == delta_formula
    norm_before=qnorm2([x[0] for x in v],eps)
    norm_error=qnorm2([x[0] for x in delta],eps)
    assert norm_before>0 and norm_error*F(1600,49)<norm_before, (norm_error,norm_before)
    return 1


def compute_sharp():
    lo,hi=0.42,0.44
    for _ in range(100):
        m=(lo+hi)/2
        if 8*m**3+2*m**2>1: hi=m
        else: lo=m
    s=(lo+hi)/2
    constant=sqrt(s/((1+4*s)*(4*s*s+s+4)))
    assert 0.4290471647<s<0.4290471648
    assert 0.1748725755<constant<0.1748725757
    return s,constant


def run():
    s,constant=compute_sharp()
    rng=Random(20261030)
    count=0
    # All cases satisfy 2h >= 1/min sqrt(alpha^2+omega^2).
    for n in [1,2,3]:
        for _ in range(80):
            eps=[F(rng.randint(1,7),rng.randint(1,6)) for _ in range(n)]
            alpha=[F(rng.randint(1,8),rng.randint(1,5)) for _ in range(n)]
            omega=[F(rng.randint(-8,8),rng.randint(1,5)) for _ in range(n)]
            h=F(1,1)
            if all(4*h*h*(a*a+o*o)>=1 for a,o in zip(alpha,omega)):
                count+=check_case(eps,alpha,omega,h)
    print(f'PASS: {count} exact-rational charged-dust instances; s*={s:.12f}; C*={constant:.12f}')

if __name__=='__main__':run()
