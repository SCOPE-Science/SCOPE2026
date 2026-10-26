"""Independent finite checks for k-limited domination in classical Sierpinski graphs.

Uses the defining pairwise adjacency rule, not a recursively generated edge list.
No third-party packages are required.
"""
from itertools import combinations, product


def adjacency(n, m):
    vertices = list(product(range(m), repeat=n))
    adj = [set() for _ in vertices]
    for i, u in enumerate(vertices):
        for j in range(i + 1, len(vertices)):
            v = vertices[j]
            for h in range(n):
                if (u[:h] == v[:h] and u[h] != v[h]
                        and all(u[t] == v[h] and v[t] == u[h]
                                for t in range(h + 1, n))):
                    adj[i].add(j)
                    adj[j].add(i)
                    break
    return vertices, adj


def feasible(mask, adj, k):
    for v, ne in enumerate(adj):
        if (mask >> v) & 1:
            if sum(not ((mask >> w) & 1) for w in ne) > k:
                return False
        elif not any((mask >> w) & 1 for w in ne):
            return False
    return True


def proposed_set(vertices, n, m, k):
    r = m - k
    residues = {a % m for t in range(1, r // 2 + 1) for a in (t, -t)}
    if r % 2:
        residues.add(0)
    assert len(residues) == r and all((-a) % m in residues for a in residues)
    if n == 1:
        return {i for i, v in enumerate(vertices) if v[0] < r}
    return {i for i, v in enumerate(vertices)
            if (v[-1] - v[-2]) % m in residues}


def check_construction(n, m):
    vertices, adj = adjacency(n, m)
    for k in range(1, m):
        D = proposed_set(vertices, n, m, k)
        mask = sum(1 << i for i in D)
        expected = (m - k) * m ** (n - 1)
        assert len(D) == expected
        assert feasible(mask, adj, k)
        if n >= 2:
            for prefix in product(range(m), repeat=n-1):
                assert sum(vertices[v][:n-1] == prefix for v in D) == m-k
    return len(vertices)


def check_exhaustive(n, m):
    vertices, adj = adjacency(n, m)
    N = len(vertices)
    if N > 16:
        return 0
    checked = 0
    for k in range(1, m):
        bound = (m - k) * m ** (n - 1)
        for mask in range(1 << N):
            checked += 1
            if mask.bit_count() < bound:
                assert not feasible(mask, adj, k), (n, m, k, mask)
    return checked


def check_block_costs():
    for m in range(2, 51):
        for k in range(1, m):
            r = m - k
            assert (m-1) * (r+1) - m*r == k-1


def main():
    checks = 0
    for n,m in [(1,2),(1,3),(1,5),(2,2),(2,3),(2,4),
                (2,5),(2,6),(3,2),(3,3),(3,4),(4,2),(4,3)]:
        order = check_construction(n,m)
        checks += m-1
        print('construction',n,m,'order',order,'PASS')
    cases = 0
    for n,m in [(2,2),(2,3),(2,4),(3,2),(4,2),(1,5)]:
        cases += check_exhaustive(n,m)
    check_block_costs()
    print('VERIFY_OK', 'construction_parameter_cases=', checks,
          'enumerated_candidate_masks=', cases,
          'block_inequality_cases=', sum(m-1 for m in range(2,51)))

if __name__ == '__main__':
    main()
