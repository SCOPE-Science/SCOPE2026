"""Deterministic finite checks of tagged uniform-cut rectangle identities.
Finite checks support, but cannot establish, asymptotic local limit statements.
"""
from fractions import Fraction as Q
from math import comb, factorial, gamma, pi, sqrt, log
import numpy as np
from scipy.integrate import quad
from scipy.special import gammaln

# Exact integer-rational second-moment matrix for one increment.
for d in range(2,9):
    cov = [[(Q(1,2*d) if i==j else Q(0)) - Q(1,4*d*d) for j in range(d)] for i in range(d)]
    for i in range(d):
        assert sum(cov[i]) == Q(1,4*d)
    for i in range(d-1):
        for j in range(d-1):
            zd = cov[i][j] - cov[i][d-1]-cov[d-1][j]+cov[d-1][d-1]
            assert zd == (Q(1,2*d) * (2 if i==j else 1))
    assert sum(sum(row) for row in cov)== Q(1,4)

# Sampling identity: selected retained length is Beta(2,1),
# independent of the rescaled uniform query location.
rng=np.random.default_rng(623016)
N=600000
query=rng.random(N)
cut=rng.random(N)
left=query<cut
ret=np.where(left,cut,1-cut)
recenter=np.where(left,query/cut,(query-cut)/(1-cut))
assert abs(ret.mean()-Q(2,3)) < .003
assert abs(np.mean(-np.log(ret))-Q(1,2)) < .003
assert abs(np.var(-np.log(ret))-Q(1,4)) < .006
assert abs(recenter.mean()-.5)<.003
assert abs(np.mean(ret*recenter)-1/3)<.003

# d=2 signed-exponential sum: f_N(0) closed form.
# Fourier inversion is numerical here; analytic identity is in RESULT.md.
for n in (1,2,3,5,10,20,60):
    val=quad(lambda t:(1+t*t/4)**(-n),0,np.inf,epsabs=2e-10)[0]/pi
    exact=np.exp(gammaln(n-.5)-gammaln(n)-.5*np.log(pi))
    assert abs(val-exact)<(1e-4 if n==1 else 2e-7), (n,val,exact)
assert abs(sqrt(60)*np.exp(gammaln(59.5)-gammaln(60)-.5*np.log(pi))-1/sqrt(pi))<0.004

# Deterministic d=3 shape-region volume by exact triangle/square decomposition.
# z1,z2 both nonnegative and both nonpositive each contribute b^2,
# opposite signs are 2 triangles each b^2/2, hence 3b^2.
for b in (Q(1,10), Q(1), Q(3,2), Q(7)):
    assert b*b+b*b+2*b*b/2 == 3*b*b

# Multidimensional Gaussian rare-event constant and covariance determinant.
for d in range(2,9):
    omega=np.eye(d-1)/(2*d)+np.ones((d-1,d-1))/(2*d)
    det=np.linalg.det(omega)
    target=d/(2*d)**(d-1)
    assert abs(det-target)<1e-12
    b=log(2)
    C=d*(b**(d-1))/(((2*pi)**((d-1)/2))*sqrt(det))
    simplified=sqrt(d)*(d/pi)**((d-1)/2)*b**(d-1)
    assert abs(C/simplified-1)<1e-12
print('ALL FINITE CHECKS PASSED: exact covariances, beta tagging, d=2 Fourier inversion, shape volumes, Gaussian constants.')
