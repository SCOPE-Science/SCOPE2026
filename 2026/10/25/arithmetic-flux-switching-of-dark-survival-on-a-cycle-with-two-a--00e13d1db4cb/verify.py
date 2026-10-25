"""Numerical cross-checks for finite cyclic coherent transport with two absorbers.

No finite computation is used as a proof of the all-size result.
"""
from math import gcd, pi
import numpy as np
from scipy.linalg import expm


def predicted(N, a, x, flux_index):
    """Exact dimension and site-localized dark weight, flux_index=0 or 1."""
    g = gcd(N, a)
    Q = N // g
    r = x % g
    if flux_index == 0:
        if Q % 2 == 0:
            return g - 1, (g / N if r else 0.0)
        if g % 2:
            return (g - 1) // 2, (g / (2*N) if r else 0.0)
        return (g - 2) // 2, (g / (2*N) if r not in (0, g // 2) else 0.0)
    if Q % 2 == 0:
        return 0, 0.0
    if g % 2:
        return (g - 1) // 2, (g / (2*N) if r else 0.0)
    if r == 0:
        w = 0.0
    elif r == g//2:
        w = g / N
    else:
        w = g / (2*N)
    return g//2, w


def residue_check(N, a, x, s):
    pp = []
    seen = set()
    for m in range(N):
        n = (-m-s) % N
        if n == m or (m,n) in seen or (n,m) in seen:
            continue
        if (m-n)*a % N == 0:
            pp.append((m,n))
            seen.add((m,n))
    weight = sum((1-np.cos(2*pi*(m-n)*x/N))/N for m,n in pp)
    return len(pp),weight


def actual_spectrum(N, a, x, flux):
    ph = flux / N
    H = np.zeros((N,N),dtype=complex)
    for j in range(N):
        k = (j+1)%N
        H[j,k] += -np.exp(1j*ph)
        H[k,j] += -np.exp(-1j*ph)
    E,V = np.linalg.eigh(H)
    groups=[]
    for i,e in enumerate(E):
        if not groups or abs(E[groups[-1][0]]-e)>2e-8:
            groups.append([i])
        else:
            groups[-1].append(i)
    total_dim=0
    proj=np.zeros((N,N),complex)
    for gr in groups:
        vec=V[:,gr]
        B=vec[[0,a],:]
        _u,sg,Vh=np.linalg.svd(B,full_matrices=True)
        rk=np.count_nonzero(sg>1e-8)
        null=vec@Vh[rk:,:].conj().T
        total_dim += null.shape[1]
        proj += null@null.conj().T
    return total_dim,proj[x,x].real,H


def main():
    checks=0
    maxerr=0.
    for N in range(3,121):
        for a in range(1,N):
            for s in (0,1):
                for x in range(N):
                    d,w=predicted(N,a,x,s)
                    de,we=residue_check(N,a,x,s)
                    assert d == de and abs(w-we)<2e-12,(N,a,x,s,d,de,w,we)
                    checks +=1
    print('Exact modular Fourier enumeration checks', checks)
    specs=0
    for N in range(3,25):
        for a in range(1,N):
            for s,flux in ((0,0.),(1,pi)):
                for x in range(N):
                    d,w=predicted(N,a,x,s)
                    da,wa,_=actual_spectrum(N,a,x,flux)
                    maxerr=max(maxerr,abs(w-wa))
                    assert d==da and abs(w-wa)<1e-8, (N,a,x,s,d,da,w,wa)
                    specs +=1
        # generic flux: nondegenerate, no dark states
        for a in range(1,N):
            d,w,_=actual_spectrum(N,a,(a+1)%N,0.37)
            assert d==0 and abs(w)<1e-10
            specs+=1
    print('Direct spectral projector checks', specs, 'maximum error',maxerr)
    # Direct evolution at several moderate sizes and different unequal sink rates.
    evchecks=0
    for N,a,x,s in [(6,3,1,0),(6,3,1,1),(8,2,3,0),(9,3,1,0),(9,3,1,1),(12,4,2,1),(12,4,1,0),(7,3,1,0)]:
        d,w,H = actual_spectrum(N,a,x,s*pi)
        Gamma=np.zeros((N,N),dtype=complex)
        Gamma[0,0]=0.8;Gamma[a,a]=1.3
        B=-1j*H-Gamma/2
        init=np.eye(N)[:,x]
        for t in (100.,500.,3000.):
            z=expm(B*t)@init
            surv=np.linalg.norm(z)**2
            assert surv +1e-8 >=w and (t < 3000. or abs(surv-w)<0.004), (N,a,x,s,t,w,surv)
            evchecks+=1
    print('Time-domain contraction checks',evchecks)
    print('All checks passed.')

if __name__=='__main__':
    main()
