"""Direct exact checks of indegree-parity acyclic-orientation counts for wheels.

Run with Python 3. No external dependencies. The brute force uses a Kahn
acyclicity test on actual directed edge lists, not the triangle criterion.
"""
from collections import defaultdict


def matrix_count(p):
    m = len(p)
    prod = [[int(i == j) for j in range(4)] for i in range(4)]
    for i in range(m):
        matrix = [[0]*4 for _ in range(4)]
        for a in (0, 1):
            for b in (0, 1):
                for c in (0, 1):
                    left = (1 + p[i] + a + b) % 2
                    right = (1 + p[(i+1) % m] + b + c) % 2
                    bad = ((b == 1 and left == 1 and right == 0)
                           or (b == 0 and right == 1 and left == 0))
                    matrix[2*a+b][2*b+c] = int(not bad)
        prod = [[sum(prod[i][k]*matrix[k][j] for k in range(4))
                 for j in range(4)] for i in range(4)]
    return sum(prod[i][i] for i in range(4)) - 2 * int(all(x == p[0] for x in p))


def brute_counts(m):
    counts = defaultdict(int)
    fibre = defaultdict(int)
    for rim in range(1 << m):
        for spoke in range(1 << m):
            out = [[] for _ in range(m+1)]
            ind = [0] * (m+1)
            for i in range(m):
                j = (i+1) % m
                u,v = (i,j) if (rim>>i)&1 else (j,i)
                out[u].append(v); ind[v] += 1
                u,v = (m,i) if (spoke>>i)&1 else (i,m)
                out[u].append(v); ind[v] += 1
            parity = tuple(x&1 for x in ind[:m])
            fibre[parity] += 1
            deg = ind[:]
            queue = [v for v,d in enumerate(deg) if d == 0]
            visited = 0
            while queue:
                u = queue.pop()
                visited += 1
                for v in out[u]:
                    deg[v] -= 1
                    if deg[v] == 0: queue.append(v)
            if visited == m+1:
                counts[parity] += 1
    return counts, fibre


def test():
    for m in range(3, 9):
        counts, fibre = brute_counts(m)
        zeros = 0
        total = 0
        for sig in range(1 << m):
            p = tuple((sig>>i)&1 for i in range(m))
            found = counts[p]
            predicted = matrix_count(p)
            assert found == predicted, (m, p, found, predicted)
            assert fibre[p] == (1 << m), (m, p, fibre[p])
            zeros += found == 0
            total += found
        assert zeros == (2 if m%2 else 0), (m, zeros)
        assert total == 3**m-3, (m,total)
        print(f"m={m}: {1<<m} parity fibres, {1<<(2*m)} orientations, "
              f"{total} acyclic; {zeros} empty fibres; all checks passed")
    print('All exact checks passed.')


if __name__ == '__main__':
    test()
