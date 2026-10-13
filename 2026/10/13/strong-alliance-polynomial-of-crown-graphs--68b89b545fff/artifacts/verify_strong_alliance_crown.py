from collections import deque
from math import comb


def adjacent(n, u, v):
    if u == v:
        return False
    su, iu = divmod(u, n)
    sv, iv = divmod(v, n)
    return su != sv and iu != iv


def connected(n, chosen):
    if not chosen:
        return False
    start = next(iter(chosen))
    seen = {start}
    q = deque([start])
    while q:
        u = q.popleft()
        for v in chosen:
            if v not in seen and adjacent(n, u, v):
                seen.add(v)
                q.append(v)
    return len(seen) == len(chosen)


def strong_alliance_direct(n, chosen):
    if not chosen or not connected(n, chosen):
        return False
    verts = range(2 * n)
    for u in chosen:
        inside = sum(adjacent(n, u, v) for v in chosen)
        outside = sum(adjacent(n, u, v) for v in verts if v not in chosen)
        if inside < outside:
            return False
    return True


def classified(n, chosen):
    if not chosen:
        return False
    I = {u for u in chosen if u < n}
    J = {u - n for u in chosen if u >= n}
    a, b = len(I), len(J)
    c = len(I & J)
    h = (n - 1 + 1) // 2
    return (c == 0 and a >= h and b >= h) or (c > 0 and a >= h + 1 and b >= h + 1)


def conv(p, q):
    out = [0] * (len(p) + len(q) - 1)
    for i, a in enumerate(p):
        for j, b in enumerate(q):
            out[i + j] += a * b
    return out


def formula(n):
    if n < 4:
        raise ValueError('formula is stated for n >= 4')
    q = [0] * (n + 1)
    if n % 2 == 0:
        m = n // 2
        for k in range(m + 1, n + 1):
            q[k] = comb(n, k)
        out = conv(q, q)
        out[n] += comb(n, m)
    else:
        m = (n - 1) // 2
        for k in range(m + 1, n + 1):
            q[k] = comb(n, k)
        out = conv(q, q)
        out[2 * m] += (m + 1) * comb(n, m)
        out[2 * m + 1] += 2 * comb(n, m)
    return out


def main():
    subset_checks = 0
    classification_checks = 0
    coefficient_checks = 0
    minimum_checks = 0
    max_order = 0
    for n in range(4, 9):
        coeff = [0] * (2 * n + 1)
        for mask in range(1 << (2 * n)):
            chosen = {v for v in range(2 * n) if (mask >> v) & 1}
            direct = strong_alliance_direct(n, chosen)
            structural = classified(n, chosen)
            subset_checks += 1
            classification_checks += 1
            if direct != structural:
                raise AssertionError((n, mask, direct, structural))
            if direct:
                coeff[len(chosen)] += 1
        expected = formula(n)
        if coeff != expected:
            raise AssertionError((n, coeff, expected))
        coefficient_checks += len(coeff)
        nz = [k for k, c in enumerate(coeff) if c]
        expected_min = n if n % 2 == 0 else n - 1
        expected_count = comb(n, n // 2) if n % 2 == 0 else ((n + 1) // 2) * comb(n, (n - 1) // 2)
        if min(nz) != expected_min or coeff[expected_min] != expected_count:
            raise AssertionError((n, min(nz), coeff[expected_min]))
        minimum_checks += 1
        max_order = max(max_order, 2 * n)

    # Boundary n=3 is C6. Connected strong alliances are the six paths of
    # each order 2 through 5, plus the whole cycle.
    n = 3
    coeff = [0] * 7
    for mask in range(1 << 6):
        chosen = {v for v in range(6) if (mask >> v) & 1}
        if strong_alliance_direct(n, chosen):
            coeff[len(chosen)] += 1
    if coeff != [0, 0, 6, 6, 6, 6, 1]:
        raise AssertionError(('boundary_n3', coeff))

    print(
        f'VERIFY_OK n_range=4..8 subset_checks={subset_checks} '
        f'classification_checks={classification_checks} coefficient_checks={coefficient_checks} '
        f'minimum_checks={minimum_checks} max_order={max_order} boundary_n3=C6'
    )


if __name__ == '__main__':
    main()
