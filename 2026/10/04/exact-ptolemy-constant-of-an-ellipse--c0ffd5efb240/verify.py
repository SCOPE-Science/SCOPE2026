import math
import random


def point(t, a, b):
    return (a * math.cos(t), b * math.sin(t))


def dist(p, q):
    return math.hypot(p[0] - q[0], p[1] - q[1])


def ptolemy_ratio(ts, a, b):
    p = [point(t, a, b) for t in ts]
    return (
        dist(p[0], p[1]) * dist(p[2], p[3])
        + dist(p[0], p[3]) * dist(p[1], p[2])
    ) / (dist(p[0], p[2]) * dist(p[1], p[3]))


def interior_angle(prev, cur, nxt):
    u = (prev[0] - cur[0], prev[1] - cur[1])
    v = (nxt[0] - cur[0], nxt[1] - cur[1])
    z = (u[0] * v[0] + u[1] * v[1]) / (
        math.hypot(*u) * math.hypot(*v)
    )
    return math.acos(max(-1.0, min(1.0, z)))


for a, b in [(1.0, 1.0), (2.0, 1.0), (5.0, 2.0), (10.0, 1.0)]:
    sharp = (a * a + b * b) / (2.0 * a * b)
    theta = 4.0 * math.atan(b / a)
    assert abs(1.0 / math.sin(theta / 2.0) - sharp) < 1e-12
    axis = [0.0, math.pi / 2.0, math.pi, 3.0 * math.pi / 2.0]
    assert abs(ptolemy_ratio(axis, a, b) - sharp) < 1e-12

    rng = random.Random(1000 + int(100 * a + b))
    for _ in range(20000):
        ts = sorted(rng.random() * 2.0 * math.pi for _ in range(4))
        gaps = [
            ts[1] - ts[0],
            ts[2] - ts[1],
            ts[3] - ts[2],
            ts[0] + 2.0 * math.pi - ts[3],
        ]
        if min(gaps) < 1e-7:
            continue
        p = [point(t, a, b) for t in ts]
        ang = [
            interior_angle(p[(i - 1) % 4], p[i], p[(i + 1) % 4])
            for i in range(4)
        ]
        opposite_min = min(ang[0] + ang[2], ang[1] + ang[3])
        assert opposite_min + 2e-11 >= theta
        assert ptolemy_ratio(ts, a, b) <= sharp + 2e-11

print("VERIFY_OK")
