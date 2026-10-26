#!/usr/bin/env python3
"""Independent exact finite-field and polynomial certificate for an explicit genus-three curve."""
from itertools import product
from math import gcd

class FiniteField:
    def __init__(self, p, modulus):
        self.p, self.modulus = p, modulus
        self.n = len(modulus)-1
        assert modulus[-1] == 1
        self.q = p**self.n
        self.elements = list(product(range(p), repeat=self.n))
        self.zero=(0,)*self.n
        self.one=(1,)+(0,)*(self.n-1)
    def integer(self,a):return (a%self.p,)+(0,)*(self.n-1)
    def add(self,a,b):return tuple((x+y)%self.p for x,y in zip(a,b))
    def mul(self,a,b):
        c=[0]*(2*self.n-1)
        for i,x in enumerate(a):
            for j,y in enumerate(b):c[i+j]=(c[i+j]+x*y)%self.p
        for k in range(2*self.n-2,self.n-1,-1):
            v=c[k]
            for j in range(self.n):c[k-self.n+j]=(c[k-self.n+j]-v*self.modulus[j])%self.p
        return tuple(c[:self.n])
    def power(self,a,n):
        ans=self.one
        while n:
            if n&1:ans=self.mul(ans,a)
            a=self.mul(a,a);n>>=1
        return ans
    def count_hyperelliptic(self):
        # i -> 2 in F_5, Q(t)=4P(t)=1+3t+4t^3+4t^4.
        assert self.p==5
        coeff=[self.integer(j) for j in (1,3,0,4,4)]
        squares={self.mul(a,a) for a in self.elements}
        count=self.q+2 # two rational points at infinity (leading coefficient 1)
        for x in self.elements:
            v=self.zero
            for c in reversed(coeff):v=self.add(self.mul(v,x),c)
            D=self.add(self.mul(v,v),self.mul(self.integer(-64),self.power(x,3)))
            count+=0 if D==self.zero else (1 if D in squares else -1)
        return count

def eval_poly(c,x,p):
    r=0
    for a in reversed(c):r=(r*x+a)%p
    return r

def poly_gcd_5(a,b):
    def normalize(v):
        v=[x%5 for x in v]
        while v and v[-1]==0:v.pop()
        return v
    a,b=normalize(a),normalize(b)
    while b:
        r=a[:]
        while len(r)>=len(b):
            k=len(r)-len(b)
            u=r[-1]*pow(b[-1],-1,5)%5
            for j,v in enumerate(b):r[k+j]=(r[k+j]-u*v)%5
            r=normalize(r)
        a,b=b,r
    return normalize(a)

def verify():
    # Each modulus is irreducible: z, z^2+2 (nonsquare -2), z^3+z+1 (no roots).
    assert all(eval_poly([1,1,0,1],x,5)!=0 for x in range(5))
    assert all(eval_poly([2,0,1],x,5)!=0 for x in range(5))
    # Q(x)^2-64x^3 modulo 5 has the following ascending coefficients.
    squarefree=[1,1,4,4,2,4,1,2,1]
    deriv=[((j+1)*squarefree[j+1])%5 for j in range(8)]
    assert len(poly_gcd_5(squarefree,deriv))==1
    counts=[]
    for modulus in ([0,1],[2,0,1],[1,1,0,1]):
        F=FiniteField(5,modulus)
        assert all(F.power(a,F.q-1)==F.one for a in F.elements if a!=F.zero)
        counts.append(F.count_hyperelliptic())
    assert counts==[7,43,133], counts
    s=[5**(i+1)+1-counts[i] for i in range(3)]
    assert s==[-1,-17,-7]
    c1=-s[0]
    c2=(s[0]**2-s[1])//2
    c3=(-s[0]**3+3*s[0]*s[1]-2*s[2])//6
    assert (c1,c2,c3)==(1,9,11)
    # h(X) = X^6 + X^5 + 9X^4 + 11X^3 + 45X^2 + 25X + 125.
    assert [125,25,45,11,9,1,1]==[5**3,5**2*c1,5*c2,c3,c2,c1,1]
    # Cubic g(Y)=Y^3+Y^2-6Y+1 has no rational root, discriminant 761.
    assert 1**3+1**2-6*1+1 == -3
    assert (-1)**3+(-1)**2-6*(-1)+1 == 7
    a,b,c,d=1,1,-6,1
    disc=b*b*c*c-4*a*c**3-4*b**3*d-27*a*a*d*d+18*a*b*c*d
    assert disc==761
    # Norm_{Q(y)/Q}(y^2-20) = -3479 = -(7^2)*71.
    # If y_i are the three roots: prod_i(y_i^2-20) = -3479.
    # prod_i (y_i^2-20) = g(sqrt(20))*g(-sqrt(20)).
    # g(sqrt(20))=(20-6)*sqrt(20)+21 = 14sqrt(20)+21.
    assert (21**2-(14**2)*20)==-3479
    assert -3479 == -7*7*71
    # Mod 71 g has a unique linear root 34; the quadratic cofactor has no root.
    assert all((j*j+35*j-23)%71!=0 for j in range(71))
    assert all((k+(-34))%71==0 or (k**3+k*k-6*k+1)%71!=0 for k in range(71))
    assert (34**2-20)%71==0
    assert all((j*j-20)%71!=0 for j in range(71) if j!=34 and (j**3+j*j-6*j+1)%71==0)
    assert 11%5!=0 # ordinary Jacobian
    print('VERIFY_OK',counts,'Frobenius=[125,25,45,11,9,1,1]','cubic_disc=761','quadratic_norm=-3479')
if __name__=='__main__':verify()
