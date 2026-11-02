#!/usr/bin/env python3
"""Independent exact local extension check for the three-sorted Latin incidence signature."""
from itertools import product

def all_reduced(n):
    a=[[-1]*n for _ in range(n)]
    for i in range(n): a[i][0]=i; a[0][i]=i
    row=[1<<i for i in range(n)]; col=[1<<i for i in range(n)]
    row[0]=(1<<n)-1;col[0]=(1<<n)-1
    def rec(k):
        if k==(n-1)*(n-1):
            yield tuple(tuple(z) for z in a);return
        r=1+k//(n-1);c=1+k%(n-1)
        for sym in range(n):
            mask=1<<sym
            if row[r]&mask or col[c]&mask:continue
            a[r][c]=sym; row[r]|=mask;col[c]|=mask
            yield from rec(k+1)
            a[r][c]=-1;row[r]^=mask;col[c]^=mask
    yield from rec(0)

def group(n,operation):
    return tuple(tuple(operation(r,c) for c in range(n)) for r in range(n))

def signature(vec,L,n):
    ss=tuple(x//n for x in vec)
    eq=tuple(int(vec[i]==vec[j]) for i in range(len(vec)) for j in range(i+1,len(vec)))
    m=tuple(int(L[vec[i]][vec[j]-n]==vec[h]-2*n)
         for i in range(len(vec)) if ss[i]==0
         for j in range(len(vec)) if ss[j]==1
         for h in range(len(vec)) if ss[h]==2)
    return ss,eq,m

def extension_map(L):
    n=len(L); domain=range(3*n); e={}
    for t in product(domain,repeat=3):
        a=signature(t,L,n)
        ex=frozenset(signature(t+(x,),L,n) for x in domain)
        if a in e:assert e[a]==ex,('not 3-homogeneous for depth 1',a)
        else:e[a]=ex
    return e

def asymmetric_rectangle(L):
    n=len(L)
    return [(r,rp,c,cp) for r in range(n) for rp in range(n) if r!=rp
            for c in range(n) for cp in range(n) if c!=cp
            if L[r][c]==L[rp][cp] and L[r][cp]!=L[rp][c]]

if __name__=='__main__':
    four=list(all_reduced(4)); five=list(all_reduced(5))
    assert len(four)==4,(len(four),'wrong reduced order-4 census')
    assert len(five)==56,(len(five),'wrong reduced order-5 census')
    base=extension_map(four[0]);checked=0
    for n,Ls in ((4,four),(5,five)):
        for L in Ls:
            em=extension_map(L)
            assert em==base,(n,L,'extension mismatch')
            checked+=1
    c4=group(4,lambda x,y:(x+y)%4)
    v4=group(4,lambda x,y:x^y)
    z5=group(5,lambda x,y:(x+y)%5)
    assert extension_map(c4)==base
    assert extension_map(v4)==base
    assert extension_map(z5)==base
    c4wit=asymmetric_rectangle(c4)
    v4wit=asymmetric_rectangle(v4)
    assert c4wit and not v4wit
    print('reduced counts n=4,5:',len(four),len(five))
    print('triple atomic types:',len(base))
    print('universal one-point atomic extension spectra identical across',checked,'reduced squares')
    print('C4, V4, Z5 have the same one-point extension spectra: YES')
    print('rank-five asymmetric rectangle: C4 YES ('+str(len(c4wit))+' ordered witnesses), V4 NO')
    print('sample C4 rows/columns witness:',c4wit[0])
