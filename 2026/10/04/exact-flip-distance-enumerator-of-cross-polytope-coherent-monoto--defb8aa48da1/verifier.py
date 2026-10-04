from collections import Counter, deque
from itertools import product
from math import comb


def vertices(m):
    return [x for x in product((-1, 0, 1), repeat=m) if any(x)]


def l1(a, b):
    return sum(abs(x-y) for x, y in zip(a, b))


def predicted(a, b):
    sa = sum(x != 0 for x in a)
    if sa == 1 and tuple(-x for x in a) == b:
        return 4
    return l1(a, b)


def neighbors(x):
    m = len(x)
    for i, xi in enumerate(x):
        if xi == 0:
            vals = (-1, 1)
        else:
            vals = (0,)
        for y in vals:
            z = list(x)
            z[i] = y
            z = tuple(z)
            if any(z):
                yield z


def bfs_all(vs):
    out = {}
    vset = set(vs)
    for s in vs:
        dist = {s: 0}
        q = deque([s])
        while q:
            x = q.popleft()
            for y in neighbors(x):
                if y in vset and y not in dist:
                    dist[y] = dist[x] + 1
                    q.append(y)
        assert len(dist) == len(vs)
        out[s] = dist
    return out


def poly_mul(a, b):
    c = [0]*(len(a)+len(b)-1)
    for i, x in enumerate(a):
        for j, y in enumerate(b):
            c[i+j] += x*y
    return c


def poly_pow(a, m):
    r = [1]
    for _ in range(m):
        r = poly_mul(r, a)
    return r


def predicted_hist(m):
    p = poly_pow([3,4,2], m)
    q = poly_pow([1,2], m)
    L = max(len(p), len(q), 5)
    p += [0]*(L-len(p))
    q += [0]*(L-len(q))
    h = [p[i] - 2*q[i] for i in range(L)]
    h[0] += 1
    h[2] -= 2*m
    h[4] += 2*m
    return h


def wiener_formula(m):
    return 4*m*9**(m-1) - 2*m*3**(m-1) + 2*m


def main():
    for m in range(2, 6):
        vs = vertices(m)
        distances = bfs_all(vs)
        hist = Counter()
        ordered_sum = 0
        for a in vs:
            for b in vs:
                d = distances[a][b]
                assert d == predicted(a,b), (m,a,b,d,predicted(a,b))
                hist[d] += 1
                ordered_sum += d
        ph = predicted_hist(m)
        for d in range(max(max(hist), len(ph)-1)+1):
            assert hist[d] == (ph[d] if d < len(ph) else 0), (m,d,hist[d],ph[d] if d < len(ph) else 0)
        assert ordered_sum % 2 == 0
        assert ordered_sum//2 == wiener_formula(m)
        N = 3**m - 1
        assert sum(hist.values()) == N*N
    print('VERIFY_OK exact signohedron flip-distance enumerator')

if __name__ == '__main__':
    main()
