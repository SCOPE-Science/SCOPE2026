import cmath, math, random

rng = random.Random(20261005)
min_margin = float("inf")
count = 20000
for _ in range(count):
    A, B, C, D = [10 ** rng.uniform(-3.0, 2.0) for _ in range(4)]
    phi = rng.uniform(-math.pi, math.pi)
    alpha = phi / 2.0
    zp = cmath.exp(-1j * alpha)
    zm = -zp
    def F(z):
        return abs(A + B*z) + abs(C + D*cmath.exp(1j*phi)*z)
    lhs = F(zp)**2 + F(zm)**2
    rhs = (A+B+C+D)**2
    scale = max(1.0, rhs)
    margin = (lhs-rhs)/scale
    min_margin = min(min_margin, margin)
    assert lhs + 2e-10*scale >= rhs

# Sharp witness P=1+z+w-zw: after maximizing over w, norm is
# max_z |1+z|+|1-z| = 2*sqrt(2), attained at z=i.
z = 1j
sharp_norm = abs(1+z) + abs(1-z)
assert abs(sharp_norm - 2*math.sqrt(2)) < 1e-14
ratio = 4.0 / sharp_norm
assert abs(ratio - math.sqrt(2)) < 1e-14
print(f"VERIFY_OK random_cases={count} min_scaled_margin={min_margin:.3e} sharp_ratio={ratio:.15f}")
