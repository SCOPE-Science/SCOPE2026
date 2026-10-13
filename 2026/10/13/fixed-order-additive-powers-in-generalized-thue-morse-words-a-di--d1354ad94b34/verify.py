"""Reproducibility checks for unbounded additive-power order classification.

All assertions concern finite ranges; the accompanying proof handles all bases and lengths.
"""
from collections import defaultdict
from math import gcd


def digit_sum_base(n, q):
    s = 0
    while n:
        n, x = divmod(n, q)
        s += x
    return s


def word(N, q):
    return [digit_sum_base(n, q) % q for n in range(N)]


def check_prefix(q, n_max):
    a = word(n_max + q + 1, q)
    prefix = [0]
    for x in a:
        prefix.append(prefix[-1] + x)
    B = q * (q - 1) // 2
    for N in range(n_max + 1):
        z, r = divmod(N, q)
        phase = a[z]
        f = sum((phase + u) % q for u in range(r))
        assert prefix[N] == z * B + f, (q, N)
    return n_max + 1


def check_saturation(q, h, cap=950000):
    masks = [0] * h
    full = (1 << q) - 1
    last = None
    for n in range(cap):
        residue = n % h
        masks[residue] |= 1 << (digit_sum_base(n, q) % q)
        if all(x == full for x in masks):
            last = n
            break
    assert last is not None, (q, h)
    return last


def max_exponent_finite(q, order, n=20000):
    a = word(n, q)
    s = [0]
    for x in a:
        s.append(s[-1] + x)
    block = [s[i + order] - s[i] for i in range(n - order + 1)]
    best = 0
    # For every residue class modulo order, equal consecutive block sums.
    for residue in range(order):
        run = 0
        previous = None
        for j in range(residue, len(block), order):
            value = block[j]
            if value == previous:
                run += 1
            else:
                run = 1
                previous = value
            best = max(best, run)
    return best


def run():
    prefix_cases = 0
    for q in range(2, 10):
        prefix_cases += check_prefix(q, 3000)
    sat = {}
    for q in range(2, 8):
        for h in range(1, 7 if q == 7 else 13):
            sat[(q, h)] = check_saturation(q, h)
    assert sat
    finite = {}
    for q in range(2, 8):
        for ell in range(1, 3 * q + 1):
            finite[(q, ell)] = max_exponent_finite(q, ell, 7000)
            if ell % q == 0:
                # A factor starting at zero has floor(n/ell) consecutive blocks
                # of the same sum, whenever the order is a multiple of q.
                assert finite[(q, ell)] >= 7000 // ell - 1
            else:
                assert finite[(q, ell)] < 7000 // ell, (q, ell, finite[(q, ell)])
    print('VERIFY_OK',
          'prefix_identity_cases=', prefix_cases,
          'saturation_pairs=', len(sat),
          'max_initial_saturation_n=', max(sat.values()),
          'additive_order_pairs=', len(finite),
          'multiples_unbounded_witnessed=', sum(ell % q == 0 for q, ell in finite),
          'nonmultiple_largest_sampled_exponent=', max(v for (q, ell), v in finite.items() if ell % q))


if __name__ == '__main__':
    run()
