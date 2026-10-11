"""Exact checks of the Fourier certificates for radius-three Hamming balls.

No external dependencies. Python 3.9+.
"""
from fractions import Fraction as Q
from itertools import combinations
from math import comb


def wt(n):
    return n.bit_count()


def spectral(d, kind, parameter=None):
    """Dictionary of exact Walsh eigenvalues indexed by binary frequencies."""
    out=[]
    for y in range(1<<d):
        S=d-2*wt(y)
        if kind=='odd_radial':
            out.append(Q((S+d)*(S*S-1),d*(d-1)))
        elif kind=='odd_vertex':
            j=parameter
            s=1 if not (y>>j)&1 else -1
            out.append(Q((S*S-1)*(1+s),d-1))
        elif kind=='even':
            alpha=parameter
            out.append(Q((S+d)*S*(S-alpha),d*(d-alpha)))
        else:
            raise ValueError(kind)
    return out


def invert_walsh(d, values):
    arr=values[:]
    N=1<<d
    step=1
    while step<N:
        for b in range(0,N,2*step):
            for i in range(b,b+step):
                a,v=arr[i],arr[i+step]
                arr[i],arr[i+step]=a+v,a-v
        step*=2
    return [v/N for v in arr]


def rank_mod(mat, prime=1000003):
    n=len(mat);m=len(mat[0]);A=[[x%prime for x in row] for row in mat]
    r=0
    for c in range(m):
        pivot=next((i for i in range(r,n) if A[i][c]),None)
        if pivot is None:continue
        A[r],A[pivot]=A[pivot],A[r]
        inv=pow(A[r][c],-1,prime)
        for j in range(c,m):A[r][j]=A[r][j]*inv%prime
        for i in range(r+1,n):
            mul=A[i][c]
            if mul:
                for j in range(c,m):A[i][j]=(A[i][j]-mul*A[r][j])%prime
        r+=1
        if r==n:break
    return r


def check_formula(d,typ,par,target):
    F=spectral(d,typ,par)
    assert min(F)>=0
    f=invert_walsh(d,F)
    assert f[0]==1,(d,typ,par,f[0])
    assert F[0]==target,(d,typ,par,F[0])
    assert sum(f)==target
    assert all(f[x]==0 for x in range(1<<d) if wt(x)>3)
    return len([x for x in f if x])

if __name__=='__main__':
    tests=0
    for d in range(3,12):
        target=2*(d+1) if d%2 else 2*d
        if d%2:
            tests+=1
            check_formula(d,'odd_radial',None,target)
            if d>=5:
                for i in range(d):
                    check_formula(d,'odd_vertex',i,target);tests+=1
        else:
            for alpha in [-2,0,2]:
                check_formula(d,'even',alpha,target);tests+=1
        # Verify exact upper identity, for arbitrary coefficients in Krawtchouk basis.
        def K(j,S):
            if j==0:return 1
            if j==1:return S
            if j==2:return Q(S*S-d,2)
            if j==3:return Q(S**3-(3*d-2)*S,6)
        zc=[1,-1,-d] if d%2 else [0,-d]
        coeff=[d,d,1] if d%2 else [2*(d-1),1]
        for j in range(4):
            lhs=K(j,d)+sum(a*K(j,z) for a,z in zip(coeff,zc))
            assert lhs==(target if j==0 else 0),(d,j,lhs)
    print('EXACT_FOURIER_VERIFY_OK dimensions=3..11 constructions=',tests)
    for d in [5,7,9]:
        mons=[sum(1<<i for i in I) for r in range(4) for I in combinations(range(d),r)]
        rows=[]
        for y in range(1<<d):
            S=d-2*wt(y)
            if S in (-1,1,-d):
                rows.append([(-1)**wt(y & mask) for mask in mons])
        rank=rank_mod(rows)
        assert rank==len(mons)-d,(d,rank,len(mons))
        print('EXACT_MODULAR_KERNEL_RANK_OK dimension=',d,'rank=',rank,'nullity=',d)
    print('VERIFY_OK')
