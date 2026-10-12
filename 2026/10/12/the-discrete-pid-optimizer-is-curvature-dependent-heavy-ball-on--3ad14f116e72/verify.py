import cmath
import math
import random

rng = random.Random(350072)

def roots_for(lam, alpha, lr, kd):
    beta = alpha + kd*(1-alpha)*lam
    A = 1 - lr*lam + beta
    disc = A*A - 4*beta
    s = cmath.sqrt(disc)
    return (A+s)/2, (A-s)/2, beta

def jury(lam, alpha, lr, kd):
    beta = alpha + kd*(1-alpha)*lam
    return (lr*lam > 0 and lr*lam < 2*(1+beta) and beta < 1)

def direct_diag(lams, x0, alpha, lr, kd, steps):
    d = len(lams)
    x = list(x0)
    V = [0.0]*d
    D = [0.0]*d
    gprev = [0.0]*d
    xs = [list(x)]
    for _ in range(steps):
        g = [lams[i]*x[i] for i in range(d)]
        Vn = [alpha*V[i] - lr*g[i] for i in range(d)]
        Dn = [alpha*D[i] + (1-alpha)*(g[i]-gprev[i]) for i in range(d)]
        xn = [x[i] + Vn[i] + kd*Dn[i] for i in range(d)]
        V, D, gprev, x = Vn, Dn, g, list(xn)
        xs.append(list(x))
    return xs

# Direct source recurrence versus the eliminated two-step recurrence after one completed update.
for _ in range(400):
    d = rng.randint(1, 7)
    lams = [10**rng.uniform(-1,1) for _ in range(d)]
    alpha = rng.uniform(0.02,0.98)
    L = max(lams)
    kd = rng.uniform(0,0.85/L)
    lr = rng.uniform(0.001,1.5/L)
    x0 = [rng.uniform(-2,2) for _ in range(d)]
    xs = direct_diag(lams,x0,alpha,lr,kd,18)
    for t in range(1,len(xs)-1):
        pred=[]
        for i,lam in enumerate(lams):
            beta = alpha + kd*(1-alpha)*lam
            pred.append((1-lr*lam)*xs[t][i] + beta*(xs[t][i]-xs[t-1][i]))
        for a,b in zip(pred,xs[t+1]):
            assert abs(a-b) < 3e-11*max(1.0,abs(a),abs(b))

# Jury criterion agrees with exact characteristic roots away from the unit circle.
for _ in range(25000):
    lam = 10**rng.uniform(-2,2)
    alpha = rng.uniform(0.01,0.99)
    kd = 10**rng.uniform(-5,1)
    lr = 10**rng.uniform(-5,1)
    z1,z2,beta = roots_for(lam,alpha,lr,kd)
    byroots = max(abs(z1),abs(z2)) < 1-1e-10
    byjury = jury(lam,alpha,lr,kd)
    if min(abs(abs(z1)-1),abs(abs(z2)-1)) > 3e-8:
        assert byroots == byjury

# Exact all-spectrum criterion over random spectral intervals.
for _ in range(1500):
    alpha = rng.uniform(0.02,0.98)
    L = 10**rng.uniform(-1,1)
    mu = L/10**rng.uniform(0,3)
    kd = rng.uniform(0,1.3/L)
    lr = rng.uniform(0.0005,4/L)
    criterion = (kd*L < 1 and 0 < lr*L < 2*(1+alpha+kd*(1-alpha)*L))
    lams = [mu,L] + [10**rng.uniform(math.log10(mu),math.log10(L)) for _ in range(80)]
    actual = all(jury(lam,alpha,lr,kd) for lam in lams)
    assert criterion == actual

# Hard gain boundary: the high-curvature mode is never strictly stable for any positive learning rate.
for alpha in (0.1,0.5,0.9):
    L = 3.0
    for mult in (1.0,1.01,1.5,3.0):
        kd = mult/L
        for lr in (1e-9,1e-5,0.001,0.01,0.1,1.0,10.0):
            z1,z2,beta = roots_for(L,alpha,lr,kd)
            assert max(abs(z1),abs(z2)) >= 1-2e-12

# Exact best isolated-mode rate floor, attained at lr*lambda = 1+beta.
for _ in range(1000):
    lam = 10**rng.uniform(-2,2)
    alpha = rng.uniform(0.01,0.95)
    kd = rng.uniform(0,0.95/lam)
    beta = alpha + kd*(1-alpha)*lam
    lr = (1+beta)/lam
    z1,z2,b = roots_for(lam,alpha,lr,kd)
    target = math.sqrt(beta)
    assert abs(abs(z1)-target) < 2e-12
    assert abs(abs(z2)-target) < 2e-12
    for factor in (0.2,0.5,0.8,1.2,1.8):
        zz1,zz2,_ = roots_for(lam,alpha,lr*factor,kd)
        assert max(abs(zz1),abs(zz2)) + 2e-12 >= target

# Positive loss scaling eventually violates the hard gain condition independently of lr.
for _ in range(500):
    alpha = rng.uniform(0.05,0.95)
    L0 = 10**rng.uniform(-2,2)
    kd = 10**rng.uniform(-4,1)
    ccrit = 1/(kd*L0)
    c = 1.05*ccrit
    L = c*L0
    for lr in (1e-10,1e-6,1e-3,0.1/max(L,1e-30),1/max(L,1e-30)):
        z1,z2,beta = roots_for(L,alpha,lr,kd)
        assert max(abs(z1),abs(z2)) >= 1-2e-12

print('verification passed')
