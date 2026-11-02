#!/usr/bin/env python3
"""Independent finite-field verification of rectangular-band algebra commutator ranks."""
import itertools

POLY = {1:3,2:7}
def mul(x,y,s):
    if s==1: return x&y
    z=0
    while y:
        if y&1: z^=x
        x<<=1
        if x&4: x^=POLY[2]
        y>>=1
    return z

def rank_gf(M,s):
    a=[row[:] for row in M]
    m=len(a); n=len(a[0]); rank=0
    for c in range(n):
        pivot=next((i for i in range(rank,m) if a[i][c]),None)
        if pivot is None:continue
        a[rank],a[pivot]=a[pivot],a[rank]
        z=a[rank][c]; inv=next(t for t in range(1,1<<s) if mul(z,t,s)==1)
        a[rank]=[mul(inv,t,s) for t in a[rank]]
        for i in range(rank+1,m):
            if a[i][c]:
                z=a[i][c]
                a[i]=[x^mul(z,y,s) for x,y in zip(a[i],a[rank])]
        rank+=1
    return rank

def counts_formula(m,n,q):
    h=(m-1)*(n-1)
    W=q**(m+n-1)
    K=W+(q**(n-1)-1)*q**(n-1)+(q**(m-1)-1)*q**(m-1)+(W-q**(n-1)-q**(m-1)+1)*q
    def F0(l):return (q**(l-1)-1)*(q**(l-1)-q)
    def F1(l):return q**(l-1)*(q**(l-1)-1)
    N2=F0(m)*F0(n)+(q*q-1)*F1(m)*F1(n)
    N0=q**(2*h)*K
    N2*=q**(2*h)
    N1=q**(2*m*n)-N0-N2
    return [N0,N1,N2]

def direct(m,n,s):
    q=1<<s; vectors=list(itertools.product(range(q),repeat=m*n)); C=[0,0,0]
    for X in vectors:
        for Y in vectors:
            # Form the commutator by expanding the two independent semigroup products.
            R=[[0]*n for _ in range(m)]
            for i in range(m):
                for j in range(n):
                    for k in range(m):
                        for l in range(n):
                            R[i][l]^=mul(X[i*n+j],Y[k*n+l],s)
                            R[k][j]^=mul(Y[k*n+l],X[i*n+j],s)
            rk=rank_gf(R,s)
            assert rk in range(3)
            C[rk]+=1
    expected=counts_formula(m,n,q)
    assert C==expected,(m,n,q,C,expected)
    print('PASS',f'm={m}',f'n={n}',f'q={q}', 'rank_counts='+str(C))
    return C

def main():
    cases=[(1,1,1),(1,2,1),(2,1,1),(2,2,1),(2,2,2),(2,3,1),(3,2,1),(3,3,1)]
    for params in cases:direct(*params)
    print('RECTANGULAR_BAND_COMMUTATOR_OK',len(cases),'complete enumerations')

if __name__=='__main__':main()
