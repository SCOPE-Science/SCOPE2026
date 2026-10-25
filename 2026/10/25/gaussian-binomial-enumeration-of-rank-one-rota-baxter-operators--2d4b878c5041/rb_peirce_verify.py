#!/usr/bin/env python3
"""Independent binary Peirce-corner count for upper triangular algebras."""
from math import comb

def gaussian(n,k,q):
    if k<0 or k>n:return 0
    if k==0 or k==n:return 1
    # Integer recurrence avoids non-integral intermediate arithmetic.
    tab=[[0]*(n+1) for _ in range(n+1)]
    for j in range(n+1):
        tab[j][0]=tab[j][j]=1
        for h in range(1,j):tab[j][h]=tab[j-1][h]+q**(j-h)*tab[j-1][h-1]
    return tab[n][k]

def rank_bits(vectors):
    basis={}
    for v in vectors:
        while v:
            bit=v.bit_length()-1
            if bit in basis:v^=basis[bit]
            else:basis[bit]=v;break
    return len(basis)

def eval_n(n):
    pairs=[(i,j) for i in range(n) for j in range(i,n)];d=len(pairs)
    def mat(z):
        a=[[0]*n for _ in range(n)]
        for k,(i,j) in enumerate(pairs):a[i][j]=(z>>k)&1
        return a
    def mult(a,b):return [[sum(a[i][t]*b[t][j] for t in range(i,j+1))%2 if i<=j else 0 for j in range(n)] for i in range(n)]
    def flat(a):return sum(a[i][j]<<k for k,(i,j) in enumerate(pairs))
    units=[]
    for i,j in pairs:
        u=[[0]*n for _ in range(n)];u[i][j]=1;units.append(u)
    identities=0;count=0;dist={}
    for x in range(1<<d):
        e=mat(x)
        if mult(e,e)!=e:continue
        identities+=1
        z=[[e[i][j]^(1 if i==j else 0) for j in range(n)] for i in range(n)]
        rl=rank_bits([flat(mult(mult(e,u),z)) for u in units])
        rr=rank_bits([flat(mult(mult(z,u),e)) for u in units])
        count+=(2**rl-1)+(2**rr-1)
        dist[tuple(e[i][i] for i in range(n))]=dist.get(tuple(e[i][i] for i in range(n)),0)+1
    prediction=2*sum(2**(k*(n-k))*(gaussian(n,k,2)-comb(n,k)) for k in range(1,n))
    assert count==prediction,(n,count,prediction)
    for diag,tally in dist.items():
        k=sum(diag)
        assert tally==2**(k*(n-k)),(diag,tally)
    print('n',n,'idempotents',identities,'rank_one_idempotent_image',count,'prediction',prediction,'OK')

if __name__=='__main__':
    for n in (2,3,4):eval_n(n)
    print('TRIANGULAR_PEIRCE_COUNTS_OK')
