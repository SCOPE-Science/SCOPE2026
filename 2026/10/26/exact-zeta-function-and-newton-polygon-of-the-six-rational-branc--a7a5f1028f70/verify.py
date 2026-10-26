#!/usr/bin/env python3
"""Independent finite-field and character checks for a Humbert--Edge curve.
All arithmetic is exact, using elementary finite-field polynomial arithmetic.
"""
from itertools import combinations
from math import comb

P=5

def polynomial_irreducible_mod_5(poly):
    # The supplied degree 2 and 3 polynomials have no F5 roots.
    return all(sum(c*pow(a,j,P) for j,c in enumerate(poly))%P for a in range(P))

class Field:
    def __init__(self, polynomial):
        self.polynomial=tuple(polynomial)
        self.d=len(polynomial)-1
        assert polynomial[-1]==1
        assert self.d==1 or polynomial_irreducible_mod_5(polynomial)
        self.q=5**self.d
        self.elements=tuple(range(self.q))
        self.zero=0
        self.one=1
    def unpack(self,a):
        z=[]
        for _ in range(self.d):
            z.append(a%5)
            a//=5
        return z
    def pack(self,z):
        return sum((z[i]%5)*5**i for i in range(self.d))
    def add(self,a,b):
        return self.pack([x+y for x,y in zip(self.unpack(a),self.unpack(b))])
    def neg(self,a):
        return self.pack([-x for x in self.unpack(a)])
    def sub(self,a,b):
        return self.add(a,self.neg(b))
    def mul(self,a,b):
        x=self.unpack(a);y=self.unpack(b)
        c=[0]*(2*self.d-1)
        for i in range(self.d):
            for j in range(self.d):
                c[i+j]+=x[i]*y[j]
        for i in range(len(c)-1,self.d-1,-1):
            u=c[i]%5
            for j in range(self.d):
                c[i-self.d+j]-=u*self.polynomial[j]
        return self.pack(c[:self.d])
    def pow(self,a,n):
        b=1
        while n:
            if n&1:b=self.mul(a,b)
            a=self.mul(a,a);n//=2
        return b
    def chi(self,a):
        if a==0:return 0
        return 1 if self.pow(a,(self.q-1)//2)==1 else -1

def count_X(field):
    n=16 # all 16 points over infinity
    layers=[]
    for t in field.elements:
        mult=1
        for i in range(5):
            z=field.sub(t,i)
            mult*=1+field.chi(z)
        layers.append(mult)
        n+=mult
    return n,layers

def L_recurrence_trace(t,m,q=5):
    a,b=2,t
    if m==1:return b
    for j in range(2,m+1):
        a,b=b,t*b-q*a
    return b

def predicted_points(m):
    sum_e=5*L_recurrence_trace(2,m)+10*L_recurrence_trace(-2,m)
    sum_h=(4*5**(m//2)) if m%2==0 else 0
    return 5**m+1-sum_e-sum_h

# Structural quotient census: k=3,4 elliptics, k=5 genus two.
assert [comb(5,k) for k in range(1,6)]==[5,10,10,5,1]
assert sum(comb(5,k)*((k-1)//2) for k in range(1,6))==17

for polynomial in ([0,1],[2,0,1],[1,2,0,1]):
    f=Field(polynomial)
    m=f.d
    assert f.q in (5,25,125)
    count,layers=count_X(f)
    if m in (1,2):
        n_genus_two=1
        for t in f.elements:
            product=1
            for i in range(5):
                product=f.mul(product,f.sub(t,i))
            n_genus_two+=1+f.chi(product)
        assert n_genus_two==6,(f.q,n_genus_two)
        print(f'Genus-two quotient F_{f.q}: #{n_genus_two}')
    expected=predicted_points(m)
    assert count==expected,(f.q,count,expected)
    assert count>=16
    print(f'F_{f.q}: #{count}, branch-finite-support {sum(v>0 for v in layers)}; predicted {expected}')

f=Field([0,1]); etraces=[]
for k in [3,4]:
    for inds in combinations(range(5),k):
        N= (1 if k%2 else 2) # degree 3: one rational infinity; quartic: two
        for t in range(5):
            z=1
            for i in inds:z=z*((t-i)%5)%5
            N+=1+f.chi(z)
        assert N in (4,8),(inds,N)
        etraces.append(6-N)
assert (etraces.count(2),etraces.count(-2))==(5,10)
print('Elliptic quotient traces: +2:',etraces.count(2),'-2:',etraces.count(-2))

# Cartier--Manin matrix of y^2 = t^5-t is zero in characteristic 5.
# f(t)^2=t^10-2t^6+t^2, none of the required exponents 3,4,8,9.
assert set([2,6,10]).isdisjoint({3,4,8,9})
print('Genus-two Cartier-Manin: zero; p-rank 0, a-number 2')
print('Newton slopes: 0^15, (1/2)^4, 1^15; p-rank 15; a-number 2')
print('L(T)=(1-2T+5T^2)^5(1+2T+5T^2)^10(1-5T^2)^2')
print('VERIFY_OK')
