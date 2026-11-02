#!/usr/bin/env python3
"""Independent exhaustive verification of the period-32 de Bruijn
linear-complexity / peak-autocorrelation classification (Python 3).
Only Python's standard library is required. No external data files.
"""
from collections import Counter

N = 32
EXPECTED_COMPLEXITY = {21: 8, 23: 12, 24: 20, 25: 32, 26: 36,
                       27: 64, 28: 180, 29: 224, 30: 448, 31: 1024}
EXPECTED_PEAKS = {4: 12, 8: 772, 12: 882, 16: 282, 20: 88, 24: 12}
PEAKS = tuple(EXPECTED_PEAKS)
EXPECTED_ROWS = {
 21: (0, 0, 0, 8, 0, 0),
 23: (0, 0, 0, 4, 0, 8),
 24: (0, 0, 12, 0, 8, 0),
 25: (0, 4, 24, 0, 4, 0),
 26: (0, 20, 16, 0, 0, 0),
 27: (4, 18, 28, 14, 0, 0),
 28: (0, 84, 60, 28, 8, 0),
 29: (0, 72, 110, 38, 4, 0),
 30: (0, 148, 212, 56, 28, 4),
 31: (8, 426, 420, 134, 36, 0),
}


def feedback_cycles():
    """Every one-cycle 5-stage reversible FSR, once, rooted at 00000."""
    cycles = set()
    for g in range(1 << 16):
        state = 0
        visited = 0
        bits = []
        for _ in range(N):
            if visited & (1 << state):
                break
            visited |= 1 << state
            bits.append(state >> 4)
            state = ((state << 1) & 31) | ((state >> 4) ^ ((g >> (state & 15)) & 1))
        if len(bits) == N and state == 0 and visited == (1 << N) - 1:
            w = tuple(bits)
            assert w not in cycles
            cycles.add(w)
    return cycles


def eulerian_cycles():
    """Independent DFS: Euler tours of the order-four binary de Bruijn digraph,
    rooted at its unique edge 00000 (edge index 0).
    """
    cycles = set()

    def dfs(vertex, used, depth, word):
        if depth == N:
            if vertex == 0:
                assert word not in cycles
                cycles.add(word)
            return
        for bit in (0, 1):
            edge = (vertex << 1) | bit
            if not (used & (1 << edge)):
                dfs(edge & 15, used | (1 << edge), depth + 1,
                    word | (((edge >> 4) & 1) << depth))

    dfs(0, 1, 1, 0)
    return {tuple((word >> j) & 1 for j in range(N)) for word in cycles}


def linear_complexity_games_chan(w):
    a = list(w)
    answer = 0
    while len(a) > 1:
        h = len(a) // 2
        b = [x ^ y for x, y in zip(a[:h], a[h:])]
        if any(b):
            answer += h
            a = b
        else:
            a = a[:h]
    return answer + a[0]


def divide_by_x_plus_1(p):
    assert p != 0 and not (p.bit_count() & 1)
    quotient = 0
    for j in range(p.bit_length() - 2, -1, -1):
        bit = ((p >> (j + 1)) ^ (quotient >> (j + 1))) & 1
        quotient |= bit << j
    assert (quotient ^ (quotient << 1)) == p
    return quotient


def linear_complexity_root_multiplicity(w):
    p = sum(bit << i for i, bit in enumerate(w))
    multiplicity = 0
    while p.bit_count() % 2 == 0:
        p = divide_by_x_plus_1(p)
        multiplicity += 1
    return N - multiplicity


def peak_sidelobe_dot(w):
    signs = [1 if bit == 0 else -1 for bit in w]
    return max(abs(sum(signs[i] * signs[(i + t) % N]
                       for i in range(N))) for t in range(1, N))


def peak_sidelobe_xor(w):
    p = sum(bit << i for i, bit in enumerate(w))
    mask = (1 << N) - 1
    return max(abs(N - 2 * (p ^ (((p << t) | (p >> (N - t))) & mask)).bit_count())
               for t in range(1, N))


def canonical(w):
    for i in range(N):
        if all(w[(i + j) % N] == 0 for j in range(5)):
            return tuple(w[i:]) + tuple(w[:i])
    raise AssertionError('missing 00000')


def orbit(w):
    return {canonical(v) for v in (list(w), list(reversed(w)),
             [1 - x for x in w], [1 - x for x in reversed(w)])}


def main():
    F = feedback_cycles()
    E = eulerian_cycles()
    assert len(F) == len(E) == 2048 and F == E
    joint, lc_margin, peak_margin = Counter(), Counter(), Counter()
    best = set()
    for w in F:
        windows = {tuple(w[(i + j) % N] for j in range(5)) for i in range(N)}
        assert len(windows) == N
        complexity = linear_complexity_games_chan(w)
        assert complexity == linear_complexity_root_multiplicity(w)
        peak = peak_sidelobe_dot(w)
        assert peak == peak_sidelobe_xor(w)
        joint[complexity, peak] += 1
        lc_margin[complexity] += 1
        peak_margin[peak] += 1
        if peak == 4:
            best.add(w)
    assert dict(lc_margin) == EXPECTED_COMPLEXITY
    assert dict(peak_margin) == EXPECTED_PEAKS
    for complexity, row in EXPECTED_ROWS.items():
        assert tuple(joint[complexity, peak] for peak in PEAKS) == row, (
            complexity, tuple(joint[complexity, peak] for peak in PEAKS), row)
    assert len(joint) == 32
    assert sum(joint.values()) == N * 64
    assert len(best) == 12
    assert sum(1 for w in best if linear_complexity_games_chan(w) == 31) == 8
    assert sum(1 for w in best if linear_complexity_games_chan(w) == 27) == 4
    remaining = set(best)
    orbits = []
    while remaining:
        w = min(remaining)
        orb = orbit(w)
        assert len(orb) == 4 and orb <= remaining
        remaining.difference_update(orb)
        orbits.append((linear_complexity_games_chan(w), ''.join(map(str, w)), len(orb)))
    assert sorted(orbits) == sorted([
        (31, '00000100011101001010110011011111', 4),
        (31, '00000100011111010011011100101011', 4),
        (27, '00000100101100110111000111110101', 4),
    ])
    print('VERIFY_OK', 'cycles=2048', 'joint_cells=32', 'optimal=8',
          'best_orbits=3', 'independent_enumerations=2',
          'independent_invariant_checks=2')

if __name__ == '__main__':
    main()
