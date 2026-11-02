"""Reproduce exact balanced-cut ranks for generalized Petersen graph states.

Requires Python 3.10+. Optional `--spectra` uses NumPy for independent
small-dimensional coefficient-matrix singular-value tests.
"""
import argparse
import math
import cmath
from itertools import product


def rank_mod_p(matrix, p):
    rows = [[v % p for v in row] for row in matrix]
    if not rows: return 0
    nr, nc = len(rows), len(rows[0])
    i = 0
    for j in range(nc):
        t = next((r for r in range(i, nr) if rows[r][j] % p), None)
        if t is None: continue
        rows[i], rows[t] = rows[t], rows[i]
        inv = pow(rows[i][j], -1, p)
        rows[i] = [(v*inv)%p for v in rows[i]]
        for r in range(nr):
            if r != i and rows[r][j]:
                factor = rows[r][j]
                rows[r] = [(v-factor*w)%p for v,w in zip(rows[r],rows[i])]
        i+=1
        if i==nr: break
    return i


def cut_matrix(m,k):
    """Independent graph-edge construction, not the circulant proof block."""
    n=2*m
    assert 1 <= k < m and m >= 2
    vertices_a = [i for i in range(0,n,2)] + [n+i for i in range(1,n,2)]
    vertices_b = [i for i in range(1,n,2)] + [n+i for i in range(0,n,2)]
    where={v:i for i,v in enumerate(vertices_b)}
    adjacency=[set() for _ in range(2*n)]
    def connect(x,y):
        assert x != y
        adjacency[x].add(y);adjacency[y].add(x)
    for i in range(n):
        connect(i,(i+1)%n)
        connect(i,n+i)
        connect(n+i,n+(i+k)%n)
    return [[int(j in adjacency[i]) for j in vertices_b] for i in vertices_a]


def trim(a,p):
    a=[v%p for v in a]
    while a and a[-1]==0: a.pop()
    return a


def rem(a,b,p):
    a=trim(a,p);b=trim(b,p)
    assert b
    ib=pow(b[-1],-1,p)
    while len(a)>=len(b):
        coeff=a[-1]*ib%p
        off=len(a)-len(b)
        for j,v in enumerate(b):a[off+j]=(a[off+j]-coeff*v)%p
        a=trim(a,p)
    return a


def poly_gcd(a,b,p):
    a,b=trim(a,p),trim(b,p)
    while b: a,b=b,rem(a,b,p)
    if a:
        scale=pow(a[-1],-1,p)
        a=[v*scale%p for v in a]
    return a


def predicted_rank(m,k,p):
    if k%2==0: return 2*m
    f=[0]*(k+2)
    for power, coeff in [(k+1,1),(k,1),(1,1),(0,1),((k+1)//2,-1)]:
        f[power] = (f[power]+coeff)%p
    cycle=[0]*(m+1)
    cycle[0]=-1; cycle[m]=1
    return 2*m-(len(poly_gcd(f,cycle,p))-1)


def explicit_k5_defect(m,p):
    assert m>=6 and p in (2,3)
    if p==2:
        if m%3: return 0
        t=0;v=m
        while v%2==0: v//=2;t+=1
        return 2*min(3,2**t)
    t=0;v=m
    while v%3==0: v//=3;t+=1
    return min(2,3**t) * (1+2*int(m%4==0))


def check_spectrum(m,k,p):
    import numpy as np
    C=np.array(cut_matrix(m,k), dtype=np.int64)
    q=p**(2*m)
    assert q<=1000
    # A and B basis enumeration. Cross-phases suffice because internal-edge
    # phases change the coefficient matrix only by diagonal unitaries.
    z=np.array(list(product(range(p),repeat=2*m)), dtype=np.int64)
    phase=(z@C@z.T)%p
    wave=np.exp(2j*np.pi*phase/p)/q
    singular=np.linalg.svd(wave,compute_uv=False)
    lam=np.sort((singular**2))[::-1]
    r=predicted_rank(m,k,p)
    spec=np.array([p**(-r)]*(p**r)+[0.]*(q-p**r))
    assert np.max(np.abs(lam-spec)) < 1e-10, (m,k,p,lam[:10],spec[:10])
    return float(np.max(np.abs(lam-spec)))


def run(spectra=False):
    tested=0;examples=[]
    for p in (2,3,5,7):
        for m in range(2,31):
            for k in range(1,m):
                B=cut_matrix(m,k)
                rank=rank_mod_p(B,p)
                predicted=predicted_rank(m,k,p)
                assert rank==predicted, (m,k,p,rank,predicted)
                if k==5 and p in (2,3):
                    assert 2*m-rank==explicit_k5_defect(m,p)
                if p==3 and k%2==1:assert rank<2*m
                if k%2==0:assert rank==2*m
                tested+=1
    # The explicit two-adic and ternary formulas are checked beyond the graph-matrix range.
    for m in range(6,300):
        for p in (2,3):
            assert 2*m-predicted_rank(m,5,p)==explicit_k5_defect(m,p)
    if spectra:
        for m,k,p in [(2,1,2),(3,1,2),(4,1,2),(2,1,3),(3,2,2)]:
            examples.append([m,k,p,check_spectrum(m,k,p)])
    print('PASS direct ranks vs independently computed polynomial gcd:',tested)
    print('PASS characteristic-three rank deficit, even-step maximality, and k=5 staircase')
    print('PASS k=5 formulas through m=299 for p=2 and p=3')
    if spectra: print('PASS direct spectra:',examples)

if __name__=='__main__':
    parser=argparse.ArgumentParser()
    parser.add_argument('--spectra',action='store_true')
    opts=parser.parse_args()
    run(opts.spectra)
