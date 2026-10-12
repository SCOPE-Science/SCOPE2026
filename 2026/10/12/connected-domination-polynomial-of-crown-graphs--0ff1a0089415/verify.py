from itertools import combinations
from math import comb


def crown_adj(n):
    adj = [set() for _ in range(2*n)]
    for i in range(n):
        for j in range(n):
            if i != j:
                adj[i].add(n+j)
                adj[n+j].add(i)
    return adj


def literal_connected_dominating(mask, n, adj):
    chosen = {v for v in range(2*n) if (mask >> v) & 1}
    if not chosen:
        return False
    for v in range(2*n):
        if v not in chosen and not (adj[v] & chosen):
            return False
    start = next(iter(chosen))
    seen = {start}
    stack = [start]
    while stack:
        v = stack.pop()
        for u in adj[v] & chosen:
            if u not in seen:
                seen.add(u)
                stack.append(u)
    return seen == chosen


def predicted(mask, n):
    P = {i for i in range(n) if (mask >> i) & 1}
    Q = {j for j in range(n) if (mask >> (n+j)) & 1}
    if len(P) < 2 or len(Q) < 2:
        return False
    return not (len(P) == len(Q) == 2 and P == Q)


def predicted_counts(n):
    counts = [0]*(2*n+1)
    for p in range(2, n+1):
        for q in range(2, n+1):
            counts[p+q] += comb(n,p)*comb(n,q)
    counts[4] -= comb(n,2)
    return counts


def run():
    subset_checks = 0
    graph_cases = 0
    total_cds = 0
    for n in range(3, 9):
        adj = crown_adj(n)
        literal = [0]*(2*n+1)
        for mask in range(1 << (2*n)):
            a = literal_connected_dominating(mask,n,adj)
            b = predicted(mask,n)
            assert a == b, (n, mask, a, b)
            subset_checks += 1
            if a:
                literal[mask.bit_count()] += 1
        expect = predicted_counts(n)
        assert literal == expect, (n, literal, expect)
        c = comb(n,2)
        assert literal[4] == c*(c-1)
        assert sum(literal) == (2**n-n-1)**2-c
        assert next(k for k,v in enumerate(literal) if v) == 4
        total_cds += sum(literal)
        graph_cases += 1
    print(f"ALL CHECKS PASSED; graph_cases={graph_cases}; subset_checks={subset_checks}; connected_dominating_sets={total_cds}; n_range=3..8")


if __name__ == '__main__':
    run()
