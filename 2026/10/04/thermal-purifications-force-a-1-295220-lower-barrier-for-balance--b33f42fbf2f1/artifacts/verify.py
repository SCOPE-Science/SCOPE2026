import math

# Solve (2-x)e^x=2 on (1,2) by bisection.
lo, hi = 1.0, 2.0
for _ in range(100):
    mid = (lo + hi) / 2
    h = (2-mid)*math.exp(mid) - 2
    if h > 0:
        lo = mid
    else:
        hi = mid
x = (lo + hi) / 2
r = math.exp(-x)
q = 2*r/(1+r)
C = 2*x*(2-x)
C2 = q/(1-q) * math.log(q/(2-q))**2
assert 1 < x < 2
assert abs((2-x)*math.exp(x)-2) < 2e-15
assert abs(C-C2) < 2e-14
assert 1.29522047 < C < 1.29522049

def finite_variance(q, L):
    z = 1-q**(L+1)
    p = [(1-q)*q**m/z for m in range(L+1)]
    s = []
    for j in range(L+1):
        total = 0.0
        for m in range(j, L+1):
            total += p[m] * math.comb(m,j) * 2.0**(-m)
        s.append(total)
    assert abs(sum(p)-1) < 2e-14
    assert abs(sum(s)-1) < 2e-14
    v = 0.0
    for m in range(L+1):
        for k in range(m+1):
            prob = p[m] * math.comb(m,k) * 2.0**(-m)
            y = math.log(s[k]) - math.log(s[m-k])
            v += prob*y*y
    return v

vals = [(L, finite_variance(q,L)) for L in (4,6,8,10,12,16,20)]
# Numerical corroboration of the analytic limiting calculation.
assert vals[-1][1] > C - 4e-11
assert vals[-1][1] < C + 1e-10
# Check exact geometric-output parameter identity.
r2 = q/(2-q)
assert abs(r-r2) < 2e-15
mean_m = q/(1-q)
limit_formula = mean_m * math.log(r)**2
assert abs(limit_formula-C) < 2e-14
print('x_star=%.15f q_star=%.15f C_star=%.15f' % (x,q,C))
for L,v in vals:
    print('L=%d V=%.15f gap=%.3e' % (L,v,C-v))
print('VERIFY_OK')
