"""Finite diagnostics for the fixed--free oscillator damping theorem.

Requires numpy and scipy. The all-size result is proved analytically in RESULT.md;
these finite tests are not a proof of that result.
"""
from math import gcd, pi
import numpy as np
from numpy.linalg import eigvals, norm
from scipy.linalg import eigh


def stiffness(n):
    T = np.diag([2.0]*(n-1) + [1.0])
    for j in range(n-1):
        T[j,j+1] = T[j+1,j] = -1.0
    return T


def loss_vectors(n, ground, bonds):
    vec=[]
    for p in ground:
        v=np.zeros(n);v[p-1]=1.0;vec.append(v)
    for b in bonds:
        v=np.zeros(n);v[b-1]=1.0
        if b>1:v[b-2]-=1.0
        vec.append(v)
    return vec


def predicted_modes(n, ground, bonds):
    N=2*n+1
    g=N
    for p in ground:g=gcd(g,p)
    for b in bonds:g=gcd(g,2*b-1)
    return g,[s for s in range(1,n+1) if ((2*s-1)%(N//g)) == 0]


def spectral_check(n, ground, bonds, amp=0.8, m=1.7, k=2.5):
    vectors=loss_vectors(n,ground,bonds)
    C=sum((amp*(j+1)/(len(vectors)+1)*np.outer(v,v) for j,v in enumerate(vectors)),np.zeros((n,n)))
    A=np.zeros((2*n,2*n))
    A[:n,n:]=np.eye(n)
    A[n:,:n]=-k/m*stiffness(n)
    A[n:,n:]=-C/m
    lam=eigvals(A)
    peripheral=sorted(abs(z.imag) for z in lam if abs(z.real)<1e-8)
    _,idx=predicted_modes(n,ground,bonds)
    expected=sorted([2*np.sqrt(k/m)*np.sin((2*s-1)*pi/(2*(2*n+1))) for s in idx for _ in range(2)])
    assert len(peripheral)==len(expected),(n,ground,bonds,peripheral,expected)
    assert all(abs(x-y)<5e-7 for x,y in zip(peripheral,expected)),(n,ground,bonds,peripheral,expected)
    assert max(z.real for z in lam)<1e-8
    return 1


def run():
    counts={'mode_index_cases':0,'single_damper_spectral_cases':0,'mixed_spectral_cases':0,'placement_counts':0,'local_kick_projectors':0}
    for n in range(2,81):
        N=2*n+1
        for p in range(1,n+1):
            for ground,bonds in [([p],[]),([],[p])]:
                vec=loss_vectors(n,ground,bonds)[0]
                g,idx=predicted_modes(n,ground,bonds)
                brute=[s for s in range(1,n+1) if abs(sum(vec[j]*np.sin((j+1)*(2*s-1)*pi/N) for j in range(n)))<2e-10]
                assert idx==brute,(n,ground,bonds,idx,brute)
                assert len(idx)==(g-1)//2
                counts['mode_index_cases']+=1
        tot=sum(gcd(p,N)==1 for p in range(1,n+1))
        tot2=sum(gcd(2*b-1,N)==1 for b in range(1,n+1))
        phi=sum(gcd(x,N)==1 for x in range(1,N))
        assert 2*tot==phi and 2*tot2==phi
        counts['placement_counts']+=1
        for d in range(1,n+1):
            g,idx=predicted_modes(n,[d],[])
            if not idx:continue
            th=np.array([(2*s-1)*pi/N for s in idx])
            for j in range(1,n+1):
                diag=(4/N)*sum(np.sin(j*th)**2)
                expected=(g/N) if (j%g) else 0.0
                assert abs(diag-expected)<1e-10,(n,d,j,diag,expected)
                counts['local_kick_projectors']+=1
    for n in range(2,16):
        for p in range(1,n+1):
            for ground,bonds in [([p],[]),([],[p])]:
                counts['single_damper_spectral_cases']+=spectral_check(n,ground,bonds)
    rng=np.random.default_rng(20261025)
    for _ in range(390):
        n=int(rng.integers(2,16));ng=int(rng.integers(0,4));nb=int(rng.integers(0,4));
        if ng+nb==0:ng=1
        ground=sorted(set(int(x) for x in rng.integers(1,n+1,ng)))
        bonds=sorted(set(int(x) for x in rng.integers(1,n+1,nb)))
        counts['mixed_spectral_cases']+=spectral_check(n,ground,bonds)
    print('PASS',counts)

if __name__=='__main__': run()
