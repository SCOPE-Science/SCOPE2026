import math

def phi(s):
    y=math.pi*s/4.0
    return 2.0*y/math.tan(y)

def h(z,xi):
    t=xi*z
    s=math.exp(-t)*(1.0+t/2.0)
    h0=xi*(1.0+t)/(2.0+t)
    return h0*phi(s)

# Exact endpoint formulas and deterministic monotonicity stress-check.
for xi in (0.1,0.5,1.0,2.0,10.0):
    assert abs(h(0.0,xi)-math.pi*xi/4.0) < 2e-14*max(1.0,xi)
    vals=[h(j/(20.0*xi),xi) for j in range(801)]
    assert all(vals[j+1] > vals[j] for j in range(len(vals)-1))
    assert all(v < 2.0*xi for v in vals)

# Universal multiplier decreases with survival.
ss=[1.0-j/10000.0 for j in range(10000)]
ph=[phi(s) for s in ss]
assert all(ph[j+1] > ph[j] for j in range(len(ph)-1))
assert abs(phi(1.0)-math.pi/2.0) < 1e-15

# First-order terminal gap.
for xi in (0.5,1.0,2.0):
    z=200.0/xi
    gap=z*(2.0*xi-h(z,xi))
    assert abs(gap-2.0) < 0.03

print('VERIFY_OK')
