#!/usr/bin/env python3
"""Independent finite-field checks for weight-zero Rota-Baxter maps on k+V, V*V=0.
No external dependencies. Complete enumeration of linear maps in listed small cases.
"""
from itertools import product
from math import prod

class Field:
    def __init__(self,q):
        assert q in (2,3,4)
        self.q=q
        if q==4:
            self.add=lambda a,b:a^b
            def mul(a,b):
                v=0
                for i in range(2):
                    for j in range(2):
                        if ((a>>i)&1) and ((b>>j)&1): v^=1<<(i+j)
                if v&8: raise AssertionError('unexpected degree')
                if v&4: v^=0b111 # x^2=x+1
                return v
            self.mul=mul
        else:
            self.add=lambda a,b:(a+b)%q
            self.mul=lambda a,b:(a*b)%q
    def addvec(self,a,b):return tuple(self.add(x,y) for x,y in zip(a,b))
    def scale(self,a,v):return tuple(self.mul(a,x) for x in v)
    def inv(self,a):
        for b in range(1,self.q):
            if self.mul(a,b)==1:return b
        raise ArithmeticError()

def gaussian_rank(cols,F):
    if not cols:return 0
    rows=[list(row) for row in zip(*cols)]
    m,n=len(rows),len(cols)
    rank=0
    for j in range(n):
        idx=next((i for i in range(rank,m) if rows[i][j]),None)
        if idx is None:continue
        rows[rank],rows[idx]=rows[idx],rows[rank]
        inv=F.inv(rows[rank][j]);rows[rank]=[F.mul(inv,x) for x in rows[rank]]
        for i in range(m):
            if i==rank or rows[i][j]==0:continue
            mult=rows[i][j]
            rows[i]=[F.add(a,F.mul(mult,b) if F.q in (2,4) else (-F.mul(mult,b))%F.q) for a,b in zip(rows[i],rows[rank])]
        rank+=1
        if rank==m:break
    return rank

def mat_vec(cols,v,F):
    res=(0,)*len(cols)
    for c,col in zip(v,cols):
        res=F.addvec(res,F.scale(c,col))
    return res

def algmul(x,y,F):
    return (F.mul(x[0],y[0]),)+tuple(F.add(F.mul(x[0],y[i]),F.mul(y[0],x[i])) for i in range(1,len(x)))

def is_rb(cols,F):
    d=len(cols)-1
    basis=[tuple(1 if i==j else 0 for i in range(d+1)) for j in range(d+1)]
    for i in range(d+1):
        for j in range(d+1):
            left=algmul(cols[i],cols[j],F)
            right=mat_vec(cols,F.addvec(algmul(basis[i],cols[j],F),algmul(cols[i],basis[j],F)),F)
            if left!=right:return False
    return True

def square_zero(B,F):
    return all(mat_vec(B,c,F)==(0,)*len(B) for c in B)

def is_predicted(cols,F):
    d=len(cols)-1
    if any(col[0]!=0 for col in cols):return False
    B=[col[1:] for col in cols[1:]]
    if not square_zero(B,F):return False
    if F.q==3 and mat_vec(B,cols[0][1:],F)!=(0,)*d:return False
    return True

def gaussian(q,n,k):
    if not (0<=k<=n):return 0
    if k==0:return 1
    a=prod(q**(n-i)-1 for i in range(k)); b=prod(q**(k-i)-1 for i in range(k))
    assert a%b==0
    return a//b

def gl(q,j):return prod(q**j-q**i for i in range(j))
def N(q,d,j):return gaussian(q,d,j)*gaussian(q,d-j,j)*gl(q,j)

def predicted_spectrum(q,d):
    from collections import Counter
    c=Counter()
    for j in range(d//2+1):
        count=N(q,d,j)
        c[(j,0)]+=count*q**j
        c[(j+1,0)]+=count*(q**(d-j)-q**j)
        if q%2==0:
            c[(j+1,1)]+=count*(q**d-q**(d-j))
    return {key:value for key,value in c.items() if value}

def full_enumeration(d,q):
    F=Field(q); n=d+1; c={}; passes=0
    for digits in product(range(q),repeat=n*n):
        cols=tuple(digits[j*n:(j+1)*n] for j in range(n))
        truth=is_rb(cols,F)
        predicted=is_predicted(cols,F)
        assert truth==predicted, ('characterization',d,q,cols,truth,predicted)
        if truth:
            passes+=1
            rk=gaussian_rank(cols,F)
            squared=any(mat_vec(cols,col,F)!=(0,)*n for col in cols)
            c[(rk,int(squared))]=c.get((rk,int(squared)),0)+1
    expect=predicted_spectrum(q,d)
    assert c==expect,('spectrum',d,q,c,expect)
    print('FULL_ENUM_OK',d,q,passes,sorted(c.items()))

def conditional_enumeration(d,q):
    F=Field(q); n=d+1;c={};sqcount=0
    for digits in product(range(q),repeat=d*d):
        B=tuple(digits[j*d:(j+1)*d] for j in range(d))
        if not square_zero(B,F):continue
        sqcount+=1
        for u in product(range(q),repeat=d):
            cols=((0,)+u,)+tuple((0,)+v for v in B)
            truth=is_rb(cols,F)
            if F.q%2==0: expected=True
            else:expected=mat_vec(B,u,F)==(0,)*d
            assert truth==expected,('identity',d,q,B,u)
            if truth:
                rk=gaussian_rank(cols,F)
                squared=any(mat_vec(cols,col,F)!=(0,)*n for col in cols)
                c[(rk,int(squared))]=c.get((rk,int(squared)),0)+1
    assert sqcount==sum(N(q,d,j) for j in range(d//2+1)),('nilpotent count',sqcount)
    expect=predicted_spectrum(q,d)
    assert c==expect,('spectrum',d,q,c,expect)
    print('CONDITIONAL_ENUM_OK',d,q,sqcount,sum(c.values()),sorted(c.items()))

if __name__=='__main__':
    for d,q in ((1,2),(1,3),(2,2),(2,3),(2,4),(3,2)):
        full_enumeration(d,q)
    for d,q in ((3,3),(4,2),(3,4)):
        conditional_enumeration(d,q)
    print('ROTA_BAXTER_MODULAR_SQUARE_ZERO_OK')
