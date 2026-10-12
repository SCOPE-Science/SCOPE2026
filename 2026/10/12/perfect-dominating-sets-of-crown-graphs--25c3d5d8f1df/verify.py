from collections import Counter, deque


def crown(n):
    adj = [set() for _ in range(2 * n)]
    for i in range(n):
        for j in range(n):
            if i != j:
                adj[i].add(n + j)
                adj[n + j].add(i)
    return adj


def is_perfect_dominating(adj, mask):
    for v in range(len(adj)):
        if not ((mask >> v) & 1):
            if sum((mask >> u) & 1 for u in adj[v]) != 1:
                return False
    return True


def is_connected(adj, mask):
    vertices = [v for v in range(len(adj)) if (mask >> v) & 1]
    if not vertices:
        return False
    seen = {vertices[0]}
    q = deque([vertices[0]])
    while q:
        v = q.popleft()
        for u in adj[v]:
            if ((mask >> u) & 1) and u not in seen:
                seen.add(u)
                q.append(u)
    return len(seen) == len(vertices)


def predicted_type(n, mask):
    I = {i for i in range(n) if (mask >> i) & 1}
    J = {i for i in range(n) if (mask >> (n + i)) & 1}
    if len(I) == n and len(J) == n:
        return 'whole'
    if len(I) == len(J) == 1 and I == J:
        return 'matched_pair'
    if n in (3, 4) and len(I) == len(J) == 2 and I | J == set(range(n)):
        return 'exceptional_four'
    return None


def expected_counter(n):
    c = Counter({2: n, 2 * n: 1})
    if n in (3, 4):
        c[4] += 6
    return c


def main():
    subset_checks = 0
    perfect_sets = 0
    coefficient_checks = 0
    classification_checks = 0
    connectivity_checks = 0
    for n in range(3, 9):
        adj = crown(n)
        counts = Counter()
        for mask in range(1 << (2 * n)):
            subset_checks += 1
            if is_perfect_dominating(adj, mask):
                perfect_sets += 1
                counts[mask.bit_count()] += 1
                typ = predicted_type(n, mask)
                classification_checks += 1
                if typ is None:
                    raise AssertionError(('unclassified', n, mask))
                conn = is_connected(adj, mask)
                connectivity_checks += 1
                if typ == 'matched_pair' and conn:
                    raise AssertionError(('pair_connected', n, mask))
                if typ == 'exceptional_four' and not conn:
                    raise AssertionError(('exception_disconnected', n, mask))
                if typ == 'whole' and not conn:
                    raise AssertionError(('whole_disconnected', n, mask))
        want = expected_counter(n)
        maxdeg = 2 * n
        for k in range(maxdeg + 1):
            coefficient_checks += 1
            if counts[k] != want[k]:
                raise AssertionError(('coefficient', n, k, counts[k], want[k]))
    print('VERIFY_OK n_range=3..8 subset_checks=%d perfect_sets=%d coefficient_checks=%d classification_checks=%d connectivity_checks=%d max_order=16' % (
        subset_checks, perfect_sets, coefficient_checks, classification_checks, connectivity_checks))


if __name__ == '__main__':
    main()
