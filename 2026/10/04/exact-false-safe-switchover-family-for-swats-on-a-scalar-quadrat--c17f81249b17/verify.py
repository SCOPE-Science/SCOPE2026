import math

def construction(alpha, b, q):
    assert alpha > 0.0
    assert 0.0 < b < 1.0
    assert q > 2.0
    s = math.sqrt(1.0-b)
    R = math.sqrt(1.0+b)
    D = math.sqrt(b+(q-1.0)**2)
    eps = alpha*s*(D-R)/(q*(D-1.0))
    x0 = alpha*(R-1.0)/(q*(D-1.0))
    assert eps > 0.0 and x0 > 0.0
    return eps, x0

def adam_step(x, a_prev, k, alpha, b, eps):
    g = x
    a = b*a_prev + (1.0-b)*g*g
    p = -alpha*math.sqrt(1.0-b**k)*g/(math.sqrt(a)+eps)
    gamma = p*p/(-p*g)
    return x+p, a, p, gamma

def replay(alpha, b, q):
    eps, x0 = construction(alpha,b,q)
    x1,a1,p1,g1 = adam_step(x0,0.0,1,alpha,b,eps)
    x2,a2,p2,g2 = adam_step(x1,a1,2,alpha,b,eps)
    assert abs(g1-q) < 5e-11*max(1.0,q)
    assert abs(g2-q) < 5e-11*max(1.0,q)
    lam1 = (1.0-b)*g1
    lam2 = b*lam1 + (1.0-b)*g2
    corrected = lam2/(1.0-b**2)
    assert abs(corrected-q) < 5e-11*max(1.0,q)
    assert abs(corrected-g2) < eps

    # After the switch, beta1=0 makes SWATS ordinary SGD with rate q.
    x = x2
    old = abs(x)
    for _ in range(8):
        x = (1.0-q)*x
        new = abs(x)
        assert new > old
        assert abs(new/old-(q-1.0)) < 2e-12*max(1.0,q)
        old = new
    return eps,x0

for b in (0.05,0.2,0.5,0.9,0.999):
    for q in (2.01,2.1,3.0,5.0,10.0):
        replay(1e-3,b,q)

# Source-scale denominator/tolerance example.
alpha = 1e-3
b = 0.999
target_eps = 1e-9

def eps_of_q(q):
    return construction(alpha,b,q)[0]

lo = 2.00003701018
hi = 2.00003701020
assert eps_of_q(lo) < target_eps
assert eps_of_q(hi) > target_eps
for _ in range(80):
    mid = (lo+hi)/2.0
    if eps_of_q(mid) < target_eps:
        lo = mid
    else:
        hi = mid
q = (lo+hi)/2.0
assert 2.00003701018 < q < 2.00003701020

eps,x0 = construction(alpha,b,q)
assert abs(eps-target_eps) < 2e-19
x1,a1,p1,g1 = adam_step(x0,0.0,1,alpha,b,eps)
x2,a2,p2,g2 = adam_step(x1,a1,2,alpha,b,eps)
lam1=(1-b)*g1
lam2=b*lam1+(1-b)*g2
corrected=lam2/(1-b**2)
assert abs(g1-q) < 2e-11
assert abs(g2-q) < 2e-11
assert abs(corrected-g2) < eps
assert q > 2.0

print("verification passed")
