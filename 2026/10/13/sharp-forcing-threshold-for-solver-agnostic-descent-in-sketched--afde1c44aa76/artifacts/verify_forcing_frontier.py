import math
import numpy as np

def frontier(a,b):
    return 2.0*math.sqrt(a*b)/(a+b)

for a,b in [(2.0,10.0),(1.0,9.0),(3.0,27.0),(5.0,5.0)]:
    assert a>0 and b>=a
    g=np.array([math.sqrt(a/(a+b)), math.sqrt(b/(a+b))])
    H=np.diag([a,b])
    Hinv_g=np.linalg.solve(H,g)
    R=float(g@Hinv_g)/(np.linalg.norm(g)*np.linalg.norm(Hinv_g))
    eta_star=frontier(a,b)
    assert abs(R-eta_star)<1e-12

    rho=eta_star*np.linalg.norm(g)*Hinv_g/np.linalg.norm(Hinv_g)
    s=np.linalg.solve(H,-g+rho)
    assert abs(float(g@s))<1e-12

    if b>a:
        eta=min(0.999999, eta_star+0.05)
        if eta>eta_star:
            rho2=eta*np.linalg.norm(g)*Hinv_g/np.linalg.norm(Hinv_g)
            s2=np.linalg.solve(H,-g+rho2)
            assert float(g@s2)>0

# Source-compatible least-squares realization.
mu=1.0
lam1=1.0
lam2=17.0
a=lam1+mu
b=lam2+mu
J=np.diag([math.sqrt(lam1),math.sqrt(lam2)])
B=J.T@J
g=np.array([math.sqrt(a/(a+b)),math.sqrt(b/(a+b))])
F=np.linalg.solve(J.T,g)
assert np.linalg.norm(J.T@F-g)<1e-12
assert np.linalg.norm(B-np.diag([lam1,lam2]))<1e-12

# Direct random checks below the frontier.
rng=np.random.default_rng(12345)
eta=0.99*frontier(a,b)
H=B+mu*np.eye(2)
for _ in range(10000):
    gg=rng.normal(size=2)
    if np.linalg.norm(gg)<1e-14:
        continue
    rr=rng.normal(size=2)
    rr=eta*np.linalg.norm(gg)*rr/np.linalg.norm(rr)
    ss=np.linalg.solve(H,-gg+rr)
    assert float(gg@ss)<1e-10

print("VERIFY_OK")
