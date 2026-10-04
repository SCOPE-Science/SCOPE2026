from decimal import Decimal, getcontext

getcontext().prec = 80
D = Decimal
seven = D(7)
r = seven.sqrt()
w = (r - D(1)) / D(6)
F = (D(1) + D(2)*w) * (D(1) - D(2)*w*w)
target_F = (D(17) + D(7)*r) / D(27)
deriv = D(2) - D(4)*w - D(12)*w*w
cmin = (D(1)/F) ** (D(1)/D(3))
eps = (D(1) - cmin*cmin).sqrt()

tol = D('1e-65')
assert D(0) < w < D('0.5')
assert abs(deriv) < tol
assert abs(F - target_F) < tol
assert D(0) < eps < D(1)

# Finite corroborative stress test only; the global proof is analytic.
best = D(0)
best_i = 0
N = 200000
for i in range(N + 1):
    ww = D(i) / D(2*N)
    val = (D(1) + D(2)*ww) * (D(1) - D(2)*ww*ww)
    if val > best:
        best = val
        best_i = i
assert best <= F + D('2e-10')
print('VERIFY_OK')
print('w_star=', w)
print('Fmax=', F)
print('epsilon=', eps)
print('grid_w=', D(best_i)/D(2*N))
