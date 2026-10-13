from collections import Counter
from math import factorial


def profile(n, mask):
    I = {i for i in range(n) if (mask >> i) & 1}
    J = {i for i in range(n) if (mask >> (n+i)) & 1}
    P = I - J
    R = J - I
    C = I & J
    return I, J, len(P), len(R), len(C)


def defensive(n, I, J):
    q = (n - 1) // 2
    for i in I:
        d_in = len(J) - (1 if i in J else 0)
        if d_in < q:
            return False
    for j in J:
        d_in = len(I) - (1 if j in I else 0)
        if d_in < q:
            return False
    return bool(I or J)


def dominating(n, I, J):
    for i in range(n):
        if i not in I and not any(j != i for j in J):
            return False
        if i not in J and not any(j != i for j in I):
            return False
    return True


def connected_induced(n, I, J):
    verts = [('a', i) for i in I] + [('b', j) for j in J]
    if len(verts) <= 1:
        return bool(verts)
    seen = {verts[0]}
    stack = [verts[0]]
    while stack:
        side, idx = stack.pop()
        if side == 'a':
            nbrs = [('b', j) for j in J if j != idx]
        else:
            nbrs = [('a', i) for i in I if i != idx]
        for v in nbrs:
            if v not in seen:
                seen.add(v)
                stack.append(v)
    return len(seen) == len(verts)


def classification(n, p, r, c):
    q = (n - 1) // 2
    if c == 0:
        is_def = p >= q and r >= q
    else:
        is_def = p + c >= q + 1 and r + c >= q + 1
    if not is_def:
        return False, False
    if n >= 5:
        return True, True
    if c > 0:
        return True, True
    if n == 4:
        return True, p >= 2 and r >= 2
    return True, False


def multinomial(parts):
    n = sum(parts)
    out = factorial(n)
    for z in parts:
        out //= factorial(z)
    return out


def formula_coeffs(n):
    if n == 3:
        return Counter({4: 9, 5: 6, 6: 1})
    if n == 4:
        return Counter({4: 36, 5: 48, 6: 28, 7: 8, 8: 1})
    q = (n - 1) // 2
    out = Counter()
    for p in range(n + 1):
        for r in range(n - p + 1):
            for c in range(n - p - r + 1):
                w = n - p - r - c
                if c == 0:
                    ok = p >= q and r >= q
                else:
                    ok = p + c >= q + 1 and r + c >= q + 1
                if ok:
                    out[p + r + 2*c] += multinomial((p, r, c, w))
    return out


def main():
    subset_checks = 0
    defensive_sets = 0
    global_sets = 0
    connected_checks = 0
    coefficient_checks = 0
    min_checks = 0
    for n in range(3, 10):
        actual = Counter()
        for mask in range(1 << (2*n)):
            subset_checks += 1
            I, J, p, r, c = profile(n, mask)
            d = defensive(n, I, J)
            g = d and dominating(n, I, J)
            cd, cg = classification(n, p, r, c)
            assert d == cd, (n, mask, p, r, c, d, cd)
            assert g == cg, (n, mask, p, r, c, g, cg)
            if d:
                defensive_sets += 1
            if g:
                global_sets += 1
                actual[len(I)+len(J)] += 1
            if n >= 5 and d:
                connected_checks += 1
                assert g
                assert connected_induced(n, I, J)
        expected = formula_coeffs(n)
        assert actual == expected, (n, actual, expected)
        coefficient_checks += 2*n + 1
        gamma = min(actual)
        if n in (3,4):
            assert gamma == 4
            assert actual[4] == (9 if n == 3 else 36)
        else:
            q = (n - 1)//2
            assert gamma == 2*q
            expected_min = factorial(n)//(factorial(q)*factorial(q)*factorial(n-2*q))
            assert actual[gamma] == expected_min
        min_checks += 1
    print(f"VERIFY_OK n_range=3..9 subset_checks={subset_checks} defensive_sets={defensive_sets} global_sets={global_sets} connected_checks={connected_checks} coefficient_checks={coefficient_checks} minimum_checks={min_checks} max_order=18")

if __name__ == '__main__':
    main()
