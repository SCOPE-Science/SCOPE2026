import math
from statistics import NormalDist

N=NormalDist()

def w_log(z,tau):
    x=z/tau
    return 2.0/(x+2.0+math.sqrt(x*x+4.0))

def w_ent(z,tau):
    return 1.0/(1.0+math.exp(z/tau))

def w_ptb(z,tau):
    return N.cdf(-z/tau)

def r_log(e,tau):
    return tau*(1.0-2.0*e)/(e*(1.0-e))

def r_ent(e,tau):
    return tau*math.log((1.0-e)/e)

def r_ptb(e,tau):
    return tau*N.inv_cdf(1.0-e)

def j_log(e,tau):
    return e*e*(1-e)*(1-e)/(tau*(1-2*e+2*e*e))

def j_ent(e,tau):
    return e*(1-e)/tau

def phi(x):
    return math.exp(-x*x/2.0)/math.sqrt(2.0*math.pi)

def j_ptb(e,tau):
    return phi(N.inv_cdf(1.0-e))/tau

for tau in (0.3,1.0,2.7):
    for e in (0.2,0.05,0.01,0.001):
        for wfun,rfun,jfun in ((w_log,r_log,j_log),(w_ent,r_ent,j_ent),(w_ptb,r_ptb,j_ptb)):
            z=rfun(e,tau)
            assert abs(wfun(z,tau)-e) < 2e-12
            h=1e-6*max(1.0,abs(z))
            fd=abs((wfun(z+h,tau)-wfun(z-h,tau))/(2*h))
            assert abs(fd-jfun(e,tau)) <= 5e-6*max(1.0,jfun(e,tau))

tau=1.0
for R in (8.0,12.0,20.0):
    assert w_ptb(R,tau) < w_ent(R,tau) < w_log(R,tau)

for e in (1e-4,1e-6):
    assert j_log(e,tau) < j_ent(e,tau) < j_ptb(e,tau)
    assert r_ptb(e,tau) < r_ent(e,tau) < r_log(e,tau)

print("VERIFY_OK")
