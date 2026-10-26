#!/usr/bin/env python3
"""Symbolic and spectral checks for the weak periodic-potential dispersion law."""
import numpy as np
import sympy as sp

D,g,v,t=sp.symbols('D gamma v t', positive=True)
N=(D**3*g*t**2+4*D**2*g**2*t+D**2*t**2*v**2+4*D*g**3+
   D*g*t*v**2+2*g**2*v**2+t*v**4)
A=D**2*t+2*D*g+v**2
K=sp.cancel(N/(g*A**2))
Kprime=sp.factor(sp.diff(K,t))
expected=v**2*(5*D**3*g*t+2*D**2*g**2+D**2*t*v**2+3*D*g*v**2+v**4)/(g*A**3)
assert sp.simplify(Kprime-expected)==0
assert sp.simplify(K.subs(v,0)-1/D)==0
assert sp.simplify(K.subs(t,0)-1/(D+v**2/(2*g)))==0
assert sp.simplify(sp.limit(K,t,sp.oo)-(1/D+v**2/(g*D**2)))==0
print('symbolic kernel derivative, limits, and passive case: PASS')
# Derive the coefficient independently from the second-order Bloch resolvent.
k,q=sp.symbols('k q', positive=True, real=True)
z=k+sp.I*q
h=sp.sqrt(g*g+v*v*k*k)
b=v*k/(g+h)
lam=D*k*k-g+h
m=lam-D*z*z
H=(m+2*g+2*b*v*z+b*b*m)/((1+b*b)*(m*(m+2*g)-v*v*z*z))
H0=sp.factor(H.subs(k,0))
H1=sp.factor(sp.diff(H,k).subs(k,0))
assert sp.simplify(H0-(D*q*q+2*g)/(q*q*(D*D*q*q+2*D*g+v*v)))==0
assert sp.factor(-q*q*(H0+sp.I*q*H1)-K.subs(t,q*q))==0
print('Bloch resolvent Taylor coefficient: PASS')


# Independent Fourier--Bloch matrix finite section, not a reimplementation
# of the rational symbolic perturbation coefficient.
def bloch_eigenvalue(eps,k,diff,tumble,speed,coef,num_modes=5):
    # coef gives Fourier coefficients U_n for n>0; U_-n=conjugate(U_n).
    n_vals=np.arange(-num_modes,num_modes+1)
    n_state=2*len(n_vals)
    M=np.zeros((n_state,n_state),complex)
    up={0:0j}
    for n,a in coef.items():
        up[n]=a
        up[-n]=np.conj(a)
    for i,n in enumerate(n_vals):
        z=k+1j*n
        M[2*i:2*i+2,2*i:2*i+2]=[
            [diff*z*z+speed*z-tumble,tumble],
            [tumble,diff*z*z-speed*z-tumble]
        ]
        for j,nn in enumerate(n_vals):
            if nn==n: continue
            b=up.get(int(n-nn),0j)
            if b!=0:
                u_prime=1j*(n-nn)*b
                zz=k+1j*nn
                for state in range(2):
                    M[2*i+state,2*j+state]+=-eps*u_prime*zz
    eigen=np.linalg.eigvals(M)
    dominant=eigen[np.argmax(eigen.real)]
    return float(dominant.real)

cases=[
 (1.0,1.0,2.0,{1:0.5}),
 (0.7,0.9,1.6,{1:0.5,2:-0.2j}),
 (2.0,0.4,1.1,{1:0.3j,2:0.2,3:0.1-0.1j}),
 (0.3,1.2,0.6,{1:0.4,3:0.2j}),
]
for diff,tumble,speed,coef in cases:
    base=diff+speed*speed/(2*tumble)
    spectral_A=0.0
    for n,a in coef.items():
        kval=float(K.subs({D:diff,g:tumble,v:speed,t:n*n}))
        spectral_A+=2*abs(a)**2*kval
    estimates=[]
    for eps in [0.08,0.04]:
        k=0.0007
        deff=(bloch_eigenvalue(eps,k,diff,tumble,speed,coef)
              +bloch_eigenvalue(eps,-k,diff,tumble,speed,coef)
              -2*bloch_eigenvalue(eps,0,diff,tumble,speed,coef))/(2*k*k)
        assert abs(deff-(base-eps*eps*spectral_A))<0.009*eps*eps+0.0002, (deff,base,spectral_A,eps)
        estimates.append((eps,deff,(base-deff)/eps**2))
    assert estimates[1][2]>0
    print('case',diff,tumble,speed,'A=',spectral_A,'data=',estimates)
print('ALL symbolic and independent Fourier--Bloch spectral checks passed')
