"""Exact integer checks for the CSM secant formula (finite tests only).

This program does not certify the infinite theorem; the incidence-and-residue
proof is given in RESULT.md.
"""
from math import comb


def binom(n, k):
    return comb(n, k) if 0 <= k <= n else 0


def incidence_csm(n, s):
    """Push-forward CSM of the smooth apolar incidence bundle.

    Euler sequence: c(T)=c(T P^s)*c(E_s tensor O(1)).
    c_j(E_s)=(-1)^j C(n-s+j,j)*h^j and
    p_*(H^(s-1+t))=C(n-s+1,t)*h^t.
    Return coefficients of [P^k] for k=0,...,2s-1.
    """
    if s == 0:
        return []
    m = n - s + 1
    result = []
    for k in range(2*s):
        val = 0
        for i in range(s + 2):
            for j in range(s + 1):
                t = s-i-j
                b = s-1-k+t
                if 0 <= t <= m and 0 <= b <= s-j:
                    val += ((-1)**j * binom(s+1, i) *
                            binom(m+j-1, j) * binom(s-j, b) *
                            binom(m, t))
        result.append(val)
    return result


def predicted(n):
    assert n % 2 == 0
    r = n//2
    return [binom(r, k//2)*binom(r, (k+1)//2)
            for k in range(n+1)]


def checked_row(r):
    n = 2*r
    a = incidence_csm(n, r)
    b = incidence_csm(n, r-1)
    secant = [(a[k] if k < len(a) else 0) -
              (b[k] if k < len(b) else 0) for k in range(n+1)]
    complement = [binom(n+1, k+1)-secant[k] for k in range(n+1)]
    assert complement == predicted(n), (r, complement)
    assert secant[-1] == 0
    assert complement[0] == 1
    assert complement[-1] == 1
    assert secant[0] == 2*r
    return complement


if __name__ == '__main__':
    for r in range(1, 13):
        row = checked_row(r)
        print(f'r={r}, coefficients={row}')
    print('VERIFY_OK')
