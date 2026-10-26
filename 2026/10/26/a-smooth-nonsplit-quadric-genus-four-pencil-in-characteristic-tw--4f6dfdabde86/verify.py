#!/usr/bin/env python3
"""Exact checks for a characteristic-two genus-four curve construction.

The finite tests supplement, but do not replace, the uniform geometric proof.
No external data or network required.
"""
from itertools import product
import sympy as sp

S,T,U,V,K = sp.symbols('S T U V K')
x,y,w = S*U, T*V, T*U+S*V
fhom = lambda a,b: a**3+a**2*b+b**3
F = y**3+y**2*w+w**3+x*y*w+x*y**2+x*w**2+(1+K)*x**3
assert sp.Poly(sp.expand(F-fhom(T,S)*fhom(V,U)-K*x**3),S,T,U,V,K,modulus=2).is_zero
s,t=sp.symbols('s t')
fpoly=lambda r:r**3+r**2+1
H=fpoly(s)*fpoly(t)+K
assert sp.Poly(sp.diff(H,s)+s**2*fpoly(t),s,t,K,modulus=2).is_zero
assert sp.Poly(sp.diff(H,t)+t**2*fpoly(s),s,t,K,modulus=2).is_zero
assert int(H.subs({s:0,t:0,K:1})) % 2 == 0

class GF:
    def __init__(self,n,poly):
        self.n,self.poly,self.q=n,poly,1<<n
    def mul(self,a,b):
        ans=0
        while b:
            if b&1: ans^=a
            b>>=1;a<<=1
            if a&self.q:a^=self.poly
        return ans
    def sq(self,a):return self.mul(a,a)
    def power(self,a,n):
        z=1
        while n:
            if n&1:z=self.mul(z,a)
            a=self.sq(a);n>>=1
        return z
    def mul3(self,a,b,c):return self.mul(self.mul(a,b),c)

def field_check(n,poly,m):
    F=GF(n,poly);q=1<<m
    sub=[a for a in range(F.q) if F.power(a,q)==a]
    assert len(sub)==q
    trace=lambda a: sum([]) if False else None
    def Tr(a):
        z=0;v=a
        for _ in range(m):z^=v;v=F.sq(v)
        return z
    c=next(a for a in sub if Tr(a)==1)
    f=lambda a:F.mul3(a,a,a)^F.sq(a)^1
    t=next(a for a in sub if f(a) not in [0,1])
    k=F.sq(f(t))
    assert k not in [0,1]
    def equations(x,y,z,w):
        xx,yy,zz,ww=[F.sq(a) for a in (x,y,z,w)]
        Q=F.mul(x,y)^zz^F.mul(z,w)^F.mul(c,ww)
        cub=F.mul(y,yy)^F.mul(yy,w)^F.mul(w,ww)^F.mul3(x,y,w)^F.mul(x,yy)^F.mul(x,ww)^F.mul(1^k,F.mul(x,xx))
        dQ=(y,x,w,z)
        dF=(F.mul(y,w)^yy^ww^F.mul(1^k,xx),yy^F.mul(x,w),0, yy^ww^F.mul(x,y))
        return Q,cub,dQ,dF
    assert equations(1,F.sq(t),t,0)[:2]==(0,0)
    # Enumerate projective points in F_(2^n), each vector normalized by first nonzero coordinate.
    hits=0;bad=0
    for i in range(4):
        for tail in product(range(F.q),repeat=3-i):
            P=(0,)*i+(1,)+tail
            Q,C,dQ,dF=equations(*P)
            if Q or C:continue
            hits+=1
            for a in range(4):
                for b in range(a+1,4):
                    if F.mul(dQ[a],dF[b])^F.mul(dQ[b],dF[a]):break
                else:continue
                break
            else:bad+=1
    assert bad==0,(m,n,bad)
    print(f'GF(2^{m}) embedded in GF(2^{n}): c={c}, t={t}, kappa={k}, points={hits}, singular={bad}')
    return hits

# irreducible polynomial bit encodings x^2+x+1, x^3+x+1, x^4+x+1, x^6+x+1
field_check(2,0b111,2)
field_check(4,0b10011,2)
field_check(3,0b1011,3)
field_check(6,0b1000011,3)
field_check(4,0b10011,4)
print('VERIFY_OK')
