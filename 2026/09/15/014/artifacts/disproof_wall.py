# Divisorial J-slope wall vs MBM wall on K3^[2]-type (locus-free algebra).
#
# Lattice model: L = Z*H + Z*delta, q(H) = 2d (d >= 1 integer),
# q(delta) = -2, q(H,delta) = 0. Ray a(s) = H - s*delta,
# b = H - t1*delta, e = delta, with 0 < t1^2 < d.
# This script checks ONLY the algebra (no ampleness claims):
#   F(s) = q(a)q(e,b) - 2q(a,b)q(e,a); F(s)/4 = t1 s^2 - 2 d s + t1 d;
#   roots satisfy s_star * s_big = d, s_star in (0,t1),
#   F(0)/4 = d t1 > 0, F(s_star) = 0 with q(e,a(s_star)) > 0.
# Geometric reading (proved in DRAFT.md, Lemma 2 + Prop): for 0 < s <= t1
# with t1 small, a(s) is Kahler, q(a,e) = 0 only at s = 0 (the MBM wall),
# while the divisorial J-slope wall F = 0 sits at interior s_star.
import math

d, t1 = 2, 0.5
assert 0 < t1 * t1 < d


def q(x, y=None):
    y = x if y is None else y
    return 2 * d * x[0] * y[0] - 2 * x[1] * y[1]


disc = 4 * d * d - 4 * t1 * t1 * d
s_star = (2 * d - math.sqrt(disc)) / (2 * t1)
s_big = (2 * d + math.sqrt(disc)) / (2 * t1)
assert abs(s_star * s_big - d) < 1e-9
assert 0 < s_star < t1 < s_big

for s in [0.0, s_star / 2, s_star, (s_star + t1) / 2, t1]:
    a = (1.0, -s)
    b = (1.0, -t1)
    e = (0.0, 1.0)
    F = q(a) * q(e, b) - 2 * q(a, b) * q(a, e)
    print(f"s={s:.6f} F/4={F/4:.6f} q(e,a)={q(a, e):.4f} "
          f"q(a)={q(a):.4f} q(a,b)={q(a, b):.4f}")

a0 = (1.0, 0.0)
b = (1.0, -t1)
e = (0.0, 1.0)
F0 = q(a0) * q(e, b) - 2 * q(a0, b) * q(a0, e)
assert abs(F0 / 4 - d * t1) < 1e-9 and F0 > 0, "on MBM wall s=0: F != 0"
aS = (1.0, -s_star)
FS = q(aS) * q(e, b) - 2 * q(aS, b) * q(aS, e)
assert abs(FS) < 1e-9 and q(aS, e) > 0, "on J-wall: q(e,a) != 0"
print(f"OK: J-wall at interior s_star={s_star:.6f} (4-sqrt(14)); "
      "MBM wall at endpoint s=0.")
