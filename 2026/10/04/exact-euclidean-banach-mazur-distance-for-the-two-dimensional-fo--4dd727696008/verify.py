from decimal import Decimal, getcontext
getcontext().prec = 80
D = Decimal
r = D(17).sqrt()

def h(s):
    return (D(1)+s)**3 * (r-s) - D(16)*s

lo, hi = D('3.511'), D('3.512')
assert h(lo) > 0 and h(hi) < 0
for _ in range(260):
    mid = (lo+hi)/2
    if h(mid) > 0:
        lo = mid
    else:
        hi = mid
s = (lo+hi)/2
res = abs(h(s))
disc = D(40) - D(24)*r
assert disc < 0
K = D(16) + (D(1)+s)**4
Dstar = K.sqrt()/(r+s*s)
d = Dstar.sqrt()
assert D('1.26068') < Dstar < D('1.26069')
assert D('1.12280') < d < D('1.12281')
assert res < D('1e-70')
print('sqrt17 =', r)
print('h(3.511) =', h(D('3.511')))
print('h(3.512) =', h(D('3.512')))
print('s_star =', s)
print('residual =', res)
print('discriminant =', disc)
print('D_star =', Dstar)
print('d_BM =', d)
