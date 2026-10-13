"""Finite checks for two-sided continuous Alexandrov relational predicates.

Two-sorted relation between finite upward-Alexandrov chains C_r and C_m.
Independent exhaustive modal and endpoint computations are compared to the
weighted multichain count, tableau product, and transfer recurrence.
"""
from fractions import Fraction
from math import comb
from itertools import product


def endpoints(row, m):
    if row == 0:
        return m, -1
    present = [k for k in range(m) if (row >> k) & 1]
    return present[0], present[-1]


def semantic_continuous(rows, m):
    r = len(rows)
    # Check all m+1 opens U_t={t,...,m-1} including empty, whole.
    for t in range(m + 1):
        umask = ((1 << m) - 1) ^ ((1 << t) - 1)
        box = [int((row & ~umask) == 0) for row in rows]
        dia = [int((row & umask) != 0) for row in rows]
        if any(box[i] > box[i+1] for i in range(r - 1)):
            return False
        if any(dia[i] > dia[i+1] for i in range(r - 1)):
            return False
    return True


def endpoint_continuous(rows, m):
    e = [endpoints(row, m) for row in rows]
    return all(e[i][0] <= e[i+1][0] and e[i][1] <= e[i+1][1]
               for i in range(len(rows) - 1))


def weighted_count(r, m):
    val = [(a, b, 1 << max(b - a - 1, 0))
           for a in range(m) for b in range(a, m)]
    dp = {(a, b): w for a, b, w in val}
    for _ in range(r - 1):
        dp = {(a, b): w * sum(t for (i, j), t in dp.items()
                                if i <= a and j <= b)
              for a, b, w in val}
    return 1 + sum(dp.values())


def exact_interval_count(r, m):
    return comb(r + m - 1, m - 1) * comb(r + m, m) // (r + 1)


def row_is_interval(row):
    if row == 0:
        return False
    lo = (row & -row).bit_length() - 1
    hi = row.bit_length() - 1
    return row == ((1 << (hi - lo + 1)) - 1) << lo


def asymptotic_constant(m):
    if m < 3:
        raise ValueError("m >= 3")
    maxw = 1 << (m - 2)
    p = Fraction(1)
    for j in range(m - 1):
        w = 1 << max(0, j - 1)
        p *= Fraction(maxw, maxw - w) ** 2
    return p


def verify():
    total = good = interval_good = 0
    cases = []
    for r in range(1, 5):
        for m in range(1, 5):
            if r*m > 16:
                continue
            found = intervals = 0
            for rows in product(range(1 << m), repeat=r):
                semantic = semantic_continuous(rows, m)
                endpoint = endpoint_continuous(rows, m)
                assert semantic == endpoint, (r, m, rows, semantic, endpoint)
                found += semantic
                intervals += semantic and (all(k == 0 for k in rows) or
                                            all(row_is_interval(k) for k in rows))
                total += 1
            assert found == weighted_count(r, m), (r,m,found,weighted_count(r,m))
            assert intervals == 1 + exact_interval_count(r,m), (r,m,intervals)
            good += found
            interval_good += intervals
            cases.append((r,m,found,intervals))
    for m in range(3, 7):
        p = asymptotic_constant(m)
        maxw = 1 << (m - 2)
        ratio = Fraction(weighted_count(80, m) - 1, maxw ** 80)
        assert abs(float(ratio-p)) < 1.e-10, (m,float(ratio),float(p))
    diagonal = [(n, weighted_count(n, n)) for n in range(1, 6)]
    assert diagonal == [(1,2),(2,7),(3,80),(4,2855),(5,374660)]
    print("VERIFY_OK")
    print("Exhaustively checked relations",total)
    print("Continuous",good,"interval-valued incl empty",interval_good)
    print("Individual chain pairs",cases)
    print("Diagonal",diagonal)
    print("Limit constants",[(m,str(asymptotic_constant(m))) for m in range(3,7)])


if __name__ == '__main__':
    verify()
