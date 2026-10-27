"""Exact-rational generator verification of the all-state star-coalescence mean."""
from itertools import combinations
from fractions import Fraction


def solve(A, b):
    n = len(b)
    mat = [list(A[i]) + [b[i]] for i in range(n)]
    for col in range(n):
        pivot = next((row for row in range(col, n) if mat[row][col]), None)
        assert pivot is not None
        mat[col], mat[pivot] = mat[pivot], mat[col]
        factor = mat[col][col]
        mat[col] = [x / factor for x in mat[col]]
        for row in range(n):
            if row != col and mat[row][col]:
                factor = mat[row][col]
                mat[row] = [x - factor*y for x, y in zip(mat[row], mat[col])]
    return [mat[i][-1] for i in range(n)]


def harmonic(n):
    return sum((Fraction(1, j) for j in range(1, n + 1)), Fraction(0))


def run():
    checks = 0
    for m in range(1, 7):
        n = m + 1
        states = [tuple(c) for k in range(2, n + 1)
                  for c in combinations(range(n), k)]
        index = {state: j for j, state in enumerate(states)}
        A = [[Fraction(int(i == j)) * 0 for j in states] for i in states]
        b = [Fraction(1)] * len(states)
        for i, state in enumerate(states):
            for u in state:
                neighbors = tuple(range(1, n)) if u == 0 else (0,)
                rate = Fraction(1, len(neighbors))
                for v in neighbors:
                    next_state = tuple(sorted((set(state) - {u}) | {v}))
                    A[i][i] += rate
                    if len(next_state) > 1:
                        A[i][index[next_state]] -= rate
        times = solve(A, b)
        for state in states:
            k = sum(v != 0 for v in state)
            if 0 in state:
                answer = (Fraction(m, m + 1) * (harmonic(k) + 1)
                          - Fraction(1, k + 1))
            else:
                assert k >= 2
                answer = Fraction(m, m + 1) * (harmonic(k - 1) + 1)
            assert times[index[state]] == answer, (m, state, times[index[state]], answer)
            checks += 1
        full = times[index[tuple(range(n))]]
        assert full == Fraction(m - 1, m + 1) + Fraction(m, m + 1)*harmonic(m)
        assert full < Fraction(m*m, m + 1) if m >= 3 else full == Fraction(m*m, m + 1)
        print(f"star order={n}; transient states={len(states)}; full={full}")
    print(f"PASS: {checks} exact-rational all-configuration generator identities")


if __name__ == '__main__':
    run()
