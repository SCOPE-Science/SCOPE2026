#!/usr/bin/env python3
"""Exact moment certificates and independent numerical spectral checks for a marked cycle."""

def adjacency(n, potential=0):
    h = [[0]*n for _ in range(n)]
    for j in range(n):
        k=(j+1)%n
        h[j][k]=h[k][j]=1
    h[0][0]=potential
    return h


def matmul(a,b):
    n=len(a)
    c=[[0]*n for _ in range(n)]
    for i in range(n):
        for k in range(n):
            v=a[i][k]
            if v:
                for j in range(n):
                    c[i][j]+=v*b[k][j]
    return c


def det_bareiss(a):
    a=[list(row) for row in a]
    n=len(a)
    sign=1; prev=1
    for k in range(n-1):
        if a[k][k]==0:
            idx=next((j for j in range(k+1,n) if a[j][k]!=0), None)
            if idx is None:return 0
            a[k],a[idx]=a[idx],a[k];sign=-sign
        pivot=a[k][k]
        for i in range(k+1,n):
            for j in range(k+1,n):
                num=a[i][j]*pivot-a[i][k]*a[k][j]
                assert num%prev==0, (num,prev)
                a[i][j]=num//prev
            a[i][k]=0
        prev=pivot
    return sign*a[-1][-1]


def moment_witness(n,t):
    m=n//2
    h=adjacency(n,t)
    a=adjacency(n,0)
    cols=[]
    # direct evolution, caching all odd powers
    ph=[[int(i==j) for j in range(n)] for i in range(n)]
    pa=[[int(i==j) for j in range(n)] for i in range(n)]
    for k in range(1,2*m,1):
        ph=matmul(ph,h);pa=matmul(pa,a)
        if k%2:
            c=pa[0][0]
            assert all(pa[j][j]==c for j in range(n))
            cols.append([ph[r][r]-c for r in range(m+1)])
    assert len(cols)==m
    witness=[[1]+[col[r] for col in cols] for r in range(m+1)]
    d=det_bareiss(witness)
    assert d==(-1)**m*t**m,(n,t,d)
    for r in range(m):
        assert cols[r][r]==t,(n,t,r,cols[r][r])
        for s in range(r):assert cols[s][r]==0
    assert all(col[m]==0 for col in cols)
    return d


def test():
    exact=0
    for n in range(3,23):
        for t in (-3,-1,1,2):
            moment_witness(n,t)
            exact+=1
    print('EXACT_WITNESS_OK',exact)
    try:
        import numpy as np
    except ImportError:
        print('NUMPY_UNAVAILABLE; exact tests passed')
        return
    nums=0;entries=0
    for n in range(3,19):
        for t in (0,-2.,-0.75,0.25,1.,3.):
            h=np.array(adjacency(n,t),dtype=float)
            lam,vec=np.linalg.eigh(h)
            groups=[]
            for j,v in enumerate(lam):
                if groups and abs(v-lam[groups[-1][0]])<1e-8:
                    groups[-1].append(j)
                else:
                    groups.append([j])
            assert t==0 or len(groups)==n
            mix=np.zeros((n,n))
            for idx in groups:
                p=vec[:,idx]@vec[:,idx].T
                mix+=p*p
            expect=n if n%2 else n//2
            if t!=0:expect=n//2+1
            got=int(np.linalg.matrix_rank(mix,tol=5e-9))
            assert got==expect,(n,t,got,expect)
            assert np.max(abs(mix.sum(axis=1)-1))<1e-9
            assert np.max(abs(mix-mix.T))<1e-9
            if t==0:
                ones=np.ones((n,n))
                if n%2:
                    expected=(n-1)/n**2*ones+np.eye(n)/n
                else:
                    p=np.zeros((n,n))
                    for j in range(n):p[j,(j+n//2)%n]=1
                    expected=(n-2)/n**2*ones+(np.eye(n)+p)/n
                assert np.max(abs(mix-expected))<1e-9
            nums+=1;entries+=n*n
    print(f'VERIFY_OK exact_witness_profiles={exact} numerical_spectral_profiles={nums} numerical_entries={entries} moment_det=(-1)^floor(n/2)*potential^floor(n/2)')
if __name__=='__main__':test()
