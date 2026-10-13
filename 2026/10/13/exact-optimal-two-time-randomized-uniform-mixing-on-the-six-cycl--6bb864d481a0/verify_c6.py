"""Exact and independent checks of randomized uniform mixing on the six-cycle."""
from sympy import symbols, sqrt, simplify, pi, acos, cos, sin, exp, I, Matrix, Rational, eye, zeros
from sympy import N as numerical

c=symbols('c',real=True)
p=[(2*c*c+2*c-1)**2/9, (1-c*c)*(2*c+1)**2/9, (1-c)**2*(2*c+1)**2/9, 4*(1-c)**3*(1+c)/9]
assert simplify(p[0]+2*p[1]+2*p[2]+p[3]-1)==0
cm=(2-sqrt(6)-sqrt(10))/4
cp=(2-sqrt(6)+sqrt(10))/4
wm=Rational(1,2)+(4*sqrt(10)-3*sqrt(15))/50
wp=1-wm
assert -1<float(numerical(cm,16))<1 and -1<float(numerical(cp,16))<1
assert 0<float(numerical(wm,16))<1 and 0<float(numerical(wp,16))<1
for d in range(4):
    v=simplify(wm*p[d].subs(c,cm)+wp*p[d].subs(c,cp)-Rational(1,6))
    assert v==0, (d,v)
assert simplify(p[1]-p[2] - 2*c*(1-c)*(2*c+1)**2/9)==0
for root in [0,1,Rational(-1,2)]:
    assert simplify(p[1].subs(c,root)-Rational(1,6))!=0
# Independent Fourier character expression for physical-time transition amplitudes.
import numpy as np
from scipy.linalg import expm
A=np.zeros((6,6),dtype=float)
for v in range(6):
    A[v,(v-1)%6]=A[v,(v+1)%6]=1.
times=[float(numerical(acos(cm),16)),float(numerical(acos(cp),16))]
w=[float(numerical(wm,16)),float(numerical(wp,16))]
Msum=np.zeros((6,6))
for tt,ww in zip(times,w):
    U=expm(1j*tt*A)
    Msum+=ww*(np.abs(U)**2)
err=np.max(np.abs(Msum-np.ones((6,6))/6))
assert err<1e-13,err
assert np.max(np.abs(expm(1j*(times[0]+6*np.pi)*A)-expm(1j*times[0]*A)))<1e-13
print('VERIFY_OK normalized=1 exact_uniform_distances=4 exact_minimality_roots=3 independent_matrix_entries=36 max_error=%.2g'%err)
