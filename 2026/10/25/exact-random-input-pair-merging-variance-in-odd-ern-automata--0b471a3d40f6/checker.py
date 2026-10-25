"""Reproducible exact checks for pair-merging moments in odd Cerny automata.

Requires only Python 3 standard library. This is a finite check of an
infinite theorem whose proof is supplied separately.
"""
from fractions import Fraction as Q
from itertools import combinations


def solve(matrix, rhs):
    n = len(rhs)
    a = [[Q(v) for v in row] + [Q(rhs[i])] for i, row in enumerate(matrix)]
    for j in range(n):
        pivot = next((i for i in range(j, n) if a[i][j]), None)
        if pivot is None:
            raise ArithmeticError('noninvertible transient-state system')
        a[j], a[pivot] = a[pivot], a[j]
        div = a[j][j]
        a[j] = [v / div for v in a[j]]
        for i in range(n):
            if i == j or not a[i][j]:
                continue
            q = a[i][j]
            a[i] = [u-q*v for u, v in zip(a[i], a[j])]
    return [row[-1] for row in a]


def direct_moments(n):
    pairs = list(combinations(range(n), 2))
    pos = {p:i for i, p in enumerate(pairs)}
    N = len(pairs)
    system = [[Q(int(i == j)) for j in range(N)] for i in range(N)]
    for i, pair in enumerate(pairs):
        for letter in (0, 1):
            if letter == 0:
                nxt = [((x + 1) % n) for x in pair]
            else:
                nxt = [(0 if x == n-1 else x) for x in pair]
            if nxt[0] != nxt[1]:
                j = pos[tuple(sorted(nxt))]
                system[i][j] -= Q(1, 2)
    e = solve(system, [1]*N)
    e2 = solve(system, [2*x-1 for x in e])
    j = pos[(0,(n-1)//2)]
    return e[j], e2[j]-e[j]**2


def mean(m):
    return 2*m*m*(4*m+3)


def variance(m):
    return Q(2*m*(2*m+1)*(32*m**4+32*m**3+6*m*m+5*m-4), 3)


def D(m, ell):
    return -4*(64*ell**2*m**2+32*ell**2*m+4*ell**2
               -128*ell*m**3-96*ell*m**2+4*ell-4*m+1)


def H(m):
    return 2*(96*m**4+88*m**3-16*m*m+2*m-1)


def run():
    for n in (3,5,7,9,11):
        mu, var = direct_moments(n)
        m = (n-1)//2
        assert mu == mean(m), ('mean',n,mu,mean(m))
        assert var == variance(m), ('variance',n,var,variance(m))
        print(f'n={n}: exact matrix: E={mu}, Var={var}')
    # After expansion, the reduced second-moment expression is a polynomial
    # of degree at most 6 in m (see the displayed D and H polynomials).
    # Seven distinct exact evaluations suffice for polynomial identity.
    for m in range(1,8):
        moment2 = m*H(m)+sum(ell*D(m,ell) for ell in range(1,m))
        assert moment2 == mean(m)**2+variance(m), ('polynomial',m)
    print('Seven exact polynomial-identity points checked (degree <= 6).')
    print('PASS')

if __name__ == '__main__':
    run()
