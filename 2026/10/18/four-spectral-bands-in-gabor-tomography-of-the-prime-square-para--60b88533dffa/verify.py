"""Recompute prime-square parabola Gabor ambiguity values directly by FFT.
Run: python verify.py (requires numpy). Tests p=3,5,7 exhaustively.
The infinite prime family is proved algebraically, not by this finite test.
"""
import numpy as np
from collections import Counter

def expected_bands(p):
    return {0:p**7-p**5+p**3-p*p+p-1,
            1:p**7*(p-1),
            p:p**5-p**3,
            p**1.5:p*(p-1),
            p*p:1}

def run(p):
    n=p*p
    observed=Counter()
    rank=0
    typecount=Counter()
    for u in range(n):
        for v in range(n):
            h=np.zeros((n,n),dtype=np.float64)
            for t in range(n):
                t2=t*t%n
                if ((t-u)**2-t2+v)%n==0:
                    h[t,t2]=1.0
            F=np.abs(np.fft.fft2(h))
            if u==0 and v==0:
                required=p**4-p**3+p*p-p+1; kind='zero_shift'
            elif u%p:
                required=p**4; kind='unit_translation'
            elif u and v%p==0:
                required=p**3; kind='nonzero_p_translation'
            else:
                required=0; kind='empty_intersection'
            count=int(np.count_nonzero(F>1.e-7))
            assert count==required,(p,u,v,count,required)
            rank+=count
            typecount[kind]+=1
            # F equals unnormalized Gauss sum: values 0,1,p,p*sqrt(p),p^2.
            possibilities=np.array([0.,1.,float(p),float(p**1.5),float(p*p)])
            nearest=np.abs(F[...,None]-possibilities).argmin(axis=-1)
            assert np.max(np.min(np.abs(F[...,None]-possibilities),axis=-1))<1.e-6
            for i,num in enumerate(np.bincount(nearest.ravel(),minlength=5)):
                observed[possibilities[i]]+=int(num)
    theoretical=expected_bands(p)
    assert rank==p**8-p**7+p**5-p**3+p*p-p+1
    assert dict(observed)==theoretical,(observed,theoretical)
    print('p=%d rank=%d bands=%s shifts=%s'%(p,rank,dict(sorted(observed.items())),dict(sorted(typecount.items()))))

if __name__=='__main__':
    for p in (3,5,7):run(p)
    print('ALL CHECKS PASSED')
