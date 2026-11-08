"""Exact birth--death group-copying fixation certificates; Python 3 standard library only.

The graph has five vertices and hyperedges (0,1),(0,2),(0,3),(0,1,4).
Run: python verify.py
"""
from fractions import Fraction as Q
from itertools import product

N = 5
EDGES = ((0, 1), (0, 2), (0, 3), (0, 1, 4))
DEGREES = tuple(sum(i in edge for edge in EDGES) for i in range(N))
M = (1 << N) - 1


def exact_solve(matrix, target):
    a = [row[:] + [target[i]] for i, row in enumerate(matrix)]
    size = len(a)
    for col in range(size):
        pivot = next((j for j in range(col, size) if a[j][col]), None)
        assert pivot is not None, "nonsingular transient system required"
        a[col], a[pivot] = a[pivot], a[col]
        divisor = a[col][col]
        for k in range(col, size + 1):
            a[col][k] /= divisor
        for row in range(col + 1, size):
            multiple = a[row][col]
            if multiple:
                for k in range(col, size + 1):
                    a[row][k] -= multiple * a[col][k]
    answer = [Q(0)] * size
    for row in reversed(range(size)):
        answer[row] = a[row][size] - sum(
            a[row][k] * answer[k] for k in range(row + 1, size)
        )
    assert all(sum(matrix[i][j] * answer[j] for j in range(size)) == target[i]
               for i in range(size))
    return answer


def convert(mask, parent, edge):
    bitset = sum(1 << i for i in edge)
    return (mask | bitset) if (mask & (1 << parent)) else (mask & ~bitset)


def transition_probabilities(mask, fitness):
    num = sum(bool(mask & (1 << i)) for i in range(N))
    total = N - num + fitness * num
    out = {}
    for parent in range(N):
        parent_fitness = fitness if mask & (1 << parent) else Q(1)
        for edge in EDGES:
            if parent in edge:
                new = convert(mask, parent, edge)
                out[new] = out.get(new, Q(0)) + parent_fitness / total / DEGREES[parent]
    assert sum(out.values(), Q(0)) == 1
    return out


def full_system(fitness):
    A = [[Q(i == j) for j in range(M - 1)] for i in range(M - 1)]
    b = [Q(0) for _ in range(M - 1)]
    for mask in range(1, M):
        for new, chance in transition_probabilities(mask, fitness).items():
            if new == M:
                b[mask - 1] += chance
            elif new > 0:
                A[mask - 1][new - 1] -= chance
    return A, b


def full_fixation(fitness):
    A, b = full_system(fitness)
    vec = exact_solve(A, b)
    sites = [vec[(1 << i) - 1] for i in range(N)]
    return sites, sum(sites, Q(0)) / N


def state(mask):
    return ((mask >> 0) & 1, (mask >> 1) & 1,
            (mask >> 4) & 1, ((mask >> 2) & 1) + ((mask >> 3) & 1))


def representative(s):
    h, a, b, count = s
    return (h << 0) | (a << 1) | (b << 4) | ((count >= 1) << 2) | ((count >= 2) << 3)


def lumped_fixation(fitness):
    states = list(product(range(2), range(2), range(2), range(3)))
    zero, full = (0, 0, 0, 0), (1, 1, 1, 2)
    transient = [s for s in states if s not in (zero, full)]
    idx = {s: j for j, s in enumerate(transient)}
    A = [[Q(i == j) for j in range(len(transient))]
         for i in range(len(transient))]
    b = [Q(0) for _ in transient]
    for s in transient:
        mask = representative(s)
        for new, chance in transition_probabilities(mask, fitness).items():
            t = state(new)
            if t == full:
                b[idx[s]] += chance
            elif t != zero:
                A[idx[s]][idx[t]] -= chance
    sol = exact_solve(A, b)
    individual = [sol[idx[state(1 << i)]] for i in range(N)]
    return individual, sum(individual, Q(0)) / N


def derivative_at_neutral():
    A, b = full_system(Q(1))
    f = exact_solve(A, b)
    # Differentiate p_i(r)=f_i(r) / [N+(r-1)m] at r=1.
    rhs = [Q(0) for _ in range(M - 1)]
    for mask in range(1, M):
        num = mask.bit_count()
        for parent in range(N):
            indicator = int(bool(mask & (1 << parent)))
            dp = Q(indicator * N - num, N * N * DEGREES[parent])
            for edge in EDGES:
                if parent not in edge:
                    continue
                new = convert(mask, parent, edge)
                value = Q(1) if new == M else (Q(0) if new == 0 else f[new - 1])
                rhs[mask - 1] += dp * value
    deriv = exact_solve(A, rhs)
    return [deriv[(1 << i) - 1] for i in range(N)], sum(
        (deriv[(1 << i) - 1] for i in range(N)), Q(0)) / N


def moran(r):
    if r == 1:
        return Q(1, N)
    return (1 - 1/r) / (1 - (1/r)**N)


def main():
    expected = {
        Q(1): (Q(1,5), Q(0)),
        Q(3,2): (Q(117586744909890489,305499880204846910),
                 Q(65312879394293469,64460474723222698010)),
        Q(2): (Q(48223659521389,94272370085844),
               -Q(13424476210445,2922443472661164)),
    }
    assert DEGREES == (4, 2, 1, 1, 1)
    for r, (p_expected, gap_expected) in expected.items():
        sites, p = full_fixation(r)
        sites2, p2 = lumped_fixation(r)
        assert (sites, p) == (sites2, p2)
        assert p == p_expected
        assert p - moran(r) == gap_expected
        if r == 1:
            assert sites == [Q(1,15), Q(2,15), Q(4,15),Q(4,15),Q(4,15)]
        print("Exact full/lumped fixation at r=", r, ":", p, "gap:", p - moran(r))
    components, derivative = derivative_at_neutral()
    assert derivative == Q(2036,4965)
    assert derivative - Q(2,5) == Q(10,993)
    assert sum(components, Q(0)) == N * derivative
    print("Exact weak-selection slope:", derivative, "Moran slope:", Q(2,5))
    print("PASS: 30-state and 24-state exact equations, neutral derivative, all fractions")


if __name__ == "__main__":
    main()
