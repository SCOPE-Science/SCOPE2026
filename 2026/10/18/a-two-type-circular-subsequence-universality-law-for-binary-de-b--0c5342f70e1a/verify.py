"""Reproduce the de Bruijn cyclic subsequence-universality theorem.

Python 3 standard library only. Every assertion is independently testable.
"""
from collections import Counter
from itertools import product
from random import Random


def all_debruijn(n):
    """Enumerate distinct binary de Bruijn circles with the unique 0**n edge fixed first."""
    N = 1 << n
    mask = (1 << (n - 1)) - 1
    used = [False] * N
    used[0] = True
    labels = [0]

    def search(vertex, count):
        if count == N:
            if vertex == 0:
                yield ''.join(map(str, labels))
            return
        for bit in (0, 1):
            edge = vertex * 2 + bit
            if not used[edge]:
                used[edge] = True
                labels.append(bit)
                yield from search(edge & mask, count + 1)
                labels.pop()
                used[edge] = False

    yield from search(0, 1)


def check_db(word, n):
    N = 1 << n
    assert len(word) == N
    return len({(word + word)[i:i+n] for i in range(N)}) == N


def arch_count(word):
    state = -1
    completed = 0
    for c in word:
        symbol = ord(c) - 48
        if state < 0:
            state = symbol
        elif symbol != state:
            completed += 1
            state = -1
    return completed


def independent_universal(word, k):
    # Test all binary k-strings as scattered subsequences, no arch method.
    for p in product('01', repeat=k):
        j = 0
        for c in word:
            if j < k and c == p[j]:
                j += 1
        if j != k:
            return False
    return True


def d_formula(n):
    if n % 2 == 0:
        numerator = 2**(n+1) - 3*n - 2
    else:
        numerator = 2**(n+1) - 6*n + 2
    assert numerator % 9 == 0
    return numerator // 9


def repeat_gap_counts(word):
    N = len(word)
    events = [i for i in range(N) if word[i] == word[(i-1) % N]]
    assert len(events) >= 2
    lengths = [events[j+1] - events[j] for j in range(len(events)-1)]
    lengths += [events[0] + N - events[-1]]
    return Counter(lengths)


def predicted(word, n):
    N = 1 << n
    alt = [i for i in range(N) if all(word[(i-j) % N] != word[(i-j-1) % N] for j in range(n-1))]
    assert len(alt) == 2
    adjacent = (alt[0] + 1) % N == alt[1] or (alt[1] + 1) % N == alt[0]
    separate = not adjacent
    k = N // 3 + int((n % 2 == 0 and separate) or (n % 2 == 1 and adjacent))
    losses = d_formula(n) + n * int((n % 2 == 0 and separate) or (n % 2 == 1 and adjacent))
    # In other words, the count of poorer cuts is D_n+n exactly at the larger throughput.
    return k, losses, separate


def verify_one(word, n, strong=False):
    assert check_db(word, n)
    N = 1 << n
    k, losses, sep = predicted(word, n)
    gaps = repeat_gap_counts(word)
    assert sum(gaps.values()) == N // 2
    for l in range(1, n-1):
        assert gaps[l] == 2**(n-l-1), (n, l, gaps)
    if sep:
        assert gaps[n] == 2 and gaps[n-1] == gaps[n+1] == 0
    else:
        assert gaps[n-1] == gaps[n+1] == 1 and gaps[n] == 0
    assert sum((l//2)*c for l,c in gaps.items()) == k
    assert sum((l//2)*c for l,c in gaps.items() if l % 2 == 0) == losses
    rooted = Counter(arch_count(word[i:]+word[:i]) for i in range(N))
    assert rooted == Counter({k-1: losses, k: N-losses}), (n, word, rooted, k, losses)
    if strong:
        for i in range(N):
            v = word[i:] + word[:i]
            q = arch_count(v)
            assert independent_universal(v, q)
            assert not independent_universal(v, q+1)
    return sep


def fkm(n):
    a = [0] * (2*n+1)
    result = []
    def db(t, p):
        if t > n:
            if n % p == 0:
                result.extend(a[1:p+1])
        else:
            a[t] = a[t-p]
            db(t+1, p)
            for c in range(a[t-p]+1, 2):
                a[t] = c
                db(t+1, t)
    db(1, 1)
    return ''.join(map(str, result))


def random_db(n, seed):
    R = Random(seed)
    mask = (1 << (n-1)) - 1
    outgoing = [[2*v, 2*v+1] for v in range(mask+1)]
    for x in outgoing: R.shuffle(x)
    vertex_stack = [0]
    labels = []
    rev = []
    while vertex_stack:
        v = vertex_stack[-1]
        if outgoing[v]:
            e = outgoing[v].pop()
            vertex_stack.append(e & mask)
            labels.append(e & 1)
        else:
            vertex_stack.pop()
            if labels:
                rev.append(labels.pop())
    return ''.join(map(str, reversed(rev)))


def run():
    totals = {}
    for n, expected in [(2, 1), (3, 2), (4, 16), (5, 2048)]:
        hits = Counter()
        for word in all_debruijn(n):
            if n >= 3:
                hits[verify_one(word, n, strong=(n <= 4))] += 1
            else:
                assert check_db(word, n)
        assert sum(hits.values()) == expected if n >= 3 else True
        totals[n] = (expected, dict(hits))
    for n in range(3, 11):
        verify_one(fkm(n), n)
    random_total = 0
    for n in range(6, 9):
        for seed in range(35):
            verify_one(random_db(n, seed), n)
            random_total += 1
    print('VERIFY_OK complete_binary_debruijn_cycles_n3_to5=2066',
          'rooted_rotations_n3_to5=65808',
          'random_derived_cycles_n6_to8=', random_total,
          'FKM_orders_3_to10=8',
          'explicit_subsequence_crosscheck_n3_to4=272')
    print('cycle_types', totals)

if __name__ == '__main__':
    run()
