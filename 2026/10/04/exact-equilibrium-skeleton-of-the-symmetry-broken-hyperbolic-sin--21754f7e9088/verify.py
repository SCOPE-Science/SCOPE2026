import math

EPS = 0.01
C = 0.2

def bisect(f, lo, hi, n=180):
    flo, fhi = f(lo), f(hi)
    assert flo == 0.0 or fhi == 0.0 or flo * fhi < 0.0
    for _ in range(n):
        mid = (lo + hi) / 2.0
        fm = f(mid)
        if flo * fm <= 0.0:
            hi, fhi = mid, fm
        else:
            lo, flo = mid, fm
    return (lo + hi) / 2.0

def M(q):
    return q * math.acosh(q) - math.sqrt(q*q - 1.0)

qsn = bisect(lambda q: M(q) - EPS, 1.04, 1.06)
assert abs(qsn - 1.0483518312766905) < 2e-15
assert 1.0 < qsn < 1.1

xC = bisect(lambda x: C*x + x*math.cosh(x) - math.sinh(x) - EPS, 0.04, 0.06)
aC = C + math.cosh(xC)
assert abs(aC - 1.2012399862498024) < 2e-15
assert 1.1 < aC < 1.656

def j(x):
    return C*x - x*math.cosh(x) + math.sinh(x) - EPS

xL = bisect(j, -0.80, -0.75)
xR = bisect(j, 0.70, 0.75)
xOut = bisect(j, 0.04, 0.06)
aL = C - math.cosh(xL)
aR = C - math.cosh(xR)
aOut = C - math.cosh(xOut)
aSN = -qsn

assert abs(aL + 1.1162333464411851) < 3e-15
assert abs(aR + 1.0769969279698951) < 3e-15
assert abs(aSN + 1.0483518312766905) < 2e-15
assert abs(aOut + 0.8012608389126760) < 3e-15
assert -1.42 < aL < aR < aSN < -0.83
assert aOut > -0.83

def changes(vals):
    signs = [1 if v > 0 else -1 for v in vals]
    return sum(signs[i] != signs[i-1] for i in range(1, len(signs)))

assert changes([1.0, C, (C-0.1)/C, 0.1]) == 0
assert changes([1.0, C, (C-(-0.1))/C, -0.1]) == 1
assert changes([1.0, C, (C-0.3)/C, 0.3]) == 2

assert abs((C*C*C + C*C*C + C + C) - ((C+C)*(C*C+1))) < 1e-14
print('VERIFY_OK')
