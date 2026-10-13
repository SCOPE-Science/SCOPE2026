import math

def r(k, ell):
    return 2.0*k*ell/(k*k*ell*ell+1.0)

def delta(n, ell, side):
    lo, hi = 0.0, 0.49
    def f(d):
        return math.sin(math.pi*d) - r(n + side*d, ell)
    if not (f(lo) < 0.0 and f(hi) > 0.0):
        raise AssertionError((n, ell, side, f(lo), f(hi)))
    for _ in range(100):
        mid=(lo+hi)/2.0
        if f(mid) > 0.0:
            hi=mid
        else:
            lo=mid
    d=(lo+hi)/2.0
    if abs(f(d)) > 2e-14:
        raise AssertionError(('residual', n, ell, side, f(d)))
    return d

for ell in (0.7, 1.0, 2.3):
    target_k=4.0/(math.pi*ell)
    target_E=8.0/(math.pi*ell)
    prev_kw=None
    prev_ew=None
    for n in (50,100,200):
        dm=delta(n,ell,-1)
        dp=delta(n,ell,+1)
        kw=n*(dm+dp)
        ew=(n+dp)**2-(n-dm)**2
        if abs(kw-target_k) > 2.0/(n*n):
            raise AssertionError(('momentum',ell,n,kw,target_k))
        if abs(ew-target_E) > 4.0/(n*n):
            raise AssertionError(('energy',ell,n,ew,target_E))
        if prev_kw is not None and abs(kw-target_k) >= abs(prev_kw-target_k):
            raise AssertionError(('momentum convergence',ell,n))
        if prev_ew is not None and abs(ew-target_E) >= abs(prev_ew-target_E):
            raise AssertionError(('energy convergence',ell,n))
        prev_kw,prev_ew=kw,ew
print('VERIFY_OK')
print('momentum_constant_ell1=',4.0/math.pi)
print('energy_constant_ell1=',8.0/math.pi)
