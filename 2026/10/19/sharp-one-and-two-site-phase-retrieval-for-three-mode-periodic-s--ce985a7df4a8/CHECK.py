"""Reproducible arithmetic tests for three-mode periodic Schrödinger intensity sampling."""
import cmath
import math
import random
import numpy as np


def fourier_coeffs(k, a, x):
    out = {0: sum(abs(z)**2 for z in a)}
    for i in range(3):
        for j in range(i+1,3):
            gap = k[j]**2-k[i]**2
            out[gap] = out.get(gap, 0)+a[j]*a[i].conjugate()*cmath.exp(1j*(k[j]-k[i])*x)
    return out


def direct_grid(k,a,x,n=16384):
    t=np.arange(n)*2*np.pi/n
    u=sum(z*np.exp(1j*(j*x-j*j*t)) for j,z in zip(k,a))
    I=np.abs(u)**2
    gaps=[0]+[k[j]**2-k[i]**2 for i in range(3) for j in range(i+1,3)]
    return {g:np.mean(I*np.exp(1j*g*t)) for g in sorted(set(gaps))}


def test():
    rng=random.Random(29147)
    checked=0
    for k in [(1,5,7),(1,2,4),(1,7,13),(2,14,22),(3,15,21),(0,1,3),(1,3,5)]:
        for trial in range(12):
            a=[complex(rng.uniform(-2,2),rng.uniform(-2,2)) for _ in range(3)]
            for x in [0.0,.77]:
                exact=fourier_coeffs(k,a,x)
                nums=direct_grid(k,a,x)
                assert all(abs(exact[g]-nums[g])<1e-10 for g in exact),(k,x,exact,nums)
                checked+=len(exact)
            if k[2]**2-k[1]**2!=k[1]**2-k[0]**2:
                f=fourier_coeffs(k,a,0.0)
                p=f[k[1]**2-k[0]**2]; q=f[k[2]**2-k[1]**2]; r=f[k[2]**2-k[0]**2]
                reconstructed_abs_a1=(p*q/r).real
                assert abs(reconstructed_abs_a1-abs(a[1])**2)<1e-10
                checked+=1
    k=(1,5,7)
    four=[[6,-5,1],[3,-7,2],[2,-7,3],[1,-5,6]]
    ref=fourier_coeffs(k,four[0],0.0)
    for a in four:
        assert all(abs(fourier_coeffs(k,a,0.0)[g]-v)<1e-10 for g,v in ref.items())
        checked+=len(ref)
    assert len(set(tuple(x) for x in four))==4
    for trial in range(200):
        a=[complex(rng.uniform(-2,2),rng.uniform(-2,2)) for _ in range(3)]
        h=rng.uniform(0,2*np.pi)
        D=k[2]-2*k[1]+k[0]
        m1=k[1]-k[0];m2=k[2]-k[1]
        M=np.array([[1,1],[cmath.exp(1j*m1*h),cmath.exp(1j*m2*h)]],complex)
        sing=np.linalg.svd(M,compute_uv=False)
        expect=np.sqrt([2+2*abs(math.cos(D*h/2)),2-2*abs(math.cos(D*h/2))])
        assert np.max(abs(sing-expect))<1e-10
        f0=fourier_coeffs(k,a,0)
        fh=fourier_coeffs(k,a,h)
        y=np.array([f0[24],fh[24]])
        p,q=np.linalg.solve(M,y)
        assert abs(p-a[1]*a[0].conjugate())<1e-9
        assert abs(q-a[2]*a[1].conjugate())<1e-9
        checked+=4
    h=math.pi/2
    m1=4;m2=2
    M=np.array([[1,1],[cmath.exp(1j*m1*h),cmath.exp(1j*m2*h)]])
    assert np.allclose(np.linalg.svd(M,compute_uv=False),[math.sqrt(2)]*2)
    checked+=1
    print(f'PASS: {checked} exact-coefficient, Fourier-quadrature, ambiguity and demixing checks.')

if __name__=='__main__':
    test()
