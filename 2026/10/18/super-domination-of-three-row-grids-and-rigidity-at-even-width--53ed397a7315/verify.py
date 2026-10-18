#!/usr/bin/env python3
"""Finite-state exact certificate for three-row grid super domination.

Uses only Python's standard library. No external files are required.
"""
from functools import lru_cache

ROWS = 3
MASK = (1 << ROWS) - 1

@lru_cache(maxsize=None)
def local_ok(window, left_boundary=False, right_boundary=False):
    """Validate all omitted vertices in the CENTER of five consecutive columns.

    The 15 low bits encode five column masks of omitted (white) vertices.
    Outside columns are encoded by zero. Boundary flags forbid imaginary
    black vertices outside the two ends from acting as witnesses.
    """
    C = tuple((window >> (3 * k)) & MASK for k in range(5))
    for row in range(ROWS):
        if not (C[2] & (1 << row)):
            continue
        found = False
        for shift, witness_row in ((-1, row), (1, row),
                                   (0, row - 1), (0, row + 1)):
            if not (0 <= witness_row < ROWS):
                continue
            if shift == -1 and left_boundary:
                continue
            if shift == 1 and right_boundary:
                continue
            witness_col = 2 + shift
            if C[witness_col] & (1 << witness_row):
                continue  # Witness must be selected, not omitted.
            omitted_neighbors = 0
            for step, neighbor_row in ((-1, witness_row),
                                       (1, witness_row),
                                       (0, witness_row - 1),
                                       (0, witness_row + 1)):
                if (0 <= neighbor_row < ROWS and
                        (C[witness_col + step] & (1 << neighbor_row))):
                    omitted_neighbors += 1
            if omitted_neighbors == 1:
                found = True
                break
        if not found:
            return False
    return True


def advance(dp, column, step, terminal_right=False):
    """One max-plus transfer; after appending column step, check step-2."""
    nxt = {}
    for old, weight in dp.items():
        a = old & MASK
        b = (old >> 3) & MASK
        c = (old >> 6) & MASK
        d = (old >> 9) & MASK
        window = a | (b << 3) | (c << 6) | (d << 9) | (column << 12)
        if step >= 2 and not local_ok(window, step == 2, terminal_right):
            continue
        key = (old >> 3) | (column << 9)
        weight_new = weight + column.bit_count()
        if weight_new > nxt.get(key, -9999999):
            nxt[key] = weight_new
    return nxt


def unrestricted_prefixes(through):
    """Return V_t for each t<=through: last four masks -> max omissions.

    All columns to the left of the final two have passed their exact local
    test. The first boundary is built in; the right boundary is still open.
    """
    dp = {0: 0}
    answer = {0: dp}
    for j in range(through):
        nxt = {}
        for col in range(8):
            for key, weight in advance(dp, col, j).items():
                if weight > nxt.get(key, -9999999):
                    nxt[key] = weight
        dp = nxt
        answer[j + 1] = dp
    return answer


def close_right(prefix, n):
    dp = prefix.copy()
    for j in (n, n + 1):
        dp = advance(dp, 0, j, terminal_right=(j == n + 1))
    return max(dp.values())


def direct_brute(n):
    """Independent exhaustive complement test (does NOT reuse local_ok)."""
    N = 3 * n
    neighbors = [0] * N
    for c in range(n):
        for r in range(3):
            v = 3*c + r
            for dc, dr in ((0,-1),(0,1),(-1,0),(1,0)):
                cc, rr = c + dc, r + dr
                if 0 <= cc < n and 0 <= rr < 3:
                    neighbors[v] |= 1 << (3*cc+rr)
    max_omitted, count = -1, 0
    for omitted in range(1 << N):
        size = omitted.bit_count()
        if size < max_omitted:
            continue
        ok = True
        for v in range(N):
            if not ((omitted >> v) & 1):
                continue
            possible = neighbors[v] & ~omitted
            if not any((neighbors[w] & omitted) == (1 << v)
                       for w in range(N) if (possible >> w) & 1):
                ok = False
                break
        if ok:
            if size > max_omitted:
                max_omitted, count = size, 0
            count += 1
    return N-max_omitted, count


def main():
    V = unrestricted_prefixes(12)
    # The transfer is identical for all steps j >= 3. Exact equalities of
    # WHOLE finite vectors V11=V9+3, V12=V10+3, not only scalar optima,
    # inductively imply V_(t+2)=V_t+3 for every integer t>=9.
    for old, new in ((9,11),(10,12)):
        assert V[old].keys() == V[new].keys()
        assert all(V[new][s] == V[old][s] + 3 for s in V[old])
    assert len(V[9]) == len(V[11]) == 1543
    expected_gamma = {1:2, 2:3, 3:5, 4:6, 5:9, 6:9,
                      7:12, 8:12, 9:15, 10:15, 11:18, 12:18}
    for n in range(1,13):
        gamma = 3*n-close_right(V[n], n)
        assert gamma == expected_gamma[n], (n, gamma)
    # Independent full enumeration verifies the local definition and
    # the 3-column transfer up through 18 vertices.
    observed = {1:(2,3), 2:(3,2), 3:(5,4), 4:(6,2), 5:(9,60), 6:(9,2)}
    for n, target in observed.items():
        assert direct_brute(n) == target, (n, direct_brute(n))
    # For arbitrary n>=9, close_right shifts by 3 because the two
    # right-terminal transfers are identical (right boundary only on the
    # second one). Hence gamma(n+2)=gamma(n)+3 for every n>=9.
    print('CERTIFICATE_OK: max-plus V11=V9+3 and V12=V10+3 on 1543 states')
    print('BASE_OK: exact grid widths n=1..12:', expected_gamma)
    print('INDEPENDENT_BRUTE_OK: n=1..6; all optimal set counts:', observed)
    print('THEOREM: gamma_sp(P3 square Pn) = 2 (n=1), 5 (n=3),')
    print('         3n/2 (even n>=2), 3(n+1)/2 (odd n>=5)')

if __name__ == '__main__':
    main()
