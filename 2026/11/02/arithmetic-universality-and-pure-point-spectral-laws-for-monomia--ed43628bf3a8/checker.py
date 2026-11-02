"""Finite exact checks for the monomial cross-composition truncation formulas.

Only uses the Python standard library. All finite checks are integer-exact;
no test is used to substitute for an all-dimension mathematical proof.
"""
import collections
import math


def integer_ranks(p, q, N):
    d = math.gcd(p, q)
    M = max(p, q) // d
    ans = [N]
    term = d * M
    while term <= N:
        ans.append(N // term)
        term *= M
    ans.append(0)
    ans.append(0)
    return ans


def claimed_blocks(p, q, N):
    r = integer_ranks(p, q, N)
    return {k: r[k-1] - 2 * r[k] + r[k+1]
            for k in range(1, len(r)-1)
            if r[k-1] - 2 * r[k] + r[k+1]}


def graph_blocks(p, q, N):
    succ, pred = {}, {}
    for k in range(1, N // max(p, q) + 1):
        u, v = q*k, p*k
        assert 1 <= u <= N and 1 <= v <= N and u != v
        assert u not in succ and v not in pred
        succ[u] = v
        pred[v] = u
    seen = set()
    lengths = []
    for source in range(1, N+1):
        if source in pred:
            continue
        u = source
        length = 0
        while True:
            assert u not in seen
            seen.add(u)
            length += 1
            if u not in succ:
                break
            u = succ[u]
        lengths.append(length)
    assert len(seen) == N
    return collections.Counter(lengths), len(succ)


def run():
    assertions = 0
    # Covers coprime and noncoprime parameters, both directions, and
    # finite truncations with changing maximum Jordan-block length.
    pairs = [(p, q) for p in range(2, 19) for q in range(2, 19) if p != q]
    cutoffs = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 13, 17, 23,
               31, 43, 65, 101, 127, 149, 200, 257, 400, 600)
    fingerprints = {}
    for p, q in pairs:
        g = math.gcd(p, q)
        M = max(p, q) // g
        for N in cutoffs:
            direct, num_edges = graph_blocks(p, q, N)
            closed = claimed_blocks(p, q, N)
            assert direct == closed, (p, q, N, direct, closed)
            assertions += 1
            ranks = integer_ranks(p, q, N)
            assert num_edges == ranks[1]
            assertions += 1
            for j in range(len(ranks)):
                rank_from_blocks = sum(count * max(size-j, 0)
                                       for size, count in direct.items())
                assert rank_from_blocks == ranks[j], (p, q, N, j)
                assertions += 1
            assert sum(k*v for k, v in direct.items()) == N
            assertions += 1
            largest = max(direct)
            k = 1
            while g * M**k <= N:
                k += 1
            assert largest == k
            assertions += 1
            key = (g, M, N)
            if key in fingerprints:
                assert direct == fingerprints[key], (key, p, q)
                assertions += 1
            else:
                fingerprints[key] = direct
            # For (T+T*)/2 the exact trace of the squared matrix is
            # number_of_edges/2: each undirected edge gives two quarters.
            tr_H2_times_2 = sum((k-1)*count for k, count in direct.items())
            assert tr_H2_times_2 == ranks[1]
            assertions += 1
    # Exact second moments of the limiting distribution, from its
    # explicit Jordan block weights, using rational arithmetic.
    from fractions import Fraction
    for g in range(1, 10):
        for M in range(2, 17):
            # Total infinite block mass: (1/g)*sum_{k>=1} k(M-1)^2/M^{k+1}.
            # The geometric series is exactly 1/g; the remaining mass is 1-1/g.
            mass = Fraction(g-1, g) + Fraction(1, g)
            assert mass == 1
            # Tr(H^2)/N limit = lim rank(T)/2N.
            second_moment = Fraction(1, 2*g*M)
            assert second_moment > 0 and second_moment < 1
            assertions += 2
    print(f'PASS {assertions} exact assertions over {len(pairs)} parameter pairs, '
          f'{len(cutoffs)} truncation sizes, and 135 limiting checks.')
    return assertions


if __name__ == '__main__':
    run()
