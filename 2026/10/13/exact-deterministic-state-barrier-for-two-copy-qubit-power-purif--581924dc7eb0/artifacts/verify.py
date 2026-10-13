import math

def f(p):
    return p*p/(p*p+(1-p)*(1-p))

def d_of_x(x):
    return x*(1-x*x)/(2*(1+x*x))

x = math.sqrt(math.sqrt(5.0)-2.0)
delta = ((math.sqrt(5.0)-1.0)/4.0)*x
assert abs(d_of_x(x)-delta) < 1e-15
assert abs(delta-0.1501415530003888) < 1e-15

# Exact-form identities checked numerically over a deterministic grid.
for k in range(1001):
    xx = k/1000.0
    pm = (1-xx)/2
    pp = (1+xx)/2
    target_gap = f(pp)-f(pm)
    assert abs(target_gap - 2*xx/(1+xx*xx)) < 2e-14
    assert abs((f(pp)-pp) - d_of_x(xx)) < 2e-14

# The critical polynomial changes sign only once in (0,1).
assert 1 - 4*(x-1e-7)**2 - (x-1e-7)**4 > 0
assert 1 - 4*(x+1e-7)**2 - (x+1e-7)**4 < 0

print("VERIFY_OK")
