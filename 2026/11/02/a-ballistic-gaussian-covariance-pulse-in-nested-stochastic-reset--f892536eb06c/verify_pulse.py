"""Independent finite-dimensional checks for the nested resetting covariance pulse.

Requires numpy and scipy. The stochastic limits are proved analytically, not
by finite numerical checks. Run: python verify_pulse.py
"""
import math
import numpy as np
from scipy.linalg import expm
from scipy.optimize import brentq
from scipy.special import gammaln, logsumexp

checks = 0

def close(a, b, tol=1e-10):
    global checks
    assert abs(a-b) <= tol * max(1.0, abs(a), abs(b)), (a,b)
    checks += 1

def covariance_matrix(N, D, r):
    # Solve stationary moment equations independently of the closed pulse.
    C = np.zeros((N, N))
    for i in range(N):
        C[i, i] = (C[i-1, i-1] if i>0 else 0.0) + 2*D/r
        for j in range(i):
            # 0=-2r C[j,i]+r C[j-1,i]+r C[j,i-1]
            C[j, i] = ((C[j-1,i] if j>0 else 0.0)+C[j,i-1])/2.0
            C[i, j] = C[j, i]
    return C

def closed_forward(n, t, D, r):
    m=n-1
    z=r*t
    V=2*D/r
    if z==0:
        return V*2.0**(-m)
    k=np.arange(m+1)
    return float(V*np.exp(-m*np.log(2)-z+logsumexp(k*np.log(2*z)-gammaln(k+1))))

def positive_peak(m):
    def root_f(z):
        # log upper term vs lower truncated sum, no overflows.
        k=np.arange(m)
        return float(logsumexp(k*np.log(2*z)-gammaln(k+1))-(m*np.log(2*z)-gammaln(m+1)))
    return brentq(root_f, max(1e-14,m/8), 2.2*m,xtol=1e-12)

for N in (2,3,5,8):
    for D,r in ((1.0,1.0),(0.37,1.8),(4.0,0.21)):
        C=covariance_matrix(N,D,r)
        A=-r*np.eye(N) + r*np.diag(np.ones(N-1),-1)
        V=2*D/r
        for n in range(1,N+1):
            close(C[0,n-1], V*2**(-(n-1)))
            close(C[n-1,n-1], n*V)
            for t in (0.0,0.1/r,1.2/r,3.5/r):
                dyn=C@expm(A.T*t)
                close(dyn[0,n-1],closed_forward(n,t,D,r))
                close(dyn[n-1,0],V*2**(-(n-1))*np.exp(-r*t))

for m in range(1,90):
    z=positive_peak(m)
    close(closed_forward(m+1,z,1.0,1.0),2.0*2.0*np.exp(-z+m*np.log(z)-gammaln(m+1)))
    if m>=3:
        # Exact optimum asymptotically m-1: numerical envelope only, not proof.
        assert m-2 < z < m
        checks += 1

for m in (100,200,500,1000):
    # Evaluate the pulse at its asymptotic location without a high-order root.
    for s in (-1.0,0.0,1.0):
        z=m+s*np.sqrt(m)
        observed=closed_forward(m+1,z,1.0,1.0)
        approx=(4.0/np.sqrt(2*np.pi*m))*np.exp(-s*s/2)
        rel=observed/approx
        assert abs(rel-1)<0.25, (m,s,rel)
        checks+=1

print('checks_passed', checks)
for n in (2,3,4,10,50,100):
    m=n-1
    z=positive_peak(m)
    print('n',n,'r_times_peak',f'{z:.12f}', 'peak_over_V',f'{closed_forward(n,z,1.,1.)/2:.12f}')
