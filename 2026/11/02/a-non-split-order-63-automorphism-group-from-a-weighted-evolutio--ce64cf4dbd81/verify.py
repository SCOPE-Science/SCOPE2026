"""Independent modular-field monomial automorphism and extension checks.
Run: python verify_weighted_cycle.py
For a weighted six-cycle evolution algebra over three prime fields.
"""
from collections import Counter
from math import gcd

def cubic_root(p):
    for z in range(2, p):
        if z != 1 and pow(z, 3, p) == 1:
            return z
    raise AssertionError("no primitive cube root")

def run(p):
    assert p in (43, 211, 337)
    assert (p - 1) % 21 == 0 and (p - 1) % 9 != 0
    zeta = cubic_root(p)
    n = 6
    w = (zeta, 1, 1, 1, 1, 1)
    def maps_for_rotation(r):
        answers = []
        for t0 in range(1, p):
            t = [t0]
            for i in range(n):
                next_t = pow(t[i], 2, p) * w[(i + r) % n] * pow(w[i], -1, p) % p
                if i == n - 1:
                    if next_t != t0:
                        break
                else:
                    t.append(next_t)
            else:
                t = tuple(t)
                for i in range(n):
                    assert w[i] * t[(i + 1) % n] % p == (t[i] ** 2) * w[(i + r) % n] % p
                answers.append((r, t))
        return answers
    per_rot = [maps_for_rotation(r) for r in range(n)]
    assert tuple(map(len, per_rot)) == (21, 0, 21, 0, 21, 0)
    group = set(sum(per_rot, []))
    assert len(group) == 63
    identity = (0, (1,) * n)
    def compose(f, g):
        # First g, then f: f(g(e_i)) = g_i f(e_{i+s}).
        r, t = f
        s, u = g
        return ((r + s) % n, tuple(u[i] * t[(i + s) % n] % p for i in range(n)))
    for x in group:
        assert compose(x, identity) == compose(identity, x) == x
        for y in group:
            assert compose(x, y) in group
    def order(x):
        v = identity
        for k in range(1, 64):
            v = compose(x, v)
            if v == identity:
                return k
        raise AssertionError("order > 63")
    spectrum = Counter(order(g) for g in group)
    assert dict(spectrum) == {1: 1, 3: 2, 7: 6, 9: 42, 21: 12}
    assert all(order(g) == 9 for g in per_rot[2] + per_rot[4])
    for g in per_rot[2]:
        cube = compose(g, compose(g, g))
        assert cube[0] == 0 and cube[1][0] == pow(zeta, -1, p)
        assert cube != identity
    # With all weights 1, the same support graph has split pure rotations.
    w = (1,) * 6
    assert tuple(len(maps_for_rotation(r)) for r in range(n)) == (21,) * 6
    print('VERIFY_CASE_OK',p,'zeta',zeta,'twisted_group_order',63,'rotations',(21,0,21,0,21,0),'order_spectrum',dict(sorted(spectrum.items())))

if __name__ == '__main__':
    for p in (43, 211, 337):
        run(p)
    print('VERIFY_OK')
