#!/usr/bin/env python3
"""Reproducible finite tests for principal Fourier sampling on two lines.

All ranks are computed over auxiliary prime fields containing roots of unity.
These tests are finite consistency checks; the general theorem needs the proof.
"""
from itertools import combinations


def primitive_root_of_order(p, ell):
    for z in range(2, ell):
        if pow(z, p, ell) == 1 and z != 1:
            return z
    raise ValueError("no root")


def rank_mod(A, ell):
    A = [[int(v) % ell for v in row] for row in A]
    n, m = len(A), len(A[0])
    r = 0
    for j in range(m):
        k = next((k for k in range(r, n) if A[k][j]), None)
        if k is None:
            continue
        A[r], A[k] = A[k], A[r]
        pivot_inv = pow(A[r][j], -1, ell)
        A[r] = [(x * pivot_inv) % ell for x in A[r]]
        for i in range(r + 1, n):
            if A[i][j]:
                t = A[i][j]
                A[i] = [(x - t*y) % ell for x,y in zip(A[i], A[r])]
        r += 1
        if r == n:
            break
    return r


class Field:
    def __init__(self, p, extension=False):
        self.p = p
        self.extension = extension
        self.q = p*p if extension else p
        assert not extension or p == 3

    def add(self, x, y):
        if not self.extension:
            return (x+y) % self.p
        return (x % 3 + y % 3) % 3 + 3*((x//3 + y//3)%3)

    def mul(self, x, y):
        if not self.extension:
            return (x*y) % self.p
        a,b,c,d = x%3,x//3,y%3,y//3
        return (a*c+2*b*d)%3 + 3*((a*d+b*c)%3)

    def neg(self,x):
        if not self.extension:
            return (-x)%self.p
        return (-x%3)+3*(-(x//3)%3)

    def power(self,x,k):
        v=1
        for _ in range(k):v=self.mul(v,x)
        return v

    def inverse(self,x):
        assert x
        return self.power(x,self.q-2)

    def dot(self,u,v):
        return self.add(self.mul(u[0],v[0]),self.mul(u[1],v[1]))

    def scalar(self,a,u):
        return (self.mul(a,u[0]), self.mul(a,u[1]))

    def trace_to_prime(self,x):
        if not self.extension:return x
        tr=self.add(x,self.power(x,3))
        assert tr < 3
        return tr

    def directions(self):
        return [(0,1)]+[(1,t) for t in range(self.q)]


def order(F,x):
    for k in range(1,F.q):
        if F.power(x,k)==1:return k
    raise AssertionError("order missing")


def predicted_nullity(F,u,v):
    a,b,c=F.dot(u,u),F.dot(v,v),F.dot(u,v)
    if not a or not b or not c:
        return 0
    rho=F.mul(F.mul(c,c),F.inverse(F.mul(a,b)))
    assert rho != 1
    return (F.q-1)//order(F,rho)


class BinaryField:
    def __init__(self, m, modulus):
        self.p = 2
        self.m = m
        self.modulus = modulus
        self.q = 2**m

    def add(self,x,y):
        return x ^ y

    def neg(self,x):
        return x

    def mul(self,x,y):
        z=0
        a=x
        while y:
            if y&1:z^=a
            a<<=1
            if a & self.q:a^=self.modulus
            y>>=1
        return z

    def power(self,x,k):
        v=1
        while k:
            if k&1:v=self.mul(v,x)
            x=self.mul(x,x)
            k>>=1
        return v

    def inverse(self,x):
        assert x
        return self.power(x,self.q-2)

    def dot(self,u,v):
        return self.add(self.mul(u[0],v[0]),self.mul(u[1],v[1]))

    def scalar(self,a,u):
        return (self.mul(a,u[0]),self.mul(a,u[1]))

    def trace_to_prime(self,x):
        tr=0
        for _ in range(self.m):
            tr=self.add(tr,x)
            x=self.mul(x,x)
        assert tr in (0,1)
        return tr

    def directions(self):
        return [(0,1)]+[(1,t) for t in range(self.q)]


def test_field(F,ell):
    z=primitive_root_of_order(F.p,ell)
    count=0
    cases={"orthogonal":0,"isotropic":0,"resonant":0}
    for u,v in combinations(F.directions(),2):
        X=[(0,0)]+[F.scalar(t,u) for t in range(1,F.q)]+[F.scalar(t,v) for t in range(1,F.q)]
        assert len(X)==len(set(X))==2*F.q-1
        B=[[pow(z,F.trace_to_prime(F.dot(x,y)),ell) for y in X] for x in X]
        actual=len(X)-rank_mod(B,ell)
        predicted=predicted_nullity(F,u,v)
        assert actual==predicted,(F.q,u,v,actual,predicted)
        a,b,c=F.dot(u,u),F.dot(v,v),F.dot(u,v)
        cases["orthogonal" if c==0 else ("isotropic" if not a or not b else "resonant")]+=1
        count+=1
    print(f"GF({F.q}): {count} line-pair tests, all exact auxiliary-field ranks match; cases {cases}")


if __name__=="__main__":
    # The auxiliary characteristic differs from the signal characteristic.
    # Agreement of ranks is a finite check, not a proof for arbitrary fields.
    for p,extension,ell in [(3,False,7),(5,False,11),(7,False,29),
                             (11,False,23),(13,False,53),(3,True,7)]:
        test_field(Field(p,extension),ell)
    for m,modulus in [(1,0b11),(2,0b111),(3,0b1011),(4,0b10011)]:
        test_field(BinaryField(m,modulus),7)
    print("PASS")
