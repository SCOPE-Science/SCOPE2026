#!/usr/bin/env python3
"""Exact finite certificates for the one-step spatial image of ECA Rule 54.

Only the Python standard library is needed.  Exhaustive searches prove finite
algebraic closure statements; the accompanying mathematical argument promotes
those statements to arbitrary words and all positive spatial periods.
"""
from collections import Counter, deque
from itertools import product

RULE = 54
FORB = ("01101", "10101", "10110", "10111101")


def local(a, b, c):
    return (RULE >> (4 * a + 2 * b + c)) & 1


def debruijn():
    edge = [[0, 0] for _ in range(4)]
    for a, b, c in product(range(2), repeat=3):
        src, dst = 2 * a + b, 2 * b + c
        edge[src][local(a, b, c)] |= 1 << dst
    assert edge == [[1, 2], [8, 4], [0, 3], [12, 0]]
    return edge


def subset_dfa(edge):
    states = [15]
    ids = {15: 0}
    moves = []
    for mask in states:
        row = []
        for symbol in range(2):
            z = 0
            for src in range(4):
                if mask & (1 << src):
                    z |= edge[src][symbol]
            if z not in ids:
                ids[z] = len(states)
                states.append(z)
            row.append(ids[z])
        moves.append(tuple(row))
    assert len(states) == 11 and states[0] == 15 and 0 in states
    return states, moves


def forbidden_dfa_agreement(states, moves):
    prefixes = {""}
    for f in FORB:
        prefixes.update(f[:k] for k in range(1, len(f)))

    def advance(suffix, symbol):
        v = suffix + str(symbol)
        if any(f in v for f in FORB):
            return None
        return max((p for p in prefixes if v.endswith(p)), key=len)

    seen = {(0, "")}
    queue = deque([(0, "")])
    while queue:
        q, suffix = queue.popleft()
        assert states[q] != 0
        for symbol in range(2):
            newq = moves[q][symbol]
            news = advance(suffix, symbol)
            # If either language machine rejects, the other must reject.
            assert (states[newq] == 0) == (news is None), (q, suffix, symbol)
            if news is not None and (newq, news) not in seen:
                seen.add((newq, news))
                queue.append((newq, news))
    assert len(seen) == 14

    def allowed(word):
        q = 0
        for s in word:
            q = moves[q][int(s)]
        return states[q] != 0

    for forbidden in FORB:
        assert not allowed(forbidden)
        assert allowed(forbidden[:-1]) and allowed(forbidden[1:])
    return allowed, len(seen)


def relation_algebra(edge):
    gen = []
    for symbol in range(2):
        gen.append(sum(1 << (4 * i + j)
                       for i in range(4)
                       for j in range(4)
                       if edge[i][symbol] & (1 << j)))
    I = sum(1 << (5 * i) for i in range(4))

    def multiply(x, y):
        result = 0
        for i in range(4):
            for j in range(4):
                if x & (1 << (4 * i + j)):
                    result |= ((y >> (4 * j)) & 15) << (4 * i)
        return result

    def shortest_cycle(r):
        q = r
        for length in range(1, 5):
            if q & I:
                return length
            q = multiply(q, r)
        return 0

    states = [I]
    parents = {I: ""}
    moves = []
    for q in states:
        row = []
        for symbol in range(2):
            target = multiply(q, gen[symbol])
            row.append(target)
            if target not in parents:
                parents[target] = parents[q] + str(symbol)
                states.append(target)
        moves.append(row)
    assert len(states) == 109
    histogram = Counter(shortest_cycle(q) for q in states)
    assert histogram == {0: 31, 1: 77, 2: 1}, histogram
    exceptional = [q for q in states if shortest_cycle(q) == 2]
    assert exceptional == [gen[1]]
    assert parents[gen[1]] == "1"
    # Identity is never revisited, and the only transition entering the
    # exceptional matrix is the single initial 1-transition.
    assert not [(q, k) for q in states for k in range(2)
                if multiply(q, gen[k]) == I]
    assert [(q, k) for q in states for k in range(2)
            if multiply(q, gen[k]) == gen[1]] == [(I, 1)]
    assert gen[1] & I == 0 and multiply(gen[1], gen[1]) & I
    return gen, I, multiply, shortest_cycle, histogram


def generating_function_certificate(states, moves):
    # Start with the matrix for the 11 reachable subset states, putting zero
    # on transitions that would enter the rejecting state.
    nstates = len(states)
    M = [[0] * nstates for _ in range(nstates)]
    for i in range(nstates):
        if states[i]:
            for j in moves[i]:
                if states[j]:
                    M[i][j] += 1
    vec = [1] + [0] * (nstates - 1)
    counts = []
    for n in range(30):
        counts.append(sum(vec[i] for i in range(nstates) if states[i]))
        vec = [sum(vec[i] * M[i][j] for i in range(nstates))
               for j in range(nstates)]
    assert counts[:12] == [1, 2, 4, 8, 16, 29, 53, 100, 187, 348, 649, 1213]
    # G(z)=N(z)/D(z) with ascending coefficients.
    N = [1, 0, 1, 1, 1, 0, 0, 1, -1]
    D = [1, -2, 1, -1, -1, 1, -1]
    for n in range(30):
        lhs = sum(D[j] * counts[n-j]
                  for j in range(min(n, len(D) - 1) + 1))
        rhs = N[n] if n < len(N) else 0
        assert lhs == rhs, (n, lhs, rhs)
    # For n >= deg(D), coefficients of D(z)G(z) are a linear sequence
    # obtained from the same 11-state integer matrix.  By Cayley-Hamilton,
    # checking 11 consecutive zeros from n=9 suffices for all n>=9.
    return counts[:12], len(M)


def independent_ring_check(gen, I, multiply, shortest_cycle):
    tested = 0
    for n in range(1, 13):
        outputs = set()
        for bits in product(range(2), repeat=n):
            outputs.add(tuple(local(bits[(i - 1) % n], bits[i],
                                    bits[(i + 1) % n]) for i in range(n)))
            tested += 1
        cyclic_image = set()
        for word in product(range(2), repeat=n):
            r = I
            for symbol in word:
                r = multiply(r, gen[symbol])
            if shortest_cycle(r):
                cyclic_image.add(word)
        if n == 1:
            assert outputs == {(0,)}
            assert cyclic_image == {(0,), (1,)}
        else:
            assert cyclic_image == outputs, n
    assert tested == 8190
    return tested


def main():
    edge = debruijn()
    states, moves = subset_dfa(edge)
    allowed, pairs = forbidden_dfa_agreement(states, moves)
    gen, I, multiply, shortest_cycle, hist = relation_algebra(edge)
    counts, dim = generating_function_certificate(states, moves)
    tested = independent_ring_check(gen, I, multiply, shortest_cycle)
    assert all(allowed(w) for w in ("01010", "1100011"))
    print("VERIFY_OK: 11 subset states, 14 language-product states,"
          " four minimal forbidden words, 109 relation matrices,"
          " period classes 31/77/1, 30 exact rational-series coefficients,"
          f" {tested} independent ring configurations")


if __name__ == '__main__':
    main()
