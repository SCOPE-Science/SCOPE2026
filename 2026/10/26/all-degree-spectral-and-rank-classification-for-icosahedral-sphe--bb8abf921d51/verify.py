#!/usr/bin/env python3
"""Independent finite-dimensional checks of icosahedral harmonic sampling formulas."""
import numpy as np
from scipy.special import sph_harm_y
from sympy import legendre, sqrt, simplify
from math import pi

phi=(1+5**0.5)/2
v=[]
for a in (-1,1):
 for b in (-1,1):
  v.extend([[0,a,b*phi],[a,b*phi,0],[b*phi,0,a]])
v=np.array(v,dtype=float)
v/=np.linalg.norm(v,axis=1)[:,None]
assert len(v)==12
D=v@v.T
assert np.allclose(np.sort(np.unique(np.round(D.flatten(),9))),np.array([-1,-5**-.5,5**-.5,1]))
assert np.allclose(v.T@v,4*np.eye(3))
print('icosahedral geometry: 12 vertices, 6 antipodal axes, tight frame checked')
for ell in range(0,26):
 p=float(legendre(ell,1/sqrt(5)))
 z=v[:,2]; az=np.arctan2(v[:,1],v[:,0]); colat=np.arccos(np.clip(z,-1,1))
 mat=np.stack([sph_harm_y(ell,m,colat,az) for m in range(-ell,ell+1)],axis=1)
 gr=(4*pi/12)*(mat@mat.conj().T)
 vals=np.linalg.eigvalsh(gr)
 if ell%2==0:
  expected=np.array([0]*6+[(2*ell+1)/6*(1+5*p)]+[(2*ell+1)/6*(1-p)]*5)
 else:
  expected=np.array([0]*6+[(2*ell+1)/6*(1+5**.5*p)]*3+[(2*ell+1)/6*(1-5**.5*p)]*3)
 assert np.max(np.abs(vals-np.sort(expected)))<1.e-10,(ell, vals,expected)
 print(f'ell={ell:02d}: p={p:+.9f}, rank={np.count_nonzero(vals>1e-8)}, error={np.max(abs(vals-np.sort(expected))):.2e}')
print('All 26 spherical-harmonic Gram spectra match the exact formulas.')
for ell in [0,2,4,6,8,10,12,14,16,18]:
 print('even Legendre',ell,simplify(legendre(ell,1/sqrt(5))))
for ell in [1,3,5]:
 print('odd Legendre',ell,simplify(legendre(ell,1/sqrt(5))))
