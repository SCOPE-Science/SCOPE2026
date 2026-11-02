"""Finite tests for the exact two-marker limited-composition theorem.

Run with Python 3: python verify_two_marker_limited_deck.py
All finite checks support, but do not replace, the all-length proof.
"""
from collections import defaultdict


def literal_profile(n, r, a, b, c):
    assert a >= 0 and b >= 0 and c >= 0 and a + b + c + 2 == n
    s = '0' * a + '1' + '0' * b + '1' + '0' * c
    return tuple(
        sum(s[k:k+L].count('1') == j for k in range(n-L+1))
        for L in range(1, r+1) for j in (0, 1, 2)
    )


def signature(r, a, b, c):
    B = b + 2
    small_outer = tuple(sorted(x for x in (a+1, c+1) if x < r))
    return (B, small_outer) if B <= r else (None, small_outer)


def predicted(n, r):
    part1 = sum(min(r, (n+2-B)//2) for B in range(2, min(r, n)+1))
    H = n-r+1
    both_small = sum(max(0, min(r-1, H-A) - A + 1)
                     for A in range(1, r))
    one_small = min(r-1, max(0, n-2*r+1))
    both_large = int(n >= 3*r-1)
    return part1 + both_small + one_small + both_large


def check_polynomials(n, a, b, c):
    prof = literal_profile(n, n, a, b, c)
    F = [0] * (n+3)
    G = [0] * (n+3)
    for L in range(1, n+1):
        F[L] = prof[3*(L-1)+1] + prof[3*(L-1)+2]
        G[L] = prof[3*(L-1)+2]
    def second(poly):
        return [poly[i] - (2*poly[i-1] if i>=1 else 0)
                + (poly[i-2] if i>=2 else 0)
                for i in range(n+3)]
    wantF = [0] * (n+3)
    wantG = [0] * (n+3)
    for at, sign in ((1,2),(a+2,-1),(b+2,-1),(c+2,-1),(n+2,1)):
        wantF[at] += sign
    for at, sign in ((b+2,1),(a+b+3,-1),(b+c+3,-1),(n+2,1)):
        wantG[at] += sign
    assert second(F) == wantF, ('F identity',n,a,b,c)
    assert second(G) == wantG, ('G identity',n,a,b,c)


def check():
    observations = 0
    profile_checks = 0
    for n in range(2, 26):
        for r in range(1, n+1):
            p_to_s, s_to_p = defaultdict(set), defaultdict(set)
            for a in range(n-1):
                for b in range(n-a-1):
                    c = n - 2 - a - b
                    p = literal_profile(n, r, a, b, c)
                    if r == n: check_polynomials(n, a, b, c)
                    s = signature(r, a, b, c)
                    p_to_s[p].add(s)
                    s_to_p[s].add(p)
                    observations += 1
            assert all(len(x) == 1 for x in p_to_s.values())
            assert all(len(x) == 1 for x in s_to_p.values())
            assert len(p_to_s) == predicted(n, r), (n, r)
            if n >= 3*r-1:
                assert len(p_to_s) == r*(3*r-1)//2
            if r >= 2 and n == 3*r-2:
                assert len(p_to_s) == r*(3*r-1)//2-1
            profile_checks += 1
    for r in range(1, 120):
        for n in range(max(2, 3*r-2), 3*r+18):
            expected = r*(3*r-1)//2
            assert predicted(n, r) == expected - int(r>=2 and n==3*r-2)
    print('VERIFY_OK literal_source_profiles=%d length_cutoff_pairs=%d' %
          (observations, profile_checks))
    print('VERIFY_OK every_literal_profile_matches_complete_signature=True')
    print('VERIFY_OK both_exact_generating_polynomial_identities=True')
    print('VERIFY_OK full_finite_length_formula=True saturation_and_boundary=True')
    print('VERIFY_OK symbolic_formula_large_r=1..119')
    for r in (1, 2, 3, 4, 5, 6, 10):
        print('r=%d saturated_capacity=%d first_saturated_length=%d' %
              (r, r*(3*r-1)//2, max(2, 3*r-1)))


if __name__ == '__main__':
    check()
