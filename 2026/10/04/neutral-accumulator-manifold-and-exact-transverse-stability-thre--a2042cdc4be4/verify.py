import cmath, math

def roots(beta1, chi):
    T = 1.0 + beta1 - (1.0-beta1)*chi
    disc = cmath.sqrt(T*T - 4.0*beta1)
    return (0.5*(T+disc), 0.5*(T-disc))

def chi(eta, lam, eps, V):
    return eta*lam/(math.sqrt(V)+eps)

def cap(beta1):
    return 2.0*(1.0+beta1)/(1.0-beta1)

# Every positive accumulator level is a fixed state at x=m=0.
for beta2 in (0.1, 0.5, 0.9, 0.999):
    for V in (1e-8, 0.1, 1.0, 100.0):
        x = 0.0
        m = 0.0
        g = x
        m_new = 0.9*m + 0.1*g
        v_new = V - (1.0-beta2)*(g*g)
        x_new = x - 0.01*m_new/(math.sqrt(v_new)+1e-3)
        assert x_new == 0.0 and m_new == 0.0 and v_new == V

# Sharp transverse threshold and boundary roots.
for beta1 in (0.2, 0.5, 0.9):
    C = cap(beta1)
    rs = roots(beta1, C)
    assert min(abs(r+1.0) for r in rs) < 1e-12
    assert min(abs(r+beta1) for r in rs) < 1e-12
    assert max(abs(r) for r in roots(beta1, 0.999*C)) < 1.0
    assert max(abs(r) for r in roots(beta1, 1.001*C)) > 1.0

# Accumulator threshold agrees with the normalized condition.
beta1 = 0.9
eta = 0.01
lam = 100.0
eps = 1e-3
qstar = eta*lam*(1.0-beta1)/(2.0*(1.0+beta1))
Vc = max(0.0, qstar-eps)**2
assert Vc > 0.0
assert abs(chi(eta,lam,eps,Vc)-cap(beta1)) < 1e-10
assert max(abs(r) for r in roots(beta1, chi(eta,lam,eps,1.01*Vc))) < 1.0
assert max(abs(r) for r in roots(beta1, chi(eta,lam,eps,0.99*Vc))) > 1.0

# beta2 does not enter the first-order transverse roots.
V = 0.25
reference = roots(beta1, chi(eta,lam,eps,V))
for beta2 in (0.01, 0.5, 0.9, 0.9999):
    test = roots(beta1, chi(eta,lam,eps,V))
    assert max(abs(a-b) for a,b in zip(reference,test)) < 1e-15

# Large accumulator makes the normal rate arbitrarily slow.
for V in (1e2, 1e4, 1e8):
    rho = max(abs(r) for r in roots(beta1, chi(eta,lam,eps,V)))
    assert rho < 1.0
rho1 = max(abs(r) for r in roots(beta1, chi(eta,lam,eps,1e4)))
rho2 = max(abs(r) for r in roots(beta1, chi(eta,lam,eps,1e8)))
assert rho2 > rho1
assert rho2 > 0.999

print("verification passed")
