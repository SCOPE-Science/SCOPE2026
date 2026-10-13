from itertools import combinations, product


def gaussian_binom(n, k, q):
    if k < 0 or k > n:
        return 0
    if k == 0 or k == n:
        return 1
    num = den = 1
    for i in range(k):
        num *= q ** (n - i) - 1
        den *= q ** (k - i) - 1
    return num // den


def galois(n, q):
    return sum(gaussian_binom(n, k, q) for k in range(n + 1))


def flag_count(n, q):
    return sum(gaussian_binom(n, u, q) * gaussian_binom(u, k, q)
               for u in range(n + 1) for k in range(u + 1))


def multinomial_flag_count(n, q):
    return sum(gaussian_binom(n, a, q) * gaussian_binom(n-a, b, q)
               for a in range(n + 1) for b in range(n-a + 1))


def rref_subspaces(n, q):
    yield tuple()
    for r in range(1, n + 1):
        for pivots in combinations(range(n), r):
            pset = set(pivots)
            free = []
            for i, p in enumerate(pivots):
                for j in range(p + 1, n):
                    if j not in pset:
                        free.append((i, j))
            for vals in product(range(q), repeat=len(free)):
                rows = [[0] * n for _ in range(r)]
                for i, p in enumerate(pivots):
                    rows[i][p] = 1
                for (i, j), v in zip(free, vals):
                    rows[i][j] = v
                yield tuple(tuple(row) for row in rows)


def rank(rows, p):
    a = [list(r) for r in rows if any(x % p for x in r)]
    if not a:
        return 0
    m, n = len(a), len(a[0])
    rr = cc = 0
    while rr < m and cc < n:
        pivot = next((i for i in range(rr, m) if a[i][cc] % p), None)
        if pivot is None:
            cc += 1
            continue
        a[rr], a[pivot] = a[pivot], a[rr]
        inv = pow(a[rr][cc] % p, -1, p)
        a[rr] = [(inv*x) % p for x in a[rr]]
        for i in range(m):
            if i != rr and a[i][cc] % p:
                c = a[i][cc] % p
                a[i] = [(x-c*y) % p for x,y in zip(a[i], a[rr])]
        rr += 1
        cc += 1
    return rr


def is_subspace(K, U, p):
    return rank(U + K, p) == rank(U, p)


def contains(U, v, p):
    return rank(U + (tuple(v),), p) == rank(U, p)

checks = 0

# Independent enumeration of subspaces and nested pairs for small prime fields.
for q, max_n in [(2, 5), (3, 4)]:
    for n in range(max_n + 1):
        subs = list(rref_subspaces(n, q))
        assert len(subs) == galois(n, q)
        checks += 1
        direct_flags = 0
        seen_signatures = set()
        ambient = list(product(range(q), repeat=n))
        for U in subs:
            for K in subs:
                if is_subspace(K, U, q):
                    direct_flags += 1
                    sig = tuple(0 if contains(K, v, q) else 1 if contains(U, v, q) else 2
                                for v in ambient)
                    assert sig not in seen_signatures
                    seen_signatures.add(sig)
                    checks += 1
        assert direct_flags == flag_count(n, q)
        assert len(seen_signatures) == direct_flags
        checks += 2

# Two exact forms of the flag sum agree for several fields and dimensions.
for q in (2, 3, 4, 5, 7):
    for n in range(0, 11):
        assert flag_count(n, q) == multinomial_flag_count(n, q)
        checks += 1

# The dominant q-exponents are exactly floor(n^2/3) and floor(n^2/4).
for n in range(0, 101):
    e_flag = max(a*b + a*c + b*c
                 for a in range(n+1)
                 for b in range(n-a+1)
                 for c in [n-a-b])
    e_sub = max(k*(n-k) for k in range(n+1))
    assert e_flag == n*n // 3
    assert e_sub == n*n // 4
    checks += 2

print('O_n(2), n=0..8:', [flag_count(n,2) for n in range(9)])
print('I_n(2), n=0..8:', [galois(n,2) for n in range(9)])
print('O_n(3), n=0..6:', [flag_count(n,3) for n in range(7)])
print('checks:', checks)
print('VERIFY_OK')
