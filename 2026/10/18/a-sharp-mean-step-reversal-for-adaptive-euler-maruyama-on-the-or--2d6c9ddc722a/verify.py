"""Reproduce the exact algebra and illustrative stationary quadrature.

Only the Python standard library is required. The analytical theorem does not
rely on these finite checks.
"""
from fractions import Fraction as F
from math import exp, sqrt, pi, fsum
from random import Random

rng = Random(260810855)
checks = 0
# Algebraic identity for arbitrary finite distributions and positive step values.
# Define the implied noise equilibrium moment v through the stationarity balance.
for _ in range(2000):
    n = rng.randint(2, 8)
    p = [F(rng.randint(1, 20)) for _ in range(n)]
    p = [x / sum(p) for x in p]
    xs = [F(rng.randint(-12, 12), 7) for _ in range(n)]
    hs = [F(rng.randint(1, 15), 12) for _ in range(n)]
    lam = F(1)
    c = lam / 2
    H = sum(x * y for x, y in zip(p, hs))
    V = sum(t * x * x for t, x in zip(p, xs))
    Z = sum(t * h * x * x for t, h, x in zip(p, hs, xs))
    Q = sum(t * h * h * x * x for t, h, x in zip(p, hs, xs))
    Delta = H * V - Z
    S = sum(t * (h - H)**2 * x*x for t,h,x in zip(p, hs, xs))
    v = (Z - c * Q) / H
    lhs = V - v / (1-c*H)
    rhs = ((1-2*c*H)*Delta+c*S) / (H*(1-c*H))
    assert lhs == rhs
    checks += 1

def stationary(h0, epsilon, lam=1., sigma=sqrt(2.), k=1.):
    # Midpoint quadrature of the Gaussian Markov kernel on [-18, 18].
    # This is a numerical illustration, not proof of the infinite-chain law.
    n = 721
    dx = 36./n
    grid = [-18+(j+.5)*dx for j in range(n)]
    hh = [h0+epsilon*exp(-k*x*x) for x in grid]
    weights = [exp(-x*x/(2*(sigma*sigma/(2*lam*(1-lam*h0/2))))) for x in grid]
    tot = fsum(weights)
    p = [z/tot for z in weights]
    K = []
    for x,h in zip(grid,hh):
        a = (1-lam*h)*x
        s = sigma*sqrt(h)
        row=[exp(-.5*((y-a)/s)**2) for y in grid]
        ss=fsum(row)
        K.append([v/ss for v in row])
    for iteration in range(400):
        q=[0.]*n
        for weight,row in zip(p,K):
            for j,val in enumerate(row): q[j] += weight*val
        if max(abs(x-y) for x,y in zip(q,p)) < 1e-13:
            p=q
            break
        p=q
    H=fsum(w*h for w,h in zip(p,hh))
    V=fsum(w*x*x for w,x in zip(p,grid))
    Delta=H*V-fsum(w*h*x*x for w,h,x in zip(p,hh,grid))
    S=fsum(w*(h-H)**2*x*x for w,h,x in zip(p,hh,grid))
    v=sigma*sigma/(2*lam)
    gap=V-v/(1-lam*H/2)
    identity=((1-lam*H)*Delta+lam*S/2)/(H*(1-lam*H/2))
    assert abs(gap-identity) < 1e-8, (gap, identity)
    return H,V,gap,identity

for h0, wanted in ((.65,+1), (1.4,-1)):
    H,V,gap,identity = stationary(h0,.05)
    assert gap*wanted > 1e-3, (h0,gap)
    checks += 2
    print('fixed baseline', h0, 'mean adaptive step', round(H,9),
          'adaptive variance', round(V,9),
          'variance gap', round(gap,9))
print(checks,'checks passed; finite computations supplement analytical proof')
