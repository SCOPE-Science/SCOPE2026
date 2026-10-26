"""Independent numerical checks of Gaussian two-sided oblique tangent leakage.
Run: python verify_beta_leakage.py. Requires NumPy and SciPy.
"""
import math
import numpy as np
from scipy.special import beta, betainc
from scipy.integrate import quad
rng = np.random.default_rng(738294)
checks = 0

def close(a,b,atol=1e-10,rtol=1e-10):
    global checks
    assert math.isclose(float(a),float(b),abs_tol=atol,rel_tol=rtol),(a,b)
    checks += 1

def exact_tail(s,t):
    alpha=s/2; B=beta(alpha,.5); eps=1/(1+t)
    # x=eps + (1-eps)u, robust enough for moderate eps
    term0=betainc(alpha,.5,eps)
    f=lambda x: (x**(alpha-1)*(1-x)**(-.5)/B)*betainc(alpha,.5,eps/x)
    a=quad(f,eps,(eps+1)/2,epsabs=2e-10,limit=300)[0]
    b=quad(f,(eps+1)/2,1,epsabs=2e-10,limit=300)[0]
    return term0+a+b

# Check actual oblique tangent projector for multiple ambient dimensions, sketch sizes.
for s in (2,3,4,7):
    for m,n in ((s,s),(s+1,s+2)):
        for _ in range(100):
            th=rng.normal(size=(s,m));om=rng.normal(size=(s,n))
            u=np.eye(m)[:,0];w=np.eye(n)[:,0]
            normal=np.outer(np.eye(m)[:,1],np.eye(n)[:,1])
            L=np.outer(u,(th@u)@th)/np.linalg.norm(th@u)**2
            R=np.outer(w,(om@w)@om)/np.linalg.norm(om@w)**2
            delta=L@normal+normal@R.T-L@normal@R.T
            aa=(th@u)@(th@np.eye(m)[:,1])/np.linalg.norm(th@u)**2
            bb=(om@w)@(om@np.eye(n)[:,1])/np.linalg.norm(om@w)**2
            close(np.linalg.norm(delta)**2,aa*aa+bb*bb+aa*aa*bb*bb,atol=2e-9)
            close(delta[0,0],-aa*bb)
            close(delta[0,1],aa)
            close(delta[1,0],bb)

# Moment formula: exact covariance and beta inverse moment.
for s in (3,4,7,20):
    E=((s-1)/(s-2))**2-1
    close(E,2/(s-2)+1/(s-2)**2)
    alpha=s/2
    EH=beta(alpha-1,.5)/beta(alpha,.5)
    close(E,EH**2-1)

# Exact finite-sample tail integral vs independent direct beta quadrature.
from scipy.integrate import dblquad
for s,t in ((2,1.),(3,1.),(4,5.),(2,100.)):
    q=1/(1+t)
    vals=rng.beta(s/2,.5,size=(700000,2))
    sim=np.mean(np.prod(vals,axis=1)<q)
    theo=exact_tail(s,t)
    assert abs(theo-sim)<.006, (s,t,theo,sim)
    checks+=1

# Leading logarithmic prefactor: convergence is slow but positive and comparable.
for s in (2,3,4):
    alpha=s/2; B=beta(alpha,.5)
    prev=None
    for t in (1e3,1e4,1e5):
        actual=exact_tail(s,t)
        asym=(t**(-alpha))*math.log(t)/(alpha*B*B)
        assert actual>0 and 0.65<actual/asym<1.8,(s,t,actual,asym)
        checks+=1

print('PASS',checks,'checks')
