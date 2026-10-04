import math
import random
import numpy as np

def matrix(h, eta, beta0, beta1):
    beta = beta1*beta1
    S = math.sqrt((1.0+beta0)**2 + beta0**2)
    eta0 = eta/S
    return np.array([
        [1.0-eta0*(1.0+beta0)*(1.0-beta)*h,
         eta0*beta0,
         -eta0*(1.0+beta0)*beta],
        [(1.0-beta)*h, 0.0, beta],
        [0.0, 1.0, 0.0],
    ], dtype=float)

def polynomial(h, eta, beta0, beta1):
    beta = beta1*beta1
    S = math.sqrt((1.0+beta0)**2 + beta0**2)
    eta0 = eta/S
    a = eta0*(1.0-beta)*h
    return np.array([
        1.0,
        -1.0 + a*(1.0+beta0),
        -beta - a*beta0,
        beta,
    ], dtype=float)

def threshold_base(beta0):
    S = math.sqrt((1.0+beta0)**2 + beta0**2)
    return 2.0*S/(1.0+2.0*beta0)

random.seed(350056)

# Matrix characteristic roots agree with the displayed cubic.
for _ in range(3000):
    h = 10.0**random.uniform(-3.0,3.0)
    eta = 10.0**random.uniform(-6.0,0.0)
    beta0 = 10.0**random.uniform(-4.0,2.0)
    beta1 = random.uniform(0.0,0.999)
    rm = np.sort_complex(np.linalg.eigvals(matrix(h,eta,beta0,beta1)))
    rp = np.sort_complex(np.roots(polynomial(h,eta,beta0,beta1)))
    assert np.max(np.abs(rm-rp)) < 2e-8

# Exact stable and unstable sides, independent of beta1.
for _ in range(3000):
    beta0 = 10.0**random.uniform(-5.0,2.0)
    beta1 = random.uniform(0.0,0.999)
    h = 10.0**random.uniform(-2.0,2.0)
    crit = threshold_base(beta0)/h
    for factor,stable in ((0.05,True),(0.5,True),(0.999,True),(1.001,False),(1.5,False)):
        eta = factor*crit
        rho = max(abs(np.linalg.eigvals(matrix(h,eta,beta0,beta1))))
        if stable:
            assert rho < 1.0
        else:
            assert rho > 1.0

# Boundary root is exactly -1 up to floating transcription.
for _ in range(1000):
    beta0 = 10.0**random.uniform(-4.0,2.0)
    beta1 = random.uniform(0.0,0.999)
    h = 10.0**random.uniform(-2.0,2.0)
    eta = threshold_base(beta0)/h
    coeff = polynomial(h,eta,beta0,beta1)
    val = ((coeff[0]*(-1.0)+coeff[1])*(-1.0)+coeff[2])*(-1.0)+coeff[3]
    assert abs(val) < 3e-12

# Noise-factor reparameterization and strict decrease.
prev = None
for k in range(10001):
    beta0 = 100.0*k/10000.0
    gamma = (1.0+beta0)**2 + beta0**2
    a = threshold_base(beta0)
    b = 2.0*math.sqrt(gamma/(2.0*gamma-1.0))
    assert abs(a-b) < 2e-14
    if prev is not None:
        assert a < prev + 1e-14
    prev = a

assert abs(threshold_base(0.0)-2.0) < 1e-15
assert abs(threshold_base(1.0)-2.0*math.sqrt(5.0)/3.0) < 1e-15
assert abs(2.0*math.sqrt(5.0)/3.0 - 1.4907119849998598) < 1e-15
assert abs(threshold_base(1e8)-math.sqrt(2.0)) < 1e-8

# At default beta0=1 the normalized eta0 ceiling is exactly 2/3.
beta0=1.0
S=math.sqrt((1.0+beta0)**2+beta0**2)
assert abs((threshold_base(beta0)/S)-2.0/3.0) < 1e-15

print("verification passed")
