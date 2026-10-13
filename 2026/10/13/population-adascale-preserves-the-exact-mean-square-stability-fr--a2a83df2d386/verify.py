import math
from math import comb

def moments(a,b,p):
    mu=p*a+(1-p)*b
    q=p*a*a+(1-p)*b*b
    v=q-mu*mu
    return mu,v,q

def direct_factor(a,b,p,S,alpha):
    mu,v,q=moments(a,b,p)
    d=mu*mu+v/S
    r=q/d
    total=0.0
    for k in range(S+1):
        prob=comb(S,k)*(p**k)*((1-p)**(S-k))
        abar=(k*a+(S-k)*b)/S
        total += prob*(1-alpha*r*abar)**2
    return total,r

def formula_factor(mu,v,q,S,alpha):
    d=mu*mu+v/S
    return 1+(q/d)*(alpha*alpha*q-2*alpha*mu)

cases=[(0.2,2.3,0.35),(0.5,4.0,0.7),(1.0,1.0,0.4)]
for a,b,p in cases:
    mu,v,q=moments(a,b,p)
    threshold=2*mu/q
    optimum=mu/q
    for S in (1,2,3,8,16):
        for alpha in (0.1*threshold,0.7*threshold,threshold,1.2*threshold,optimum):
            direct,r=direct_factor(a,b,p,S,alpha)
            closed=formula_factor(mu,v,q,S,alpha)
            assert abs(direct-closed)<2e-12*max(1.0,abs(closed))
            assert abs(r-q/(mu*mu+v/S))<2e-13
        below=formula_factor(mu,v,q,S,0.999*threshold)
        edge=formula_factor(mu,v,q,S,threshold)
        above=formula_factor(mu,v,q,S,1.001*threshold)
        assert below<1.0
        assert abs(edge-1.0)<3e-12
        assert above>1.0
        qstar=formula_factor(mu,v,q,S,optimum)
        target=v/(S*mu*mu+v) if v>0 else 0.0
        assert abs(qstar-target)<3e-12
        eps=1e-5*max(1.0,optimum)
        assert qstar <= formula_factor(mu,v,q,S,optimum-eps)+1e-14
        assert qstar <= formula_factor(mu,v,q,S,optimum+eps)+1e-14
        # Fixed linear scaling has the stated exact base-rate ceiling.
        lin_thr=2*mu/(S*mu*mu+v)
        def lin_factor(alpha):
            return 1-2*alpha*S*mu+alpha*alpha*S*S*(mu*mu+v/S)
        assert lin_factor(0.999*lin_thr)<1.0
        assert abs(lin_factor(lin_thr)-1.0)<3e-12
        assert lin_factor(1.001*lin_thr)>1.0
        if S>1:
            assert lin_thr < threshold + 1e-14

# Strict scale improvement at the optimal base rate when variance is positive.
a,b,p=0.1,3.0,0.4
mu,v,q=moments(a,b,p)
optimum=mu/q
vals=[formula_factor(mu,v,q,S,optimum) for S in (1,2,4,8,16,32)]
assert all(vals[i+1]<vals[i] for i in range(len(vals)-1))

print('verification passed')
