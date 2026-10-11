"""Reproduce finite-cyclic and Floquet checks for a two-periodic difference operator.
Python 3 with numpy; deterministic runs, not a replacement for the proof.
"""
import math
import cmath
import numpy as np


def sharp_constant(a,b):
    r=abs(a*b)
    if abs(r-1)<1.e-12: return math.inf
    s=abs(a)**2+abs(b)**2+2
    d=abs(r-1)
    return math.sqrt((s+math.sqrt(max(0,s*s-4*d*d)))/2)/d


def fiber(a,b,z):
    return np.array([[-a,1],[z,-b]], dtype=complex)


def cyclic_matrix(a,b,k):
    n=2*k
    mat=np.zeros((n,n),dtype=complex)
    for i in range(n):
        mat[i,i] = -a if i%2==0 else -b
        mat[i,(i+1)%n] = 1
    return mat


def checks():
    rng=np.random.default_rng(241017)
    count=0
    for t in range(400):
        a=(0.3+2.1*rng.random())*np.exp(1j*rng.uniform(-math.pi,math.pi))
        b=(0.3+2.1*rng.random())*np.exp(1j*rng.uniform(-math.pi,math.pi))
        if abs(abs(a*b)-1)<0.02: continue
        c=sharp_constant(a,b)
        z=(a*b)/abs(a*b)
        fs=np.linalg.svd(fiber(a,b,z),compute_uv=False)
        assert abs(1/fs[-1]-c) <= 1e-10*max(1,c)
        for phase in np.linspace(0,2*math.pi,17):
            g=np.linalg.svd(fiber(a,b,np.exp(1j*phase)),compute_uv=False)
            assert 1/g[-1] <= c*(1+1e-10)
            count+=1
    for a,b in [(0,0), (0,1), (1,0), (.4,1.5), (2,3), (-.5,1.2),(0.3+0.5j,0.6-0.1j)]:
        c=sharp_constant(a,b)
        k=24
        cyc=np.linalg.svd(cyclic_matrix(a,b,k),compute_uv=False)
        obs=1/cyc[-1]
        assert obs<=c*(1+2e-10)
        if not a or not b or (a*b).imag==0 and (a*b).real>0:
            assert abs(obs-c) <=1e-9*max(1,c)
        count+=1
    for r in [0.1,0.2,0.5,2,3,10]:
        target=1/abs(math.sqrt(r)-1)
        c=sharp_constant(math.sqrt(r),math.sqrt(r))
        assert abs(c-target)<=1e-10*target
        for skew in [1.01,2,5,20]:
            unequal=sharp_constant(skew*math.sqrt(r),math.sqrt(r)/skew)
            assert unequal>c
            count+=1
    print('VERIFY_OK',count,'checks')

if __name__=='__main__':
    checks()
