from fractions import Fraction

def N(delta, a, b):
    return max(abs(a), (abs(b) + delta * abs(a)) / (1 + delta))

def fplus(delta, a, b):
    return (delta * a + b) / (1 + delta)

def fminus(delta, a, b):
    return (-delta * a + b) / (1 + delta)

def check(eps):
    assert 0 < eps < 1
    delta = eps / (2 - eps)
    assert 0 < delta < 1
    assert 2 * delta / (1 + delta) == eps
    x = (Fraction(0), 1 + delta)
    rp = (Fraction(1), delta)
    rm = (Fraction(-1), delta)
    assert N(delta, *x) == 1
    assert N(delta, *rp) == 1
    assert N(delta, *rm) == 1
    assert fplus(delta, *x) == 1 and fminus(delta, *x) == 1
    assert fplus(delta, *rp) == eps and fminus(delta, *rp) == 0
    assert fplus(delta, *rm) == 0 and fminus(delta, *rm) == eps
    s = Fraction(1, 3) if eps <= Fraction(2, 3) else eps / 2
    y1 = (s * rp[0], s * rp[1])
    y2 = rm
    w = (y1[0] + y2[0], y1[1] + y2[1])
    assert N(delta, *y1) == s
    assert N(delta, *y2) == 1
    assert N(delta, *w) == 2 * s
    assert min(N(delta, *y1), N(delta, *y2)) == N(delta, w[0] / 2, w[1] / 2)
    fp = fplus(delta, *w)
    fm = fminus(delta, *w)
    assert {fp, fm} == {s * eps, eps}
    threshold = min(abs(fp), abs(fm)) / N(delta, *w)
    assert threshold == eps / 2

for eps in [Fraction(1,10), Fraction(1,3), Fraction(1,2), Fraction(2,3), Fraction(3,4), Fraction(9,10), Fraction(99,100)]:
    check(eps)
print("VERIFY_OK")
