"""Exact rational checks of Johnson low-pass two-coordinate-face concentration."""
from fractions import Fraction as Q
from itertools import combinations
from math import comb


def matmul(A, B):
    n = len(A)
    C = [[Q(0) for _ in range(n)] for _ in range(n)]
    for i in range(n):
        row = C[i]
        for k, a in enumerate(A[i]):
            if a:
                bk = B[k]
                for j in range(n):
                    row[j] += a * bk[j]
    return C


def projector(n, k, L):
    sets = list(combinations(range(n), k))
    m = len(sets)
    A = [[Q(0) for _ in range(m)] for _ in range(m)]
    bsets = list(map(set, sets))
    for i in range(m):
        for j in range(m):
            if len(bsets[i] & bsets[j]) == k - 1:
                A[i][j] = Q(1)
    th = [(k-j)*(n-k-j)-j for j in range(k+1)]
    coefs = [Q(0)] * (k+1)
    for j in range(L+1):
        poly = [Q(1)]
        den = Q(1)
        for h in range(k+1):
            if h == j:
                continue
            den *= th[j] - th[h]
            new = [Q(0)] * (len(poly)+1)
            for i, c in enumerate(poly):
                new[i] -= th[h] * c
                new[i+1] += c
            poly = new
        for i, c in enumerate(poly):
            coefs[i] += c / den
    I = [[Q(i==j) for j in range(m)] for i in range(m)]
    P = [[coefs[k]*I[i][j] for j in range(m)] for i in range(m)]
    for h in range(k-1, -1, -1):
        P = matmul(P,A)
        for i in range(m):
            for j in range(m):
                P[i][j] += coefs[h] * I[i][j]
    assert matmul(P,P) == P
    return sets,P


def mass(n, k, t):
    N=n-2*t
    K=k-t
    return Q(K*(K-1), N*(N-1))


def boundary(n,k,t):
    N=n-2*t
    K=k-t
    return mass(n,k,t) + Q(2*(K-1)*(N-K), N*(N-2))


def check(n,k,L):
    sets,P=projector(n,k,L)
    m=len(sets)
    assert sum(P[i][i] for i in range(m)) == comb(n,L)
    # P M_{1_{1,2 in S}} P; columns outside the coordinate face vanish in M.
    C=[[sum((P[i][h]*P[h][j] for h,s in enumerate(sets) if s[0:2] == (0,1)),Q(0)) for j in range(m)] for i in range(m)]
    vals=[]
    if L==0:
        vals=[(mass(n,k,0),1)]
    else:
        d=lambda t:comb(n-2,t)-(comb(n-2,t-1) if t else 0)
        vals=[(Q(1),comb(n-2,L-2) if L>=2 else 0),
              (boundary(n,k,L-1),d(L-1)), (mass(n,k,L),d(L))]
    assert sum(v for lam,v in vals) <= comb(n,L)
    fixed_C = C
    power = [[Q(i==j) for j in range(m)] for i in range(m)]
    for p in range(1,5):
        power = matmul(power,fixed_C)
        got = sum(power[i][i] for i in range(m))
        want = sum(lam**p*mult for lam,mult in vals)
        assert got==want,(n,k,L,p,got,want)
    # The exact minimal-polynomial annihilator checks all spectral values.
    distinct = sorted({Q(0)} | {lam for lam,mult in vals if mult})
    annihilator = [[Q(i==j) for j in range(m)] for i in range(m)]
    for lam in distinct:
        factor = [[fixed_C[i][j] - (lam if i==j else 0) for j in range(m)] for i in range(m)]
        annihilator = matmul(annihilator, factor)
    assert all(x==0 for row in annihilator for x in row), (n,k,L,"annihilator")
    return m


def run():
    count=0; total=0
    for n in range(4,9):
        for k in range(2,n//2+1):
            for L in range(k):
                m=check(n,k,L)
                count+=1;total+=m
    print(f'VERIFY_OK parameter_sets={count} exact_coordinate_rows={total} moments=1..4 spectral_annihilator=true projection_idempotence=true')

if __name__ == '__main__':
    run()
