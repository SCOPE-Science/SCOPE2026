"""Finite statistical checks of the exact 3x3 numerical-information loss identities.

Requires NumPy. Run: python numerical_information_check.py
"""
import numpy as np

rng = np.random.default_rng(37051)
n = 400000
x = rng.standard_normal((n, 3)) + 1j * rng.standard_normal((n, 3))
x = x / np.linalg.norm(x, axis=1, keepdims=True)
p = abs(x)**2
B = np.array([[1+2j, 2+1j, 0.3+0.7j],[-0.4+1.3j, 3-0.2j, 1+0.3j],[0.2+0.2j,-1.1+0.5j,1.6+0.4j]], dtype=complex)
z = np.einsum('ni,ij,nj->n', x.conj(),B,x)
off = B-np.diag(np.diag(B))
base = np.sum(abs(off)**2)/12
for r in (0.12,0.5,0.87):
    t=r*p[:,1]+p[:,2]
    ell=np.minimum(t/r,(1-t)/(1-r))
    d=B[1,1]-(1-r)*B[0,0]-r*B[2,2]
    predictor=B[0,0]*(1-t)+B[2,2]*t+d*ell/2
    expected=base+abs(d)**2/24
    observed=np.mean(abs(z-predictor)**2)
    assert abs(observed-expected) < 0.035, (r,observed,expected)
    print('three collinear',r,round(observed,5),round(expected,5))
# Three noncollinear eigenvalues: p recovered from complex numerical value.
predictor=np.einsum('j,nj->n',np.diag(B),p)
observed=np.mean(abs(z-predictor)**2)
assert abs(observed-base) < 0.035
print('three noncollinear',round(observed,5),round(base,5))
# Two eigenvalues: the conditional projector averages the doubly degenerate block.
avg=(B[0,0]+B[1,1])/2
predictor=avg*(p[:,0]+p[:,1])+B[2,2]*p[:,2]
D=B-np.diag([avg,avg,B[2,2]])
expected=np.sum(abs(D)**2)/12
observed=np.mean(abs(z-predictor)**2)
assert abs(observed-expected) < 0.035
print('two eigenvalues',round(observed,5),round(expected,5))
# One eigenvalue: only the scalar trace is visible.
predictor=np.trace(B)/3
expected=(np.sum(abs(B)**2)-abs(np.trace(B))**2/3)/12
observed=np.mean(abs(z-predictor)**2)
assert abs(observed-expected) < 0.035
print('one eigenvalue',round(observed,5),round(expected,5))
print('all finite checks passed')
