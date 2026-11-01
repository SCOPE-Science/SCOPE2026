#!/usr/bin/env python3
"""Reproduce finite exact-degree-band Fourier block checks for two latitude rings.
Scientific statement and normalization appear in RESULT.md.
Requires numpy and scipy (sph_harm_y). Does not certify universal quantifiers.
"""
from math import pi,sqrt,cos,log,sin
import numpy as np
from scipy.special import sph_harm_y

def evaluation(L,h,delta):
    m=2*L; angles=np.array([2*pi*j/m for j in range(m)])
    ph=np.r_[angles,angles+delta]
    th=np.r_[np.full(m,np.arccos(h)),np.full(m,np.arccos(-h))]
    E=np.empty((2*m,(L+1)**2),complex)
    j=0
    for ell in range(L+1):
        for q in range(-ell,ell+1):
            E[:,j]=sqrt(4*pi)*sph_harm_y(ell,q,th,ph)
            j+=1
    return E

def fourier_blocks(L,h,delta):
    m=2*L; blocks=[]
    for r in range(m):
        A=0.; B=0j
        for ell in range(L+1):
            for q in range(-ell,ell+1):
                if (q-r)%m:continue
                x= sqrt(4*pi)*sph_harm_y(ell,q,np.arccos(h),0.)
                w=abs(x)**2
                A+=m*w
                B+=m*w*((-1)**(ell+q))*np.exp(-1j*q*delta)
        blocks.append(np.array([[A,B],[B.conjugate(),A]],complex))
    return blocks

def check():
    total=0
    for L in range(2,10):
        m=2*L
        for h in [.19,.47,.73]:
            G_ref=evaluation(L,h,pi/m)
            vals_ref=np.linalg.eigvalsh(G_ref@G_ref.conj().T)
            assert min(vals_ref)>1e-10, (L,h,min(vals_ref))
            sign0,log0=np.linalg.slogdet(G_ref@G_ref.conj().T)
            assert sign0>0
            for frac in [0.,.1,.23,.5,.71,.91,1.]:
                delta=frac*2*pi/m
                G=evaluation(L,h,delta)
                B=fourier_blocks(L,h,delta)
                vals=np.linalg.eigvalsh(G@G.conj().T)
                bvals=np.sort(np.concatenate([np.linalg.eigvalsh(v) for v in B]))
                assert np.allclose(vals,bvals,atol=2e-8,rtol=5e-9), (L,h,frac,vals,bvals)
                positive_expected=frac not in (0.,1.)
                rank=np.linalg.matrix_rank(G,tol=1e-9)
                assert rank==(2*m if positive_expected else 2*m-1),(L,h,frac,rank)
                if positive_expected:
                    sign,logdet=np.linalg.slogdet(G@G.conj().T)
                    assert sign>0
                    assert abs((logdet-log0)-log(sin(L*delta)**2))<3e-5,(L,h,frac,logdet-log0)
                    cond=np.sqrt(vals[-1]/vals[0]); opt=np.sqrt(vals_ref[-1]/vals_ref[0])
                    assert cond>=opt-1e-7,(L,h,frac,cond,opt)
                # Only the single Nyquist block varies in spectrum with delta.
                diff=[np.max(np.abs(np.linalg.eigvalsh(B[i])-np.linalg.eigvalsh(fourier_blocks(L,h,pi/m)[i]))) for i in range(m) if i!=L]
                assert max(diff)<2e-8,(L,h,frac)
                total+=1
    print(f'PASS {total} spectral/rank/logdet/optimality configurations; L=2..9, h=0.19,0.47,0.73, 7 phase offsets.')
    print('The analytic proof, not these finite tests, establishes the all-integer/all-real theorem.')
if __name__=='__main__':check()
