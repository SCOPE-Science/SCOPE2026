"""Independent finite checks for the flux-resolved one-excitation sink theorem.
Requires numpy and scipy. Run: python verify_flux_sink.py
"""
import itertools, math
import numpy as np
from scipy.linalg import expm

count=0

def check(p,msg):
    global count
    if not p: raise AssertionError(msg)
    count+=1

def dark_theory(n,sinks,ell):
    assert sinks and all(0<=s<n for s in sinks)
    g=n
    root=sinks[0]
    for s in sinks[1:]:g=math.gcd(g,(s-root)%n)
    m=n//g
    t=math.gcd(2,m)
    u=math.gcd(2,n)
    countsol=g*t if ell%t==0 else 0
    fixed=u if ell%u==0 else 0
    assert (countsol-fixed)%2==0 and countsol>=fixed
    return (countsol-fixed)//2

def hmat(n,phi):
    h=np.zeros((n,n),complex)
    for j in range(n):
        h[j,(j+1)%n] += np.exp(1j*phi/n)
        h[(j+1)%n,j] += np.exp(-1j*phi/n)
    return h

def dark_pairs(n,sinks,ell):
    root=sinks[0]
    seen=set();vec=[]
    for k in range(n):
        m=(-k-ell)%n
        if k==m or k in seen or m in seen: continue
        seen.add(k);seen.add(m)
        if any((k-m)*(s-root)%n!=0 for s in sinks): continue
        v=np.array([np.exp(2j*np.pi*k*j/n)-np.exp(2j*np.pi*(k-m)*root/n)*np.exp(2j*np.pi*m*j/n) for j in range(n)],complex)/np.sqrt(2*n)
        vec.append(v)
    return vec

for n in range(3,15):
    sinksets=[(0,), (0,n//2), tuple(range(min(n,3))), (0,1), (0,2%n), (0,n-1)]
    sinksets += [tuple(j for j in range(n) if mask>>j&1) for mask in range(1,1<<min(n,6))]
    sinksets=sorted(set(tuple(sorted(set(s))) for s in sinksets))
    for ss in sinksets:
        for ell in (0,1):
            vv=dark_pairs(n,ss,ell)
            check(len(vv)==dark_theory(n,ss,ell), f'dimension n={n} s={ss} phi={ell}')
            if vv:
                V=np.column_stack(vv)
                check(np.linalg.norm(V.conj().T@V-np.eye(len(vv)))<1e-10,'orthonormality')
                h=hmat(n,ell*np.pi)
                for v in vv:
                    for s in ss:check(abs(v[s])<1e-10, 'node')
                    lam=np.vdot(v,h@v)
                    check(np.linalg.norm(h@v-lam*v)<1e-10, 'eigenvector')

for n in range(4,28,2):
    for ell in (0,1):
        V=np.column_stack(dark_pairs(n,(0,),ell))
        P=V@V.conj().T
        for y in range(n):
            expected=0 if y==0 else (1 if (ell==1 and y==n//2) else (0 if y==n//2 else 0.5))
            check(abs(P[y,y].real-expected)<1e-10, f'projection {n} {ell} {y}')
    for phi in (0.22,0.7,1.9,4.2):
        lam=np.linalg.eigvalsh(hmat(n,phi))
        check(np.min(np.diff(lam))>1e-7, f'generic eigenvalues {n} {phi}')

for n in (4,6,8):
    for ell in (0,1):
        H=hmat(n,ell*np.pi)
        loss=np.zeros((n,n),complex);loss[0,0]=1
        A=-1j*H-0.5*loss
        y=n//2
        psi=np.eye(n,dtype=complex)[:,y]
        for t in (0.01,0.3,2,8):
            amp=expm(t*A)@psi
            if ell==1:check(abs(np.linalg.norm(amp)**2-1)<1e-8, f'perfect darkness {n} {t}')
        if ell==0:
            amp=expm(1500*A)@psi
            check(np.linalg.norm(amp)**2<0.05, f'eventual trapping {n}')

print(f'PASS {count} finite checks')
