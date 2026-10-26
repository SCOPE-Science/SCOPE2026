from math import comb
from itertools import product

def partitions(n):
    # restricted-growth strings
    if n == 0:
        yield ()
        return
    def gen(a,m):
        if len(a)==n:
            yield tuple(a)
            return
        for j in range(m+2):
            a.append(j)
            yield from gen(a,max(m,j))
            a.pop()
    yield from gen([0],0)

def connected(ps,n):
    par=list(range(n))
    def find(x):
        while par[x]!=x:
            par[x]=par[par[x]]
            x=par[x]
        return x
    for p in ps:
        root={}
        for i,block in enumerate(p):
            if block in root:
                a=find(i);b=find(root[block]);par[a]=b
            else:root[block]=i
    return len({find(i) for i in range(n)})==1

B=[1]
for n in range(1,16):
    B.append(sum(comb(n-1,k)*B[k] for k in range(n)))
for r in (2,3):
    C=[0]*(len(B))
    for n in range(1,len(B)):
        C[n]=B[n]**r-sum(comb(n-1,k-1)*C[k]*B[n-k]**r for k in range(1,n))
    for n in range(1,6):
        pts=list(partitions(n))
        tot=0
        for ps in product(pts,repeat=r):
            tot+=connected(ps,n)
        assert tot==C[n],(n,r,tot,C[n])
    print('EXHAUSTIVE_CONNECTIVITY_OK',r,[(n,C[n],B[n]**r) for n in range(1,6)])
    for n in (6,8,10,12,15):
        deficit=(B[n]**r-C[n])/(B[n]**r)
        lam=n*(B[n-1]/B[n])**r
        print('n,r,deficit,lambda,ratio',n,r,round(deficit,9),round(lam,9),round(deficit/lam,9))
print('PARTITION_JOIN_CHECK_OK')
