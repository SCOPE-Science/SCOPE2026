from collections import Counter
from itertools import product

def convolve(a, b):
    out = Counter()
    for i, ai in a.items():
        for j, bj in b.items():
            out[i + j] += ai * bj
    return out

def power(poly, n):
    out = Counter({0: 1})
    for _ in range(n):
        out = convolve(out, poly)
    return out

def formula(n):
    T = Counter({1: 1, 2: 3, 3: 2, 4: 1})
    U = Counter({1: 1, 2: 2, 3: 1})
    V = Counter({2: 2, 3: 1})
    out = power(T, n)
    for k, v in power(U, n).items():
        out[k] -= v
    for k, v in power(V, n).items():
        out[k] += v
    return Counter({k: v for k, v in out.items() if v})

def edges(n):
    adj = [set() for _ in range(2 * n)]
    for i in range(n):
        for j in range(i + 1, n):
            adj[i].add(j)
            adj[j].add(i)
        adj[i].add(n + i)
        adj[n + i].add(i)
    return adj

def roman(labels, adj):
    for v, val in enumerate(labels):
        if val == 0 and not any(labels[u] == 2 for u in adj[v]):
            return False
    return True

def main():
    assignments = 0
    coefficient_checks = 0
    for n in range(2, 7):
        adj = edges(n)
        brute = Counter()
        for labels in product(range(3), repeat=2 * n):
            assignments += 1
            if roman(labels, adj):
                brute[sum(labels)] += 1
        expected = formula(n)
        assert brute == expected, (n, brute, expected)
        coefficient_checks += len(expected)
        minimum = min(brute)
        assert minimum == n + 1, (n, minimum)
        assert brute[minimum] == n, (n, brute[minimum])
        assert sum(brute.values()) == 7 ** n - 4 ** n + 3 ** n
    print(
        "VERIFY_OK n_range=2..6 "
        f"assignments={assignments} "
        f"coefficient_checks={coefficient_checks} "
        "minimum_checks=5 total_checks=5 max_order=12"
    )

if __name__ == "__main__":
    main()
