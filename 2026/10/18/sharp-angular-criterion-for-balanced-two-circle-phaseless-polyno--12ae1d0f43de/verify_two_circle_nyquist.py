"""Standalone numerical cross-checks of a two-radius polynomial-intensity theorem.

This program corroborates a symbolic theorem; it is not a substitute for the proof.
Requires Python 3 with NumPy installed. It uses a fixed random seed.
"""
import cmath
import math
import numpy as np

rng=np.random.default_rng(671251)
assertions=0
for degree in range(1,16):
    count=2*degree
    for phase in (0.193, 0.193 + math.pi/(2*degree), 0.193+0.31/degree):
        radii=(0.37, 0.83)
        theta=(0.193,phase)
        a=rng.normal(size=degree+1)+1j*rng.normal(size=degree+1)
        ctop=a[degree]*np.conj(a[0])
        top_b=[]
        for r,th in zip(radii,theta):
            angles=th+2*math.pi*np.arange(count)/count
            z=r*np.exp(1j*angles)
            intensities=np.abs(np.polynomial.polynomial.polyval(z,a))**2
            for m in range(degree):
                coefficient= r**m*sum(a[j+m]*np.conj(a[j])*r**(2*j) for j in range(degree-m+1))
                transformed=np.mean(intensities*np.exp(-1j*m*angles))
                assert abs(transformed-coefficient) < 1e-7*(1+abs(coefficient))
                assertions+=1
            b=np.mean(intensities*((-1)**np.arange(count)))/(2*r**degree)
            assert abs(b-(ctop*np.exp(1j*degree*th)).real) < 1e-7*(1+abs(ctop))
            assertions+=1
            top_b.append(b)
        A=np.array([[math.cos(degree*t),-math.sin(degree*t)] for t in theta])
        if abs(np.linalg.det(A))>1e-8:
            c_est=np.linalg.solve(A,top_b)
            assert abs(c_est[0]+1j*c_est[1]-ctop)<1e-6*(1+abs(ctop))
            assertions+=1
            sing=np.linalg.svd(A,compute_uv=False)
            expected=np.sqrt([1+abs(math.cos(degree*(theta[1]-theta[0]))),1-abs(math.cos(degree*(theta[1]-theta[0])))] )
            assert np.max(abs(sing-expected))<1e-9
            assertions+=1
    for phase in (0,math.pi/degree, -2*math.pi/degree):
        theta=(0.193,0.193+phase)
        for r,th in zip((0.37,0.83),theta):
            angles=th+2*math.pi*np.arange(count)/count
            z=r*np.exp(1j*angles)
            f=z**degree-1j*np.exp(1j*degree*theta[0])
            g=z**degree+1j*np.exp(1j*degree*theta[0])
            assert np.max(abs(abs(f)**2-abs(g)**2))<1e-7
            assertions+=1
    # Equal-radius obstruction (works at every possible set of angles).
    for th in (0.0,0.17):
        r=0.5
        z=r*np.exp(1j*(th+2*math.pi*np.arange(count)/count))
        assert np.max(abs(abs(z)**2-r*r))<1e-8
        assertions+=1
print('PASS', assertions, 'independent numerical consistency checks for degrees 1..15')
