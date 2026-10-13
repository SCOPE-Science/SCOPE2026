"""Numerical corroboration of prime-open-chain stroboscopic recurrence.
Run: python verify.py (requires numpy and scipy).
This finite test does not replace the cyclotomic proof.
"""
import math
import numpy as np
from scipy.linalg import solve_discrete_lyapunov


def spectral(p):
    js=np.arange(1,p)
    e=2*np.cos(np.pi*js/p)
    w=2*np.sin(np.pi*js/p)**2/p
    assert abs(np.sum(w)-1)<1e-12
    return e,w


def phase_partition(e,tau,tol=1e-8):
    phases=np.exp(-1j*tau*e)
    groups=[]
    for j,z in enumerate(phases):
        for g in groups:
            if abs(z-phases[g[0]])<tol:
                g.append(j)
                break
        else:groups.append([j])
    return groups


def lyapunov_mean(e,w,tau,tol=2e-6):
    groups=phase_partition(e,tau)
    zs=np.array([np.exp(-1j*tau*e[g[0]]) for g in groups])
    ws=np.array([sum(w[g]) for g in groups]);psi=np.sqrt(ws)
    u=np.diag(zs)
    q=(np.eye(len(zs))-np.outer(psi,psi))@u
    gram=solve_discrete_lyapunov(q.conj().T,np.eye(len(zs)))
    t=float(np.real(np.vdot(psi,gram@psi)))
    if abs(t-len(groups))>tol:
        raise AssertionError((t,len(groups),tau,groups))
    return len(groups),t


def expected_groups(p,typ,i,j=None):
    e,_=spectral(p);m=(p-1)//2
    if typ=='generic': return p-1
    if typ=='antipodal':return p-2
    if typ in ('sum','difference'):return p-3
    raise ValueError(typ)


def test():
    cases=0; classes=0;collision=0
    for p in [3,5,7,11,13,17,19]:
        e,w=spectral(p);m=(p-1)//2
        gaps=[]
        # positive eigenvalues are e[0:m], negatives in reverse order
        a=e[:m]
        for i in range(m):gaps.append(('antipodal',i,None,2*a[i]))
        for i in range(m):
            for j in range(i+1,m):
                gaps.extend([('difference',i,j,a[i]-a[j]),('sum',i,j,a[i]+a[j])])
        assert len(gaps)==m*m
        # numeric pair-gap collision multiplicities and cross-class separation
        for typ,i,j,d in gaps:
            assert d>0
            tau=2*np.pi/d
            groups=phase_partition(e,tau)
            observed=p-1-sum(len(g)-1 for g in groups)
            assert observed==expected_groups(p,typ,i,j),(p,typ,i,j,observed,groups)
            assert max(map(len,groups))<=2
            collisions=sum(len(g)==2 for g in groups)
            assert collisions==(1 if typ=='antipodal' else 2)
            classes+=1;collision+=collisions
            if p<=11:
                _,t=lyapunov_mean(e,w,tau,2e-5)
                cases+=1
        # generic sampling not hitting small resonances
        tau=math.sqrt(2)/7
        assert len(phase_partition(e,tau))==p-1
        if p<=11:
            _,t=lyapunov_mean(e,w,tau,1e-4);cases+=1
    print(f'VERIFY_OK distinct_resonance_ladders={classes} pair_collisions={collision} direct_lyapunov_means={cases}')

if __name__=='__main__':test()
