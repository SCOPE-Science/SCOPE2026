#!/usr/bin/env python3
"""Exact polynomial and finite-field checks for the Wiman plane model.

Requires only Python's standard library. This is finite corroboration;
the proof of the arbitrary-extension formulas is in RESULT.md.
"""
from itertools import product
from math import comb


def add(*polys):
    out = {}
    for d in polys:
        for k, v in d.items():
            out[k] = out.get(k, 0) + v
    return {k: v for k, v in out.items() if v}


def mul(a, b):
    out = {}
    for (i, j, k), u in a.items():
        for (l, m, n), v in b.items():
            t = (i+l, j+m, k+n)
            out[t] = out.get(t, 0) + u*v
    return {k: v for k, v in out.items() if v}


def scale(a, n):
    return {k: n*v for k, v in a.items()}


def power(a, n):
    out = {(0,0,0): 1}
    for _ in range(n):
        out = mul(out,a)
    return out


def equal_mod(a,b,p):
    return all((a.get(k,0)-b.get(k,0))%p==0 for k in set(a)|set(b))

x={(1,0,0):1};y={(0,1,0):1};z={(0,0,1):1}
Q=add(power(x,2),power(y,2),power(z,2))
P=mul(mul(x,y),z)
F=add(power(x,6),power(y,6),power(z,6),mul(Q,add(power(x,4),power(y,4),power(z,4))),scale(power(P,2),-12))
L2=mul(mul(add(x,y),add(y,z)),add(z,x))
L3=mul(mul(mul(add(x,y,z),add(scale(x,-1),y,z)),add(x,scale(y,-1),z)),add(x,y,scale(z,-1)))
assert equal_mod(F,power(L2,2),2)
assert equal_mod(F,mul(Q,L3),3)
assert equal_mod(F,add(scale(power(Q,3),2),power(P,2)),5)
print('THREE_INTEGRAL_POLYNOMIAL_IDENTITIES_PASS')

# Quadratic tangent cone in local coordinates x=1+u,y=1+v,z=1.
quadratic={}
for (a,b,c),val in F.items():
    for i in range(min(a,2)+1):
        for j in range(min(b,2-i)+1):
            if i+j==2:
                quadratic[i,j]=(quadratic.get((i,j),0)+val*comb(a,i)*comb(b,j))%5
assert quadratic=={(2,0):2,(1,1):3,(0,2):2},quadratic
assert (quadratic[1,1]**2-4*quadratic[2,0]*quadratic[0,2])%5==3
assert {i*i%5 for i in range(5)}=={0,1,4}
print('FOUR_NONSPLIT_ORDINARY_NODES_MOD_5_PASS')

# The four intrinsic marked points are a projective frame in p=3 and p=5.
from itertools import combinations
frame=[(1,1,1),(-1,1,1),(1,-1,1),(1,1,-1)]
def determinant(v,w,t):
    a,b,c=v;d,e,f=w;g,h,i=t
    return a*(e*i-f*h)-b*(d*i-f*g)+c*(d*h-e*g)
for p in (3,5):
    assert all(determinant(*triple)%p for triple in combinations(frame,3))
print('PROJECTIVE_FRAME_IN_BOTH_CHARACTERISTICS_PASS')

class Field:
    def __init__(self,p,degree):
        self.p=p;self.degree=degree
        self.q=p**degree
        if degree==2:
            # t^2 = r*t + s: irreducible for these three fields.
            self.r,self.s=({2:(1,1),3:(0,2),5:(0,2)})[p]
        else:
            self.r,self.s=0,0
    def add(self,a,b):
        if self.degree==1:return (a+b)%self.p
        return ((a%self.p+b%self.p)%self.p + self.p*((a//self.p+b//self.p)%self.p))
    def neg(self,a):
        if self.degree==1:return -a%self.p
        return (-a%self.p)+self.p*(-(a//self.p)%self.p)
    def mul(self,a,b):
        p=self.p
        if self.degree==1:return (a*b)%p
        a0,a1=a%p,a//p;b0,b1=b%p,b//p
        return ((a0*b0+self.s*a1*b1)%p)+p*((a0*b1+a1*b0+self.r*a1*b1)%p)
    def pow(self,a,n):
        result=1
        while n:
            if n&1:result=self.mul(result,a)
            a=self.mul(a,a);n>>=1
        return result

def polynomial(X,Y,Z,k):
    a=k.add(k.add(k.pow(X,6),k.pow(Y,6)),k.pow(Z,6))
    sq=k.add(k.add(k.pow(X,2),k.pow(Y,2)),k.pow(Z,2))
    fourth=k.add(k.add(k.pow(X,4),k.pow(Y,4)),k.pow(Z,4))
    t=k.mul(k.mul(X,Y),Z)
    return k.add(k.add(a,k.mul(sq,fourth)),k.mul((-12)%k.p,k.pow(t,2)))

def count(k):
    ans=0
    for a,b in product(range(k.q),repeat=2):
        ans+=(polynomial(a,b,1,k)==0)
    for a in range(k.q):
        ans+=(polynomial(a,1,0,k)==0)
    ans+=(polynomial(1,0,0,k)==0)
    return ans

for p in (2,3,5):
    for n in (1,2):
        k=Field(p,n)
        actual=count(k);q=k.q
        expected=({2:3*q+1,3:5*q-5,5:q+1-4*(-1)**n})[p]
        assert actual==expected,(p,n,actual,expected)
        print('POINTS',p,n,actual,'PASS')

# Exhaustive singular supports on P^2(F5) and P^2(F3).
for p in (3,5):
    sing=set()
    for X,Y in product(range(p),repeat=2):
        for a,b,c in [(X,Y,1)]:
            F0=(a**6+b**6+c**6+(a*a+b*b+c*c)*(a**4+b**4+c**4)-12*a*a*b*b*c*c)%p
            if p==5:
                q=(a*a+b*b+c*c)%p
                deriv=(2*a*(q*q+b*b*c*c),2*b*(q*q+a*a*c*c),2*c*(q*q+a*a*b*b))
            else:
                # Derivatives of the original sextic, in characteristic 3.
                q=(a*a+b*b+c*c)%p
                deriv=(2*a*(a**4+b**4+c**4)+4*a**3*q,
                       2*b*(a**4+b**4+c**4)+4*b**3*q,
                       2*c*(a**4+b**4+c**4)+4*c**3*q)
            if F0==0 and all(t%p==0 for t in deriv):sing.add((a,b,c))
    for X in range(p):
        a,b,c=X,1,0
        F0=(a**6+b**6+(a*a+b*b)*(a**4+b**4))%p
        if p==5:
            q=(a*a+b*b)%p
            deriv=(2*a*q*q,2*b*q*q,0)
        else:
            q=(a*a+b*b)%p
            deriv=(2*a*(a**4+b**4)+4*a**3*q,2*b*(a**4+b**4)+4*b**3*q,0)
        if F0==0 and all(t%p==0 for t in deriv):sing.add((a,b,c))
    # point [1:0:0] is not on the curve in these characteristics.
    assert len(sing)==10,(p,sing)
    print('SINGULAR_SUPPORT',p,len(sing),'PASS')

print('WIMAN_BAD_PRIME_EXACT_CHECKS_PASS')
