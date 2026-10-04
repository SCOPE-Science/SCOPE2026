import math

rho = 1.5
A = 2.0 ** (1.0 / 3.0)
m = 3.0 / (2.0 ** (4.0 / 3.0))
d2 = 2.0 ** (5.0 / 3.0) / 3.0

def rp(t):
    return 2.0 * (1.0 + rho * t * t) / ((2.0 + 6.0 * t * t) ** (2.0 / 3.0))

def rm(s):
    den = ((1.0 + s) ** 1.5 + (1.0 - s) ** 1.5) ** (4.0 / 3.0)
    return 2.0 * (rho + s * s) / den

assert abs(rp(0.0) - A) < 1e-12
assert abs(rp(1.0 / math.sqrt(3.0)) - m) < 1e-12
assert abs(rm(0.0) - m) < 1e-12
assert abs(rm(math.sqrt(3.0) / 2.0) - A) < 1e-12
assert abs(A / m - d2) < 1e-12

n = 200000
pvals = [rp(i / n) for i in range(n + 1)]
mvals = [rm(i / n) for i in range(n + 1)]
lo = min(min(pvals), min(mvals))
hi = max(max(pvals), max(mvals))
assert lo >= m - 2e-10
assert hi <= A + 2e-10
assert abs(hi / lo - d2) < 5e-9

print('VERIFY_OK')
print('d2=', repr(d2))
print('d=', repr(math.sqrt(d2)))
print('rho=', repr(rho))
print('sample_min=', repr(lo))
print('sample_max=', repr(hi))
