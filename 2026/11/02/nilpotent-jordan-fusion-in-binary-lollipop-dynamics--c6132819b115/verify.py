"""Direct finite checks for binary neighbor-sum dynamics on lollipop graphs.

Run: python3 verify.py
Only standard-library integer arithmetic is used.
"""


def lollipop(n, m):
    size = n + m
    rows = [0] * size
    def edge(a, b):
        rows[a] ^= 1 << b
        rows[b] ^= 1 << a
    for i in range(n):
        edge(i, (i + 1) % n)
    for j in range(m):
        edge(0 if j == 0 else n + j - 1, n + j)
    return rows


def multiply(a, b):
    out = []
    for row in a:
        x = 0
        while row:
            bit = row & -row
            x ^= b[bit.bit_length() - 1]
            row -= bit
        out.append(x)
    return out


def rank(rows):
    basis = {}
    for row in rows:
        while row:
            bit = row.bit_length() - 1
            if bit in basis:
                row ^= basis[bit]
            else:
                basis[bit] = row
                break
    return len(basis)


def value_at(rows, x):
    y = 0
    for i, row in enumerate(rows):
        if (row & x).bit_count() & 1:
            y |= 1 << i
    return y


def two_power_part(x):
    return x & -x


def expected_blocks(n, m):
    e = two_power_part(n)
    s = two_power_part(m + 2)
    if n & 1:
        return [] if m & 1 else [s - 1]
    if m & 1:
        return [e - 1]
    if m % 4 == 2:
        return sorted([1, e + s - 3])
    d = min(e // 2, two_power_part(m) - 1)
    return sorted([d, e - d])


def path_poly_values(limit):
    p = [1, 2]
    for _ in range(2, limit + 1):
        p.append((p[-1] << 1) ^ p[-2])
    return p


def poly_mul(a, b):
    result = 0
    while b:
        if b & 1:
            result ^= a
        b >>= 1
        a <<= 1
    return result


def char_poly_direct(rows):
    """Det(xI-A) via subset assignment DP, valid since signs vanish in F2."""
    size = len(rows)
    dp = [0] * (1 << size)
    dp[0] = 1
    for mask in range(1 << size):
        r = mask.bit_count()
        if r == size or not dp[mask]:
            continue
        rem = ((1 << size) - 1) ^ mask
        while rem:
            bit = rem & -rem
            c = bit.bit_length() - 1
            if c == r:
                dp[mask | bit] ^= dp[mask] << 1
            elif (rows[r] >> c) & 1:
                dp[mask | bit] ^= dp[mask]
            rem -= bit
    return dp[-1]


def check():
    matrix_cases = 0
    power_cases = 0
    characteristic_cases = 0
    exhaustive_states = 0
    exhaustive_cases = 0
    max_seen = 0
    for n in range(3, 33):
        for m in range(1, 33):
            rows = lollipop(n, m)
            size = n + m
            blocks = expected_blocks(n, m)
            assert all(b > 0 for b in blocks), (n, m, blocks)
            q = sum(blocks)
            B = max(blocks, default=0)
            max_seen = max(max_seen, B)
            power = [1 << i for i in range(size)]
            for t in range(B + 3):
                nullity = size - rank(power)
                expected = sum(min(t, b) for b in blocks)
                assert nullity == expected, (n, m, t, nullity, expected)
                power = multiply(power, rows)
                power_cases += 1
            matrix_cases += 1
            if size <= 11:
                p = path_poly_values(size + 2)
                characteristic = char_poly_direct(rows)
                assert characteristic == poly_mul(p[n - 1], p[m + 1]), (n, m)
                characteristic_cases += 1
                # Entire finite functional graph, separate from linear-rank formulas.
                hist = [0] * (B + 1)
                for x in range(1 << size):
                    seen = {}
                    z = x
                    while z not in seen:
                        seen[z] = len(seen)
                        z = value_at(rows, z)
                    tau = seen[z]
                    assert tau <= B, (n, m, x, tau, B)
                    hist[tau] += 1
                    exhaustive_states += 1
                for t in range(B + 1):
                    predicted = (1 << (size - q + sum(min(t, b) for b in blocks)))
                    assert sum(hist[:t + 1]) == predicted, (n, m, t)
                exhaustive_cases += 1
    print('OK matrix_parameter_pairs', matrix_cases)
    print('OK direct_rank_power_checks', power_cases)
    print('OK direct_characteristic_polynomial_checks', characteristic_cases)
    print('OK exhaustive_functional_graph_pairs', exhaustive_cases)
    print('OK exhaustive_states', exhaustive_states)
    print('OK largest_tested_transient_length', max_seen)


if __name__ == '__main__':
    check()
