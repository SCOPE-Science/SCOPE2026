#!/usr/bin/env python3
"""Finite-field checks for tensor-order Rota-Baxter square-zero factor theorem.
Run: python3 verify.py
"""
from itertools import product

def rank(mat, p):
    a=[list(map(lambda z:z%p, row)) for row in mat]
    if not a:return 0
    nr=len(a); nc=len(a[0]); pivot=0
    for col in range(nc):
        idx=next((i for i in range(pivot,nr) if a[i][col]),None)
        if idx is None: continue
        a[pivot],a[idx]=a[idx],a[pivot]
        inv=pow(a[pivot][col],-1,p)
        a[pivot]=[(inv*z)%p for z in a[pivot]]
        for i in range(nr):
            if i!=pivot:
                scale=a[i][col]
                a[i]=[(x-scale*y)%p for x,y in zip(a[i],a[pivot])]
        pivot+=1
        if pivot==nr:break
    return pivot

def mulmat(A,B,p):
    return [[sum(A[i][k]*B[k][j] for k in range(len(B)))%p for j in range(len(B[0]))] for i in range(len(A))]

def addvec(a,b,p): return [(x+y)%p for x,y in zip(a,b)]
def scalevec(a,c,p):return [c*x%p for x in a]

def check(m,n,Q,R,p,lam,expected_rank=None):
    d=1+m+n+m*n
    U=range(1,1+m); W=range(1+m,1+m+n)
    T=lambda i,j:1+m+n+i*n+j
    basis=[[int(i==j) for i in range(d)] for j in range(d)]
    def multiplication(x,y):
        out=[(x[0]*y[k]+y[0]*x[k])%p for k in range(d)];out[0]=x[0]*y[0]%p
        for i in range(m):
            for j in range(n):out[T(i,j)]=(out[T(i,j)]+x[1+i]*y[1+m+j]+y[1+i]*x[1+m+j])%p
        return out
    def makeP(reverse):
        P=[[0]*d for _ in range(d)]
        for i in range(m):
            for k in range(m):P[1+k][1+i]=Q[k][i]%p
        for j in range(n):
            for k in range(n):P[1+m+k][1+m+j]=R[k][j]%p
        for i in range(m):
            for j in range(n):
                if reverse:
                    for k in range(m):P[T(k,j)][T(i,j)]=Q[k][i]%p
                else:
                    for k in range(n):P[T(i,k)][T(i,j)]=R[k][j]%p
        return P
    def apply(P,x):return [sum(P[i][j]*x[j] for j in range(d))%p for i in range(d)]
    assert all(all(x==0 for x in row) for row in [[(z+lam*y)%p for z,y in zip(a,b)] for a,b in zip(mulmat(Q,Q,p),Q)])
    assert all(all(x==0 for x in row) for row in [[(z+lam*y)%p for z,y in zip(a,b)] for a,b in zip(mulmat(R,R,p),R)])
    vals=[]
    for reverse in (False,True):
        P=makeP(reverse);r=rank(P,p);vals.append(r)
        assert all((mulmat(P,P,p)[i][j]+lam*P[i][j])%p==0 for i in range(d) for j in range(d))
        for x,y in product(basis,repeat=2):
            Px,Py=apply(P,x),apply(P,y)
            lhs=multiplication(Px,Py)
            rhs=apply(P,addvec(addvec(multiplication(Px,y),multiplication(x,Py),p),scalevec(multiplication(x,y),lam,p),p))
            assert lhs==rhs,(m,n,p,lam,reverse,x,y)
        for i in range(m):
            for j in range(n):
                # verify triple products vanish (radical cube zero)
                assert multiplication(multiplication(basis[1+i],basis[1+m+j]),basis[1+i])==[0]*d
    rQ=rank(Q,p);rR=rank(R,p)
    assert vals==[rQ+(m+1)*rR,rR+(n+1)*rQ]
    if expected_rank is not None:assert vals==[expected_rank,expected_rank]
    print('OK',{'dim':d,'m':m,'n':n,'p':p,'lambda':lam,'rankQ':rQ,'rankR':rR,'tensorRanks':vals})

def zero(m,n):return [[0]*n for _ in range(m)]

def weight0(p):
    Q=zero(2,2); Q[1][0]=1
    R=zero(4,4); R[1][0]=R[3][2]=1
    check(2,4,Q,R,p,0,7)
    # A conjugate pair of square-zero operators with equal dimensions and rank
    Q2=zero(2,2);Q2[1][0]=1
    R2=zero(2,2);R2[0][1]=1
    check(2,2,Q2,R2,p,0,4)
    check(1,2,zero(1,1),zero(2,2),p,0,0)

def weight1(p):
    lam=1
    Q=zero(2,2);Q[0][0]=p-1
    R=zero(4,4);R[0][0]=R[1][1]=p-1
    check(2,4,Q,R,p,lam,7)
    Q2=zero(2,2);Q2[0][0]=p-1
    R2=zero(2,2);R2[1][1]=p-1
    check(2,2,Q2,R2,p,lam,4)
    Qa=zero(1,1);Qa[0][0]=p-1
    Ra=zero(2,2);Ra[0][0]=Ra[1][1]=p-1
    check(1,2,Qa,Ra,p,lam,5)

if __name__=='__main__':
    for p in (3,5,7):weight0(p);weight1(p)
    print('VERIFY_OK')
