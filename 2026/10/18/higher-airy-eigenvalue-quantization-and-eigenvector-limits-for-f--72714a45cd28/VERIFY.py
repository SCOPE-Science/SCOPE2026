"""Algebraic checks and finite spectral diagnostics for Airy edge quantization.

Requires Python 3, NumPy, and SciPy for the spectral diagnostics.
The limit theorem is analytic and is not inferred from finite computations.
"""
from fractions import Fraction as F
import math
import numpy as np
from scipy.linalg import eigh_tridiagonal
from scipy.special import ai_zeros


def exact_form_test(s, t, r, q):
    s,t,r,q = map(F,(s,t,r,q))
    D = r + 1/r
    L = (r+t)/2
    assert r*r-(s-t)*r == 1
    m = [F(1),r*r,r*r,F(1)]
    c = [r,s*r*r,r,t]
    for j in range(4):
        assert 2*L*m[j] == c[(j-1)%4]+c[j]
    S = sum(1/x for x in c)
    alpha = F(4)/( (1+r*r)*S)
    assert alpha == 2*s*t/(L*(s+t)*D)
    v = [F(1),F(-2),F(3),F(1,2),F(-3,2),F(2),F(0),F(0)]
    mass = sum(m[j%4]*v[j]**2 for j in range(len(v)))
    cross = sum(c[j%4]*q**j*v[j]*v[j+1] for j in range(len(v)-1))
    left = L*mass-cross
    kin = sum(c[j%4]*q**j*(v[j+1]-v[j])**2/2 for j in range(len(v)-1))
    # Add terminal edge with v_{len(v)}=0 (our last v entry is already zero).
    boundary=t*v[0]**2/2
    potential=sum((c[j%4]*(1-q**j)+c[(j-1)%4]*(1-q**(j-1)))*v[j]**2/2 for j in range(1,len(v)))
    assert left==kin+boundary+potential, (left,kin+boundary+potential)
    d=F(7,4)
    increments=[d/(S*x) for x in c]
    assert sum(increments)==d
    assert sum(c[j]*increments[j]**2 for j in range(4)) == d*d/S
    return float(L),float(alpha)


def spectral_test(s,t,eps):
    q=math.exp(-eps)
    h=eps**(1/3)
    n=int(28/h)
    j=np.arange(n-1)
    p=np.ones(n-1)
    p[j%4==1]=s
    p[j%4==3]=t
    edges=0.5*p*np.exp(-eps*j)
    eig=eigh_tridiagonal(np.zeros(n),edges,select='i',select_range=(n-3,n-1),check_finite=False)[0][::-1]
    L=(s+t+math.sqrt(4+(s-t)**2))/4
    kappa=2*s*t*L/((s+t)*math.sqrt(4+(s-t)**2))
    targets=-ai_zeros(3)[0]*kappa**(1/3)
    observed=(L-eig)/h**2
    assert np.all(np.diff(eig)<0)
    assert np.all(observed>0)
    return np.max(np.abs(observed-targets)),observed,targets


if __name__=='__main__':
    exact_form_test('1','1','1','9/10')
    exact_form_test('2','1/2','2','9/10')
    print('EXACT_GROUND_STATE_AND_CELL_TESTS_OK')
    for s,t in [(1.,1.),(2.,.5)]:
        prev=float('inf')
        for eps in (1e-3,1e-4,1e-5):
            error, obs, targets=spectral_test(s,t,eps)
            print('s=',s,'t=',t,'eps=',eps,'max_scaled_error=',round(error,6))
            assert error<prev
            prev=error
    print('FINITE_AIRY_SPECTRAL_DIAGNOSTICS_OK')
