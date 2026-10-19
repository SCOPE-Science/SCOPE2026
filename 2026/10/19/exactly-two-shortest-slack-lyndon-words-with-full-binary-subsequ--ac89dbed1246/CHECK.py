"""Reproducible finite tests for shortest Lyndon binary subsequence universality.
Run with Python 3; no third-party packages or external data needed.
The infinite statement is established by the written combinatorial proof.
"""
from itertools import product


def greedy_index(w):
    completed = 0
    seen = 0
    for ch in w:
        seen |= 1 << int(ch)
        if seen == 3:
            completed += 1
            seen = 0
    return completed


def direct_universal(w, k):
    for pattern in product('01', repeat=k):
        pos = 0
        for c in w:
            if pos < k and c == pattern[pos]:
                pos += 1
        if pos < k:
            return False
    return True


def primitive_lyndon(w):
    return all(w < w[j:] + w[:j] for j in range(1, len(w)))


def witness(k):
    return {'001' + '01' * (k-1), '01' * k + '1'}


def run():
    # Distinct algorithmic criteria (direct subsequence vs greedy arches).
    for k in range(1, 7):
        for n in (2*k, 2*k+1):
            for symbols in product('01', repeat=n):
                w = ''.join(symbols)
                assert (greedy_index(w) >= k) == direct_universal(w, k), (k, n, w)
    # Exhaustive Lyndon-spectrum classification (all binary words, not sampling).
    for k in range(1, 10):
        n = 2*k+1
        U = 0
        actual = set()
        for symbols in product('01', repeat=n):
            w = ''.join(symbols)
            if greedy_index(w) >= k:
                U += 1
                if primitive_lyndon(w):
                    actual.add(w)
        assert U == (k+2) * 2**k, (k, U)
        assert actual == witness(k), (k, actual, witness(k))
        print(f'k={k}: U={U}, Lyndon universal={sorted(actual)}')
    for k in range(2, 10):
        n = 2*k
        assert not any(
            greedy_index(w) >= k and primitive_lyndon(w)
            for w in (''.join(s) for s in product('01', repeat=n))
        ), k
    # Large-parameter witness tests; not an infinite proof.
    for k in (10, 15, 20, 30, 50, 100, 200):
        for w in witness(k):
            assert greedy_index(w) == k
            assert primitive_lyndon(w)
    print('ALL CHECKS PASSED')


if __name__ == '__main__':
    run()
