import math
from statistics import NormalDist

N = NormalDist()
SQRT2PI = math.sqrt(2.0*math.pi)

def phi(z):
    return math.exp(-0.5*z*z)/SQRT2PI

def barphi(z):
    return 0.5*math.erfc(z/math.sqrt(2.0))

def mills(z):
    return barphi(z)/phi(z)

def F(z):
    return z*mills(z)

def bisect(q, lo=0.0, hi=2.0):
    while F(hi) < q:
        hi *= 2.0
    for _ in range(160):
        mid=(lo+hi)/2.0
        if F(mid) < q:
            lo=mid
        else:
            hi=mid
    return (lo+hi)/2.0

def optimum(k):
    r=(k-1.0)/(k+1.0)
    q=1.0/(1.0+r)
    z=bisect(q)
    x=math.sqrt(k)*z/(k+1.0)
    m=N.cdf(r*z)+phi(r*z)*mills(z)
    return r,z,x,m

# The universal large-kappa endpoint constant.
zstar=bisect(0.5)
cstar=zstar*phi(zstar)
assert abs(zstar-0.6120031809624808) < 2e-13
assert abs(cstar-0.20245649018802463) < 2e-13

# Direct source formula and transformed formula agree at representative points.
def source_g(k,x):
    a=(k-1.0)*x/math.sqrt(k)
    b=(k+1.0)*x/math.sqrt(k)
    return N.cdf(a)+math.exp(2.0*x*x)*barphi(b)

for k in [1.01,1.1,2.0,10.0,100.0]:
    r,z,x,m=optimum(k)
    assert abs(source_g(k,x)-m) < 2e-12
    # Local minimum regression check.
    for fac in [0.85,0.95,1.05,1.15]:
        assert source_g(k,x*fac) > m-2e-13

# Endpoint-rate regression checks. These do not prove the asymptotics.
for eps in [2e-2,1e-2,5e-3]:
    r,z,x,m=optimum(1.0+eps)
    assert abs((m-0.5)/math.sqrt(eps/math.pi)-1.0) < 0.015
    assert abs(x*math.sqrt(2.0*eps)-1.0) < 0.015
for k in [100.0,300.0,1000.0]:
    r,z,x,m=optimum(k)
    assert abs((1.0-m)*k-cstar) < 0.002
    assert abs(x*math.sqrt(k)-zstar) < 0.012

print("VERIFY_OK zstar=%.15f cstar=%.15f" % (zstar,cstar))
