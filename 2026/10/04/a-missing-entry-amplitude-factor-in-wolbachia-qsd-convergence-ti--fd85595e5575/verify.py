from fractions import Fraction
import math

a1 = Fraction(1, 100)
a2 = Fraction(1, 50)
r = Fraction(1, 1)
r1 = Fraction(1, 4)
r2 = Fraction(3, 4)
K = 10
A = r1 * (r - a2) / (r2 * (r - a1))
assert A == Fraction(98, 297)

a1f, a2f, rf, r1f, r2f = map(float, (a1, a2, r, r1, r2))
gap = a2f - a1f
naive = math.log(K) / gap
adjusted = (math.log(K) - math.log(float(A))) / gap

def ratio(t):
    w = r1f / (rf - a1f) * (math.exp(-a1f*t) - math.exp(-rf*t))
    i = r2f / (rf - a2f) * (math.exp(-a2f*t) - math.exp(-rf*t))
    return w / i

lo, hi = 1e-9, 1000.0
for _ in range(200):
    mid = (lo + hi) / 2
    if ratio(mid) < K:
        lo = mid
    else:
        hi = mid
root = (lo + hi) / 2
assert abs(ratio(root) - K) < 1e-10
assert abs(root - adjusted) < 1e-9
assert adjusted - naive > 100.0
print('VERIFY_OK')
