#!/usr/bin/env python3
"""Independent finite-dimensional linear-chain diagnostics (not the proof)."""
import math
import numpy as np

m=28
a=4.0
b=4.0*999/1000
r=b/a
eta=1-3*r
kappa=2*r
assert abs(a-4.0)<1e-15 and abs(b-2*kappa)<1e-15

def omega_tau(k):
 th=k*math.pi/m
 om=math.sqrt(a-(-1)**k*b*math.cos(th)**m)
 return om,m*math.tan(th)/om

T=[omega_tau(k)[1] for k in range(1,m//2)]
assert T[0]<T[2]<T[1]<T[3]
for j in range(3,len(T)-1):assert T[j]<T[j+1]
print('critical first thresholds k=1,3,2,4:',*[f'{T[j-1]:.12f}' for j in [1,3,2,4]])

for tau,wanted in [(1.0,0),(3.0,2),(4.474,2),(4.476,4),(4.479,2),(6.0,2)]:
 lam=m/tau
 A=np.zeros((m+2,m+2))
 A[0,1]=1
 A[1,0]=-a;A[1,m+1]=b
 A[2,0]=lam;A[2,2]=-lam
 for j in range(3,m+2):A[j,j-1]=lam;A[j,j]=-lam
 vals=np.linalg.eigvals(A)
 unstable=sum(z.real>1e-7 for z in vals)
 assert unstable==wanted,(tau,unstable,sorted(z.real for z in vals)[-6:])
 print('tau',tau,'unstable',unstable,'spectral_abscissa',max(z.real for z in vals))
print('PASS spectral diagnostics')
