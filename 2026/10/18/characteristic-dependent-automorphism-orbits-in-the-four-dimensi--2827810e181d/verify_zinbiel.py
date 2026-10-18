#!/usr/bin/env python3
"""Finite-field verification of element orbits for four-dimensional null-filiform Zinbiel algebra."""
from itertools import product
from math import comb, gcd

class Field:
    def __init__(self,p,m=1,poly=None):
        self.p,self.m,self.q,self.poly=p,m,p**m,poly
        self.add_table=[[self.add0(a,b) for b in range(self.q)] for a in range(self.q)]
        self.mul_table=[[self.mul0(a,b) for b in range(self.q)] for a in range(self.q)]
    def digits(self,a):
        d=[]
        for _ in range(self.m):d.append(a%self.p);a//=self.p
        return d
    def from_digits(self,d):return sum(x*self.p**i for i,x in enumerate(d))
    def add0(self,a,b):return self.from_digits([(x+y)%self.p for x,y in zip(self.digits(a),self.digits(b))])
    def mul0(self,a,b):
        d,e=self.digits(a),self.digits(b)
        c=[0]*(2*self.m-1)
        for i,x in enumerate(d):
            for j,y in enumerate(e):c[i+j]=(c[i+j]+x*y)%self.p
        if self.m>1:
            for k in range(len(c)-1,self.m-1,-1):
                f=c[k]
                for j in range(self.m):c[k-self.m+j]=(c[k-self.m+j]-f*self.poly[j])%self.p
        return self.from_digits(c[:self.m])
    def add(self,a,b):return self.add_table[a][b]
    def mul(self,a,b):return self.mul_table[a][b]
    def times(self,i,a):
        out=0
        for _ in range(i%self.p):out=self.add(out,a)
        return out
    def inv(self,a):
        assert a!=0
        return next(b for b in range(1,self.q) if self.mul(a,b)==1)

def zinbiel_product(F,v,w):
    out=[0]*4
    for i in range(1,5):
        for j in range(1,5-i):
            c=comb(i+j-1,j)%F.p
            if c:
                out[i+j-1]=F.add(out[i+j-1], F.times(c,F.mul(v[i-1],w[j-1])))
    return tuple(out)

def orbit_census(F):
    q=F.q
    elements=tuple(product(range(q), repeat=3))
    unseen=set(elements)
    orbit_sizes=[]
    powers=lambda a,n: pow_field(F,a,n)
    autos=[]
    for a1 in range(1,q):
      for a2 in range(q):
       for a3 in range(q):
        image1=(a1,a2,a3,0)
        image2=zinbiel_product(F,image1,image1)
        image3=zinbiel_product(F,image1,image2)
        image4=zinbiel_product(F,image1,image3)
        # Verified homomorphism: source basis relations check directly, all image products.
        im=(image1,image2,image3,image4)
        for i in range(1,5):
          for j in range(1,5):
            c=comb(i+j-1,j)%F.p if i+j<=4 else 0
            lhs=zinbiel_product(F,im[i-1],im[j-1]);rhs=(0,0,0,0)
            if c: rhs=tuple(F.times(c,x) for x in im[i+j-1])
            assert lhs==rhs,(F.q,im,i,j,lhs,rhs)
        assert F.mul(F.mul(powers(a1,1),powers(a1,2)),F.mul(powers(a1,3),powers(a1,4))) !=0
        autos.append(tuple(tuple(im[j][i] for i in range(1,4)) for j in range(1,4)))
    while unseen:
        v=next(iter(unseen)); orb=set()
        for auto in autos:
            out=[]
            for coordinate in range(3):
                total=0
                for j in range(3):total=F.add(total,F.mul(v[j],auto[j][coordinate]))
                out.append(total)
            orb.add(tuple(out))
        assert orb <= unseen,(F.q,v,len(orb),len(orb-unseen))
        unseen-=orb
        orbit_sizes.append(len(orb))
    total=1+len(orbit_sizes) # all vectors with nonzero e1-coordinate one orbit
    if F.p==2: predicted=2*q+2+gcd(3,q-1)
    elif F.p==3: predicted=2*q+3+gcd(4,q-1)
    else: predicted=4+gcd(3,q-1)+gcd(4,q-1)
    print('p,m,q',F.p,F.m,q,'AUT',len(autos)*q,'ORBITS',total,'PRED',predicted,'SIZEFREQ', {z:orbit_sizes.count(z) for z in sorted(set(orbit_sizes))})
    assert total==predicted
    assert sum(orbit_sizes)==q**3
    return total

def pow_field(F,a,n):
    r=1
    for i in range(n):r=F.mul(r,a)
    return r

if __name__=='__main__':
    for case in [(2,1,None),(3,1,None),(2,2,[1,1,1]),(5,1,None),(7,1,None),(2,3,[1,1,0,1]),(3,2,[1,0,1]),(11,1,None)]:
        orbit_census(Field(*case))
    print('VERIFY_OK')
