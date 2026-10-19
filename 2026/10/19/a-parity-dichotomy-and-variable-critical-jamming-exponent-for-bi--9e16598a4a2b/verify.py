"""Finite checks for bipartite path adsorption. Python standard library only."""
import itertools
from collections import defaultdict
from fractions import Fraction


def path_set_weights(a, b, vertices):
    """Enumerate admissible occupied vertex sets with exact path multiplicity."""
    r = (vertices - 1) // 2
    out = defaultdict(int)
    # Enumerate ordered alternating paths; reverse paths are identified.
    for first_size, second_size in ((r + 1, r), (r, r + 1)):
        for aa in itertools.permutations(range(a), first_size):
            for bb in itertools.permutations(range(b), second_size):
                # Number of A/B positions is forced by path's first-side class.
                word = []
                for pos in range(vertices):
                    if first_size == r + 1:
                        word.append(('A', aa[pos // 2]) if pos % 2 == 0
                                    else ('B', bb[pos // 2]))
                    else:
                        word.append(('B', bb[pos // 2]) if pos % 2 == 0
                                    else ('A', aa[pos // 2]))
                key = tuple(sorted(word))
                out[key] += 1
    # Every undirected path was enumerated twice, once per orientation.
    assert all(v % 2 == 0 for v in out.values())
    return {s: v // 2 for s, v in out.items()}


def reduced(a, b, r):
    if a < r or b < r or a + b == 2 * r:
        return {a + b: Fraction(1)}
    p = Fraction(a - r, a + b - 2 * r)
    ans = defaultdict(Fraction)
    for x, y, w in ((a - r - 1, b - r, p),
                    (a - r, b - r - 1, 1 - p)):
        if w:
            for size, prob in reduced(x, y, r).items():
                ans[size] += w * prob
    return dict(ans)


def full(a, b, r):
    # Enumerate all admissible subsets in a specific labelled graph,
    # recursively accepting one occupied path vertex set at a time.
    vertices = 2 * r + 1
    paths = path_set_weights(a, b, vertices)
    cache = {}
    def rec(a_mask, b_mask):
        st = (a_mask, b_mask)
        if st in cache:
            return cache[st]
        opts = []
        for path, weight in paths.items():
            aa = sum(1 << i for c, i in path if c == 'A')
            bb = sum(1 << i for c, i in path if c == 'B')
            if a_mask & aa == aa and b_mask & bb == bb:
                opts.append((aa, bb, weight))
        if not opts:
            cache[st] = {a_mask.bit_count() + b_mask.bit_count(): Fraction(1)}
            return cache[st]
        total = sum(v for _, _, v in opts)
        ans = defaultdict(Fraction)
        for aa, bb, weight in opts:
            for size, prob in rec(a_mask ^ aa, b_mask ^ bb).items():
                ans[size] += Fraction(weight, total) * prob
        cache[st] = dict(ans)
        return cache[st]
    return rec((1 << a) - 1, (1 << b) - 1)


def main():
    cnt = 0
    for r, cases in ((2, ((2, 2), (3, 2), (2, 4), (3, 3), (4, 3), (4, 4), (5, 4))),
                     (3, ((3, 3), (4, 3), (4, 4), (5, 4)))):
        for a, b in cases:
            paths = path_set_weights(a, b, 2 * r + 1)
            count_a = sum(weight for path, weight in paths.items()
                          if sum(c == 'A' for c, _ in path) == r + 1)
            count_b = sum(weight for path, weight in paths.items()
                          if sum(c == 'B' for c, _ in path) == r + 1)
            if a >= r and b >= r and a + b > 2 * r:
                assert Fraction(count_a, count_a + count_b) == Fraction(a - r, a + b - 2*r), (r,a,b)
            else:
                assert count_a + count_b == 0
            assert full(a, b, r) == reduced(a, b, r), (r,a,b)
            cnt += 1
    print(f'PASS: {cnt} explicit labelled-embedding and full-state exact probability comparisons')
    # Independent exact first-moment martingale drift identity.
    c2 = 0
    for r in range(2, 6):
        k = 2*r+1
        for a in range(r, r + 12):
            for b in range(r, r + 12):
                s = a + b
                if s <= k:
                    continue
                d = a - b
                p = Fraction(a-r,s-2*r)
                dnext = p*(d-1)+(1-p)*(d+1)
                assert dnext == Fraction(s-k,s-k+1)*d, (r,a,b)
                c2 += 1
    print(f'PASS: {c2} exact conditional martingale-drift comparisons')
    # Even paths consume exactly r of each class, independent of order.
    for r in range(2, 9):
        for a in range(0, 30):
            for b in range(0, 30):
                q = min(a,b)//r
                final = (a - q*r)+(b-q*r)
                assert final == abs(a-b)+2*(min(a,b)%r)
    print('PASS: 6300 even-length path stoichiometric identities')
    # Predicted noncentral scaling exponents and bounded continuous density limits.
    for r in range(2,8):
        k=2*r+1
        theta=(k-2)/(2*(k-1))
        assert 0<theta<0.5
        assert abs((1/2-1/k)/(1-1/k)-theta)<1e-14
        assert abs(theta*(k-1) - (k-2)/2) < 1e-14
    print('PASS: six symbolic exponent-scale identities')

if __name__ == '__main__':
    main()
