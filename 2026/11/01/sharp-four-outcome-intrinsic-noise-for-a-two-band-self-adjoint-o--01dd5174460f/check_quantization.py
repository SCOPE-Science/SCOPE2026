"""Finite checks for the four-outcome operator moment variance formula.

These computations check instances only; the infinite-dimensional statement
requires the analytical operator-inequality proof.
"""
import math
import numpy as np


def optimal_nodes(a):
    assert 0 <= a < 1
    s = (2 * math.sqrt(1 + 3 * a * a) - 1) / 3
    e = (2 - math.sqrt(1 + 3 * a * a)) ** 2 / 9
    return [-1.0, -s, s, 1.0], e


def variance_at(t, nodes):
    assert nodes[0] <= t <= nodes[-1]
    for left, right in zip(nodes[:-1], nodes[1:]):
        if left <= t <= right:
            return (t - left) * (right - t)
    raise RuntimeError('not bracketed')


def band_error(a, nodes):
    # Exact sup of the piecewise quadratic on the two spectral bands.
    points = [-1.0, -a, a, 1.0]
    for lo, hi in zip(nodes[:-1], nodes[1:]):
        mid = (lo + hi) / 2
        if -1 <= mid <= -a or a <= mid <= 1:
            points.append(mid)
    return max(variance_at(t, nodes) for t in points)


def assert_close(a, b, rtol=2e-10, atol=2e-11):
    if abs(a - b) > atol + rtol * max(abs(a), abs(b)):
        raise AssertionError((a, b))


def run():
    counts = {'parameters': 0, 'random_supports': 0, 'operator_matrices': 0}
    rng = np.random.default_rng(20260506)
    for a in (0, .01, .1, .25, .5, .8, .99):
        nodes, e = optimal_nodes(a)
        s = nodes[2]
        assert a < s < 1
        assert_close((1 - s)**2 / 4, s**2 - a**2)
        assert_close(band_error(a, nodes), e)
        # Exact node constraints for finite diagonal spectral models.
        points = np.array([-1., -(1+s)/2, -s, -a, a, s, (s+1)/2, 1.])
        weights = np.zeros((4, len(points)))
        for j, t in enumerate(points):
            for i in range(3):
                lo, hi = nodes[i], nodes[i + 1]
                if lo - 1e-14 <= t <= hi + 1e-14:
                    weights[i, j] = (hi - t) / (hi - lo)
                    weights[i+1,j] = (t - lo) / (hi - lo)
                    break
        assert np.min(weights) >= -1e-14
        assert np.max(abs(weights.sum(axis=0) - 1)) < 1e-14
        assert np.max(abs(np.array(nodes) @ weights - points)) < 1e-14
        variance = np.array(nodes)**2 @ weights - points**2
        assert np.min(variance) >= -1e-14
        assert_close(np.max(variance), e)
        counts['parameters'] += 1
        for _ in range(500):
            u, v = np.sort(rng.uniform(-1, 1, size=2))
            other = [-1., float(u), float(v), 1.]
            assert band_error(a, other) + 1e-12 >= e
            counts['random_supports'] += 1
    # Arbitrary *noncommuting* positive effects: check the quadratic
    # interpolation lower bounds N >= (T-l_i I)(l_{i+1} I-T).
    for d in (2, 3, 5):
        for _ in range(150):
            lam = np.sort(rng.uniform(-2, 2, size=4))
            raw = []
            for j in range(4):
                mat = rng.normal(size=(d,d)) + 1j*rng.normal(size=(d,d))
                raw.append(mat.conj().T @ mat)
            total = sum(raw)
            eigs, vecs = np.linalg.eigh(total)
            invsqrt = (vecs / np.sqrt(eigs)) @ vecs.conj().T
            ps = [invsqrt @ mat @ invsqrt for mat in raw]
            ident = np.eye(d)
            t = sum(z*p for z,p in zip(lam,ps))
            z2 = sum(z*z*p for z,p in zip(lam,ps))
            noise = z2-t@t
            assert np.linalg.norm(sum(ps)-ident) < 2e-12
            assert np.linalg.eigvalsh(noise).min() > -2e-12
            for left, right in zip(lam[:-1], lam[1:]):
                rhs = (t-left*ident)@(right*ident-t)
                assert np.linalg.eigvalsh(noise-rhs).min() > -2e-12
            counts['operator_matrices'] += 1
    print('PASS', counts, 'total=', sum(counts.values()))


if __name__ == '__main__':
    run()
