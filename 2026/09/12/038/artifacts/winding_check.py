"""Winding-number check for the rotation lemma (lane-1181 artifact).

Mechanism: let rho(z) = -z, p in R^2 \\ {0}, and gamma a polygonal path from p
to -p avoiding the origin. The symmetric loop Gamma = gamma followed by
rho(gamma) has odd winding number about the origin (1 mod 2). We verify this
numerically on (a) the exact circle and (b) random polygonal paths, via the
discrete total-angle sum  W = (1/2pi) * sum(atan2(cross, dot)).
"""
import math
import random


def winding_number(loop):
    total = 0.0
    n = len(loop)
    for i in range(n):
        x0, y0 = loop[i]
        x1, y1 = loop[(i + 1) % n]
        cross = x0 * y1 - y0 * x1
        dot = x0 * x1 + y0 * y1
        total += math.atan2(cross, dot)
    return total / (2.0 * math.pi)


def symmetric_loop(gamma):
    # gamma: list of points from p to -p; rho(gamma) reflected, same direction
    # gives closed loop p -> -p -> p.
    rho = [(-x, -y) for (x, y) in gamma]
    # Concatenate gamma (p..-p) with rho(gamma) reversed segment (-p..p):
    # rho(gamma) runs rho(p)..rho(-p) = -p..p, exactly the closing half.
    return gamma + rho[1:]


def random_path_avoiding_origin(p, seed):
    rng = random.Random(seed)
    # waypoints in the half-plane, lifted away from origin; reflect endpoints
    q = (-p[0], -p[1])
    pts = [p]
    for _ in range(4):
        x = rng.uniform(-3.0, 3.0)
        y = rng.uniform(0.6, 3.0)  # keep upper half to avoid origin
        pts.append((x, y))
    pts.append(q)
    return pts


def main():
    # (a) exact circle radius 2: expected winding exactly 1
    circ = [(2 * math.cos(t), 2 * math.sin(t))
            for t in [2 * math.pi * k / 400 for k in range(400)]]
    w_circ = winding_number(circ)
    print(f"circle winding = {w_circ:.6f}")
    assert abs(w_circ - 1.0) < 1e-9, "circle winding must be 1"

    # (b) random symmetric loops: winding must be an odd integer
    for seed in range(6):
        p = (2.0, 0.0)
        gamma = random_path_avoiding_origin(p, seed)
        loop = symmetric_loop(gamma)
        w = winding_number(loop)
        nearest = round(w)
        print(f"seed {seed}: winding = {w:.6f}, nearest int = {nearest}")
        assert abs(w - nearest) < 1e-9, "winding must be near-integer"
        assert nearest % 2 == 1, f"winding {nearest} must be odd"
    print("OK: all symmetric-loop windings are odd (nonzero), as claimed.")


if __name__ == "__main__":
    main()
