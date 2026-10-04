import math, random

def direct(x0, lam, eta, beta, sigma, eps):
    # Source initialization.
    m0 = 0.0
    d0 = 0.0
    B0 = 0.0

    # t = 0
    g1 = lam*x0
    m1 = g1
    a0 = 0.0
    B1 = B0 - a0*d0*d0
    D1 = max(abs(B1), sigma)
    d1 = m1/D1
    x1 = x0 - eta*d1

    # t = 1
    g2 = lam*x1
    m2 = beta/(1.0+beta)*m1 + 1.0/(1.0+beta)*g2
    a1 = (d1*(m2-m1) + d1*B1*d1) / ((abs(d1)+eps)**4)
    B2 = B1 - a1*d1*d1
    D2 = max(abs(B2), sigma)
    d2 = m2/D2
    x2 = x1 - eta*d2
    return x1,m1,d1,m2,B2,D2,x2

def closed_B2(x0, lam, eta, beta, sigma, eps):
    q = eta*lam/sigma
    u = lam*abs(x0)/sigma
    return eta*lam/(1.0+beta)*(u/(u+eps))**4

random.seed(11)

# Closed forms versus the direct recurrence.
for _ in range(1000):
    x0 = (1.0 if random.random() < 0.5 else -1.0)*10.0**random.uniform(-8,3)
    lam = 10.0**random.uniform(-3,3)
    eta = 10.0**random.uniform(-5,-1)
    beta = random.uniform(0.01,0.99)
    sigma = 10.0**random.uniform(-4,0)
    eps = 10.0**random.uniform(-8,-2)
    x1,m1,d1,m2,B2,D2,x2 = direct(x0,lam,eta,beta,sigma,eps)
    q = eta*lam/sigma
    assert abs(x1-(1.0-q)*x0) < 2e-11*max(1.0,abs(x1))
    m2_closed = lam*x0*(1.0-q/(1.0+beta))
    assert abs(m2-m2_closed) < 2e-11*max(1.0,abs(m2))
    b2_closed = closed_B2(x0,lam,eta,beta,sigma,eps)
    assert abs(B2-b2_closed) < 2e-10*max(1.0,abs(B2),abs(b2_closed))
    if B2 <= sigma:
        x2_closed = (1.0-2.0*q+q*q/(1.0+beta))*x0
        assert abs(x2-x2_closed) < 2e-10*max(1.0,abs(x2))

# Universal inactive region q <= 1 + beta.
for _ in range(1000):
    beta = random.uniform(0.01,0.99)
    sigma = 10.0**random.uniform(-4,0)
    lam = 10.0**random.uniform(-2,2)
    q = random.uniform(1e-6, 1.0+beta)
    eta = q*sigma/lam
    eps = 10.0**random.uniform(-8,-2)
    x0 = (1.0 if random.random() < 0.5 else -1.0)*10.0**random.uniform(-10,8)
    *_,B2,D2,x2 = direct(x0,lam,eta,beta,sigma,eps)
    assert B2 < sigma*(1.0+2e-12)
    assert abs(D2-sigma) < 2e-12*max(1.0,sigma)

# Active region q > 1 + beta and exact initialization boundary.
for _ in range(500):
    beta = random.uniform(0.05,0.95)
    sigma = 10.0**random.uniform(-4,-1)
    lam = 10.0**random.uniform(-2,2)
    q = (1.0+beta)*random.uniform(1.01,20.0)
    eta = q*sigma/lam
    eps = 10.0**random.uniform(-7,-3)
    threshold = sigma*eps/(lam*((q/(1.0+beta))**0.25-1.0))
    for factor,active in ((0.5,False),(0.999,False),(1.001,True),(2.0,True)):
        x0 = threshold*factor
        *_,B2,D2,x2 = direct(x0,lam,eta,beta,sigma,eps)
        if active:
            assert B2 > sigma
            assert abs(D2-B2) < 2e-12*max(1.0,B2)
        else:
            assert B2 < sigma
            assert abs(D2-sigma) < 2e-12*max(1.0,sigma)

# Paper-scale illustration.
beta = 0.9
sigma = 0.01
eps = 1e-4
eta = 0.01
for lam in (0.1,1.0,1.9):
    q = eta*lam/sigma
    assert q <= 1.0+beta
    for x0 in (1e-12,1e-6,1.0,1e12):
        *_,B2,D2,x2 = direct(x0,lam,eta,beta,sigma,eps)
        assert B2 < sigma*(1.0+2e-12)
        assert abs(D2-sigma) < 2e-12*max(1.0,sigma)

print("verification passed")
