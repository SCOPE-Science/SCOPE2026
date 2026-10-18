"""Independent numerical checks of an augmented cyclic Gabor phase-retrieval theorem.
The theorem's all-order proof does not rely on these finite checks.
"""
import numpy as np

def run(n):
    r=0.5
    indices=np.arange(n)
    g=r**indices.astype(float)
    w=np.r_[np.ones(n//2),1j*np.ones(n//2)] if n%2==0 else None
    projectors=[]
    for a in range(n):
        shift=np.roll(g,a)
        for b in range(n):
            v=shift*np.exp(2j*np.pi*b*indices/n)
            projectors.append(np.outer(v,np.conj(v)).reshape(-1))
    M=np.array(projectors)
    rank=np.linalg.matrix_rank(M,tol=1e-8)
    expected=n*n-(n//2 if n%2==0 else 0)
    assert rank==expected,(n,rank,expected)
    if w is not None:
        P=np.outer(w,np.conj(w)).reshape(1,-1)
        aug_rank=np.linalg.matrix_rank(np.concatenate([M,P]),tol=1e-8)
        assert aug_rank==rank+1,(n,aug_rank,rank)
        for j in range(n//2):
            z=np.zeros(n,dtype=complex)
            z[j]=1.0;z[j+n//2]=1.0+1.0j
            zz=np.zeros(n,dtype=complex)
            zz[j]=1.0;zz[j+n//2]=1.0-1.0j
            d=np.abs(M@np.outer(z,np.conj(z)).reshape(-1)-M@np.outer(zz,np.conj(zz)).reshape(-1))
            assert np.max(d)<1e-9,(n,j,float(np.max(d)))
            extra=abs(np.vdot(w,z))**2-abs(np.vdot(w,zz))**2
            assert abs(extra)>1e-8,(n,j,extra)
        return f'N={n}: Gabor rank={rank}/{n*n}; augmented rank={aug_rank}; {n//2} antipodal ambiguity pairs separated'
    return f'N={n}: Gabor rank={rank}/{n*n}; informationally complete'

for N in [2,3,4,5,6,7,8,9,10,11,12]:
    print(run(N))
print('All finite numerical checks passed; universal result uses an analytic proof.')
