"""Standalone exact check of dyadic Rudin-Shapiro frontiers; Python 3."""
from collections import defaultdict


def a(n):
    return 1 if ((n & (n >> 1)).bit_count() % 2 == 0) else -1


def dilation(k, p):
    return sum((1 + 2 * ((p >> j) & 1)) * (4 ** j) for j in range(k))


def lower_height(k, p):
    u = 1 << k
    q = u >> 1
    return u - 2 - 2 * p if p < q else 2 * (p - q) + 1


def main():
    max_k = 7
    largest = dilation(max_k, (1 << max_k) - 1)
    horizon = 2 * largest + 1
    S = T = 0
    xys = defaultdict(list)
    m_edges = defaultdict(list)
    previous_Y = 0
    for n in range(horizon + 1):
        term = a(n)
        S += term
        T += (-1 if n & 1 else 1) * term
        assert (S + T) % 2 == 0
        X, Y = (S + T)//2, (S - T)//2
        xys[(X, Y)].append(n)
        if n % 2:
            m = n // 2
            m_edges[S_for_m].append((m, min(previous_Y, Y), max(previous_Y, Y)))
        else:
            S_for_m = X
            previous_Y = Y
    checks = 0
    for k in range(1, max_k + 1):
        u = 1 << k
        predicted_edges = []
        for p in range(u):
            m = dilation(k, p)
            h = lower_height(k, p)
            predicted_edges.append((m, h, h + 1))
            assert m_edges[u][p] == (m, h, h + 1), (k, p, m_edges[u][p], (m,h,h+1))
            checks += 1
        assert len(m_edges[u]) == u
        for v in range(u+1):
            expected = []
            for m, h, top in predicted_edges:
                if v == h:
                    expected.append(2*m + (1 if h % 2 == 0 else 0))
                if v == top:
                    expected.append(2*m + (0 if h % 2 == 0 else 1))
            # Limit to indices at which this level has been fully traversed.
            assert sorted(expected) == sorted(xys[(u,v)]), (k,v,expected,xys[(u,v)])
            checks += 1
    print(f'PASS: all {checks} dyadic edge and point inverses, k=1..{max_k}; direct a(n) through n={horizon}')


if __name__ == '__main__':
    main()
