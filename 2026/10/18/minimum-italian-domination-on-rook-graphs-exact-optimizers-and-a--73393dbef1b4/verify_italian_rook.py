"""Independent exhaustive checks for Italian domination of rook graphs.
Public science artifact; no external dependencies.
"""
from itertools import product, combinations
from math import comb, factorial


def onto(n, m):
    return sum((-1) ** j * comb(m, j) * (m - j) ** n for j in range(m + 1))


def predicted(m, n):
    assert 1 <= m <= n
    k = min(n, 2 * m)
    if n < 2 * m:
        count = onto(n, m)
    elif n > 2 * m:
        count = (n + comb(n, 2)) ** m
    else:
        count = (n + comb(n, 2)) ** m + onto(n, m) - factorial(n) // (2 ** m)
    return k, count


def valid(labels, m, n, nb):
    for v, w in enumerate(labels):
        if w == 0 and sum(labels[u] for u in nb[v]) < 2:
            return False
    return True


def check(m, n):
    N = m * n
    adj = tuple(tuple(u for u in range(N) if u != v and (u // n == v // n or u % n == v % n)) for v in range(N))
    gamma, count = predicted(m, n)
    low, num = 2 * N + 1, 0
    checked = 0
    for a in product((0, 1, 2), repeat=N):
        checked += 1
        w = sum(a)
        if w > gamma:
            continue
        if valid(a, m, n, adj):
            if w < low:
                low, num = w, 1
            elif w == low:
                num += 1
    assert (low, num) == (gamma, count), ((m,n), (low,num), (gamma,count))
    return checked, num



def check_low_weight(m, n):
    """Independently enumerate every labeling of weight <= the claimed optimum."""
    N = m * n
    adj = tuple(tuple(u for u in range(N) if u != v and (u // n == v // n or u % n == v % n)) for v in range(N))
    gamma, expected = predicted(m, n)
    best, count, checked = 2 * N + 1, 0, 0
    cells = tuple(range(N))
    for w in range(gamma + 1):
        for t in range(w // 2 + 1):
            ones = w - 2 * t
            for twos in combinations(cells, t):
                omitted = set(twos)
                avail = tuple(c for c in cells if c not in omitted)
                for pos1 in combinations(avail, ones):
                    checked += 1
                    labels = [0] * N
                    for v in twos: labels[v] = 2
                    for v in pos1: labels[v] = 1
                    if valid(labels, m, n, adj):
                        if w < best:
                            best, count = w, 1
                        elif w == best:
                            count += 1
    assert (best, count) == (gamma, expected), ((m, n), (best, count), (gamma, expected))
    return checked, count


def main():
    cases = [(1,n) for n in range(1,8)] + [(2,n) for n in range(2,7)] + [(3,n) for n in range(3,5)]
    total = 0
    for m, n in cases:
        a, num = check(m,n)
        total += a
        print(f"PASS {m}x{n}: {a} labelings, {num} minimizers")
    print(f"PASS total {len(cases)} graph orders, {total} complete assignments")
    more = [(3, 5), (3, 6), (4, 5), (4, 6)]
    extra = 0
    for m, n in more:
        checked, num = check_low_weight(m, n)
        extra += checked
        print(f"PASS {m}x{n}: {checked} low-weight labelings, {num} minimizers")
    print(f"PASS additional {extra} exhaustive at-or-below-optimum labelings")


if __name__ == '__main__':
    main()
