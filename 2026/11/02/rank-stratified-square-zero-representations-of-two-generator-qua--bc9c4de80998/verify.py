"""Independent exhaustive finite-field checks of square-zero twisted matrix-pair rank counts.

Run with Python 3. Uses only the standard library. For each declared field and
size, enumerates every possible block pair and evaluates defining equations.
"""
from collections import Counter
from itertools import product
from math import prod


def operations(q):
    if q in (2, 3):
        return lambda a, b: (a + b) % q, lambda a, b: (a * b) % q
    if q == 4:
        def times(a, b):
            t = 0
            for k in range(2):
                if (b >> k) & 1:
                    t ^= a << k
            if t & 8:
                t ^= 0b1100
            if t & 4:
                t ^= 0b0111
            return t
        return lambda a, b: a ^ b, times
    raise ValueError(q)


def mul(A, B, r, add, times):
    return tuple(_sum((times(A[i*r+k], B[k*r+j]) for k in range(r)), add)
                 for i in range(r) for j in range(r))


def _sum(seq, add):
    v = 0
    for x in seq:
        v = add(v, x)
    return v


def rank(M, n, q, add, times):
    V = [list(M[i*n:(i+1)*n]) for i in range(n)]
    pivot = 0
    for col in range(n):
        row = next((i for i in range(pivot, n) if V[i][col]), None)
        if row is None:
            continue
        V[pivot], V[row] = V[row], V[pivot]
        for i in range(pivot+1, n):
            if not V[i][col]:
                continue
            alpha = V[i][col]
            beta = V[pivot][col]
            for j in range(col, n):
                # Characteristic p, subtract via p-1; for binary extension use addition.
                neg_prod = times(alpha, V[pivot][j])
                if q == 3:
                    neg_prod = (q-neg_prod) % q
                V[i][j] = add(times(beta, V[i][j]), neg_prod)
        pivot += 1
        if pivot == n:
            break
    return pivot


def gauss(n, k, q):
    if k < 0 or k > n:
        return 0
    # exact product of factors, with divisions at the very end
    return prod(q**(n-i)-1 for i in range(k)) // prod(q**(i+1)-1 for i in range(k))


def gl(k, q):
    return prod(q**k-q**i for i in range(k))


def predicted(r, q):
    ans = Counter()
    for j in range(r//2 + 1):
        n_j = gauss(r,j,q)*gauss(r-j,j,q)*gl(j,q)
        h=r-2*j
        for t in range(h+1):
            ans[2*j+t] += n_j*q**(2*j*(r-j))*gauss(h,t,q)**2*gl(t,q)
    return dict(ans)


def test(q, r, zeta):
    add, times = operations(q)
    mats = list(product(range(q), repeat=r*r))
    zero = (0,)*(r*r)
    observed = Counter()
    qualifying = 0
    for A in mats:
        if mul(A, A, r, add, times) != zero:
            continue
        for C in mats:
            AC, CA = mul(A,C,r,add,times), mul(C,A,r,add,times)
            if any(add(AC[i], times(zeta, CA[i])) for i in range(r*r)):
                continue
            n = 2*r
            Y = tuple((A[i*r+j] if j<r else C[i*r+j-r])
                      if i<r else (0 if j<r else times(zeta,A[(i-r)*r+(j-r)]))
                      for i in range(n) for j in range(n))
            Y_sq = mul(Y, Y, n, add, times)
            assert Y_sq == (0,)*(n*n)
            # X is upper-right block identity; verify XY=zeta*YX directly.
            X = tuple((1 if i<r and j == i+r else 0)
                      for i in range(n) for j in range(n))
            XY,YX = mul(X,Y,n,add,times),mul(Y,X,n,add,times)
            assert all(XY[i]==times(zeta,YX[i]) for i in range(n*n))
            observed[rank(Y,n,q,add,times)] += 1
            qualifying +=1
    expected = predicted(r,q)
    assert dict(observed)==expected,(q,r,zeta,observed,expected)
    print('PASS',q,r,zeta,'Y rank fibers:',dict(sorted(observed.items())),'total',qualifying)


if __name__=='__main__':
    for q,r,zeta in [(2,1,1),(2,2,1),(3,2,1),(3,2,2),(4,2,2),(4,2,3),(2,3,1)]:
        test(q,r,zeta)
    print('TWISTED_SQZERO_MAXRANK_OK 7 complete block enumerations')
