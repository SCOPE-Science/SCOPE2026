"""Direct finite-field linear-algebra checks for the prime-alphabet injective-word operator."""
from itertools import permutations
from math import factorial
import numpy as np

def words(n):
    return [w for j in range(n+1) for w in permutations(range(n),j)]

def prod(a,w):
    s=set(a)
    return a + tuple(c for c in w if c not in s)

def rank_mod(A,p):
    B=np.array(A,dtype=np.int64,copy=True)%p
    m,n=B.shape
    row=0
    for col in range(n):
        hits=np.flatnonzero(B[row:,col])
        if hits.size==0:continue
        h=row+int(hits[0]);B[[row,h]]=B[[h,row]]
        inv=pow(int(B[row,col]),-1,p)
        B[row,col:]=(B[row,col:]*inv)%p
        j=np.flatnonzero(B[row+1:,col])+row+1
        if j.size:
            B[j,col:]=(B[j,col:]-B[j,col,None]*B[row,col:])%p
        row+=1
        if row==m:break
    return row

def check(n,p):
    ws=words(n);d=len(ws); ix={w:i for i,w in enumerate(ws)}
    X=np.zeros((d,d),dtype=np.int64)
    for j,w in enumerate(ws):
        for a in range(n):X[ix[prod((a,),w)],j]+=1
    X%=p
    J=X.copy()
    for _ in range(p-1):J=(J@X)%p
    Delta=(J-X)%p
    R=rank_mod(Delta,p)
    assert R==1,(n,p,'defect rank',R)
    assert np.array_equal((Delta@Delta)%p,np.zeros_like(X))
    # The product annihilator identity for the first collision
    f=(J@X-X@X)%p
    assert not np.any(f),(n,p,'wrong f annihilator')
    # derive all eigenspace generalized dimensions from ranks of (X-aI), (X-aI)^2
    I=np.eye(d,dtype=np.int64)
    ranks={}
    for a in range(p):
        D=(X-a*I)%p
        if a==0:
            r1=rank_mod(D,p);r2=rank_mod(D@D,p)
            ranks[a]=(r1,r2)
            assert d-r1==factorial(p),(n,p,'zero eigenspace',d-r1)
            assert d-r2==factorial(p)+1,(n,p,'generalized zero',d-r2)
        else:
            r1=rank_mod(D,p)
            ranks[a]=r1
            assert d-r1==factorial(p)//factorial(a),(n,p,a,d-r1)
    print('PASS', 'alphabet',n,'characteristic',p,'matrix_dimension',d,'rank_delta',R,'kernel_data',ranks)

if __name__=='__main__':
    for p in (2,3,5): check(p,p)
    print('VERIFY_OK_MODULAR_FIRST_COLLISION')
