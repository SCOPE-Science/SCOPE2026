#!/usr/bin/env python3
"""Exact finite-field certificates for harmonic sampling on 12 rhombicuboctahedral vertex lines.
Run: python3 checker.py. Standard library only.
"""
from fractions import Fraction
from itertools import product

PRIMES_AND_ROOTS = ((1000000007, 59713600), (1000000009, 291087696))
MAX_TESTED_DEGREE = 119

def nodes():
    # A sign-positive representative from each antipodal pair (all coordinates nonzero).
    out = []
    for pos in range(3):
        for tail in product((-1, 1), repeat=2):
            signs = (1,) + tail
            out.append((pos, signs))
    assert len(out) == 12
    return out

def modular_data(p, rt):
    assert pow(rt, 2, p) == 2
    t = (1+rt) % p
    den = (t*t+2) % p
    assert den
    inv = pow(den, -1, p)
    out = []
    for i,s in nodes():
        vec = tuple((s[k] * (t if k==i else 1)) % p for k in range(3))
        out.append(vec)
    return [[(sum(X[k]*Y[k] for k in range(3))*inv)%p for Y in out] for X in out]

def legendre_tables(p, dot):
    # Exact recurrence (l+1)P_(l+1)=(2l+1)x P_l-l P_(l-1) in prime characteristic.
    prev = [[1]*12 for _ in range(12)]
    curr = [row[:] for row in dot]
    yield prev
    yield curr
    for ell in range(1, MAX_TESTED_DEGREE):
        inv = pow(ell+1, -1, p)
        nxt = [[((2*ell+1)*dot[i][j]*curr[i][j]-ell*prev[i][j])*inv%p
                for j in range(12)] for i in range(12)]
        yield nxt
        prev,curr = curr,nxt

def rank(A,p):
    M = [row[:] for row in A]
    m=len(M); n=len(M[0]); h=0
    for col in range(n):
        pivot=next((i for i in range(h,m) if M[i][col]), None)
        if pivot is None: continue
        M[h],M[pivot]=M[pivot],M[h]
        inv=pow(M[h][col],-1,p)
        for j in range(col,n): M[h][j]=M[h][j]*inv%p
        for i in range(h+1,m):
            a=M[i][col]
            if a:
                for j in range(col,n): M[i][j]=(M[i][j]-a*M[h][j])%p
        h+=1
        if h==m: break
    return h

# Exact Q(sqrt(2)) arithmetic, Fractions for the one nontrivial identity.
class Q2:
    def __init__(self,a,b=0):
        self.a=Fraction(a); self.b=Fraction(b)
    def __add__(self,y):
        y=y if isinstance(y,Q2) else Q2(y)
        return Q2(self.a+y.a,self.b+y.b)
    __radd__=__add__
    def __neg__(self): return Q2(-self.a,-self.b)
    def __sub__(self,y): return self+(-y if isinstance(y,Q2) else -Q2(y))
    def __rsub__(self,y): return y+(-self)
    def __mul__(self,y):
        y=y if isinstance(y,Q2) else Q2(y)
        return Q2(self.a*y.a+2*self.b*y.b,self.a*y.b+self.b*y.a)
    __rmul__=__mul__
    def __truediv__(self,n):
        assert isinstance(n,int) and n!=0
        return Q2(self.a/n,self.b/n)
    def __eq__(self,y):
        y=y if isinstance(y,Q2) else Q2(y)
        return self.a==y.a and self.b==y.b
    def __repr__(self): return f'({self.a}) + ({self.b})sqrt(2)'

def P(ell,x):
    if ell==0: return Q2(1)
    prev,curr=Q2(1),x
    for n in range(1,ell):
        prev,curr=curr,(((2*n+1)*x*curr)-n*prev)/(n+1)
    return curr

def main():
    a=Q2(Fraction(7,17),Fraction(4,17))
    b=Q2(Fraction(-3,17),Fraction(8,17))
    c=Q2(Fraction(5,17),Fraction(-2,17))
    assert 1-3*P(9,a)+2*P(9,b)+2*P(9,c)==0
    assert 1-3*P(3,a)+2*P(3,b)+2*P(3,c)==0
    print('Exact annihilator identity at degrees 3 and 9: verified in Q(sqrt(2)).')
    # Independently verify the two pointwise left-kernel relations on all 12 antipodal lines.
    t=Q2(1,1); inv_den=Q2(Fraction(5,17),Fraction(-2,17))
    vertices=[]
    for pos, signs in nodes():
        vertices.append(tuple((t if i==pos else Q2(1))*signs[i] for i in range(3)))
    gram=[]
    for x in vertices:
        gram.append([P(9, sum(x[k]*y[k] for k in range(3))*inv_den) for y in vertices])
    signs=[signs[0]*signs[1]*signs[2] for pos,signs in nodes()]
    for i,j in ((0,1),(0,2)):
        w=[signs[k]*((pos==i)-(pos==j)) for k,(pos,_) in enumerate(nodes())]
        assert any(w)
        assert all(sum(gram[r][k]*w[k] for k in range(12))==0 for r in range(12))
    print('Both explicit degree-9 missing-data functionals annihilate the exact Gram matrix.')
    expected = [min(12,2*l+1) - (2 if l==9 else 0) for l in range(MAX_TESTED_DEGREE+1)]
    for p,r in PRIMES_AND_ROOTS:
        data=modular_data(p,r)
        ranks=[rank(G,p) for G in legendre_tables(p,data)]
        assert ranks==expected, [(l,x,y) for l,(x,y) in enumerate(zip(ranks,expected)) if x!=y]
        print(f'Prime {p}, sqrt2={r}: all {len(ranks)} degrees verified; ranks 0..12 = {ranks[:13]}.')
    print('Certificate PASSED.')

if __name__=='__main__': main()
