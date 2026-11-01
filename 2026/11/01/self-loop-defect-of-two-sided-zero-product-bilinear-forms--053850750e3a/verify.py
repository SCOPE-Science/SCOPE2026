"""Independent exhaustive checks for two-sided zero-product bilinear forms.

Run: python3 verify_twosided_quiver.py
Only small finite prime fields are enumerated; the theorem is proved algebraically.
"""
import itertools


def rank(rows, p):
    pivots = {}
    for raw in rows:
        a = list(raw)
        while True:
            j = next((i for i, v in enumerate(a) if v % p), None)
            if j is None:
                break
            if j in pivots:
                v = a[j]
                a = [(x - v*y) % p for x, y in zip(a, pivots[j])]
            else:
                inv = pow(a[j] % p, -1, p)
                pivots[j] = [(x * inv) % p for x in a]
                break
    return len(pivots)


def check(n, arrows, p):
    N = n + len(arrows)
    rules = [[-1]*N for _ in range(N)]
    for i in range(n):
        rules[i][i] = i
    for j, (s, t) in enumerate(arrows):
        rules[s][n+j] = n+j
        rules[n+j][t] = n+j

    def product(a, b):
        z = [0]*N
        for i, x in enumerate(a):
            if x:
                for j, y in enumerate(b):
                    k = rules[i][j]
                    if k != -1 and y:
                        z[k] = (z[k] + x*y) % p
        return z

    bas = [tuple(int(i == j) for i in range(N)) for j in range(N)]
    two_product_rows = []
    for out in range(N):
        two_product_rows.append([product(bas[i], bas[j])[out]
                                 for i in range(N) for j in range(N)])
        two_product_rows.append([product(bas[j], bas[i])[out]
                                 for i in range(N) for j in range(N)])
    rproduct = rank(two_product_rows, p)

    vectors = list(itertools.product(range(p), repeat=N))
    zero_pair_tensors = []
    for a in vectors:
        for b in vectors:
            if all(v == 0 for v in product(a,b)) and all(v == 0 for v in product(b,a)):
                zero_pair_tensors.append([x*y % p for x in a for y in b])
    rzero = rank(zero_pair_tensors, p)
    loops = sum(s == t for s, t in arrows)
    assert rproduct == n + 2*len(arrows) - loops, (n, arrows, p, rproduct)
    assert N*N - rzero == n + 2*len(arrows), (n, arrows, p, rzero)
    assert N*N - rzero - rproduct == loops
    return (N, rproduct, rzero, loops)


def main():
    cases = [
        (1, []), (1, [(0,0)]), (1, [(0,0),(0,0)]),
        (2, []), (2, [(0,1)]), (2, [(0,1),(0,1)]),
        (2, [(0,1),(1,0)]), (2, [(0,0)]),
        (2, [(0,0),(0,1)]), (2, [(0,0),(1,1)]),
        (3, [(0,1),(1,2)]), (3, [(0,1),(1,2),(2,0)]),
        (3, [(0,1),(1,0),(0,0)]),
    ]
    k = 0
    for n, arr in cases:
        print('q=2 n=%s arrows=%s dims=%s' % (n, arr, check(n,arr,2)))
        k += 1
    for n, arr in [
        (1, [(0,0)]), (2, [(0,1)]), (2, [(0,1),(1,0)]),
        (2, [(0,0),(0,1)]), (3, [(0,1),(1,2)]),
    ]:
        print('q=3 n=%s arrows=%s dims=%s' % (n, arr, check(n,arr,3)))
        k += 1
    print('VERIFY_OK: %s exhaustive prime-field configurations' % k)


if __name__ == '__main__':
    main()
