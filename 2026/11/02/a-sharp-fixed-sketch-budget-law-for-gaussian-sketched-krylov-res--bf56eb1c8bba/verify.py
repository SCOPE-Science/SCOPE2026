"""Independent numerical checks for Gaussian-sketch Krylov budget theorem.
Run: python verify.py (requires numpy and scipy).
Computations are crosschecks, not replacements for the analytical proof.
"""
import numpy as np
from scipy.special import ndtr
from scipy.stats import f as f_distribution
from scipy.optimize import minimize_scalar


def nodes_and_weights(k, K):
    nodes = (K+1)/2 + (K-1)/2*np.cos(np.arange(k+1)*np.pi/k)
    D = np.array([np.prod([nodes[i]-nodes[j] for j in range(k+1) if j != i]) for i in range(k+1)])
    weights = 1/(nodes*np.abs(D))
    weights /= np.sum(weights)
    return nodes, weights


def logcosh(x):
    return np.logaddexp(x, -x) - np.log(2.)


def theoretical_risk(s, k, K):
    a = np.arccosh((K+1)/(K-1))
    return np.exp(np.log(s-1)-np.log(s-k-1)-2*logcosh(k*a))


for K in (1.5, 4., 13., 100.):
    for k in (1, 2, 3, 4):
        lam, w = nodes_and_weights(k, K)
        p = np.polynomial.chebyshev.chebval((2*lam-(K+1))/(K-1), [0]*k+[1])
        p /= np.polynomial.chebyshev.chebval(-(K+1)/(K-1), [0]*k+[1])
        assert np.isclose(np.sum(w*p*p), 1/np.cosh(k*np.arccosh((K+1)/(K-1)))**2, rtol=1e-9)
        assert max(abs(np.sum(w*p*(lam**j))) for j in range(1,k+1)) < 1e-6
        V = np.stack([np.sqrt(w)*lam**j for j in range(1,k+1)], axis=1)
        residual = np.sqrt(w) - V @ np.linalg.lstsq(V, np.sqrt(w), rcond=None)[0]
        assert np.isclose(residual@residual, np.sum(w*p*p), rtol=2e-8)

rng=np.random.default_rng(1149)
k=2;s=9;K=5.
lam,w=nodes_and_weights(k,K)
A=np.diag(lam)
r=np.sqrt(w)
V=np.column_stack([lam**j *r for j in range(1,k+1)])
least_res=r - V @ np.linalg.lstsq(V,r,rcond=None)[0]
delta2 = least_res@least_res
nsamples=18000
observed=np.empty(nsamples)
for i in range(nsamples):
    S=rng.standard_normal((s,k+1))
    y=np.linalg.lstsq(S@V,S@r,rcond=None)[0]
    observed[i]=np.sum((r-V@y)**2)
expected=delta2*(s-1)/(s-k-1)
assert abs(observed.mean()/expected-1)<0.065, (observed.mean(),expected)
threshold=delta2*(1+k/(s-k+1))
# Exact pivot law: (R/delta²-1)/k * nu = F_{k,nu}
nu=s-k+1
q50=delta2*(1+k/nu*f_distribution.ppf(.5,k,nu))
assert abs(np.mean(observed<=q50)-.5)<.023

for K in (4.,16.,100.,1000.,17.+12.*np.sqrt(2)):
    a=np.arccosh((K+1)/(K-1))
    B=1/np.expm1(2*a)
    target=int(np.floor(B))+1
    for s in (max(40,target+15),max(120,target+25),300):
        all_risks=np.array([theoretical_risk(s,k,K) for k in range(s-1)])
        k_best=int(np.argmin(all_risks))
        assert s-k_best-1==target,(K,s,target,s-k_best-1,B)
print('VERIFY_OK chebyshev_cases=16 gaussian_sketch_draws=18000 finite_budget_cases=15 tie_case=1')
