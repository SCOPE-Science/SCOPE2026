#!/usr/bin/env python3
"""Independent finite-instance checks for symmetric bistar heat-gradient bounds.

Uses only Python's standard library.  The finite checks complement, rather than
replace, the proof of the all-degree and asymptotic assertions.
"""
import math

COUNT = 0


def check(condition, message):
    global COUNT
    COUNT += 1
    if not condition:
        raise AssertionError(message)


def parameters(m):
    delta = math.sqrt((m + 3) ** 2 - 8)
    low = 4 / (m + 3 + delta)
    high = (m + 3 + delta) / 2
    slow = (m + 1 - low) / delta
    fast = (2 - low) / delta
    amp_low = (2 - low) * (m + 1 - low) / (m * delta)
    amp_high = (high - 2) * (m + high - 1) / (m * delta)
    return low, high, slow, fast, amp_low, amp_high


def bridge_and_leaf_upper(m, t):
    low, high, slow, fast, amp_low, amp_high = parameters(m)
    bridge = 2 * (slow * math.exp(-low * t) + fast * math.exp(-high * t))
    leaf_upper = (2 * (1 - 1 / m) * math.exp(-t)
                  + 2 * math.exp(-(m + 1) * t)
                  + amp_low * math.exp(-low * t)
                  + amp_high * math.exp(-high * t))
    return bridge, leaf_upper


def heat_column_difference(m, t, u, v):
    """Uniformization of e^{-t L}(delta_u-delta_v), not spectral formulas."""
    size = 2 * m + 2
    edges = [(0, 1)] + [(0, 2 + i) for i in range(m)] + [
        (1, 2 + m + i) for i in range(m)]
    neighbors = [[] for _ in range(size)]
    for i, j in edges:
        neighbors[i].append(j)
        neighbors[j].append(i)
    rate = m + 1
    x = [0.0] * size
    x[u] = 1.0
    x[v] = -1.0
    output = [0.0] * size
    mu = t * rate
    term = math.exp(-mu)
    for k in range(350):
        for j in range(size):
            output[j] += term * x[j]
        if k > mu + 16 and term < 2e-16:
            break
        x = [(1 - len(neighbors[j]) / rate) * x[j] +
             sum(x[h] for h in neighbors[j]) / rate for j in range(size)]
        term *= mu / (k + 1)
    return output


def main():
    for m in range(2, 13):
        low, high, slow, fast, a, b = parameters(m)
        check(abs((low + high) - (m + 3)) < 1e-11, 'trace')
        check(abs(low * high - 2) < 1e-11, 'determinant')
        check(0 < low < 1 and high > m + 2, 'positive rates')
        check(0 < slow < 1 and 0 < fast < 1 and abs(slow + fast - 1) < 1e-11, 'weights')
        check(a > 0 and b > 0, 'mode magnitudes')
        for t in (0, 0.02, 0.1, 0.25, 0.7, 1.5, 2.0):
            c, bound = bridge_and_leaf_upper(m, t)
            br = heat_column_difference(m, t, 0, 1)
            lf = heat_column_difference(m, t, 0, 2)
            check(abs(sum(abs(v) for v in br) - c) < 2e-11, 'bridge norm')
            check(sum(abs(v) for v in lf) <= bound + 2e-11, 'leaf upper')
            check(all(v >= -1e-12 for v in br[:1] + br[2:2+m]), 'positive half')
            check(all(v <= 1e-12 for v in br[1:2] + br[2+m:]), 'negative half')
            check(abs(sum(br)) < 2e-11, 'mass zero')
            check(abs(sum(lf)) < 2e-11, 'mass zero leaf')
    for m in (20, 100, 1000, 10000, 100000):
        low, high, slow, fast, a, b = parameters(m)
        check(abs(m * low - 2) < 6 / m, 'slow rate asymptotic')
        check(abs(slow - 1) < 4 / m, 'slow weight asymptotic')
        val, _ = bridge_and_leaf_upper(m, m / 4)
        check(abs(val / 2 - math.exp(-0.5)) < 3 / m, 'scaled profile')
        check(a <= 2 / m + 1e-12, 'leaf slow amplitude bound')
        check(b <= 6 + 1e-12, 'leaf fast amplitude bound')
    print('PASS:', COUNT, 'finite deterministic assertions (no external dependencies)')

if __name__ == '__main__':
    main()
