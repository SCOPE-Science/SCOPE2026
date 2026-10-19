#!/usr/bin/env python3
"""Independent finite-field checks for commutation in binomial presemifields.
Uses literal polynomial arithmetic, Frobenius powering, and direct products.
No third-party packages are needed.
"""
from itertools import product


def irreducible_poly(p, n):
    # Exhaustive polynomial search, only for the small test degrees.
    def trim(a):
        a = list(a)
        while len(a) > 1 and a[-1] == 0:
            a.pop()
        return a
    def remainder(a, b):
        a = trim(a)
        while len(a) >= len(b) and a != [0]:
            d = len(a) - len(b)
            z = a[-1] * pow(b[-1], -1, p) % p
            for i, c in enumerate(b):
                a[i+d] = (a[i+d] - z*c) % p
            a = trim(a)
        return a
    for tail in product(range(p), repeat=n):
        if tail[0] == 0:
            continue
        f = list(tail) + [1]
        if all(remainder(f, list(g)+[1]) != [0]
               for k in range(1, n//2+1)
               for g in product(range(p), repeat=k)):
            return tuple(tail)
    raise ValueError('missing irreducible polynomial')

class Field:
    def __init__(self, p, n):
        self.p, self.n = p, n
        self.q = p**n
        self.mod = irreducible_poly(p,n)
    def coeff(self, a):
        p = self.p
        out = []
        for _ in range(self.n):
            out.append(a%p); a//=p
        return out
    def val(self,a):
        return sum(int(c) * self.p**i for i,c in enumerate(a))
    def add(self,a,b):
        x,y = self.coeff(a),self.coeff(b)
        return self.val([(u+v)%self.p for u,v in zip(x,y)])
    def sub(self,a,b):
        x,y = self.coeff(a),self.coeff(b)
        return self.val([(u-v)%self.p for u,v in zip(x,y)])
    def mul(self,a,b):
        p,n = self.p,self.n
        x,y=self.coeff(a),self.coeff(b)
        out=[0]*(2*n-1)
        for i in range(n):
            for j in range(n):
                out[i+j]=(out[i+j]+x[i]*y[j])%p
        for k in range(2*n-2,n-1,-1):
            t=out[k]
            for i in range(n):
                out[k-n+i]=(out[k-n+i]-t*self.mod[i])%p
        return self.val(out[:n])
    def power(self,a,m):
        acc=1
        while m:
            if m&1:acc=self.mul(acc,a)
            a=self.mul(a,a)
            m>>=1
        return acc
    def norm(self,a):
        return self.power(a,(self.q-1)//(self.p-1))
    def product(self,x,y,c,r,s):
        return self.sub(self.mul(x,y),self.mul(c,self.mul(self.power(x,self.p**r),self.power(y,self.p**s))))


def verify(p,n,r,s):
    F=Field(p,n)
    Q=F.q
    g=__import__('math').gcd(n,r-s)
    H=p**g
    fieldH={z for z in range(Q) if F.power(z,H)==z}
    assert len(fieldH)==H
    c=next(z for z in range(1,Q) if F.norm(z)!=1)
    # Test the nonzero-product property exhaustively for fields up to size 125,
    # and on a prescribed grid in larger fields; its general proof uses norms.
    for x in (range(1,Q) if Q<=125 else range(1,min(Q,41))):
        for y in (range(1,Q) if Q<=125 else range(1,min(Q,97))):
            assert F.product(x,y,c,r,s)!=0
    # Literal commutation agrees exactly with a subfield-line condition.
    pair_count=0
    for x in (range(Q) if Q<=125 else range(0,min(Q,40))):
        commuting=[]
        for y in range(Q):
            direct=F.product(x,y,c,r,s)==F.product(y,x,c,r,s)
            expected=(x==0 or y in {F.mul(x,t) for t in fieldH})
            assert direct==expected,(p,n,r,s,x,y)
            pair_count+=direct
            if direct:commuting.append(y)
        assert len(commuting)==(Q if x==0 else H)
    if Q<=125:
        assert pair_count==1+((Q-1)//(H-1))*(H**2-1)
    # Check a third-arity count by explicit enumeration for small field sizes.
    if Q<=27:
        direct3=0
        P=[[F.product(x,y,c,r,s)==F.product(y,x,c,r,s)
               for y in range(Q)] for x in range(Q)]
        for x in range(Q):
            for y in range(Q):
                if P[x][y]:
                    direct3+=sum(P[x][z] and P[y][z] for z in range(Q))
        assert direct3==1+((Q-1)//(H-1))*(H**3-1)
    print('PASS',{'p':p,'n':n,'r':r,'s':s,'irreducible_polynomial_coeffs':F.mod,'c':c,'norm_c':F.norm(c),'line_size':H,'checked_pair_hits':pair_count,'checked_x_count':(Q if Q<=125 else min(Q,40))})

if __name__=='__main__':
    for parameters in [(3,3,1,2),(5,3,1,2),(3,4,1,3),(3,4,1,2),(3,6,1,5),(3,6,2,4)]:
        verify(*parameters)
    print('VERIFY_OK_TWISTED_FIELDS')
