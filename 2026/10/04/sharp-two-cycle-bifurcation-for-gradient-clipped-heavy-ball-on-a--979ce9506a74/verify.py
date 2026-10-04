from fractions import Fraction
import cmath


def clip(u, C):
    if u > C:
        return C
    if u < -C:
        return -C
    return u


def step(x, vprev, alpha, lam, C, beta):
    v = beta * vprev + clip(lam * x, C)
    return x - alpha * v, v


def roots(beta, q):
    tr = 1 + beta - q
    disc = tr * tr - 4 * beta
    z = cmath.sqrt(disc)
    return (tr + z) / 2, (tr - z) / 2

# Exact critical-cycle check with rational arithmetic.
beta = Fraction(1, 2)
lam = Fraction(3, 1)
C = Fraction(6, 1)
r = C / lam
qstar = 2 * (1 + beta)
alpha = qstar / lam
for a in (Fraction(1, 4), Fraction(1, 1), r):
    vprev = -2 * a / alpha
    b, v0 = step(a, vprev, alpha, lam, C, beta)
    a2, v1 = step(b, v0, alpha, lam, C, beta)
    assert b == -a
    assert a2 == a
    assert v0 == 2 * a / alpha
    assert v1 == -2 * a / alpha

# Subcritical and supercritical local root checks.
for beta_f in (0.0, 0.2, 0.6, 0.9):
    qstar_f = 2 * (1 + beta_f)
    r1, r2 = roots(beta_f, 0.9 * qstar_f)
    assert max(abs(r1), abs(r2)) < 1
    r1, r2 = roots(beta_f, 1.1 * qstar_f)
    assert max(abs(r1), abs(r2)) > 1
    r1, r2 = roots(beta_f, qstar_f)
    vals = sorted((round(abs(r1), 12), round(abs(r2), 12)))
    assert vals == sorted((round(beta_f, 12), 1.0))

# Supercritical center-band cycles, including both endpoints and the center.
for beta_f in (0.0, 0.3, 0.8):
    lam_f = 2.0
    C_f = 5.0
    r_f = C_f / lam_f
    qstar_f = 2 * (1 + beta_f)
    q_f = 1.35 * qstar_f
    alpha_f = q_f / lam_f
    c = alpha_f * C_f / (2 * (1 + beta_f))
    width = c - r_f
    assert width > 0
    for d in (-width, -0.4 * width, 0.0, 0.7 * width, width):
        a = d + c
        b = d - c
        vprev = -C_f / (1 + beta_f)
        b2, v0 = step(a, vprev, alpha_f, lam_f, C_f, beta_f)
        a2, v1 = step(b2, v0, alpha_f, lam_f, C_f, beta_f)
        assert abs(b2 - b) < 1e-12
        assert abs(a2 - a) < 1e-12
        assert abs(v0 - C_f / (1 + beta_f)) < 1e-12
        assert abs(v1 + C_f / (1 + beta_f)) < 1e-12

# Below the threshold, the saturated two-cycle gap would be too small to put
# one point beyond +r and the other beyond -r.
for beta_f in (0.0, 0.4, 0.9):
    lam_f = 1.7
    C_f = 2.3
    r_f = C_f / lam_f
    qstar_f = 2 * (1 + beta_f)
    q_f = 0.75 * qstar_f
    alpha_f = q_f / lam_f
    gap = alpha_f * C_f / (1 + beta_f)
    assert gap < 2 * r_f

# Interior normal-attraction recurrence and predicted limiting center.
beta_f = 0.6
lam_f = 1.0
C_f = 1.0
qstar_f = 2 * (1 + beta_f)
q_f = 1.4 * qstar_f
alpha_f = q_f / lam_f
r_f = C_f / lam_f
c = alpha_f * C_f / (2 * (1 + beta_f))
width = c - r_f
assert width > 0
d_ref = 0.2 * width
# State phase has positive x and previous velocity negative.
x = d_ref + c + 0.01 * width
vprev = -C_f / (1 + beta_f) + 0.005
# Compute e_0 after the first momentum update, matching the proof indexing.
x1, v0 = step(x, vprev, alpha_f, lam_f, C_f, beta_f)
d0 = x - c
e0 = v0 - C_f / (1 + beta_f)
dinf = d0 - alpha_f * e0 / (1 - beta_f)
assert -width < dinf < width
# Advance from state x_1 with v_0, checking alternating clipping remains strict.
xcur, vp = x1, v0
for t in range(1, 80):
    phase = -1 if t % 2 else 1
    assert phase * xcur > r_f
    xcur, vp = step(xcur, vp, alpha_f, lam_f, C_f, beta_f)
phase = -1 if 80 % 2 else 1
center_est = xcur - phase * c
assert abs(center_est - dinf) < 1e-10

print('verification passed')
