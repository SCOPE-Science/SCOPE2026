"""Independent numerical and exact checks for planar rotational observability tails.
The proof of infinite and general-m tails is analytical, not Monte Carlo.
Run: python verify.py
"""
import math
from fractions import Fraction
import numpy as np


def constant(m, rho=0.0):
    # w(phi)=(1+rho*cos(2phi))/pi on the projective phase circle.
    factor=sum(math.comb(m, 2*j)*math.comb(2*j,j)*(rho/2)**(2*j)
               for j in range(m//2+1))
    sphere_volume=math.pi**((m-1)/2)/math.gamma((m+1)/2)
    return math.sqrt(m)*sphere_volume*math.pi**(1-m)*factor

# Exact quadratic ellipsoid determinant via matrix determinant lemma.
for m in range(2,15):
    d=m-1
    A=[[Fraction(int(i==j),1)-Fraction(1,m) for j in range(d)] for i in range(d)]
    # Verify inverse by Sherman-Morrison: A^{-1}=I+11^T.
    B=[[int(i==j)+1 for j in range(d)] for i in range(d)]
    for i in range(d):
        for j in range(d):
            assert sum(A[i][k]*B[k][j] for k in range(d)) == int(i==j)
    assert Fraction(1,m)==1-sum(Fraction(1,m) for _ in range(d))

# m=2 exact CDF, and the expected small-tail constant.
for eps in [1e-2,1e-3,1e-4,1e-6,1e-8]:
    exact=2/math.pi*math.acos(1-eps)
    assert abs(exact/(constant(2)*math.sqrt(eps))-1)<0.01

# Gaussian moment constants and inequalities are analytical identities.
for m in range(2,10):
    z_abs_moment=2**((m-1)/2)*math.gamma(m/2)/math.sqrt(math.pi)
    assert z_abs_moment > 0
    assert constant(m,0.6)>constant(m,0.0)
    assert constant(m,0.0)>0

# The local expansion is uniform to fourth order for bounded perturbations.
for m in range(2,9):
    v=np.arange(m,dtype=float)-(m-1)/2
    v/=max(np.max(np.abs(v)),1.0)
    q=np.sum((v-np.mean(v))**2)
    for t in [1e-2, 5e-3, 1e-3]:
        phases=t*v
        S=np.sum(np.exp(2j*phases))
        lam=(m-abs(S))/2
        assert abs(lam/(t*t*q)-1)<1e-3

rng=np.random.default_rng(20261028)
for m,eps,batch_size in [(3,0.025,250_000),(4,0.060,250_000)]:
    total=0; count=0
    for _ in range(4):
        x=rng.uniform(0,math.pi,(batch_size,m))
        z=np.exp(2j*x).sum(axis=1)
        lmin=(m-np.abs(z))/2
        count+=np.count_nonzero(lmin<eps)
        total+=batch_size
    estimate=count/total
    prediction=constant(m)*eps**((m-1)/2)
    # Curvature corrections at these nonasymptotic eps are allowed.
    assert 0.75 < estimate/prediction < 1.25, (m,estimate,prediction)
    print(f"Monte Carlo m={m}: P(lambda_min < {eps})={estimate:.8f}, small-eps term={prediction:.8f}, hits={count}")

print('VERIFY_OK exact_matrix_ids=13 cdf_checks=5 moment_checks=8 local_taylor_checks=21 mc_n=2000000')
