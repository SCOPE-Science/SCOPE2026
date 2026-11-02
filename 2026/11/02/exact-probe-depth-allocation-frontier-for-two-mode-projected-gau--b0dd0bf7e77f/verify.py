"""Reproducible checks of the two-mode projected Gaussian Lanczos trace law.

Run: python verify.py. NumPy is the only dependency. Numerical checks support,
but do not replace, the analytic identities in RESULT.md.
"""
import math
import numpy as np

checks = 0

def near(x, y, tol=2e-10):
    global checks
    assert abs(x-y) <= tol * (1 + abs(y)), (x, y)
    checks += 1

def theory(a, b):
    root = math.sqrt(a*b)
    trace = 1/a + 1/b
    mean1 = 2/root
    bias = trace-mean1
    var1 = 4*(a+b-root)/(a*b)**1.5
    var2 = 2*(1/a**2+1/b**2)
    ncross = 2*(a+b)/(math.sqrt(a)-math.sqrt(b))**2
    mcross = 4*(a*a-a*root+a*b-b*root+b*b)/(math.sqrt(a)-math.sqrt(b))**4
    return trace, mean1, bias, var1, var2, ncross, mcross

rng = np.random.default_rng(7022026)
angles = (np.arange(65536)+0.5)*(2*math.pi/65536)
c2 = np.cos(angles)**2
s2 = 1-c2
for _ in range(90):
    b = math.exp(rng.uniform(-1, 1))
    a = b*math.exp(rng.uniform(0.08, 2.2))
    target, m1, bias, v1, v2, nc, mc = theory(a,b)
    denom=a*c2+b*s2
    near(float(np.mean(1/denom)),1/math.sqrt(a*b),tol=1e-8)
    near(float(np.mean(1/denom**2)),(a+b)/(2*(a*b)**1.5),tol=1e-8)
    near(target-m1,bias)
    near(v2-v1,2*(a+b)*(math.sqrt(a)-math.sqrt(b))**2/(a*b)**2)
    near(nc,(v2-v1)/bias**2)
    near(mc,(2*v2-v1)/bias**2)
    # Exact MSE crossing signs at a fixed Gaussian-probe count.
    near(bias*bias+v1/nc,v2/nc)
    # Matvec budget crossing.
    near(bias*bias+v1/mc,2*v2/mc)
    for factor in [0.25,0.8,1.2,4.0]:
        N = factor * nc
        d=(bias*bias+v1/N)-v2/N
        assert (d < 0) == (factor < 1)
        checks += 1
        M = factor * mc
        d2=(bias*bias+v1/M)-2*v2/M
        assert (d2 < 0) == (factor < 1)
        checks += 1

# Source's reprojected Krylov construction with a genuinely nonzero
# coupling to the resolved subspace.
a,b=4.,1.
A=np.array([[3.,0.3,0.],[0.3,a,0.],[0.,0.,b]])
projector=np.diag([0.,1.,1.])
B=projector@A@projector
Q=np.eye(3)[:,1:]
near(float(np.min(np.linalg.eigvalsh(A)))>0,True)
near(float(np.linalg.norm(Q.T@A@Q-np.diag([a,b]))),0.)
for _ in range(120):
    xi=rng.standard_normal(3)
    u=projector@xi
    q=u/np.linalg.norm(u)
    alpha=q@(B@q)
    one=np.linalg.norm(u)**2/alpha
    # Two-by-two Lanczos: orthogonalize and invert its tridiagonalization.
    w=B@q-alpha*q
    beta=np.linalg.norm(w)
    assert beta>1e-8
    q2=w/beta
    T=np.array([[alpha,beta],[beta,q2@(B@q2)]])
    two=np.linalg.norm(u)**2*np.linalg.inv(T)[0,0]
    exact=u@(Q@np.linalg.inv(Q.T@A@Q)@Q.T)@u
    near(two,exact)
    near(one,np.linalg.norm(u)**4/(u@A@u))

near(theory(4,1)[1],1.)
near(theory(4,1)[2],0.25)
near(theory(4,1)[3],1.5)
near(theory(4,1)[4],2.125)
near(theory(4,1)[5],10.)
near(theory(4,1)[6],44.)
near(theory(4,1)[2]**2+theory(4,1)[3]/20,0.1375)
near(2*theory(4,1)[4]/20,0.2125)

# Seeded finite-sample moment estimates, not a proof.
n=260000
g=rng.standard_normal((n,2))
r2=np.sum(g*g,axis=1)
S1=(r2*r2)/(4*g[:,0]**2+g[:,1]**2)
S2=g[:,0]**2/4+g[:,1]**2
assert abs(S1.mean()-1.)<0.012
assert abs(S1.var()-1.5)<0.045
assert abs(S2.mean()-1.25)<0.015
assert abs(S2.var()-2.125)<0.065
checks += 4
print(f"PASS {checks} analytic-identity, quadrature, matrix-Lanczos, and seeded sampling checks")
