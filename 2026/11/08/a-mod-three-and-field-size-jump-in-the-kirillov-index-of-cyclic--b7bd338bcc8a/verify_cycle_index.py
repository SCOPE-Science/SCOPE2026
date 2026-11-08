#!/usr/bin/env python3
"""Independent finite-field tests for the cyclic graph-Lie Kirillov theorem.
Uses explicit published Lie brackets and Gaussian elimination, not determinant factorization.
"""
from itertools import product

class Field:
    def __init__(self,q):
        assert q in (2,3,4,5)
        self.q=q
    def add(self,a,b):
        return a^b if self.q==4 else (a+b)%self.q
    def neg(self,a):
        return a if self.q==4 else (-a)%self.q
    def sub(self,a,b):
        return self.add(a,self.neg(b))
    def mul(self,a,b):
        if self.q!=4: return a*b%self.q
        # F4=F2[z]/(z^2+z+1), 2 is z.
        out=0
        for i in range(2):
            for j in range(2):
                if (a>>i)&1 and (b>>j)&1:
                    k=i+j
                    out ^= {0:1,1:2,2:3}[k]
        return out
    def inv(self,a):
        assert a
        for v in range(1,self.q):
            if self.mul(a,v)==1: return v
        raise ValueError('noninvertible')

def rank(M,F):
    A=[r[:] for r in M]; h=len(A); w=len(A[0]); pivotrow=0
    for col in range(w):
        r=next((i for i in range(pivotrow,h) if A[i][col]),None)
        if r is None: continue
        A[pivotrow],A[r]=A[r],A[pivotrow]
        v=F.inv(A[pivotrow][col]); A[pivotrow]=[F.mul(v,x) for x in A[pivotrow]]
        for k in range(pivotrow+1,h):
            factor=A[k][col]
            if factor:
                A[k]=[F.sub(A[k][j],F.mul(factor,A[pivotrow][j])) for j in range(w)]
        pivotrow+=1
        if pivotrow==h:break
    return pivotrow

def kirillov(n,F,t,edge_values=None):
    assert n>=3 and len(t)==n
    e=edge_values if edge_values is not None else [0]*n
    K=[[0]*(2*n) for _ in range(2*n)]
    def put(i,j,a):
        K[i][j]=F.add(K[i][j],a)
        K[j][i]=F.sub(K[j][i],a)
    if n==3:
        # Ordered edges (01),(02),(12), central paths (012),(021),(102).
        put(0,1,e[0]);put(0,2,e[1]);put(1,2,e[2])
        put(0,3+2,F.sub(t[0],t[1])) # [v0,a12]
        put(1,3+1,F.sub(t[2],t[1])) # [v1,a02]
        put(2,3+0,F.sub(t[2],t[0])) # [v2,a01]
    else:
        for i in range(n):
            put(i,(i+1)%n,e[i])
            # w_i=[x_i,a_{i+1}]=[a_i,x_{i+2}].
            put(i,n+(i+1)%n,t[i])
            put((i+2)%n,n+i,F.neg(t[i]))
    return K

def predicted_index(n,q):
    return n if n%3==0 and q>=3 else n+2

def prod(a,F):
    v=1
    for x in a:v=F.mul(v,x)
    return v

def fullrank_count_formula(n,q):
    if n%3:return 0
    m=n//3
    a=q**m-(q-1)**m
    b=(q-1)**(m-1)
    return 3*(q-1)*(q-2)*a*b*b+(q-1)*(q-2)*(q-3)*b*b*b

def witness(n,F):
    if n%3==0:
        ts=[1]*n;ts[0]=0
        if F.q>=3:ts[2]=2
        return ts
    return [1]*n

def main():
    witness_count=0; exhaustive_t=0; exhaustive_full=0; complete_form_tests=0
    for q in (2,3,4,5):
        F=Field(q)
        for n in range(3,19):
            t=witness(n,F)
            kr=rank(kirillov(n,F,t),F)
            assert kr==3*n-predicted_index(n,q),(n,q,kr,predicted_index(n,q))
            witness_count+=1
        for n in range(3,7 if q<=3 else 6):
            full=0;maxrank=0
            for t in product(range(q),repeat=n):
                kr=rank(kirillov(n,F,t),F)
                maxrank=max(maxrank,kr)
                full+=(kr==2*n)
                exhaustive_t+=1
            assert maxrank==3*n-predicted_index(n,q),(q,n,maxrank)
            assert full==fullrank_count_formula(n,q),(q,n,full,fullrank_count_formula(n,q))
            exhaustive_full+=full
            print('exact_t_field',q,'n',n,'total',q**n,'maxrank',maxrank,'fullcentral',full)
    for q,n in ((2,3),(2,4),(2,5),(2,6),(3,3),(3,4)):
        F=Field(q)
        maxrank=0
        for t in product(range(q),repeat=n):
            for e in product(range(q),repeat=n):
                kr=rank(kirillov(n,F,t,e),F)
                maxrank=max(maxrank,kr); complete_form_tests+=1
        assert maxrank==3*n-predicted_index(n,q),(q,n,maxrank)
    print('VERIFY_OK',f'witnesses={witness_count}',f'exhaustive_central_assignments={exhaustive_t}',f'fullcentral_assignments={exhaustive_full}',f'exhaustive_all_noncentral_forms={complete_form_tests}', 'n_witness=3..18','fields=2,3,4,5')
if __name__=='__main__': main()
