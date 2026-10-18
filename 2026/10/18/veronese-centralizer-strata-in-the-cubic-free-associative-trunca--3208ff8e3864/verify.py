from itertools import product
from collections import Counter

def basis_words():
    return [()] + [(a,) for a in (0,1)] + list(product(range(2),repeat=2)) + list(product(range(2),repeat=3))
W=basis_words(); idx={w:i for i,w in enumerate(W)}

def matrix(v,p):
    A=[[0]*len(W) for _ in W]
    for i,c in enumerate(v):
        if not c: continue
        for j,w in enumerate(W):
            if len(W[i])+len(w)>=4:continue
            u=W[i]+w; z=w+W[i]
            A[idx[u]][j]=(A[idx[u]][j]+c)%p
            A[idx[z]][j]=(A[idx[z]][j]-c)%p
    return A

def rank(A,p):
    A=[r[:] for r in A]
    i=0
    for j in range(len(A[0])):
        if i>=len(A):break
        piv=next((u for u in range(i,len(A)) if A[u][j]%p),None)
        if piv is None:continue
        A[i],A[piv]=A[piv],A[i]
        v=pow(A[i][j],-1,p)
        A[i]=[(z*v)%p for z in A[i]]
        for u in range(i+1,len(A)):
            if A[u][j]:
                v=A[u][j]
                A[u]=[(a-v*b)%p for a,b in zip(A[u],A[i])]
        i+=1
    return i

for p in (2,3,5,7):
    counts=Counter()
    for cs in product(range(p),repeat=6):
        v=[0]+list(cs)+[0]*8
        counts[rank(matrix(v,p),p)]+=1
    expected={0:1,1:p*p-1,2:p**4-p*p,4:p**4*(p*p-1)}
    assert counts==expected,(p,counts,expected)
    print(p,'parameterized rank histogram',dict(counts),'OK')
