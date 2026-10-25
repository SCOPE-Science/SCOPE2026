"""Reproduce exact fourth-cumulant coefficients for a freely rotating, uniformly reorienting particle."""
import math
import sympy as S
import numpy as np

w=S.symbols('w',real=True)
A1=1/(2*(1-S.I*w))
A2=A1/(2*(1-2*S.I*w))
a2=S.factor(S.re(S.expand_complex(A1)))
B1=(A2/2-a2*A1)/(1-S.I*w)
a4=S.factor(S.re(S.expand_complex(B1)))
expected_a2=1/(2*(1+w*w))
expected_a4=(3*w**4-10*w*w-1)/(8*(1+w*w)**3*(1+4*w*w))
assert S.simplify(a2-expected_a2)==0
assert S.simplify(a4-expected_a4)==0
print('Exact Fourier perturbation identities: PASS')
x=S.symbols('x',real=True)
poly=3*x*x-10*x-1
root=(5+2*S.sqrt(7))/3
assert S.simplify(poly.subs(x,root))==0
assert root>0 and (5-2*S.sqrt(7))/3<0
assert S.simplify(S.diff(poly,x).subs(x,root))>0
print('Unique positive squared-chirality root: PASS')
print('Critical |omega|/gamma:',S.N(S.sqrt(root),16))
checks=4
for W in (0.,.4,1.,1.8,1.85216113609,2.2,3.,5.):
    aa2=float(expected_a2.subs(w,W))
    aa4=float(expected_a4.subs(w,W))
    # The Fourier modes |n|<=6 suffice for the displayed small-tilt tests.
    N=6
    for tilt in (.08,.04,.02):
        matrix=np.zeros((2*N+1,2*N+1),dtype=complex)
        for i,n in enumerate(range(-N,N+1)):
            matrix[i,i]=(-1+1j*n*W) if n else 0
            if i>0: matrix[i,i-1]=tilt/2
            if i<2*N:matrix[i,i+1]=tilt/2
        eigs=np.linalg.eigvals(matrix)
        leading=min(eigs,key=abs)
        assert abs(leading.imag)<2e-10
        estimate=(leading.real-aa2*tilt**2)/tilt**4
        assert abs(estimate-aa4)<.0006,(W,tilt,estimate,aa4)
        checks+=2
print('Independent finite Fourier eigenvalue checks:',checks,'PASS')
print('Sample fourth cumulant rate (v=gamma=1):')
for W in (0.,1.,2.,3.):
    print(W,float(24*expected_a4.subs(w,W)))
