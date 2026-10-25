"""Numerical checks for low-dilation Fourier concentration coefficients.
Requires numpy, scipy, sympy. Not a proof of the asymptotic theorem.
"""
import numpy as np
from scipy.special import roots_legendre
from fractions import Fraction
from sympy import Matrix, Rational, pi, factorial

E=[(Rational(-1),Rational(-1,4)),(Rational(2,5),Rational(7,5))]
F=[(Rational(-1,2),Rational(-1,10)),(Rational(1,5),Rational(7,10))]

def m(k, regions):
    return sum((b**(k+1)-a**(k+1))/(k+1) for a,b in regions)
def h(n, regions):
    if n==0: return m(0,regions)
    H0=Matrix([[m(i+j,regions) for i in range(n)] for j in range(n)]).det()
    H1=Matrix([[m(i+j,regions) for i in range(n+1)] for j in range(n+1)]).det()
    return H1/H0

def quadrature(intervals,k=90):
    z,v=roots_legendre(k)
    xs=[];ws=[]
    for a,b in intervals:
        a=float(a);b=float(b)
        xs.extend(((b-a)*z/2+(b+a)/2).tolist())
        ws.extend(((b-a)*v/2).tolist())
    return np.array(xs),np.array(ws)

x,wx=quadrature(E); u,wu=quadrature(F)
print('moments:')
for n in range(4):
    he,hf=h(n,E),h(n,F)
    C= (2*pi)**(2*n)/factorial(n)**2*he*hf
    print('n',n,'hE',he,'hF',hf,'coefficient',float(C))

for scale in [0.30,0.20,0.13]:
    mat = np.exp(-2j*np.pi*scale*x[:,None]*u[None,:])*np.sqrt(wx[:,None]*wu[None,:])
    sing=np.linalg.svd(mat,compute_uv=False)
    actual=scale*sing[:3]**2
    ratios=[]
    for n in range(3):
        C=(2*pi)**(2*n)/factorial(n)**2*h(n,E)*h(n,F)
        ratios.append(round(float(actual[n]/(scale**(2*n+1)*float(C))),7))
    print(f'scale {scale:.2f} ratio_to_proved_leading_coefficients {ratios}')

# Input singular functions approach orthogonal polynomials, with phases disregarded.
V=np.vander(x,N=3,increasing=True)
Q,_=np.linalg.qr(np.sqrt(wx)[:,None]*V)
for scale in [.20,.13,.08]:
    mat = np.exp(-2j*np.pi*scale*x[:,None]*u[None,:])*np.sqrt(wx[:,None]*wu[None,:])
    # Input right singular vectors (L2(E)) are rows of Vh.
    _,_,vh=np.linalg.svd(mat,full_matrices=False)
    overlaps=[abs(np.vdot(Q[:,n],vh[n,:].conj())) for n in range(3)]
    print('scale',scale,'input_mode_overlaps',list(np.round(overlaps,7)))
