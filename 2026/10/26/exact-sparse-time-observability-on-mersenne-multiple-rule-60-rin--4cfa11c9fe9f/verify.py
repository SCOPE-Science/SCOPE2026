"""Exact bit-vector reconstruction checks for sparsely observed cyclic Rule 60.

Python 3 standard library only. For each tested ring, the rows are computed
from the local update (not from the closed rank formula).
"""
from math import gcd
from random import Random


def predicted_rank(r, a, q):
    if r < 2 or a < 0 or q < 1:
        raise ValueError("Parameters require r>=2, a>=0, q>=1")
    m = (1 << r) - 1
    odd = q
    b = 0
    while not (odd & 1):
        b += 1
        odd //= 2
    g = gcd(odd, m)
    distinct_nonzero = (m - 1) if g == 1 else (m // g)
    local_length = 1 << max(a - b, 0)
    zero_length = ((1 << a) + q - 1) // q
    return zero_length + local_length * distinct_nonzero


def observed_rank(n, q):
    """Independent row-space elimination using directly computed Rule-60 rows."""
    full = (1 << n) - 1

    def shift_left(v):
        return ((v << 1) | (v >> (n - 1))) & full

    def cyclic_convolution(a, b):
        out = 0
        while b:
            low = b & -b
            k = low.bit_length() - 1
            out ^= (a if k == 0 else ((a << k) | (a >> (n - k))) & full)
            b ^= low
        return out

    h = 1
    for _ in range(q):
        h ^= shift_left(h)
    rows = {}
    row = 1
    for index in range(n + 1):
        v = row
        while v:
            pivot = v.bit_length() - 1
            if pivot not in rows:
                rows[pivot] = v
                break
            v ^= rows[pivot]
        if not v:
            return index
        row = cyclic_convolution(row, h)
    raise AssertionError("More than n independent observations")


def run():
    cases = 0
    for r in range(2, 6):
        for a in range(4 if r <= 3 else 2):
            n = ((1 << r) - 1) * (1 << a)
            if n > 128:
                continue
            for q in range(1, 45):
                got = observed_rank(n, q)
                predicted = predicted_rank(r, a, q)
                assert got == predicted, (r, a, q, got, predicted)
                cases += 1
    rng = Random(602026)
    random_cases = 0
    for _ in range(240):
        r = rng.randint(2, 6)
        a = rng.randint(0, 4)
        n = ((1 << r) - 1) * (1 << a)
        if n > 300:
            continue
        q = rng.randint(1, 120)
        got = observed_rank(n, q)
        predicted = predicted_rank(r, a, q)
        assert got == predicted, (r, a, q, got, predicted)
        random_cases += 1
    print("VERIFY_OK exhaustive_parameter_cases=%d random_cases=%d" % (cases, random_cases))
    for r, a, q in [(3,0,1), (3,0,7), (3,1,3), (3,1,7), (4,1,3), (4,1,7)]:
        n = ((1<<r)-1)*(1<<a)
        print("example n=%d q=%d rank=%d" % (n,q,observed_rank(n,q)))


if __name__ == "__main__":
    run()
