from collections import defaultdict


def cdist(n, x, y):
    d = abs(x - y) % n
    return min(d, n - d)


def code_on_cycle(L, a, x):
    n = 2 * L
    return tuple(sorted((cdist(n, x, 0), cdist(n, x, a), cdist(n, x, L))))


def normalized(L, a, x):
    s = code_on_cycle(L, a, x)
    return (s[1] - s[0], s[2] - s[0]), s[0]


def predicted_tau(L, a):
    if a % 2 == 0:
        return a // 2
    return min(a, (L - a) // 2)


def predicted_pairs(L, a):
    if a % 2 == 0:
        return {
            tuple(sorted((j, (2 * L + a // 2 - j) % (2 * L))))
            for j in range(a, L - a // 2 + 1)
        }
    if 3 * a <= L:
        return {tuple(sorted(((L - a) // 2, (3 * L - a) // 2)))}
    t = (L - a) // 2
    return {
        tuple(sorted((j, (2 * L - t - j) % (2 * L))))
        for j in range(t, a + 1)
    }


def check_cycle_classification(limit=301):
    for L in range(7, limit + 1, 2):
        for a in range(1, (L - 1) // 2 + 1):
            fibres = defaultdict(list)
            for x in range(2 * L):
                h, mu = normalized(L, a, x)
                fibres[h].append((x, mu))
            repeated = [v for v in fibres.values() if len(v) > 1]
            assert repeated
            assert all(len(v) == 2 for v in repeated)
            actual_pairs = {tuple(sorted((v[0][0], v[1][0]))) for v in repeated}
            assert actual_pairs == predicted_pairs(L, a)
            diffs = {abs(v[0][1] - v[1][1]) for v in repeated}
            assert diffs == {predicted_tau(L, a)}


def best_a(L):
    q, r = divmod(L, 6)
    if r == 1:
        return 2 * q + 1
    if r == 3:
        return 2 * q + 1
    if r == 5:
        return 2 * q + 3
    raise ValueError("L must be odd")


def resolves(m, n, a):
    L = n // 2
    seen = {}
    for i in range(m):
        for x in range(n):
            base = code_on_cycle(L, a, x)
            code = tuple(z + i for z in base)
            if code in seen:
                return False
            seen[code] = (i, x)
    return True


def check_cylinders():
    for m in range(3, 41):
        upper = min(6 * m + 80, 400)
        for n in range(6 * m, upper):
            if n % 4 == 2:
                L = n // 2
                a = best_a(L)
                assert predicted_tau(L, a) == L // 3
                assert resolves(m, n, a)


if __name__ == "__main__":
    check_cycle_classification()
    check_cylinders()
    print("cycle classification: verified for odd 7 <= L <= 301 and all admissible a")
    print("cylinder construction: verified for 3 <= m <= 40 over the stated finite test band")
