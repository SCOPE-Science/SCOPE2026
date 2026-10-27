#!/usr/bin/env python3
"""Independent numerical checks for the finite-tree ancestor-sum spectrum.
Run: python check_tree.py. Uses numpy and scipy; does not replace the analytic proof.
"""
import numpy as np
from scipy.linalg import eigvalsh_tridiagonal

def parents(b,h):
    out=[-1]
    levels=[[0]]
    for _ in range(h):
        row=[]
        for par in levels[-1]:
            for _ in range(b):
                row.append(len(out));out.append(par)
        levels.append(row)
    return out

def blocks(b,h):
    eigen=[]
    for ell in range(h+1):
        diag=np.array([b+1.]*ell+[1.])
        off=np.full(ell,-np.sqrt(b))
        vals=eigvalsh_tridiagonal(diag,off)
        mult=1 if ell==h else (b-1)*b**(h-ell-1)
        eigen.extend(list(vals)*mult)
    return np.sort(np.array(eigen))

def full(b,h):
    ps=parents(b,h); n=len(ps)
    B=np.eye(n)
    for i in range(1,n):
        B[i,ps[i]]=-1
    return np.sort(np.linalg.eigvalsh(B.T@B))

for b in (2,3,4):
    for h in range(1,5):
        a=blocks(b,h);v=full(b,h)
        assert len(a)==len(v)
        err=np.max(np.abs(a-v))
        assert err<1e-10,(b,h,err)
        sharp=a[0]**(-.5)
        direct=v[0]**(-.5)
        print('b,h,n,sharp,err:',b,h,len(v),sharp,err)
print('all finite spectrum tests PASS')
for b in (2,3,4):
    for h in (8,12,16):
        lam=eigvalsh_tridiagonal(np.r_[np.full(h,b+1.),1.],np.full(h,-np.sqrt(b)),select='i',select_range=(0,0))[0]
        ratio=lam*b**(h+2)/(b-1)**2
        assert abs(ratio-1)<.01 if h>=12 else abs(ratio-1)<.1,(b,h,ratio)
        print('asymptotic lambda ratio',b,h,ratio)
print('asymptotic tests PASS')
