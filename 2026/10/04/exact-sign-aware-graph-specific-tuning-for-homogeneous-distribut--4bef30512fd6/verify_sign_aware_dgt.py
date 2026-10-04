import math
import numpy as np

def rr(lam,beta):
    # (z-lam)^2 + beta*lam*(z-1)
    roots=np.roots([1.0, lam*(beta-2.0), lam*lam-beta*lam])
    return max(abs(z) for z in roots)

def rplus(beta,p):
    if p==0: return 0.0
    return (p*(2-beta)+math.sqrt(beta*p*(4*(1-p)+beta*p)))/2

def rminus(beta,n):
    return math.sqrt(n*(n+beta)) if n else 0.0

def closed(p,n):
    rp=math.sqrt(p) if p else 0.0
    rn=(math.sqrt(n*(4+5*n))-n)/2 if n else 0.0
    r=max(rp,rn)
    return 1-r,r

# Endpoint formulas versus direct roots.
for beta in np.linspace(0.01,1.99,50):
    for p in np.linspace(0.0,0.95,20):
        if p: assert abs(rr(p,beta)-rplus(beta,p)) < 2e-12
    for n in np.linspace(0.0,0.95,20):
        if n: assert abs(rr(-n,beta)-rminus(beta,n)) < 2e-12

# Closed optimizer versus a dense grid; grid spacing controls tolerance.
grid=np.linspace(1e-5,1.99999,40001)
for p in np.linspace(0.0,0.95,20):
    for n in np.linspace(0.0,0.95,20):
        bstar,rstar=closed(float(p),float(n))
        vals=np.maximum.reduce([
            np.abs(1-grid),
            np.array([rplus(float(b),float(p)) for b in grid]),
            np.array([rminus(float(b),float(n)) for b in grid])])
        j=int(np.argmin(vals))
        assert abs(grid[j]-bstar) < 6e-5
        assert abs(vals[j]-rstar) < 6e-5
        if p: assert abs(1-(1-math.sqrt(p))-math.sqrt(p)) < 1e-14
        if n:
            bn=1+n/2-math.sqrt(n*(4+5*n))/2
            assert abs((1-bn)**2-n*(n+bn)) < 3e-15

# Negative-only two-agent example W=[[0.2,0.8],[0.8,0.2]].
n=0.6
bstar,rstar=closed(0.0,n)
assert abs(bstar-0.2753049234040402) < 2e-15
assert abs(rstar-0.7246950765959598) < 2e-15
assert rstar < math.sqrt(n)
print('VERIFY_OK')
