#!/usr/bin/env python3
"""Reproduce Kirillov-rank strata and central additive-commutator fibers of T_4(F_q)."""
from itertools import product
from collections import Counter

POSITIONS = [(i,j) for i in range(4) for j in range(i,4)]
OFF = [(i,j) for i,j in POSITIONS if i<j]

class Field:
    def __init__(self,q):
        self.q=q
        assert q in (2,3,4,5)
    def add(self,a,b):
        return a^b if self.q==4 else (a+b)%self.q
    def neg(self,a):
        return a if self.q==4 else (-a)%self.q
    def sub(self,a,b):
        return self.add(a,self.neg(b))
    def mul(self,a,b):
        if self.q!=4:return a*b%self.q
        t=0
        for k in range(2):
            if (b>>k)&1:t^=a<<k
        if t&8:t^=0b1100   # x^3 = x^2+x
        if t&4:t^=0b111    # x^2 = x+1
        return t
    def inv(self,a):
        assert a
        return next(x for x in range(1,self.q) if self.mul(a,x)==1)

def rank(rows,F):
    a=[r[:] for r in rows]
    if not a:return 0
    n,m=len(a),len(a[0]); k=0
    for j in range(m):
        pivot=next((i for i in range(k,n) if a[i][j]!=0),None)
        if pivot is None:continue
        a[k],a[pivot]=a[pivot],a[k]
        z=F.inv(a[k][j]); a[k]=[F.mul(z,u) for u in a[k]]
        for i in range(k+1,n):
            if a[i][j]:
                z=a[i][j]
                a[i]=[F.sub(v,F.mul(z,w)) for v,w in zip(a[i],a[k])]
        k+=1
        if k==n:break
    return k

def bracket_matrix(lam,F):
    mu=dict(zip(OFF,lam)); M=[]
    for i,j in POSITIONS:
        row=[]
        for k,l in POSITIONS:
            val=0
            if j==k:val=F.add(val,mu.get((i,l),0))
            if l==i:val=F.sub(val,mu.get((k,j),0))
            row.append(val)
        M.append(row)
    return M

def predicted_rank(vals,F):
    a,b,c,d,e,f=vals
    if c:
        return 8 if F.sub(F.mul(b,e),F.mul(c,d)) else 6
    if b and e:
        return 8 if F.add(F.mul(a,e),F.mul(b,f)) else 6
    if b:return 6 if f else 4
    if e:return 6 if a else 4
    return 2*sum(v!=0 for v in (a,d,f))

def multiplicities(q):
    z=q-1
    return {0:1,2:3*z,4:2*q*q*z+3*z*z,
        6:3*q*q*z*z+z**3+z*q**4,
        8:q*q*z**3+z*z*q**4}

def central_formula(q,h):
    z=q-1
    A=(q**14+3*z*q**12+(2*q*q*z+3*z*z)*q**10 +
       (3*q*q*z*z+z**3)*q**8+q*q*z**3*q**6)
    B=z*q**4*q**8+z*z*q**4*q**6
    return A+B if h==0 else A-B//z

def mat_mul(A,B,F):
    return [[sum_terms([F.mul(A[i][k],B[k][j]) for k in range(4)],F) for j in range(4)] for i in range(4)]

def sum_terms(terms,F):
    val=0
    for t in terms:val=F.add(val,t)
    return val

def inspect():
    for q in (2,3,4,5):
        F=Field(q)
        observed=Counter()
        for t in product(range(q),repeat=6):
            r=rank(bracket_matrix(t,F),F)
            assert r==predicted_rank(t,F),(q,t,r,predicted_rank(t,F))
            observed[r]+=1
        assert observed==multiplicities(q),(q,observed,multiplicities(q))
        assert sum(observed.values())==q**6
        print('Kirillov ranks',q,dict(sorted(observed.items())))
    # Direct commutator linear systems: exhaust all A in T_4(F_2), solve [A,B]=C.
    F=Field(2)
    ms=[]
    for vals in product(range(2),repeat=10):
        X=[[0]*4 for _ in range(4)]
        for (i,j),v in zip(POSITIONS,vals):X[i][j]=v
        ms.append(X)
    basis=[]
    for i,j in POSITIONS:
        E=[[0]*4 for _ in range(4)];E[i][j]=1;basis.append(E)
    cc=Counter()
    for A in ms:
        cols=[]
        for E in basis:
            AB=mat_mul(A,E,F);BA=mat_mul(E,A,F)
            cols.append([F.sub(AB[i][j],BA[i][j]) for i,j in OFF])
        rows=[[cols[j][i] for j in range(10)] for i in range(6)]
        r=rank(rows,F)
        for h in (0,1):
            C=[0,0,h,0,0,0]
            if rank([row+[target] for row,target in zip(rows,C)],F)==r:
                cc[h]+=2**(10-r)
    for h in (0,1):
        assert cc[h]==central_formula(2,h),(h,cc[h],central_formula(2,h))
    print('Central commutator targets q=2',cc[0],cc[1])
    # Additional cross-check: Fourier rational sums yield positive integral counts.
    for q in (2,3,4,5,7,8,9,11):
        for h in (0,1):
            actual=central_formula(q,h)
            assert actual>0
            if h==0:
                assert actual==q**8*(q*q+q-1)*(q**4+5*q**3-3*q*q-4*q+2)
            else:
                assert actual==q**8*(q-1)*(q+1)*(q*q+q-1)*(q*q+4*q-2)
        assert central_formula(q,0)-central_formula(q,1)==q**11*(q*q+q-1)
    print('VERIFY_OK_BOREL4_CENTRAL_COMMUTATOR_RANKS')
if __name__=='__main__':inspect()
