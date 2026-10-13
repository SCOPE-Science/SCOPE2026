import itertools
import math

def coeffs(beta1, beta2, tau):
    c1 = (1.0-beta1)/(1.0-beta1**tau)
    c2 = math.sqrt((1.0-beta2)/(1.0-beta2**tau))
    return c1, c2

def mini_active_update(d, k, G, eta, eps, beta1, beta2, tau):
    c1, c2 = coeffs(beta1, beta2, tau)
    rms = G*math.sqrt(k/d)
    return eta*c1*G/(c2*rms+eps)

def adam_active_update(G, eta, eps, beta1, beta2, tau):
    c1, c2 = coeffs(beta1, beta2, tau)
    return eta*c1*G/(c2*G+eps)

# Exact equal-support ratio and its sharp large-amplitude limit.
for beta1, beta2, tau in [
    (0.0, 0.0, 1),
    (0.9, 0.95, 1),
    (0.9, 0.95, 17),
    (0.9, 0.999, 1000),
]:
    c1, c2 = coeffs(beta1, beta2, tau)
    for d in (2, 5, 17, 64):
        for k in (1, min(2,d), d):
            G = 1e12
            eps = 1e-8
            umini = mini_active_update(d,k,G,1.0,eps,beta1,beta2,tau)
            uadam = adam_active_update(G,1.0,eps,beta1,beta2,tau)
            ratio = umini/uadam
            closed = (c2*G+eps)/(c2*G*math.sqrt(k/d)+eps)
            assert abs(ratio-closed) < 1e-12*max(1.0,abs(closed))
            target = math.sqrt(d/k)
            assert abs(ratio-target) < 1e-8*max(1.0,target)

# Universal coordinate bound from direct arbitrary impulses.
tests = [
    [3.0, -4.0, 0.0, 1.0],
    [1.0, 0.0, 0.0, 0.0],
    [1.0, -2.0, 7.0, 0.5, -0.1],
]
for g in tests:
    d = len(g)
    norm = math.sqrt(sum(x*x for x in g))
    beta1, beta2, tau = 0.8, 0.97, 23
    c1,c2 = coeffs(beta1,beta2,tau)
    eps = 1e-7
    eta = 0.3
    denom_mini = c2*norm/math.sqrt(d)+eps
    for x in g:
        if x == 0:
            continue
        umini = eta*c1*abs(x)/denom_mini
        uadam = eta*c1*abs(x)/(c2*abs(x)+eps)
        assert umini/uadam <= math.sqrt(d)+1e-12

# Enumerate all positive integer compositions and verify the minimax block size.
def compositions(n,b):
    if b == 1:
        yield (n,)
        return
    for first in range(1,n-b+2):
        for rest in compositions(n-first,b-1):
            yield (first,)+rest

for N in range(1,14):
    for B in range(1,N+1):
        vals = [max(c) for c in compositions(N,B)]
        exact = min(vals)
        assert exact == math.ceil(N/B)
        assert abs(math.sqrt(exact)-math.sqrt(math.ceil(N/B))) < 1e-15

# Balanced constructions attain the frontier.
for N,B in [(10,3),(100,9),(17,4),(12,12)]:
    q,r = divmod(N,B)
    sizes = [q+1]*r + [q]*(B-r)
    assert sum(sizes)==N
    assert max(sizes)==math.ceil(N/B)

print("verification passed")
