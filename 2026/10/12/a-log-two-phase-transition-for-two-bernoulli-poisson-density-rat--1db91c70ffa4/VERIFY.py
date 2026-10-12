import math


def ratios(p, q):
    s = p + q
    assert s > 0.0
    delta = (p*p + q*q) / s
    r0 = math.exp(s) * (1.0-p) * (1.0-q)
    r1 = math.exp(s) * (p*(1.0-q) + q*(1.0-p)) / s
    r2 = math.exp(s) * (2.0*p*q) / (s*s)
    return s, delta, r0, r1, r2, max(r0, r1, r2)


def envelope(delta):
    return max(math.exp(delta), 0.5*math.exp(2.0*delta))

count = 0
for i in range(0, 99):
    for j in range(0, 99):
        if i == 0 and j == 0:
            continue
        p = i / 100.0
        q = j / 100.0
        s, delta, r0, r1, r2, rho = ratios(p, q)
        assert 0.0 < delta < 1.0
        assert delta <= s + 1e-15
        assert s <= 2.0*delta + 1e-15
        assert r0 < 1.0 + 1e-15
        assert abs(r1 - math.exp(s)*(1.0-s+delta)) < 2e-14
        assert abs(r2 - math.exp(s)*(1.0-delta/s)) < 2e-14
        assert rho <= envelope(delta) + 2e-13
        assert envelope(delta) < 1.0/(1.0-delta) + 1e-13
        count += 1

cases = [0.1, 0.4, 0.65, 0.75, 0.9, math.log(2.0)]
for d in cases:
    # one-active endpoint
    _, delta1, _, _, _, rho1 = ratios(d, 0.0)
    assert abs(delta1-d) < 1e-15
    assert abs(rho1-math.exp(d)) < 2e-14
    # equal-two endpoint
    _, delta2, _, _, _, rho2 = ratios(d, d)
    assert abs(delta2-d) < 2e-15
    if d >= 0.5:
        assert abs(rho2-0.5*math.exp(2.0*d)) < 2e-14

assert math.exp(math.log(2.0)) == 2.0
assert abs(0.5*math.exp(2.0*math.log(2.0)) - 2.0) < 2e-15
print(f"VERIFY_OK grid={count} equality_cases={len(cases)}")
