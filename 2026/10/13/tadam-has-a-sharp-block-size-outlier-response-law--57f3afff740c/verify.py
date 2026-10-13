import math

def w(nu,d,D):
    return (nu+d)/(nu+D)

def Wstar(beta,nu,d):
    return beta*(nu+d)/(nu*(1-beta))

def mix(beta,nu,d,D):
    ww=w(nu,d,D)
    W=Wstar(beta,nu,d)
    return ww/(W+ww)

for beta in (0.6,0.75,0.9,0.99):
    for nu,d in ((1.0,1),(3.0,5),(10.0,10),(2.5,100)):
        W=beta/(1-beta)
        a=(2*beta-1)/beta
        w0=w(nu,d,0.0)
        for _ in range(10000):
            W=a*W+w0
        assert abs(W-Wstar(beta,nu,d)) < 2e-10*max(1.0,W)
        assert abs(mix(beta,nu,d,0.0)-(1-beta)) < 2e-14

for beta in (0.51,0.7,0.9,0.97):
    for nu,d in ((0.7,1),(2.0,8),(20.0,20)):
        for D in (0.0,0.01,0.2,1.0,5.0,100.0,1e6):
            closed=(1-beta)*nu/(nu+beta*D)
            assert abs(mix(beta,nu,d,D)-closed) < 3e-14*max(1.0,abs(closed))

for beta in (0.55,0.8,0.9,0.99):
    for nu in (0.5,1.0,10.0,100.0):
        Dstar=nu/beta
        def phi(D):
            return (1-beta)*nu*math.sqrt(D)/(nu+beta*D)
        exact=(1-beta)*0.5*math.sqrt(nu/beta)
        assert abs(phi(Dstar)-exact) < 3e-14*max(1.0,exact)
        for factor in (1e-6,1e-3,0.1,0.5,0.9,1.1,2.0,10.0,1e3,1e6):
            assert phi(Dstar*factor) <= exact*(1+2e-14)

for beta in (0.6,0.9,0.99):
    for d in (1,4,16,100):
        for k in (1,max(1,d//2),d):
            z=math.sqrt(d/(beta*k))
            D=k*z*z
            rel=d/(d+beta*D)
            assert abs(rel-0.5) < 2e-14
            assert d/(d+beta*k*(0.999*z)**2) > 0.5
            assert d/(d+beta*k*(1.001*z)**2) < 0.5

beta=0.9
coef=(1-beta)*0.5/math.sqrt(beta)
threshold=1/math.sqrt(beta)
assert abs(coef-0.05270462766947298) < 2e-15
assert abs(threshold-1.0540925533894598) < 2e-15

print("verification passed")
