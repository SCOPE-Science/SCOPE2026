"""Direct graph checks of a size-enumerator for maximal induced bipartite rook subgraphs.

Uses only Python's standard library. Execute: python verify.py
"""
from collections import Counter
from fractions import Fraction
from itertools import combinations
from math import factorial


def two_factor_count(n):
    """Coefficient recurrence of exp(-t/2)/sqrt(1-t), multiplied by (n!)**2."""
    if n == 0:
        return 1
    if n == 1:
        return 0
    a = [Fraction(1), Fraction(0)]
    for k in range(1, n):
        a.append((k*a[k] + a[k-1]/2)/(k+1))
    v = a[n]*factorial(n)**2
    assert v.denominator == 1
    return v.numerator


def saturated_row_count(m, n):
    """Independent state DP for each of m rows choosing two distinct columns."""
    state = {(0,)*n: 1}
    for _ in range(m):
        new = {}
        for coldegrees, multiplicity in state.items():
            for i, j in combinations(range(n), 2):
                if coldegrees[i] == 2 or coldegrees[j] == 2:
                    continue
                v = list(coldegrees)
                v[i] += 1
                v[j] += 1
                v = tuple(v)
                new[v] = new.get(v, 0) + multiplicity
        state = new
    return sum(state.values())


def predicted(m, n):
    assert 2 <= m <= n
    if m < n:
        return {2*m: saturated_row_count(m, n)}
    ans = {2*n: two_factor_count(n)}
    low = n*n*two_factor_count(n-1)
    if low:
        ans[2*n-1] = low
    return ans


def is_bipartite(mask, adj, vertex_count):
    color = [-1]*vertex_count
    for start in range(vertex_count):
        if not (mask >> start & 1) or color[start] != -1:
            continue
        color[start] = 0
        stack = [start]
        while stack:
            v = stack.pop()
            for u in adj[v]:
                if not (mask >> u & 1):
                    continue
                if color[u] == color[v]:
                    return False
                if color[u] == -1:
                    color[u] = 1-color[v]
                    stack.append(u)
    return True


def brute(m, n):
    N = m*n
    adj = [[] for _ in range(N)]
    for u in range(N):
        for v in range(N):
            if u != v and (u//n == v//n or u%n == v%n):
                adj[u].append(v)
    bip = bytearray(1 << N)
    for mask in range(1 << N):
        bip[mask] = is_bipartite(mask, adj, N)
        if bip[mask]:
            row = [0]*m
            col = [0]*n
            for v in range(N):
                if mask >> v & 1:
                    row[v//n] += 1
                    col[v%n] += 1
            assert max(row) <= 2 and max(col) <= 2
        else:
            row = [0]*m
            col = [0]*n
            for v in range(N):
                if mask >> v & 1:
                    row[v//n] += 1
                    col[v%n] += 1
            assert max(row) >= 3 or max(col) >= 3
    count = Counter()
    full = (1 << N)-1
    for mask in range(1 << N):
        if not bip[mask]:
            continue
        missing = full ^ mask
        maximal = True
        while missing:
            bit = missing & -missing
            missing -= bit
            if bip[mask | bit]:
                maximal = False
                break
        if maximal:
            count[mask.bit_count()] += 1
    return dict(count)


def main():
    cases = [(2,2),(2,3),(2,4),(2,5),(3,3),(3,4),(3,5),(4,4)]
    for m,n in cases:
        actual = brute(m,n)
        assert actual == predicted(m,n), (m,n,actual,predicted(m,n))
    for n in range(2,8):
        assert saturated_row_count(n,n) == two_factor_count(n)
    for m in range(2,6):
        for n in range(m+1,9):
            assert saturated_row_count(m,n) >= 1
    assert [two_factor_count(n) for n in range(2,7)] == [1,6,90,2040,67950]
    print('VERIFY_OK graph_instances=8 graph_subsets='+str(sum(1 << (m*n) for m,n in cases))+' balanced_factor_checks=6 rectangular_checks='+str(sum(8-m for m in range(2,6))))

if __name__ == '__main__':
    main()
