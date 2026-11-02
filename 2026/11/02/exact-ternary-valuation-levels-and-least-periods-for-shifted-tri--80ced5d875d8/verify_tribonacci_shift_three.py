#!/usr/bin/env python3
"""Integer checks for ternary divisibility levels of shifted Tribonacci numbers.

Only the Python standard library is needed.  These calculations check
finite premises and finite consequences; the infinite assertion follows
from the separate matrix-lifting argument.
"""
from collections import Counter

M = ((0, 1, 0), (0, 0, 1), (1, 1, 1))
I = ((1, 0, 0), (0, 1, 0), (0, 0, 1))
R = (3, 8, 10)


def mul(A, B, mod=None):
    C = tuple(tuple(sum(A[i][k] * B[k][j] for k in range(3))
                    for j in range(3)) for i in range(3))
    if mod is not None:
        C = tuple(tuple(x % mod for x in row) for row in C)
    return C


def power(e, mod=None):
    A, B = I, M
    while e:
        if e % 2:
            A = mul(A, B, mod)
        B = mul(B, B, mod)
        e //= 2
    return A


def trib_matrix(n, mod):
    # T_0=0,T_1=T_2=1; first row of M^n acts on (0,1,1).
    E = power(n, mod)
    return (E[0][1] + E[0][2]) % mod


def v3_capped(x, cap):
    assert x > 0
    v = 0
    while v < cap and x % 3 == 0:
        x //= 3
        v += 1
    return v


def main():
    P = power(13)
    B = tuple(tuple((P[i][j] - I[i][j]) // 3 for j in range(3))
              for i in range(3))
    assert all((P[i][j] - I[i][j]) % 3 == 0
               for i in range(3) for j in range(3))
    assert B == ((91, 141, 168), (168, 259, 309), (309, 477, 568))
    seq = [0, 1, 1]
    for _ in range(40):
        seq.append(sum(seq[-3:]))
    assert [r for r in range(13) if (seq[r] + 1) % 3 == 0] == list(R)
    assert [(seq[r + 13] - seq[r]) // 3 % 3 for r in R] == [2, 2, 2]
    assert seq[3] == 2 and seq[8] == 44 and seq[10] == 149
    roots = dict.fromkeys(R, 0)
    levels = [dict(roots)]
    for k in range(1, 8):
        nxt = {}
        for r in R:
            options = [roots[r] + digit * 3 ** (k - 1)
                       for digit in range(3)]
            winners = [m for m in options
                       if (trib_matrix(13 * m + r, 3 ** (k + 1)) + 1)
                       % (3 ** (k + 1)) == 0]
            assert len(winners) == 1, (k, r, winners)
            nxt[r] = winners[0]
        assert nxt[10] == 3 ** k - 1
        levels.append(nxt)
        roots = nxt
    assert levels[1] == {3: 1, 8: 0, 10: 2}
    assert levels[2] == {3: 7, 8: 6, 10: 8}
    assert levels[3] == {3: 16, 8: 24, 10: 26}
    assert levels[4] == {3: 16, 8: 78, 10: 80}

    for t in range(1, 7):
        q = 13 * 3 ** t
        prev = levels[t - 1]
        now = levels[t]
        residues = set()
        for r in R:
            for digit in range(3):
                m = prev[r] + digit * 3 ** (t - 1)
                if m != now[r]:
                    residues.add(13 * m + r)
        assert len(residues) == 6
        assert all(0 <= a < q for a in residues)
        assert all(((trib_matrix(a, 3 ** (t + 1)) + 1) % (3 ** t) == 0
                    and (trib_matrix(a, 3 ** (t + 1)) + 1) % (3 ** (t + 1)) != 0)
                   for a in residues)
        # Since q has only prime factors 3 and 13, nonperiodicity
        # at q/3 and q/13 establishes least period q.
        for d in (q // 3, q // 13):
            assert any(((a + d) % q) not in residues for a in residues)

    # Two implementations: direct recurrence modulo 3^7 versus
    # 3-adic digit lifting with matrix exponentiation at sparse indices.
    mod = 3 ** 7
    a, b, c = 0, 1, 1
    checked = 125000
    observed = Counter()
    for n in range(checked):
        actual = v3_capped((a + 1) % mod or mod, 7)
        r = n % 13
        if r not in R:
            expected = 0
        else:
            m = n // 13
            expected = 1
            for k in range(1, 7):
                if m % (3 ** k) == levels[k][r]:
                    expected = k + 1
                else:
                    break
        assert expected == actual, (n, expected, actual)
        if r == 10:
            assert actual == min(7, 1 + v3_capped(n + 3, 6))
        observed[actual] += 1
        a, b, c = b, c, (a + b + c) % mod

    print("VERIFY_OK matrix_power=13 roots_mod13=3,8,10"
          " derivative_mod3=2,2,2 lifted_levels=7"
          " least_period_levels=6 direct_terms=125000"
          " explicit_integer_root=-1")
    print("root_residues_first_four=" + str(levels[1:5]))
    print("direct_valuation_counts_capped_at_7=" + str(dict(sorted(observed.items()))))


if __name__ == "__main__":
    main()
