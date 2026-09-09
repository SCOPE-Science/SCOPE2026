"""Definitional enumerator for quasi-symmetric plane partitions (candidate defs).

Candidate D2 (hypothesis): pi[i][j] == pi[j][i] for all i+j != a+1 (symmetric
except possibly on anti-diagonal). 1-indexed.
Candidate D1 (alternative): pi[i][j] == pi[j][i] for all i != j (except main diag).
"""
import sys, time


def count_qspp(a, c, mode):
    """Count plane partitions in (a,a,c) box satisfying quasi-symmetry `mode`.
    mode='D2': symmetric except anti-diagonal; mode='D1': except main diagonal;
    mode='full': fully symmetric; mode='none': all plane partitions."""
    pi = [[-1]*a for _ in range(a)]  # 0-indexed; anti-diagonal: i+j == a-1

    def constrained(i, j):
        if mode == 'none':
            return None
        if mode == 'full':
            if j < i:
                return pi[j][i]
            return None
        if mode == 'D1':
            if i != j and j < i:
                return pi[j][i]
            return None
        if mode == 'D2':
            if (i + j != a - 1) and j < i:
                return pi[j][i]
            return None
        raise ValueError(mode)

    sys.setrecursionlimit(10000)
    cells = [(i, j) for i in range(a) for j in range(a)]
    n = len(cells)
    total = [0]

    def rec(k):
        if k == n:
            total[0] += 1
            return
        i, j = cells[k]
        ub = c
        if i > 0:
            ub = min(ub, pi[i-1][j])
        if j > 0:
            ub = min(ub, pi[i][j-1])
        forced = constrained(i, j)
        if forced is not None:
            if forced <= ub:
                pi[i][j] = forced
                rec(k+1)
                pi[i][j] = -1
            return
        for v in range(ub, -1, -1):
            pi[i][j] = v
            rec(k+1)
            pi[i][j] = -1

    rec(0)
    return total[0]


if __name__ == '__main__':
    # Appendix A.1 table rows: (a, c, expected)
    tests = [(1, 1, 2), (2, 1, 6), (2, 2, 20), (3, 1, 12), (3, 2, 69),
             (4, 1, 32), (2, 3, 50), (3, 3, 272)]
    for a, c, exp in tests:
        for mode in ('D1', 'D2'):
            t = time.time()
            got = count_qspp(a, c, mode)
            print(f"a={a} c={c} mode={mode}: got={got} expected={exp} "
                  f"{'OK' if got == exp else 'MISMATCH'} ({time.time()-t:.2f}s)",
                  flush=True)
