"""Reproducibility checks for the exact Gaussian PALD observation-law theorem.
Run with Python 3 and NumPy. Mathematical universality is proved in RESULT.md.
"""
import math
import numpy as np

G = np.array([[1.0], [1.0], [1.0]]) / math.sqrt(3)
B = np.column_stack((np.array([1.,-1.,0.])/math.sqrt(2),
                     np.array([1.,1.,-2.])/math.sqrt(6)))
n,k = 3,1
I=np.eye(n)
assert np.allclose(G.T @ G, np.eye(k), atol=2e-15)
assert np.allclose(B.T @ B, np.eye(n-k), atol=2e-15)
assert np.allclose(G.T @ B, np.zeros((k,n-k)), atol=2e-15)
assert np.allclose(B@B.T, I-G@G.T, atol=2e-15)

sigma_b2,sigma_c2=1.,1.
s=sigma_b2+sigma_c2
cov_Z = s*I+B@B.T
assert np.allclose(np.linalg.eigvalsh(cov_Z), [2.,3.,3.], atol=2e-14)
assert not np.allclose(cov_Z, np.trace(cov_Z)/n*I)
assert np.allclose(B.T@cov_Z@B, (1+s)*np.eye(2), atol=2e-14)
assert np.allclose(B.T@B, np.eye(2), atol=2e-14) # Cov(B^T Z, xi | eta)
mi = (n-k)/2 * math.log1p(1/s)
assert math.isclose(mi, math.log(1.5), abs_tol=2e-15)

eta=np.array([0.8]); xi=np.array([0.2,-0.35]); latent=G@eta+B@xi
z=np.array([1.1, -0.5, 0.3])
def gaussian_density(z,mu,cov):
    d=z-mu
    sign,logdet=np.linalg.slogdet(cov)
    assert sign>0
    return math.exp(-0.5*(len(z)*math.log(2*math.pi)+logdet+d@np.linalg.solve(cov,d)))

for variance_pair in [(1.0,1.0),(0.5,1.5),(0.1,1.9)]:
    c,b=variance_pair
    assert abs(c+b-s) < 1e-14
    v=gaussian_density(z,latent,(c+b)*I)
    v0=gaussian_density(z,latent,2*I)
    assert math.isclose(v,v0,rel_tol=1e-14)

# A log likelihood depending on s alone has proportional score derivatives.
info_s=3/(2*s*s)   # conditional on fixed X, n-dimensional normal with known mean
info2=info_s*np.ones((2,2))
assert np.allclose(np.linalg.eigvalsh(info2),[0,2*info_s],atol=2e-15)
print('VERIFY_OK')
print('covariance_eigenvalues',np.linalg.eigvalsh(cov_Z))
print('hidden_channel_mutual_information_nats',format(mi,'.15f'))
print('conditional_observation_density',format(gaussian_density(z,latent,2*I),'.15e'))
print('variance_split_information_eigenvalues',np.linalg.eigvalsh(info2))
