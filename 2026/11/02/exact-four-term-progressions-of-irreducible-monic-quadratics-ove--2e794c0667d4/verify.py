#!/usr/bin/env python3
"""Independent finite-field verification of four-term quadratic prime-polynomial progressions.
Pure Python 3, no external packages. Run: python3 verify.py
"""
from itertools import product


def trim(v):
    while v and v[-1] == 0:
        v.pop()
    return v


def rempoly(a, b, p):
    a = trim(a[:]); b = trim(b[:])
    inv = pow(b[-1], -1, p)
    while len(a) >= len(b):
        coeff = (a[-1] * inv) % p
        shift = len(a) - len(b)
        for i, value in enumerate(b):
            a[i + shift] = (a[i + shift] - coeff * value) % p
        trim(a)
    return a


def modulus_for(p, degree):
    if degree == 1:
        return None
    for low in product(range(p), repeat=degree):
        if low[0] == 0:
            continue
        polynomial = list(low) + [1]
        if all(rempoly(polynomial, list(low_div) + [1], p)
               for d in range(1, degree // 2 + 1)
               for low_div in product(range(p), repeat=d)):
            return polynomial
    raise RuntimeError('No irreducible modulus')


class Field:
    def __init__(self, p, degree):
        self.p = p; self.degree = degree; self.q = p ** degree
        self.mod = modulus_for(p, degree)
        self.digits = [self.unpack(i) for i in range(self.q)]
        self.add = [[self.encode([(a+b)%p for a,b in zip(self.digits[i],self.digits[j])])
                     for j in range(self.q)] for i in range(self.q)]
        self.mul = [[self.rawmul(i,j) for j in range(self.q)] for i in range(self.q)]
        self.neg = [self.encode([(-a)%p for a in self.digits[i]]) for i in range(self.q)]
        self.square_set = {self.mul[x][x] for x in range(self.q)}
        self.chi = [0 if x == 0 else (1 if x in self.square_set else -1)
                    for x in range(self.q)]

    def unpack(self, n):
        v=[]
        for _ in range(self.degree):
            v.append(n%self.p); n//=self.p
        return v

    def encode(self, v):
        n=0; s=1
        for x in v:
            n+=x*s; s*=self.p
        return n

    def rawmul(self, x, y):
        p=self.p; d=self.degree
        if d == 1:
            return (x*y)%p
        a=self.digits[x]; b=self.digits[y]
        c=[0]*(2*d-1)
        for i in range(d):
            for j in range(d):
                c[i+j]=(c[i+j]+a[i]*b[j])%p
        for deg in range(2*d-2,d-1,-1):
            z=c[deg]
            for i in range(d):
                c[deg-d+i]=(c[deg-d+i]-z*self.mod[i])%p
        return self.encode(c[:d])

    def A(self,x,y): return self.add[x][y]
    def M(self,x,y): return self.mul[x][y]
    def N(self,x): return self.neg[x]
    def C(self,k): return k % self.p


def analytic_count(F):
    q=F.q; p=F.p
    if p==2:
        return q*(q-2)//4, ('characteristic 2',)
    if p==3:
        return (q-1)*(q-3)//8, ('characteristic 3',)
    A=F.A; M=F.M; N=F.N; C=F.C; chi=F.chi
    H=V=U=0
    for x in range(q):
        H+=chi[M(x, A(M(x,x), N(C(1))))]  # x*(x^2 - 1)
        V+=chi[M(x, M(A(x,C(2)), A(x,C(3))))]
        U+=chi[M(x, M(A(M(C(2),x),N(C(1))), A(M(C(3),x),N(C(2)))))]
    eps=chi[N(C(1))]
    value=q*q-7*q+8+2*(1+eps)*chi[C(3)]\
          +(1+eps)*chi[C(6)]*H+2*chi[N(C(2))]*V-U
    assert value%16==0, ('not integer',q,value)
    return value//16,(H,V,U)


def direct_count(F,u,v):
    q=F.q; A=F.A; M=F.M; N=F.N
    # A monic quadratic is reducible iff it vanishes at a field element.
    reducible = [bytearray(q) for _ in range(q)]
    for a in range(q):
        for t in range(q):
            b=N(A(M(t,t),M(a,t)))
            reducible[a][b]=1
    offsets=[]
    for j in range(4):
        jj=F.C(j)
        offsets.append((M(jj,u),M(jj,v)))
    count=0
    for a in range(q):
        for b in range(q):
            if all(not reducible[A(a,du)][A(b,dv)] for du,dv in offsets):
                count+=1
    return count


def verify():
    configs=[(2,1),(2,2),(2,3),(2,4),
             (3,1),(3,2),(3,3),
             (5,1),(5,2),(5,3),
             (7,1),(7,2),
             (11,1),(13,1),(17,1),(19,1),(23,1),(29,1),(31,1)]
    fields=0; shifts=0; pairs=0
    print('q; predicted; H,V,U; shifts tested')
    for p,d in configs:
        F=Field(p,d); q=F.q
        predicted, traces=analytic_count(F)
        us = list(range(1,q)) if q<=9 else ([1,2] if q>2 else [1])
        vs = list(range(q)) if q<=9 else [0,1]
        count=0
        for u in us:
            for v in vs:
                got=direct_count(F,u,v)
                assert got==predicted,(p,d,q,u,v,got,predicted,traces)
                shifts+=1;count+=1;pairs+=q*q
        if p>3 and q>=11:
            assert predicted>0
        if q in (2,3,5):
            assert predicted==0
        print(q,predicted,traces,count)
        fields+=1
    print('VERIFY_OK fields=%d shift_cases=%d polynomial_pairs=%d root_test=independent' % (fields,shifts,pairs))


if __name__=='__main__':verify()
