from collections import deque

def vertices(n):
    return list(range(1, (1 << n) - 1))

def build(n):
    V = vertices(n)
    adj = {u: set() for u in V}
    for i, u in enumerate(V):
        for v in V[i+1:]:
            if (u & v) == 0:
                adj[u].add(v)
                adj[v].add(u)
    return V, adj

def all_dist(V, adj):
    out = {}
    for s in V:
        d = {s: 0}
        q = deque([s])
        while q:
            x = q.popleft()
            for y in adj[x]:
                if y not in d:
                    d[y] = d[x] + 1
                    q.append(y)
        out[s] = d
    return out

def F(m):
    return 2**(m//2) + 2**((m+1)//2)

for n in range(2, 10):
    V, adj = build(n)
    ds = all_dist(V, adj)
    minD = len(V) + 1
    minimizers = []
    full = (1 << n) - 1

    for i, A in enumerate(V):
        for B in V[i+1:]:
            D = [w for w in V if ds[A][w] != ds[B][w]]
            k = len(D)
            if k < minD:
                minD = k
                minimizers = [(A, B)]
            elif k == minD:
                minimizers.append((A, B))

    threshold = len(V) - minD + 1
    if n == 2:
        expected = 1
    elif n == 3:
        expected = 3
    else:
        expected = 2**n - F(n-1) - 2
    assert threshold == expected, (n, threshold, expected)

    if n >= 4:
        assert minD == F(n-1) + 1
        for A, B in minimizers:
            # Orient as A subset B.
            if (A & B) == A:
                small, big = A, B
            elif (A & B) == B:
                small, big = B, A
            else:
                raise AssertionError(("nonnested minimizer", n, A, B))

            assert (big ^ small).bit_count() == 1
            a = small.bit_count()
            d = (full ^ big).bit_count()
            assert abs(a - d) <= 1

        # Conversely every balanced one-coordinate inclusion is minimizing.
        expected_pairs = set()
        for small in V:
            outside = [i for i in range(n) if not (small >> i) & 1]
            for i in outside:
                big = small | (1 << i)
                if big == full:
                    continue
                a = small.bit_count()
                d = (full ^ big).bit_count()
                if abs(a - d) <= 1:
                    expected_pairs.add(tuple(sorted((small, big))))
        actual_pairs = {tuple(sorted(x)) for x in minimizers}
        assert actual_pairs == expected_pairs, (n, len(actual_pairs), len(expected_pairs))

print("VERIFY_OK")
