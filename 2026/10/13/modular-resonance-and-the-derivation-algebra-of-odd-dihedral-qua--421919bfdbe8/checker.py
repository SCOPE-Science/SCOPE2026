"""Independent finite-field checks for derivations of odd dihedral quandle algebras.

All arithmetic is in the prime field. No external packages are needed.
"""
from math import gcd


def row_rank_mod_p(rows, p):
    """Sparse modular elimination of independently constructed Leibniz equations."""
    pivots = {}
    for row in rows:
        row = {k: v % p for k, v in row.items() if v % p}
        while row:
            k = min(row)
            if k not in pivots:
                inv = pow(row[k], -1, p)
                pivots[k] = {j: (v * inv) % p for j, v in row.items() if v % p}
                break
            fac = row[k]
            for j, val in pivots[k].items():
                new = (row.get(j, 0) - fac * val) % p
                if new:
                    row[j] = new
                else:
                    row.pop(j, None)
    return len(pivots)


def direct_derivation_dim(n, p):
    """Kernel dimension for D(e_i e_j)=D(e_i)e_j+e_iD(e_j)."""
    equations = []
    for i in range(n):
        for j in range(n):
            product = (2 * j - i) % n
            for k in range(n):
                row = {}

                def add(out, col, amount):
                    idx = out * n + col
                    row[idx] = row.get(idx, 0) + amount

                add(k, product, 1)
                add((2 * j - k) % n, i, -1)
                for a in range(n):
                    if (2 * a - i) % n == k:
                        add(a, j, -1)
                equations.append(row)
    return n * n - row_rank_mod_p(equations, p)


def order_mod(a, d):
    val, t = a % d, 1
    while val != 1:
        val = val * a % d
        t += 1
    return t


def predicted_dim(n, p):
    if p == 2:
        return 0
    ans = 0
    for d in range(3, n + 1, 2):
        if n % d:
            continue
        t = order_mod(2, d)
        power_set = {pow(2, j, d) for j in range(t)}
        minus_in = d - 1 in power_set
        orbit_length = t if minus_in else 2 * t
        compatible = pow(2, t, p) == 1
        if minus_in:
            compatible &= (t % 2 == 0 and pow(2, t // 2, p) == p - 1)
        if compatible:
            phi = sum(gcd(j, d) == 1 for j in range(1, d + 1))
            assert phi % orbit_length == 0
            ans += phi // orbit_length
    return ans


def check_explicit_R11_F3():
    n, p = 11, 3
    residues = {x * x % n for x in range(1, n)}
    kernel = [0] + [1 if t in residues else p - 1 for t in range(1, n)]
    for i in range(n):
        for j in range(n):
            for k in range(n):
                left = kernel[(k - (2 * j - i)) % n]
                right = kernel[((2 * j - k) - i) % n]
                right += sum(kernel[(a - j) % n]
                             for a in range(n) if (2 * a - i) % n == k)
                assert (left - right) % p == 0, (i, j, k)
    assert predicted_dim(n, p) == direct_derivation_dim(n, p) == 1
    return kernel


def main():
    tests = 0
    nonzero = []
    for n in (3, 5, 7, 9, 11, 13, 15, 17, 19, 21):
        for p in (2, 3, 5, 7, 11, 13, 17, 19):
            if n % p == 0:
                continue
            a = direct_derivation_dim(n, p)
            b = predicted_dim(n, p)
            assert a == b, (n, p, a, b)
            tests += 1
            if a:
                nonzero.append((n, p, a))
    kernel = check_explicit_R11_F3()
    assert kernel == [0, 1, 2, 1, 1, 1, 2, 2, 2, 1, 2]
    print('VERIFY_OK', tests, 'dimension comparisons; nonzero:', nonzero,
          '; R11/F3 full Leibniz check')


if __name__ == '__main__':
    main()
