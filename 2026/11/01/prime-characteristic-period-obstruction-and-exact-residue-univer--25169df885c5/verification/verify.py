"""Independent small-instance enumeration for modular neighbor-sum graph dynamics."""
from collections import Counter
from itertools import product
from math import lcm


def order(a, p):
    assert a % p
    for d in range(1, p):
        if pow(a, d, p) == 1:
            return d
    raise AssertionError("not a finite-field unit")


def predicted(p, parts):
    r = len(parts)
    assert r >= 2 and all(n >= 1 for n in parts)
    a = parts[0] % p
    assert all(n % p == a for n in parts)
    N = sum(parts)
    if a == 0:
        rank = r - (1 if (r - 1) % p == 0 else 0)
        return Counter({(0, 1): 1, (1, 1): p**(N-rank)-1,
                        (2, 1): p**N-p**(N-rank)})
    d = order(-a, p)
    recurrent = Counter({1: 1})
    if r % p == 0:
        recurrent[d] += p**(r-1)-1
        recurrent[p*d] += p**r-p**(r-1)
        dim = r
    elif (r-1) % p == 0:
        recurrent[d] += p**(r-1)-1
        dim = r-1
    else:
        e = order(a*(r-1), p)
        recurrent[d] += p**(r-1)-1
        recurrent[e] += p-1
        recurrent[lcm(d,e)] += (p**(r-1)-1)*(p-1)
        dim = r
    fiber = p**(N-dim)
    ans = Counter()
    for period, points in recurrent.items():
        if points:
            ans[(0, period)] = points
            if fiber > 1:
                ans[(1, period)] = points*(fiber-1)
    return ans


def observed(p, parts):
    r = len(parts)
    N = sum(parts)
    groups = [list(range(sum(parts[:i]), sum(parts[:i+1]))) for i in range(r)]
    owner = [i for i,g in enumerate(groups) for _ in g]
    def step(x):
        sums = [sum(x[j] for j in g) % p for g in groups]
        total = sum(sums) % p
        return tuple((total - sums[owner[j]]) % p for j in range(N))
    ans = Counter()
    for x in product(range(p), repeat=N):
        visited = {}
        orbit = []
        y = x
        while y not in visited:
            visited[y] = len(orbit)
            orbit.append(y)
            y = step(y)
        t = visited[y]
        period = len(orbit)-t
        ans[(t,period)] += 1
    return ans


def main():
    cases = [
        (3,(1,1)), (3,(1,1,1)), (3,(2,2,2)),
        (3,(1,4,1)), (3,(1,1,1,1)), (3,(1,1,1,1,1)),
        (3,(3,3)),
        (3,(2,2,2,2)), (3,(2,2,2,2,2)),
        (5,(1,1)), (5,(1,1,1)), (5,(1,1,1,1,1)),
        (5,(1,1,1,1,1,1)),
        (7,(1,1,1)),
    ]
    total = 0
    for p, parts in cases:
        count = p**sum(parts)
        if count > 100_000:
            raise AssertionError("unbounded test case")
        expected = predicted(p,parts)
        actual = observed(p,parts)
        if expected != actual:
            raise AssertionError((p, parts, dict(expected), dict(actual)))
        assert sum(actual.values()) == count
        print(f"p={p}, parts={parts}, configurations={count}, classes={dict(sorted(actual.items()))}")
        total += count
    print(f"MODULAR_MULTIPARTITE_VERIFY_OK cases={len(cases)} configurations={total}")


if __name__ == '__main__':
    main()
