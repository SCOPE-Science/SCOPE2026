import math

def accepted_u(r, eta, beta):
    c = 2.0 - eta
    t = 1.0
    while t*r > c:
        t *= beta
    return t*r

def qbound(eta, r0, beta):
    return max(1.0-min(r0,beta*(2.0-eta)), 1.0-eta)

def qopt(r0,beta):
    h=2.0*beta/(1.0+beta)
    return 1.0-min(r0,h), min(r0,h)

for beta in [0.2,0.5,0.8]:
    for eta in [0.1,0.4,0.7,0.95]:
        c=2.0-eta
        for r in [0.03,0.5,c,1.000001*c,3*c,100*c]:
            u=accepted_u(r,eta,beta)
            assert u <= c*(1+1e-14)
            if r <= c:
                assert abs(u-r) < 1e-14
            else:
                assert u > beta*c*(1-1e-13)

for beta in [0.25,0.5,0.75]:
    for r0 in [0.05,0.3,0.8,1.5]:
        qstar, etastar=qopt(r0,beta)
        assert 0.0 < etastar < 1.0
        # Dense eta check of minimax envelope.
        vals=[]
        for j in range(1,20000):
            eta=j/20000.0
            vals.append(qbound(eta,r0,beta))
        assert qstar <= min(vals) + 1e-4
        assert abs(qbound(etastar,r0,beta)-qstar) < 1e-12
        # Dense raw-step stress test.
        qb=qbound(etastar,r0,beta)
        for j in range(1,10000):
            r=r0*math.exp(j*math.log(1e4/r0)/9999.0) if r0<1e4 else r0+j
            u=accepted_u(r,etastar,beta)
            assert abs(1.0-u) <= qb + 1e-12

print("VERIFY_OK")
