"""Direct exhaustive checks for two locating-dominating colour classes of K_n square K_2.

No mathematical formula or column-pattern classification is used in the oracle.
Run: python3 ld_prism_verify.py
"""
from collections import Counter, deque


def direct_good(n, mask):
    total = 2 * n
    vertex_mask = (1 << total) - 1
    neighborhoods = []
    for row in range(2):
        for column in range(n):
            own_row = sum(1 << (row * n + j) for j in range(n) if j != column)
            rung = 1 << ((1 - row) * n + column)
            neighborhoods.append(own_row | rung)
    for chosen in (mask, vertex_mask ^ mask):
        signatures = [neighborhoods[v] & chosen for v in range(total)
                      if not (chosen & (1 << v))]
        if 0 in signatures or len(set(signatures)) != len(signatures):
            return False
    return True


def classification(n, mask):
    a = b = c = d = 0
    for i in range(n):
        x = bool(mask & (1 << i))
        y = bool(mask & (1 << (n + i)))
        if x and y:
            a += 1
        elif not x and not y:
            b += 1
        elif x:
            c += 1
        else:
            d += 1
    return (a <= 1 and b <= 1
            and not (a == 1 and b == 0 and (c == 0 or d == 0))
            and not (b == 1 and a == 0 and (c == 0 or d == 0)))


def theoretical_coefficients(n):
    t = n * (2 ** (n - 1) - 2)
    u = 2 ** n + n * (n - 1) * (2 ** (n - 2))
    return {n - 1: t, n: u, n + 1: t}


def components(n, valid):
    unseen = set(valid)
    sizes = []
    while unseen:
        root = unseen.pop()
        queue = deque([root])
        size = 1
        while queue:
            cur = queue.popleft()
            for v in range(2*n):
                nxt = cur ^ (1 << v)
                if nxt in unseen:
                    unseen.remove(nxt)
                    queue.append(nxt)
                    size += 1
        sizes.append(size)
    return sorted(sizes, reverse=True)


def verify():
    checked = 0
    for n in range(4, 9):
        valid = set()
        sizes = Counter()
        for mask in range(1 << (2*n)):
            good = direct_good(n, mask)
            predicted = classification(n, mask)
            assert good == predicted, (n, mask, good, predicted)
            checked += 1
            if good:
                valid.add(mask)
                sizes[mask.bit_count()] += 1
        assert dict(sizes) == theoretical_coefficients(n), (n,sizes)
        expected = sum(theoretical_coefficients(n).values())
        assert len(valid) == expected
        degree_sum = sum(sum(((s ^ (1 << v)) in valid) for v in range(2*n))
                         for s in valid)
        assert degree_sum % 2 == 0
        edges = degree_sum // 2
        assert edges == n * (n+1) * (2**n - 4), (n,edges)
        comps = components(n, valid)
        assert comps == [expected-2, 1, 1], (n, comps)
        for isolated in [sum(1 << i for i in range(n)),
                         sum(1 << (n+i) for i in range(n))]:
            assert isolated in valid
            assert all((isolated ^ (1 << v)) not in valid for v in range(2*n))
        print('n=',n, 'good=',expected,'size_counts=',dict(sorted(sizes.items())),
              'components=',comps, 'edges=',edges)
    # Boundary condition, only a verification datum, not part of the infinite theorem.
    n = 3
    valid = [s for s in range(1 << (2*n)) if direct_good(n,s)]
    assert len(valid) == 20 and all(s.bit_count() == 3 for s in valid)
    assert components(n,valid) == [1]*20
    print('n=3 boundary: good=20, all singleton components')
    print('VERIFY_OK oracle_masks=',checked, 'infinite_formula_cases=5')


if __name__ == '__main__':
    verify()
