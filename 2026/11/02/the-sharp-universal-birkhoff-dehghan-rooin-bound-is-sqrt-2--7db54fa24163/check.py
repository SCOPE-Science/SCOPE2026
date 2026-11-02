"""Exact finite arithmetic supplements for an angular/skew-angular norm inequality."""
from fractions import Fraction as F

checks = 0

def assert_exact(condition, message):
    global checks
    assert condition, message
    checks += 1

# Sharp algebraic envelope on the s >= 1 branch.
for k in range(1, 501):
    s = F(k + 99, 100)
    assert_exact(32*s**3 - 27*(2*s-1)**2 == (2*s-3)**2*(8*s-3), f"factor {s}")
    assert_exact(27*(2*s-1)**2 <= 32*s**3, f"large-scale envelope {s}")

# The precise dyadic switch for the s <= 1 branch.
for k in range(1, 101):
    s = F(k, 100)
    if s <= F(1, 2):
        assert_exact(4*s <= 2, f"small-scale envelope {s}")
    else:
        assert_exact(1/s <= 2, f"intermediate-scale envelope {s}")

# Exact squared norm profiles of four square-plane Birkhoff-orthogonal pairs.
examples = [((1, 1), (1, 0)), ((1, -1), (1, 0)),
            ((-1, 1), (0, 1)), ((-1, -1), (0, 1))]

def infnorm(z):
    return max(abs(z[0]), abs(z[1]))

for u, v in examples:
    assert_exact(infnorm(u) == infnorm(v) == 1, "unit vectors")
    # In each example a coordinate of u of absolute value 1 has v-coordinate zero.
    assert_exact(any(abs(u[i]) == 1 and v[i] == 0 for i in (0, 1)), "Birkhoff witness")
    m = infnorm((u[0]-v[0], u[1]-v[1]))
    for k in range(1, 601):
        s = F(k, 200)
        d = infnorm((s*u[0]-v[0], s*u[1]-v[1]))
        assert_exact(d > 0 and s*m*m <= 2*d*d, f"sharp bound {u} {v} {s}")

u, v, s = (1, 1), (1, 0), F(1, 2)
m = infnorm((u[0]-v[0], u[1]-v[1]))
d = infnorm((s*u[0]-v[0], s*u[1]-v[1]))
assert_exact(s*m*m == 2*d*d, "sharp attainment")
assert_exact(F(32,27) < F(2,1), "large-scale gap")
print(f"PASS: {checks} supplementary exact-rational assertions")
