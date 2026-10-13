"""Exhaustive checks of the two-by-two Sylvester nullity distribution.
Usage: python verify_sylvester.py
"""
from itertools import product
from collections import Counter

def rank_mod(a,p):
    a=[list(row) for row in a];rows=len(a);cols=len(a[0]);r=0
    for c in range(cols):
        pivot=next((i for i in range(r,rows) if a[i][c]%p),None)
        if pivot is None:continue
        a[r],a[pivot]=a[pivot],a[r]
        k=pow(a[r][c],-1,p)
        a[r]=[(v*k)%p for v in a[r]]
        for i in range(rows):
            if i!=r and a[i][c]%p:
                k=a[i][c]
                a[i]=[(a[i][j]-k*a[r][j])%p for j in range(cols)]
        r+=1
        if r==rows:break
    return r

def calc(a,b,p):
    # vectorization of X by row-major order: (00,01,10,11)
    cols=[]
    for i in range(2):
      for j in range(2):
        x=[[0,0],[0,0]];x[i][j]=1
        w=[]
        for u in range(2):
          for v in range(2):
            w.append((sum(a[2*u+k]*x[k][v] for k in range(2))-
                      sum(x[u][k]*b[2*k+v] for k in range(2)))%p)
        cols.append(w)
    mat=[[cols[j][i] for j in range(4)] for i in range(4)]
    return 4-rank_mod(mat,p)

def expected(q):
    n1=q*q*(q-1)*(q+1)**2*(q*q-2)
    n2=q*(q-1)*(q**4+q**3+4*q*q+3*q+1)
    n4=q
    n0=q**8-n1-n2-n4
    return {0:n0,1:n1,2:n2,4:n4}

if __name__=='__main__':
 for p in (2,3,5):
    matrices=list(product(range(p),repeat=4))
    counter=Counter(calc(a,b,p) for a in matrices for b in matrices)
    assert set(counter).issubset({0,1,2,4}),counter
    assert dict(counter)==expected(p),(p,counter,expected(p))
    print('PASS',p,dict(counter))

def gf4mul(x,y):
    z=0
    while y:
        if y & 1: z ^= x
        y >>= 1
        x <<= 1
        if x & 4: x ^= 7
    return z

def rank4(a):
    a=[r[:] for r in a];r=0
    inverse={1:1,2:3,3:2}
    for c in range(len(a[0])):
        t=next((i for i in range(r,len(a)) if a[i][c]),None)
        if t is None: continue
        a[r],a[t]=a[t],a[r]
        inv=inverse[a[r][c]]
        a[r]=[gf4mul(inv,v) for v in a[r]]
        for k in range(len(a)):
            if k!=r and a[k][c]:
                v=a[k][c]
                a[k]=[u^gf4mul(v,w) for u,w in zip(a[k],a[r])]
        r+=1
        if r==len(a):break
    return r

def calc4(a,b):
    cols=[]
    for i in range(2):
      for j in range(2):
        x=[[0,0],[0,0]];x[i][j]=1;w=[]
        for u in range(2):
          for v in range(2):
            w.append((gf4mul(a[2*u],x[0][v]) ^ gf4mul(a[2*u+1],x[1][v]) ^
                      gf4mul(x[u][0],b[v]) ^ gf4mul(x[u][1],b[2+v])))
        cols.append(w)
    return 4-rank4([[cols[j][i] for j in range(4)] for i in range(4)])

if __name__=='__main__':
    matrices4=list(product(range(4),repeat=4))
    counter4=Counter(calc4(a,b) for a in matrices4 for b in matrices4)
    assert dict(counter4)==expected(4),(counter4,expected(4))
    print('PASS 4',dict(counter4))
    print('VERIFY_OK')
