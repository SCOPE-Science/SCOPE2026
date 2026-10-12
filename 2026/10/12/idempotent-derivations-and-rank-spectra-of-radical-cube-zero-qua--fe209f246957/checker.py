#!/usr/bin/env python3
"""Check the parameter-generic idempotent-derivation rank formula.

Independent brute-force checks on the four-dimensional case enumerate all
possible generator images, including scalar components, and apply Leibniz
and idempotence to every basis element. No external packages required.
"""
from itertools import product
from collections import Counter
from math import comb

class Field:
    def __init__(self,q):
        self.q=q
    def add(self,a,b):
        return a^b if self.q==4 else (a+b)%self.q
    def neg(self,a):
        return a if self.q==4 else (-a)%self.q
    def mul(self,a,b):
        if self.q!=4:return (a*b)%self.q
        x=0
        while b:
            if b&1:x^=a
            b>>=1; a<<=1
            if a&4:a^=7 # polynomial t^2+t+1
        return x
    def mat_rank(self, columns):
        rows=[list(row) for row in zip(*columns)]
        q=self.q
        rank=0
        for j in range(len(columns)):
            piv=next((i for i in range(rank,len(rows)) if rows[i][j]!=0),None)
            if piv is None:continue
            rows[rank],rows[piv]=rows[piv],rows[rank]
            inv=next(x for x in range(1,q) if self.mul(x,rows[rank][j])==1)
            rows[rank]=[self.mul(x,inv) for x in rows[rank]]
            for i in range(len(rows)):
                if i==rank:continue
                fac=rows[i][j]
                if fac:
                    rows[i]=[self.add(rows[i][k],self.neg(self.mul(fac,rows[rank][k]))) for k in range(len(columns))]
            rank+=1
        return rank

def predicted(n,q):
    out=Counter()
    if q%2:
        E=(n-1)**2+comb(n-1,2)
        out[0]=1
        out[n]=n*q**E
    else:
        for r in range(n+1):
            u=n-r
            E=r*(comb(r,2)+comb(u,2)+u*u)
            out[r+r*u]+=comb(n,r)*q**E
    return dict(out)

def brute_two(q,t):
    F=Field(q)
    Z=(0,0,0,0)
    unit=(1,0,0,0)
    ex=(0,1,0,0)
    ey=(0,0,1,0)
    ez=(0,0,0,1)
    basis=[unit,ex,ey,ez]
    add=lambda a,b:tuple(F.add(x,y) for x,y in zip(a,b))
    scalar=lambda c,a:tuple(F.mul(c,x) for x in a)
    def mul(a,b):
        return (F.mul(a[0],b[0]),
            F.add(F.mul(a[0],b[1]),F.mul(a[1],b[0])),
            F.add(F.mul(a[0],b[2]),F.mul(a[2],b[0])),
            F.add(F.add(F.mul(a[0],b[3]),F.mul(a[3],b[0])),
                F.add(F.mul(a[1],b[2]),F.mul(t,F.mul(a[2],b[1])))))
    # identity-quotient multiplication, with x_2*x_1=t*x_1*x_2
    table=[[mul(a,b) for b in basis] for a in basis]
    observed=Counter()
    orbit_reps=set()
    valid=0
    for coeffs in product(range(q),repeat=8):
        X=coeffs[:4];Y=coeffs[4:]
        # D(z) from D(x*y) and D(1)=0
        Dz=add(mul(X,ey),mul(ex,Y))
        Dcols=(Z,X,Y,Dz)
        def D(v):
            out=Z
            for i,c in enumerate(v):
                if c:out=add(out,scalar(c,Dcols[i]))
            return out
        if any(D(table[i][j])!=add(mul(Dcols[i],basis[j]),mul(basis[i],Dcols[j])) for i in range(4) for j in range(4)):
            continue
        if any(D(Dcols[i])!=Dcols[i] for i in range(4)):
            continue
        valid+=1
        observed[F.mat_rank(Dcols)]+=1
        assert X[0]==Y[0]==X[2]==Y[1]==0
        lam=(X[1],Y[2])
        assert all(v in (0,1) for v in lam)
        pair=F.add(lam[0],lam[1])
        for diagonal,tail in [(lam[0],X[3]),(lam[1],Y[3])]:
            diff=F.add(diagonal,F.neg(pair))
            if diff==0:
                assert tail==0
            else:
                h=next(z for z in range(q) if F.mul(diff,z)==tail)
                assert F.mul(diff,h)==tail # an actual shear-conjugacy certificate
        orbit_reps.add(lam)
    want=predicted(2,q)
    assert dict(observed)==want,(q,t,dict(observed),want)
    assert len(orbit_reps)==(4 if q%2==0 else 3)
    return valid,dict(observed)

def direct_normal_form(n,q):
    # Enumerate diagonal idempotent lambda choices and allowed quadratic terms
    # without using closed-form E(r), independently summing all choices.
    F=Field(q)
    hist=Counter()
    for lam in product((0,1),repeat=n):
        sums=[F.add(lam[i],lam[j]) for i in range(n) for j in range(i+1,n)]
        if any(x not in (0,1) for x in sums):continue
        admissible=sum(F.add(lam[i],b)==1 for i in range(n) for b in sums)
        rank=sum(lam)+sum(x==1 for x in sums)
        hist[rank]+=q**admissible
    assert dict(hist)==predicted(n,q),(n,q,dict(hist),predicted(n,q))
    return dict(hist)

if __name__=='__main__':
    for q,t in [(4,2),(4,3),(5,2),(5,3)]:
        total,hist=brute_two(q,t)
        print('full_generator_enumeration',q,t,total,hist)
    for q in [4,5,7]:
        for n in range(2,7):
            print('normal_form',n,q,direct_normal_form(n,q))
    print('VERIFY_OK')
