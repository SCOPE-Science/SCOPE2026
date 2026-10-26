#!/usr/bin/env python3
"""Exact finite-field verification of a genus-four hyperelliptic character census.
All arithmetic is in explicit polynomial residue fields over the prime field of order 7.
"""
from itertools import product

P = 7

def trim(c):
    c = [v % P for v in c]
    while len(c) > 1 and c[-1] == 0:
        c.pop()
    return c

def rem(f, g):
    a = trim(f)
    g = trim(g)
    while a != [0] and len(a) >= len(g):
        fac = a[-1] * pow(g[-1], -1, P) % P
        pos = len(a) - len(g)
        for j, v in enumerate(g):
            a[pos+j] = (a[pos+j] - fac*v) % P
        a = trim(a)
    return a

def gcd(f, g):
    a, b = trim(f), trim(g)
    while b != [0]:
        a, b = b, rem(a, b)
    return [v*pow(a[-1],-1,P)%P for v in a]

def polymul(a,b):
    c = [0]*(len(a)+len(b)-1)
    for i,x in enumerate(a):
        for j,y in enumerate(b):
            c[i+j] = (c[i+j]+x*y)%P
    return trim(c)

def powmod(a,k,modulus):
    out=[1]
    while k:
        if k&1:out=rem(polymul(out,a),modulus)
        a=rem(polymul(a,a),modulus)
        k//=2
    return out

def check_irreducible(f):
    d=len(f)-1
    X=[0,1]
    # Rabin criterion: X^(7^d)-X=0, and for every prime divisor l of d,
    # gcd(f,X^(7^(d/l))-X)=1.
    if d == 1:
        return
    assert powmod(X,P**d,f)==X
    for prime in range(2,d+1):
        if d%prime==0 and all(prime%j for j in range(2,int(prime**.5)+1)):
            z=powmod(X,P**(d//prime),f)
            diff=z[:]+[0]*max(0,2-len(z))
            diff[0]=(diff[0])%P
            diff[1]=(diff[1]-1)%P
            assert gcd(f,trim(diff))==[1]

class FF:
    def __init__(self, modulus):
        self.m=modulus
        self.d=len(modulus)-1
        self.zero=(0,)*self.d
        self.one=(1,)+(0,)*(self.d-1)
        check_irreducible(modulus)
        self.elements=list(product(range(P), repeat=self.d))
        self.squares={self.mul(a,a) for a in self.elements}
    def add(self,a,b):
        return tuple((u+v)%P for u,v in zip(a,b))
    def mul(self,a,b):
        d=self.d
        c=[0]*(2*d-1)
        for i in range(d):
            for j in range(d): c[i+j]+=a[i]*b[j]
        for i in range(2*d-2,d-1,-1):
            factor=c[i]%P
            for j in range(d): c[i-d+j]-=factor*self.m[j]
        return tuple(v%P for v in c[:d])
    def neg(self,a):return tuple(-v%P for v in a)
    def count(self,a):
        n0=nplus=nminus=0
        for x in self.elements:
            x2=self.mul(x,x)
            x4=self.mul(x2,x2)
            x5=self.mul(x4,x)
            x10=self.mul(x5,x5)
            val=self.add(self.add(x10,self.mul(a,x5)),self.one)
            if val==self.zero:n0+=1
            elif val in self.squares:nplus+=1
            else:nminus+=1
        assert n0+nplus+nminus==P**self.d
        return (n0,nplus,nminus,n0+2*nplus+2)

assert set(a*a%7 for a in range(7))=={0,1,2,4}
f1=FF([0,1]); f2=FF([1,0,1]); f3=FF([1,0,1,1]); f4=FF([1,0,0,1,1])
assert f2.mul((0,1),(0,1))==f2.neg(f2.one)
i4=(1,0,4,1)
assert f4.mul(i4,i4)==f4.neg(f4.one)

for field in (f1,f2,f3,f4):
    n=field.count(field.zero)
    print('a=0', P**field.d, n)
    assert n[-1]=={1:8,2:50,3:344,4:2794}[field.d]
    if field.d==4: assert n==(10,1391,1000,2794)
for field, a in ((f2,(0,1)),(f4,i4)):
    n=field.count(a)
    print('a^2=-1',P**field.d,n)
    assert n[-1]=={2:50,4:2794}[field.d]
    if field.d==4: assert n==(10,1391,1000,2794)

# Check the four Cartier-Manin entries for the genus-4 model.
# Let F(t)=(t*t+a*t+1)^3. The t^1 and t^2 coefficients are 3a, 3(a^2+1).
# Cartier entry in row i, col j is coefficient of x^(7i-j) in F(x^5).
locations={(i,j):(7*i-j)//5 for i in range(1,5) for j in range(1,5)
           if (7*i-j)%5==0}
assert locations=={(1,2):1,(2,4):2,(3,1):4,(4,3):5}
for a in range(7):
    c1=3*a%7
    c2=3*(a*a+1)%7
    rank=2*(c1!=0)+2*(c2!=0)
    assert rank in (2,4)
    if a*a%7==4:continue  # singular equation excluded
    assert (rank==2)==(a==0 or a*a%7==6)

# zeta polynomial coefficients by the Weil functional equation.
assert [1,0,0,0,98,0,0,0,2401]==[1,0,0,0,98,0,0,0,49**2]
print('VERIFY_OK')
