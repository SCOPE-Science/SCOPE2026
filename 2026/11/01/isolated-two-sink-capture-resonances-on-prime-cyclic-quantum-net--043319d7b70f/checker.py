"""Finite-dimensional consistency tests for two-sink resonances on prime cyclic quantum networks."""
import math
import numpy as np
from scipy.linalg import eigvalsh, eigh, expm

PRIMES = [5,7,11,13,17,19,23,29]
EPS = 1.e-8
cases = 0
entries = 0
min_res_gap = 1e100
max_site_error = 0.0
max_decay_error = 0.0

for p in PRIMES:
    m = (p - 1)//2
    pairs = [(k,l) for k in range(1,m+1) for l in range(k+1,m+1) if k+l>=m+1]
    assert len(pairs) == (m*m)//4, (p,len(pairs))
    resonances = [(-1/(2*(math.cos(2*math.pi*k/p)+math.cos(2*math.pi*l/p))),k,l) for k,l in pairs]
    assert all(r>0 for r,_,_ in resonances)
    for a in range(len(resonances)):
        for b in range(a+1,len(resonances)):
            min_res_gap=min(min_res_gap,abs(resonances[a][0]-resonances[b][0]))
            assert abs(resonances[a][0]-resonances[b][0])>1.e-8
    ring1=np.zeros((p,p))
    ring2=np.zeros((p,p))
    for i in range(p):
        for hop,M in [(1,ring1),(2,ring2)]:
            M[i,(i+hop)%p]=M[i,(i-hop)%p]=1
    for r,k,l in resonances:
        H=ring1+r*ring2
        w,U=eigh(H)
        lam=2*math.cos(2*math.pi*k/p)+2*r*math.cos(4*math.pi*k/p)
        sel=np.where(abs(w-lam)<1.e-8)[0]
        assert len(sel)==4,(p,k,l,r,len(sel))
        V=U[:,sel]
        for d in range(1,p):
            B=V[[0,d],:]
            _,sv,vh=np.linalg.svd(B,full_matrices=True)
            assert sv[-1]>1.e-8
            W=V@vh.conj().T[:,2:]
            Q=W@W.conj().T
            assert np.linalg.norm(Q@H-H@Q)<1.e-7
            assert np.max(abs(Q[[0,d],:]))<1.e-7
            assert abs(np.trace(Q)-2)<1.e-7
            fd=math.cos(2*math.pi*k*d/p)+math.cos(2*math.pi*l*d/p)
            for x in range(p):
                fx=math.cos(2*math.pi*k*x/p)+math.cos(2*math.pi*l*x/p)
                fy=math.cos(2*math.pi*k*(x-d)/p)+math.cos(2*math.pi*l*(x-d)/p)
                q=4/p*(1-(fx*fx+fy*fy-fd*fx*fy)/(4-fd*fd))
                error=abs(q-Q[x,x].real)
                max_site_error=max(max_site_error,error)
                assert error<1.e-9,(p,k,l,d,x,q,Q[x,x])
                assert -1.e-8<q<1+1.e-8
                entries+=1
            cases+=1
    for r in [0.2,0.5,1.0,2.0,3.0]:
        H=ring1+r*ring2
        w,U=eigh(H)
        if any(np.isclose(r,t[0],rtol=0,atol=1e-9) for t in resonances):
            continue
        for d in range(1,p):
            # Every 1D or 2D band is observed at two sites.
            for lam in np.unique(np.round(w,8)):
                sel=np.where(abs(w-lam)<1.e-8)[0]
                assert len(sel) in (1,2),(p,r,lam,len(sel))
                assert np.linalg.matrix_rank(U[[0,d],:][:,sel],tol=1e-8)==len(sel)
            cases+=1
    if p <= 11:
        d=2
        for r in [0.7,resonances[0][0]]:
            H=ring1+r*ring2
            K=H.astype(complex)-0.5j*np.diag([1.25 if j==0 else 0.7 if j==d else 0 for j in range(p)])
            evolved=expm(-1j*K*5000.0)
            survival=float(np.linalg.norm(evolved,'fro')**2/p)
            predicted=0 if r==0.7 else 2/p
            max_decay_error=max(max_decay_error,abs(survival-predicted))
            assert abs(survival-predicted)<1e-6,(p,r,survival,predicted)
print('primes_checked',PRIMES)
print('resonant_and_generic_pairs_checked',cases)
print('individual_site_comparisons',entries)
print('min_resonance_spacing',format(min_res_gap,'.12g'))
print('max_projector_formula_error',format(max_site_error,'.3e'))
print('max_large_time_loss_error',format(max_decay_error,'.3e'))
print('PASS')
