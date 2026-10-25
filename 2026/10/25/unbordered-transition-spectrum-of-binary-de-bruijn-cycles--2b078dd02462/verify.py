"""Two exhaustive computations of unbordered factors in de Bruijn cycles.

Only Python's standard library is required.  Every search domain is finite
and exhaustively visited; the proof in RESULT.md explains the bijections.
"""
from collections import Counter
from fractions import Fraction


def unbordered(word):
    return all(word[:length] != word[-length:] for length in range(1, len(word)))


def feedback_distribution(k):
    width = 1 << (k - 1)
    states = 1 << k
    complete = (1 << states) - 1
    weights = []
    for v in range(width):
        b = format(v, f'0{k-1}b')
        weights.append(int(unbordered('0' + b + '1')) +
                       int(unbordered('1' + b + '0')))
    dist = Counter()
    switches = Counter()
    for mask in range(1 << width):
        current = 0
        seen = 0
        for _ in range(states):
            if (seen >> current) & 1:
                break
            seen |= 1 << current
            a, v = current >> (k-1), current & (width-1)
            current = (v << 1) | (a ^ ((mask >> v) & 1))
        if current == 0 and seen == complete:
            score = sum(weights[v] for v in range(width) if (mask >> v) & 1)
            dist[score] += 1
            switches[mask.bit_count()] += 1
    return weights, dist, switches


def debruijn_cycles(k):
    """List once each cyclic binary de Bruijn word beginning at its sole 0^k."""
    n = 1 << k
    word = [0] * k
    seen = {0}

    def visit():
        if len(word) == n:
            wrap = word + word[:k-1]
            observed = {
                tuple(wrap[i:i+k]) for i in range(n)
            }
            if len(observed) == n:
                yield tuple(word)
            return
        prefix = 0
        for bit in word[-(k-1):]:
            prefix = (prefix << 1) | bit
        for bit in (0, 1):
            key = ((prefix << 1) | bit) & (n-1)
            if key not in seen:
                word.append(bit)
                seen.add(key)
                yield from visit()
                seen.remove(key)
                word.pop()
    yield from visit()


def direct_distribution(k):
    dist = Counter()
    for bits in debruijn_cycles(k):
        n = len(bits)
        circular = bits + bits[:k]
        statistic = sum(
            unbordered(tuple(circular[i:i+k+1]))
            for i in range(n)
        )
        dist[statistic] += 1
    return dist


if __name__ == '__main__':
    known = {2: 1, 3: 2, 4: 16, 5: 2048}
    expected5 = {9: 192, 10: 288, 11: 160, 12: 576,
                 13: 320, 14: 160, 15: 288, 17: 64}
    for k in range(2, 6):
        weight, fast, sw = feedback_distribution(k)
        direct = direct_distribution(k)
        assert fast == direct, (k, fast, direct)
        assert sum(fast.values()) == known[k], (k, fast)
        if k == 5:
            assert fast == expected5
            mean = Fraction(sum(v * n for v, n in fast.items()), 2048)
            second = Fraction(sum(v * v * n for v, n in fast.items()), 2048)
            assert mean == Fraction(49, 4) and second - mean * mean == Fraction(63, 16)
            assert {v for v, w in enumerate(weight) if w == 2} == {0, 6, 9, 15}
            assert all(w in (1, 2) for w in weight)
            assert {m for m in sw} == {7, 9, 11, 13}
            assert {m: sw[m] for m in sorted(sw)} == {7: 576, 9: 960, 11: 448, 13: 64}
        print(f'k={k}: {dict(sorted(fast.items()))}; cycles={sum(fast.values())}')
    examples = (
        ('00000100011001010011101011011111', 10),
        ('00000100011001010110111010011111', 12),
    )
    for word, expected_ub in examples:
        factors = [(word + word[:5])[i:i+6] for i in range(32)]
        assert len(set(factors)) == 32
        assert sum(w == w[::-1] for w in factors) == 2
        assert sum(unbordered(w) for w in factors) == expected_ub
    print('PASS: two independent complete enumerators and weight table')
