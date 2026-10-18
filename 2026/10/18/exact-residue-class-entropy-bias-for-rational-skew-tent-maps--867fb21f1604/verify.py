"""Exact rational geometry and numerical entropy checks for a rational skew-tent map.

Run: python verify.py
Only the Python standard library is needed. Arithmetic for probabilities is exact;
transcendental logarithms are checked numerically and their analytical identities
are proved in RESULT.md.
"""
from fractions import Fraction as Q
from math import gcd, log, isclose


def overlap(a, b, c, d):
    return max(Q(0), min(b, d) - max(a, c))


def H(probs):
    assert sum(probs, Q(0)) == 1, probs
    return -sum(float(x) * log(float(x)) for x in probs if x)


def direct_matrix(N, p, q):
    """Independent preimage construction in original [0,1] coordinates."""
    L = p + q
    a = Q(p, L)
    M = []
    for j in range(N):
        low, high = Q(j, N), Q(j + 1, N)
        row = []
        for k in range(N):
            # Left inverse branch x=(p/L)y; right x=1-(q/L)y.
            u, v = Q(p*k, L*N), Q(p*(k+1), L*N)
            z, w = 1 - Q(q*(k+1), L*N), 1 - Q(q*k, L*N)
            part_left = overlap(low, high, max(Q(0), u), min(a, v))
            part_right = overlap(low, high, max(a, z), min(Q(1), w))
            row.append(N * (part_left + part_right))
        assert sum(row, Q(0)) == 1, (N, p, q, j, row)
        M.append(row)
    for k in range(N):
        assert sum((M[j][k] for j in range(N)), Q(0)) == 1
    return M


def E(L, s, j):
    a, b = Q(L*j, s), Q(L*(j+1), s)
    v = []
    for k in range(a.numerator // a.denominator, -(-b.numerator // b.denominator)):
        w = Q(s, L) * overlap(a, b, Q(k), Q(k+1))
        if w:
            v.append(w)
    return H(v)


def boundary(N, p, q):
    L = p + q
    tau = Q((N*p) % L, L)
    if not tau:
        return 0.0
    A = Q(L, p) * tau
    B = Q(L, q) * (1 - tau)
    K = max(-(-A.numerator // A.denominator), -(-B.numerator // B.denominator))
    v = [Q(p,L)*overlap(Q(k),Q(k+1),Q(0),A)
         + Q(q,L)*overlap(Q(k),Q(k+1),Q(0),B)
         for k in range(K)]
    return H(v)


def predicted_total(N, p, q):
    L = p+q
    a, b = N*p//L, N*q//L
    return sum(E(L,p,j) for j in range(a)) + sum(E(L,q,j) for j in range(b)) + boundary(N,p,q)


def limit_H(p,q):
    L=p+q
    return (sum(E(L,p,j) for j in range(p)) + sum(E(L,q,j) for j in range(q))) / L


def run():
    tested = 0
    for p in range(1, 7):
        for q in range(1, 7):
            if gcd(p,q) != 1:
                continue
            L = p+q
            h = limit_H(p,q)
            for N in range(1, 2*L+3):
                mat = direct_matrix(N,p,q)
                actual = sum(H(row) for row in mat)
                predicted = predicted_total(N,p,q)
                assert isclose(actual,predicted,rel_tol=1.e-12,abs_tol=1.e-12), (p,q,N,actual,predicted)
                later = predicted_total(N+L,p,q)
                assert isclose(later-predicted,L*h,rel_tol=1.e-12,abs_tol=1.e-12), (p,q,N)
                tested += 1
    p,q=1,4
    h=limit_H(p,q)
    exact_h=log(5)-Q(4,5)*log(2)-Q(6,25)*log(3)
    exact_c4=Q(2,25)*log(Q(32,27))
    assert isclose(h,exact_h,rel_tol=1.e-13,abs_tol=1.e-13)
    assert exact_c4>0
    for k in range(10):
        for N,expected in ((5*k+1,-h),(5*k+4,exact_c4),(5*k+5,0)):
            actual=predicted_total(N,p,q)-N*h
            assert isclose(actual,expected,rel_tol=1.e-11,abs_tol=1.e-11),(N,actual,expected)
    print('VERIFY_OK', 'p,q,N triples',tested,'limit',round(h,12),'C4',round(exact_c4,12))


if __name__ == '__main__':
    run()
