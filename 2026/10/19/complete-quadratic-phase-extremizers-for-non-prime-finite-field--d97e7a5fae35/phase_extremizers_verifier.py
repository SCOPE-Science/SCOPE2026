#!/usr/bin/env python3
"""Exact prime-field linear relation certificates for threefold parabola fibers.

No floating-point comparisons or searches outside the specified finite fields.
"""

def field_data(p, nonsquare=None):
    if nonsquare is None:
        q = p
        add = lambda x, y: (x + y) % p
        mul = lambda x, y: (x * y) % p
        trace = lambda x: x % p
        basis = (1,)
    else:
        q = p * p
        add = lambda x, y: ((x % p + y % p) % p) + p * ((x // p + y // p) % p)
        mul = lambda x, y: ((x % p * (y % p) + nonsquare * (x // p) * (y // p)) % p) + p * (((x % p) * (y // p) + (x // p) * (y % p)) % p)
        trace = lambda x: (2 * (x % p)) % p
        basis = (1, p)
    return q, add, mul, trace, basis


def analyze(p, nonsquare=None):
    q, add, mul, trace, basis = field_data(p, nonsquare)
    if nonsquare is not None:
        assert nonsquare not in {(i * i) % p for i in range(p)}
        assert all(len({mul(x, y) for y in range(q)}) == q for x in range(1, q))
    square = [mul(x, x) for x in range(q)]
    sums = [[add(x, y) for y in range(q)] for x in range(q)]
    quadratic_character_rows = [[trace(mul(alpha, x)) for x in range(q)] for alpha in basis]
    quadratic_character_rows += [[trace(mul(beta, square[x])) for x in range(q)] for beta in basis]
    basis_rows = [[1] * q] + quadratic_character_rows
    pivots = {}
    fibers = {}
    fiber_counts = {}
    comparisons = 0
    for a in range(q):
        for b in range(q):
            s_ab = sums[a][b]
            t_ab = sums[square[a]][square[b]]
            for c in range(q):
                key = (sums[s_ab][c], sums[t_ab][square[c]])
                fiber_counts[key] = fiber_counts.get(key, 0) + 1
                if key not in fibers:
                    row = [0] * q
                    for x in (a, b, c):
                        row[x] = (row[x] + 1) % p
                    fibers[key] = row
                    continue
                row = [(-v) % p for v in fibers[key]]
                for x in (a, b, c):
                    row[x] = (row[x] + 1) % p
                comparisons += 1
                assert all(sum(u * v for u, v in zip(row, f)) % p == 0 for f in basis_rows)
                for pivot, vector in sorted(pivots.items()):
                    coeff = row[pivot]
                    if coeff:
                        row = [(x - coeff * y) % p for x, y in zip(row, vector)]
                pivot = next((i for i, val in enumerate(row) if val), None)
                if pivot is not None:
                    inv = pow(row[pivot], -1, p)
                    pivots[pivot] = [(val * inv) % p for val in row]
    rank = len(pivots)
    # The constant, linear-trace and quadratic-trace functions are independent exactly
    # when all p^(2n) projective patterns appear as distinct solutions of the linear equations.
    expected = q - (1 + 2 * len(basis))
    assert rank == expected, (q, rank, expected)
    assert len(fibers) == q * q
    assert sum(v*v for v in fiber_counts.values()) == q**4 + q**3 - q**2
    if nonsquare is not None:
        # A field-of-size-p^2 witness for the non-prime Frobenius coefficient obstruction.
        E_nonzero = 0
        for a in range(q):
            for b in range(q):
                ab = mul(a, b)
                phi = add(add(square[a], ab), square[b])
                if phi != 1:
                    continue
                ap1 = mul(a, pow_field(a, p, mul))
                bp1 = mul(b, pow_field(b, p, mul))
                abp1 = mul(add(a, b), pow_field(add(a, b), p, mul))
                expr = add(add(add(ap1, bp1), abp1), p - 2)
                E_nonzero += (expr != 0)
        assert E_nonzero > 0
    else:
        E_nonzero = None
    print(f"q={q} p={p} fibers={len(fibers)} sixth_moment_fiber_square_sum={q**4+q**3-q**2} triple_comparisons={comparisons} relation_rank={rank} projective_phase_dimension={2*len(basis)} E1_witness_count={E_nonzero}")


def pow_field(a, exponent, mul):
    result = 1
    while exponent:
        if exponent & 1:
            result = mul(result, a)
        a = mul(a, a)
        exponent >>= 1
    return result


if __name__ == '__main__':
    analyze(5)
    analyze(7)
    analyze(5, 2)
    analyze(7, 3)
    print('ALL EXACT TESTS PASSED')
