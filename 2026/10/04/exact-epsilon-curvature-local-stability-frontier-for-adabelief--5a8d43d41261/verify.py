import math, cmath

def roots(beta1, chi):
    T = 1.0 + beta1 - (1.0-beta1)*chi
    d = cmath.sqrt(T*T - 4.0*beta1)
    return ((T+d)/2.0, (T-d)/2.0)

def D(beta2, eps):
    return math.sqrt(eps/(1.0-beta2)) + eps

def curvature_ceiling(beta1,beta2,alpha,eps):
    return (2.0*(1.0+beta1)/(1.0-beta1))*D(beta2,eps)/alpha

for b1 in (0.0,0.2,0.5,0.9):
    cap = 2.0*(1.0+b1)/(1.0-b1)
    rs = roots(b1,cap)
    assert min(abs(r+1.0) for r in rs) < 1e-10
    assert min(abs(r+b1) for r in rs) < 1e-10
    assert max(abs(r) for r in roots(b1,0.999*cap)) < 1.0
    assert max(abs(r) for r in roots(b1,1.001*cap)) > 1.0

for b1 in (0.1,0.5,0.9):
    q = math.sqrt(b1)
    lo = (1.0-q)/(1.0+q)
    hi = (1.0+q)/(1.0-q)
    for chi in (0.25*lo+0.75*hi,0.5*(lo+hi),0.75*lo+0.25*hi):
        rs = roots(b1,chi)
        assert abs(rs[0].imag) > 1e-12
        assert abs(abs(rs[0])-q) < 1e-11
        assert abs(abs(rs[1])-q) < 1e-11

b1,b2,alpha = 0.9,0.999,1e-3
c8 = curvature_ceiling(b1,b2,alpha,1e-8)
c16 = curvature_ceiling(b1,b2,alpha,1e-16)
assert abs(c8-120.16693108639836) < 1e-10
assert abs(c16-0.01201665511243984) < 1e-14

eps = 1e-8
s = 0.0
target = eps/(1.0-b2)
for t in range(1,200):
    s = b2*s + eps
    shat = s/(1.0-b2**t)
    assert abs(shat-target) <= 2e-12*target

print("verification passed")
