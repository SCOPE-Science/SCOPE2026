"""Newton firewall: true symmetric 3-periodic orbits confirm the O(eps^3) barrier.

For A in {0, pi/5}, L(A,t;eps) = 2|g(A)-g(A+t)| + |g(A+t)-g(A-t)|,
g(th) = (1+eps*cos(5th))(cos th, sin th).
Newton-solve F(t) = dL/dt = 0 from t0 = 2pi/3 (central differences),
then ell(A;eps) = L(A,t*;eps). Prints Delta/eps^3 with
Delta = ell(pi/5)-ell(0); expect -> -855*sqrt(3) ~ -1480.90, both signs.
Also checks t*-2pi/3 ~ u1*eps with u1 = +/-7*sqrt(3)/2 ~ +/-6.062.
Run: python3 newton_check.py
"""
import math

S3 = math.sqrt(3)
TS = 2 * math.pi / 3


def gamma(th, eps):
    r = 1 + eps * math.cos(5 * th)
    return (r * math.cos(th), r * math.sin(th))


def dist(p, q):
    return math.hypot(p[0] - q[0], p[1] - q[1])


def Lval(A, t, eps):
    gA = gamma(A, eps)
    g1 = gamma(A + t, eps)
    g2 = gamma(A - t, eps)
    return 2 * dist(gA, g1) + dist(g1, g2)


def solve_t(A, eps):
    h = 1e-5
    t = TS
    for _ in range(20):
        Fp = (Lval(A, t + h, eps) - Lval(A, t - h, eps)) / (2 * h)
        Fpp = (Lval(A, t + h, eps) - 2 * Lval(A, t, eps)
               + Lval(A, t - h, eps)) / (h * h)
        dt = Fp / Fpp
        t -= dt
        if abs(dt) < 1e-13:
            break
    return t


if __name__ == '__main__':
    print('target const = -855*sqrt(3) =', -855 * S3)
    print('predicted u1 = +/-7*sqrt(3)/2 =', 7 * S3 / 2)
    for eps in [0.02, 0.01, 0.005, 0.0025, 0.001,
                -0.01, -0.005, -0.0025, -0.001]:
        e0, e1 = solve_t(0.0, eps), solve_t(math.pi / 5, eps)
        l0, l1 = Lval(0.0, e0, eps), Lval(math.pi / 5, e1, eps)
        d = l1 - l0
        print(f'eps={eps:+.4f} t0-shift={(e0-TS)/eps:+.5f} '
              f't1-shift={(e1-TS)/eps:+.5f} Delta/eps^3={d/eps**3:.4f}')
