import math
import numpy as np

def A(c, mu):
    return np.array([[c, -mu],[1.0, 0.0]])

def rho(M):
    return max(abs(z) for z in np.linalg.eigvals(M))

muc = 3.0 - 2.0*math.sqrt(2.0)
nuc = 3.0 + 2.0*math.sqrt(2.0)

for mu in (0.01, 0.1, muc*0.999, 0.3, 0.7, 0.95):
    r = math.sqrt(mu)
    for c in np.linspace(-2*r, 2*r, 101):
        assert abs(rho(A(c,mu)) - r) < 3e-8

for mu in (0.02, 0.1, muc*0.999, muc*1.001, 0.5, 0.9):
    r = math.sqrt(mu)
    for c1 in np.linspace(-2*r,2*r,51):
        for c2 in np.linspace(-2*r,2*r,51):
            P = A(c2,mu) @ A(c1,mu)
            T = c1*c2 - 2*mu
            D = mu*mu
            assert abs(np.trace(P)-T) < 2e-12
            assert abs(np.linalg.det(P)-D) < 2e-12
            jury = (1-D>0 and 1-T+D>0 and 1+T+D>0)
            if min(abs(1-T+D),abs(1+T+D)) > 1e-7:
                assert (rho(P) < 1.0) == jury

for mu in (0.05, muc, 0.4, 0.9):
    r = math.sqrt(mu)
    P = A(-2*r,mu) @ A(2*r,mu)
    vals = sorted(np.linalg.eigvals(P), key=lambda z: abs(z), reverse=True)
    targets = sorted([-mu*(3+2*math.sqrt(2)), -mu*(3-2*math.sqrt(2))], key=abs, reverse=True)
    assert max(abs(vals[i]-targets[i]) for i in range(2)) < 3e-12

def mu_star(nu):
    s = math.sqrt(nu)
    return ((s-1)/(s+1))**2

assert abs(muc*(3+2*math.sqrt(2))-1.0) < 2e-15
assert abs(nuc*muc-1.0) < 2e-15
assert abs(mu_star(nuc)-muc) < 3e-15
assert mu_star(5.0) < muc
assert mu_star(6.0) > muc

print("verification passed")
