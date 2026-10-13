from collections import Counter
import math


def trunc(s, t):
    return s if s < t else t


def profile(n, i, j, r):
    N = n - 1
    A = (1 << r) - 1
    B = 1 << r
    if i == j:
        x = (trunc(i, A), trunc(N - i, A))
        y = (x[1], x[0])
        return ("eq", min(x, y))
    if i < j:
        eps, left, middle, right = 1, i, j - i - 1, N - j
    else:
        eps, left, middle, right = -1, j, i - j - 1, N - i
    p = (eps, trunc(left, A), trunc(middle, B), trunc(right, A))
    q = (-eps, p[3], p[2], p[1])
    return ("neq", min(p, q))


def atomic(n):
    return {(i, j): (0 if i == j else 1 if abs(i - j) == 1 else 2)
            for i in range(n) for j in range(n)}


def refine(colors, n):
    signatures = {}
    for i in range(n):
        for j in range(n):
            m = Counter((colors[(i, z)], colors[(z, j)]) for z in range(n))
            signatures[(i, j)] = (colors[(i, j)], tuple(sorted(m.items())))
    ids = {}
    out = {}
    for p, s in signatures.items():
        if s not in ids:
            ids[s] = len(ids)
        out[p] = ids[s]
    return out


def same_partition_by_profile(colors, n, r):
    p_to_c = {}
    c_to_p = {}
    for i in range(n):
        for j in range(n):
            p = profile(n, i, j, r)
            c = colors[(i, j)]
            if p in p_to_c and p_to_c[p] != c:
                return False
            p_to_c[p] = c
            if c in c_to_p and c_to_p[c] != p:
                return False
            c_to_p[c] = p
    return True


def same_partition(a, b):
    pairs = list(a)
    class_map_ab = {}
    class_map_ba = {}
    for p in pairs:
        x, y = a[p], b[p]
        if x in class_map_ab and class_map_ab[x] != y:
            return False
        class_map_ab[x] = y
        if y in class_map_ba and class_map_ba[y] != x:
            return False
        class_map_ba[y] = x
    return True


def predicted_depth(n):
    if n <= 2:
        return 0
    return int(math.floor(math.log2(n - 1)))


def exact_depth(n):
    c = atomic(n)
    r = 0
    while True:
        d = refine(c, n)
        if same_partition(c, d):
            return r
        c = d
        r += 1


def main():
    checked_profiles = 0
    checked_depths = 0
    for n in range(1, 41):
        c = atomic(n)
        r = 0
        assert same_partition_by_profile(c, n, 0), (n, 0)
        checked_profiles += 1
        while True:
            d = refine(c, n)
            assert same_partition_by_profile(d, n, r + 1), (n, r + 1)
            checked_profiles += 1
            if same_partition(c, d):
                got = r
                break
            c = d
            r += 1
        want = predicted_depth(n)
        assert got == want, (n, got, want)
        checked_depths += 1
    print(f"VERIFY_OK paths=1..40 profile_checks={checked_profiles} depth_checks={checked_depths}")


if __name__ == "__main__":
    main()
