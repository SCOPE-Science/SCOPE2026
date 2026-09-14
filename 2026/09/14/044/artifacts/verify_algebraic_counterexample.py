"""Verify algebraic Einstein counterexample: sec>0 but not 3-positive."""
import numpy as np

rng = np.random.default_rng(0)

# Eigenvalues of A+ , A- (curvature operator blocks), trace 1 each (s=4, s/12=1/3)
a = np.array([-0.2, -0.1, 1.3])
b = np.array([0.25, 0.3, 0.45])
print("sum a:", a.sum(), "sum b:", b.sum())

# Weyl eigenvalues
wa = a - 1/3
wb = b - 1/3
print("W+:", wa, "sum:", wa.sum())
print("W-:", wb, "sum:", wb.sum())

# Sectional min formula
sec_min = (a.min() + b.min()) / 2
print("sec_min =", sec_min)
assert sec_min > 0, "need strictly positive sectional"

# 3-positivity
c = np.sort(np.concatenate([a, b]))
print("sorted combined:", c)
s3 = c[0] + c[1] + c[2]
print("sum 3 smallest =", s3)
assert s3 < 0, "need failure of 3-positivity"
assert (a.min() + b.min()) > 0 and s3 <= 0

# Brute-force check over random planes: K = (u+^T A+ u+ + u-^T A- u-)/2
Aplus = np.diag(a)
Aminus = np.diag(b)
mins = []
for _ in range(200000):
    u1 = rng.normal(size=3); u1 /= np.linalg.norm(u1)
    u2 = rng.normal(size=3); u2 /= np.linalg.norm(u2)
    K = 0.5 * (u1 @ Aplus @ u1 + u2 @ Aminus @ u2)
    mins.append(K)
mins = np.array(mins)
print("random sample min K:", mins.min(), " (theory 0.025)")
assert mins.min() > 0.0
# theory min attained at eigenvectors for a1,b1:
assert abs(0.5*(a[0]+b[0]) - 0.025) < 1e-12

# Baselines: round S^4 (all 1/3) and CP^2 FS (1,0,0,1/3,1/3,1/3)
for name, vals in [("S4", np.full(6, 1/3)), ("CP2", np.array([1.,0,0,1/3,1/3,1/3]))]:
    cs = np.sort(vals)
    print(name, "sec_min proxy (a1+b1)/2:", (cs[0] if False else "n/a"), "sum3:", cs[:3].sum())
print("ALL CHECKS PASSED")
