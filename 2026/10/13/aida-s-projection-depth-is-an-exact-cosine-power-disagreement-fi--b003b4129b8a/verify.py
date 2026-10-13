import math
import random
import numpy as np

def project_pair(m,g,xi):
    q=float(np.dot(g,m))
    return q*g/(float(np.dot(g,g))+xi), q*m/(float(np.dot(m,m))+xi)

def signed_cos(m,g):
    return float(np.dot(m,g))/(np.linalg.norm(m)*np.linalg.norm(g))

random.seed(350087)
rng=np.random.default_rng(350087)

for d in (2,3,8,31):
    for _ in range(500):
        m=rng.normal(size=d)
        g=rng.normal(size=d)
        if np.linalg.norm(m)<1e-8 or np.linalg.norm(g)<1e-8:
            continue
        s=signed_cos(m,g)
        c=abs(s)
        xi=10**random.uniform(-8,1)
        mm,gg=m.copy(),g.copy()
        M0=np.linalg.norm(mm); G0=np.linalg.norm(gg)
        for k in range(1,6):
            M=np.linalg.norm(mm); G=np.linalg.norm(gg)
            mn,gn=project_pair(mm,gg,xi)
            Mnext=np.linalg.norm(mn); Gnext=np.linalg.norm(gn)
            assert abs(Mnext-c*M*(G*G)/(G*G+xi)) < 2e-10*max(1.0,Mnext)
            assert abs(Gnext-c*G*(M*M)/(M*M+xi)) < 2e-10*max(1.0,Gnext)
            if Mnext>1e-12 and Gnext>1e-12:
                assert abs(signed_cos(mn,gn)-s) < 2e-9
            assert Mnext <= (c**k)*M0 + 2e-10
            assert Gnext <= (c**k)*G0 + 2e-10
            mm,gg=mn,gn

# Exact xi=0 cosine-power discrepancy law.
for d in (2,5,17):
    for _ in range(1000):
        m=rng.normal(size=d)
        g=rng.normal(size=d)
        if np.linalg.norm(m)<1e-9 or np.linalg.norm(g)<1e-9:
            continue
        c=abs(signed_cos(m,g))
        D0=np.linalg.norm(m-g)
        mm,gg=m.copy(),g.copy()
        for K in range(1,7):
            mm,gg=project_pair(mm,gg,0.0)
            lhs=np.linalg.norm(mm-gg)
            rhs=(c**K)*D0
            assert abs(lhs-rhs) < 2e-9*max(1.0,D0)

# Orthogonal pairs are annihilated for every xi.
m=np.array([1.0,0.0,0.0])
g=np.array([0.0,2.0,0.0])
for xi in (0.0,1e-20,1e-6,1.0):
    mm,gg=project_pair(m,g,xi)
    assert np.linalg.norm(mm)==0.0 and np.linalg.norm(gg)==0.0

# Collinear xi=0 pairs receive no discrepancy suppression.
m=np.array([2.0,-4.0,1.0])
g=-3.0*m
D0=np.linalg.norm(m-g)
mm,gg=m.copy(),g.copy()
for _ in range(5):
    mm,gg=project_pair(mm,gg,0.0)
    assert abs(np.linalg.norm(mm-gg)-D0)<2e-11

# Source-default K=2 gives c^4 squared-energy factor in xi=0 limit.
for _ in range(1000):
    m=rng.normal(size=7)
    g=rng.normal(size=7)
    c=abs(signed_cos(m,g))
    D0=np.linalg.norm(m-g)
    mm,gg=m.copy(),g.copy()
    for _ in range(2):
        mm,gg=project_pair(mm,gg,0.0)
    if D0>1e-12:
        ratio=np.linalg.norm(mm-gg)**2/(D0*D0)
        assert abs(ratio-c**4)<2e-9

print("verification passed")
