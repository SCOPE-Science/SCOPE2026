"""Reproducibility checks for Gaussian negative type on Steiner 2-design incidence metrics.
Requires NumPy and SciPy. Exact incidence identities plus independent all-pairs shortest paths
and symmetric eigenspectra are checked for several nonisomorphic structures.
The general theorem uses a separate analytic proof; the finite tests are only corroboration.
"""
from itertools import combinations, product
from math import log2
import numpy as np
from scipy.sparse.csgraph import shortest_path
from scipy.sparse import csr_matrix


def sts13():
    v=13
    bases=((0,1,4),(0,2,7))
    return v,sorted({tuple(sorted((a+t)%v for a in B)) for B in bases for t in range(v)})

def affine9():
    q=3
    pts=list(product(range(q),repeat=2))
    id_of={p:i for i,p in enumerate(pts)}
    L=set()
    for dx,dy in [(1,0),(0,1),(1,1),(1,2)]:
        for p in pts:
            line=tuple(sorted(id_of[((p[0]+t*dx)%q,(p[1]+t*dy)%q)] for t in range(q)))
            L.add(line)
    return len(pts),sorted(L)

def pg32():
    pts=[x for x in range(1,16)]
    L=set()
    for a,b in combinations(pts,2):
        L.add(tuple(sorted((a-1,b-1,(a^b)-1))))
    return len(pts),sorted(L)

def edges(v):
    return v,list(combinations(range(v),2))

def check(name,datum):
    v,blocks=datum
    ell=len(blocks)
    k=len(blocks[0])
    assert k>=2 and ell>v
    r=(v-1)//(k-1)
    assert r*(k-1)+1==v
    assert ell*k==v*r
    M=np.zeros((v,ell),dtype=np.int64)
    for j,block in enumerate(blocks):
        assert len(block)==k and len(set(block))==k
        M[list(block),j]=1
    assert np.all(M.sum(axis=1)==r)
    assert np.all(M.sum(axis=0)==k)
    assert np.array_equal(M@M.T,(r-1)*np.eye(v,dtype=np.int64)+np.ones((v,v),dtype=np.int64))
    A=M.T@M-k*np.eye(ell,dtype=np.int64)
    assert np.all((A==0)|(A==1))
    assert np.all(A.sum(axis=1)==k*(r-1))
    n=v+ell
    adj=np.zeros((n,n),dtype=np.float64)
    adj[:v,v:]=M
    adj[v:,:v]=M.T
    d=shortest_path(csr_matrix(adj),directed=False,unweighted=True)
    expected=np.zeros((n,n),dtype=np.int64)
    expected[:v,:v]=2*(np.ones((v,v),dtype=np.int64)-np.eye(v,dtype=np.int64))
    expected[:v,v:]=3-2*M
    expected[v:,:v]=expected[:v,v:].T
    expected[v:,v:]=4*(np.ones((ell,ell),dtype=np.int64)-np.eye(ell,dtype=np.int64))-2*A
    assert np.array_equal(d,expected)
    p=log2(k/(k-1))
    H=np.eye(n)-np.ones((n,n))/n
    target_null=ell-v if k>=3 else ell-1
    for exponent,stage in ((p*.5,'strict'),(p,'endpoint'),(p+.07,'forbidden')):
        D=np.where(d==0,0.,d**exponent)
        G=-.5*H@D@H
        eig=np.linalg.eigvalsh((G+G.T)*.5)
        tol=3e-8
        null=int((abs(eig)<tol).sum())-1 # remove global-constant zero
        if stage=='strict':
            assert null==0,(name,stage,null)
            assert eig[0]>-tol
        elif stage=='endpoint':
            assert null==target_null,(name,stage,null,target_null)
            assert eig[0]>-tol
        else:
            assert eig[0]<-1e-5,(name,stage,eig[0])
        print('%s k=%d v=%d blocks=%d %s exponent=%.10f min=%.8f zero_sum_null=%d' % (name,k,v,ell,stage,exponent,eig[0],null))
    a=2**p;z=3**p
    assert abs((k-1)*a*a-k*a)<1e-12
    contrast=np.r_[np.ones(v),(-v/ell)*np.ones(ell)]
    real=float(contrast@np.where(d==0,0.,d**p)@contrast/v)
    algebra=-2*(k-1)*(r-1)*(z-1)+(r*(3*k-2)-(k*k+2*k-2))/(k-1)
    assert abs(real-algebra)<1e-8,(name,real,algebra)
    assert real<0
    if k>=3:
        assert z-1>(3*k-2)/(2*(k-1)**2)
        assert algebra < -k
    else:
        assert abs(real+2)<1e-8
    print('%s checked exact incidence, shortest paths, spectral ranks, contrast and endpoint bound.'%name)

def main():
    cases={'cyclic_STS13':sts13(),'affine_AG23':affine9(),'projective_PG32':pg32(),'all_pair_design_v4':edges(4),'all_pair_design_v6':edges(6)}
    for label,design in cases.items():check(label,design)
    print('PASS: all five independent sample designs, including the two endpoint-nullity regimes.')
if __name__=='__main__':main()
