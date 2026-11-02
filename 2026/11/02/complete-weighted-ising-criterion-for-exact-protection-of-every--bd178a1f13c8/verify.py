"""Independent finite-size checks for weighted Ising singlet-protection theorem.
Run with python verify.py (NumPy 1.24+). No external data needed.
"""
import itertools
import math
import numpy as np

CHECKS=0

def check(cond,msg):
    global CHECKS
    CHECKS+=1
    if not cond: raise AssertionError(msg)

def perfect_matchings(seq):
    if not seq:
        yield ()
        return
    a=seq[0]
    for j in range(1,len(seq)):
        b=seq[j]
        for rest in perfect_matchings(seq[1:j]+seq[j+1:]):
            yield ((a,b),)+rest

def dimer(N,pairs):
    result=np.zeros(2**N,dtype=float)
    for mask in range(1<<len(pairs)):
        bits=[0]*N
        phase=1
        for r,(i,j) in enumerate(pairs):
            if mask>>r&1:
                bits[i],bits[j]=1,0
                phase*=-1
            else:bits[i],bits[j]=0,1
        ix=sum(t<<(N-1-k) for k,t in enumerate(bits))
        result[ix]=phase / math.sqrt(2**len(pairs))
    return result

def operators(N,J,h):
    n=2**N
    diag=np.empty(n)
    for ix in range(n):
        z=np.array([1-2*((ix>>(N-1-k))&1) for k in range(N)])
        diag[ix]=sum(J[i,j]*z[i]*z[j] for i in range(N) for j in range(i+1,N))
    H=np.diag(diag)
    for k in range(N):
        for ix in range(n): H[ix,ix^(1<<(N-1-k))]+=h[k]
    return H

def singlet_projector(N):
    # No representation-theoretic shortcut: compute exact total-spin raising kernel
    # inside the zero-magnetization computational sector.
    mids=[q for q in range(2**N) if q.bit_count()==N//2]
    ups=[q for q in range(2**N) if q.bit_count()==N//2-1]
    pos={q:i for i,q in enumerate(ups)}
    plus=np.zeros((len(ups),len(mids)))
    for c,ix in enumerate(mids):
        for k in range(N):
            bit=1<<(N-1-k)
            if ix&bit:
                plus[pos[ix^bit],c]=1
    u,s,vh=np.linalg.svd(plus,full_matrices=True)
    rank=sum(s>1e-9)
    K=vh[rank:,:].T
    P=np.zeros((2**N,2**N))
    P[np.ix_(mids,mids)]=K@K.T
    return P, K.shape[1]

def formula(J,h,pairs):
    Q=0.0
    for r,(i,j) in enumerate(pairs):
        for k,l in pairs[r+1:]:
            delta=J[i,k]-J[i,l]-J[j,k]+J[j,l]
            Q+=delta**2
    return Q+sum((h[i]-h[j])**2 for i,j in pairs)

def verify():
    rng=np.random.default_rng(20261027)
    for N in (2,4,6,8):
        pairslist=list(perfect_matchings(tuple(range(N))))
        P, dim=singlet_projector(N)
        catalan=math.comb(N,N//2)//(N//2+1)
        check(dim==catalan,f'Catalan {N}')
        check(np.linalg.norm(P@P-P)<1e-9,f'projection {N}')
        # Dense heterogeneous protected family; every dimer has zero variance.
        a=rng.integers(-3,4,size=N).astype(float)
        J=np.add.outer(a,a);np.fill_diagonal(J,0)
        h=np.full(N,2.0)
        H=operators(N,J,h)
        E=-sum(a)
        check(np.linalg.norm((H-E*np.eye(2**N))@P)<1e-8, f'additive eigenblock N={N}')
        for pairs in pairslist:
            psi=dimer(N,pairs)
            check(np.linalg.norm(P@psi-psi)<1e-8,'dimer singlet')
            check(abs(psi@(H@H@psi)-(psi@H@psi)**2)<1e-7,'protected variance')
        # Sparse star also protects all singlets, regardless of number of leaves.
        if N>=4:
            J=np.zeros((N,N))
            for j in range(1,N):J[0,j]=J[j,0]=1.25
            H=operators(N,J,np.full(N,1.3))
            check(np.linalg.norm((H+1.25*np.eye(2**N))@P)<1e-8,f'star N={N}')
        # Arbitrary graph couplings: cross-check the independent energy-variance
        # computation against the analytical paired Rademacher formula.
        trials=5 if N<=6 else 2
        sample_pairs=pairslist if N<=4 else [pairslist[i] for i in rng.choice(len(pairslist),min(35,len(pairslist)),replace=False)]
        for t in range(trials):
            X=rng.integers(-4,5,size=(N,N));J=np.triu(X,1).astype(float);J+=J.T
            h=rng.integers(-3,4,size=N).astype(float)
            H=operators(N,J,h)
            for pairs in sample_pairs:
                psi=dimer(N,pairs)
                actual=psi@(H@(H@psi))-(psi@(H@psi))**2
                predicted=formula(J,h,pairs)
                check(abs(actual-predicted)<1e-8, f'variance N={N}, pairs={pairs}')
        # Single edge perturbation breaks entire protection for N>=4.
        if N>=4:
            a=np.linspace(0.1,0.7,N)
            J=np.add.outer(a,a);np.fill_diagonal(J,0)
            J[0,1]+=0.3;J[1,0]+=0.3
            H=operators(N,J,np.full(N,0.2))
            check(np.linalg.norm((np.eye(2**N)-P)@H@P)>1e-5,f'broken edge N={N}')
        # Non-uniform transverse fields necessarily create magnetization leakage.
        h=np.ones(N);h[0]+=0.25
        J=np.zeros((N,N));H=operators(N,J,h)
        check(np.linalg.norm((np.eye(2**N)-P)@H@P)>1e-5,'broken field')
    print(f'PASS {CHECKS} finite independent checks')

if __name__=='__main__':verify()
