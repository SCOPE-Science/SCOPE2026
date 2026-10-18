#!/usr/bin/env python3
"""Standalone finite-matrix checks for coherent tunneling through an unweighted barbell."""
import math
import numpy as np
from numpy.testing import assert_allclose
from scipy.linalg import expm

def reduced_blocks(n):
    a=(n-2)/(n-1)
    b=1/math.sqrt(n)
    c=1/n
    plus=np.array([[a,b],[b,c]])
    minus=np.array([[a,b],[b,-c]])
    return plus, minus

def phases(n,t):
    pp,mm=reduced_blocks(n)
    vp,up=np.linalg.eigh(pp)
    vm,um=np.linalg.eigh(mm)
    fp=np.sum(up[0,:]**2*np.exp(-1j*vp*t))
    fm=np.sum(um[0,:]**2*np.exp(-1j*vm*t))
    gp=(expm(-1j*pp*t))[1,0]
    gm=(expm(-1j*mm*t))[1,0]
    return (fp-fm)/2, (gp-gm)/2, 1-vm[1]

def full_graph(n):
    z=np.zeros((2*n,2*n))
    for s in (0,n):
        for j in range(s,s+n):
            for k in range(s,s+n):
                if j!=k: z[j,k]=1
    z[n-1,n]=z[n,n-1]=1
    d=z.sum(axis=1)
    return z/np.sqrt(d[:,None]*d[None,:])

def right_probability(n,t):
    a,b,delta=phases(n,t)
    return abs(a)**2+abs(b)**2

def main():
    count=0
    rng=np.random.default_rng(20260305)
    for n in (3,4,5,7,10,17,30,60,100,200):
        plus,minus=reduced_blocks(n)
        evp=np.linalg.eigvalsh(plus)
        evm=np.linalg.eigvalsh(minus)
        assert abs(evp[1]-1)<5e-15; count+=1
        assert abs(evp[0]+1/(n*(n-1)))<5e-15; count+=1
        assert abs((1-evm[1])*(1-evm[0])-2/(n*(n-1)))<5e-14;count+=1
        theta=(n*n-3*n+1+math.sqrt((n*n-3*n+1)**2+4*n*(n-1)*(2*n-3)))/(2*n*(n-1))
        assert abs(theta-evm[1])<1e-12; count+=1
        for t in (0,0.3,2,15,n*n*0.1,n*n*0.47,n*n*math.pi/2):
            amp,br,delta=phases(n,t)
            p=abs(amp)**2+abs(br)**2
            assert -1e-13<=p<=1+1e-12; count+=1
            assert abs(p-math.sin(delta*t/2)**2)<=8*n/(n-1)**2+1e-12;count+=1
            if n<=17:
                H=full_graph(n)
                v=np.zeros(2*n);v[:n-1]=1/math.sqrt(n-1)
                evolved=expm(-1j*H*t)@v
                assert_allclose(evolved[n+1:2*n].sum()/math.sqrt(n-1),amp,atol=1e-12);count+=1
                assert_allclose(evolved[n],br,atol=1e-12);count+=1
                assert_allclose(np.sum(np.abs(evolved[n:])**2),p,atol=1e-12);count+=1
                # Fixed-localized state: only 1/(n-1) of the launched vector is bright.
                w=np.zeros(2*n);w[0]=1
                actual=np.sum(np.abs((expm(-1j*H*t)@w)[n:])**2)
                assert_allclose(actual,p/(n-1),atol=1e-12);count+=1
                # Arbitrary complex wavepackets: the dark component never leaves.
                for _ in range(3):
                    packet=rng.normal(size=n-1)+1j*rng.normal(size=n-1)
                    packet=packet/np.linalg.norm(packet)
                    launch=np.zeros(2*n,dtype=complex);launch[:n-1]=packet
                    alpha=np.sum(packet)/math.sqrt(n-1)
                    prob=np.sum(np.abs((expm(-1j*H*t)@launch)[n:])**2)
                    assert_allclose(prob,abs(alpha)**2*p,atol=1e-12);count+=1
        # Strong spectral asymptotics are numerical diagnostics only.
    for n in (100,300,1000,5000):
        _,_,delta=phases(n,0)
        assert abs(n*n*delta-2)<3/n+0.025;count+=1
        t=math.pi/delta
        assert right_probability(n,t)>1-9/n;count+=1
    print('PASS',count,'matrix/spectral/numerical assertions')
if __name__=='__main__': main()
