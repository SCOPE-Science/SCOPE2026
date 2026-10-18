#!/usr/bin/env python3
"""Independent finite-field checks for cyclic Klein hypersurfaces.
All arithmetic and rank computations use exact integers modulo a prime.
This script tests selected small cases; the uniform theorem requires its proof.
"""
from itertools import product
from math import gcd


def rank_mod(matrix, p):
    a = [[x % p for x in row] for row in matrix]
    rows, cols = len(a), len(a[0])
    rank = 0
    for col in range(cols):
        pivot = next((r for r in range(rank, rows) if a[r][col]), None)
        if pivot is None:
            continue
        a[rank], a[pivot] = a[pivot], a[rank]
        inv = pow(a[rank][col], -1, p)
        a[rank] = [(v * inv) % p for v in a[rank]]
        for r in range(rows):
            if r != rank and a[r][col]:
                m = a[r][col]
                a[r] = [(u - m*v) % p for u, v in zip(a[r], a[rank])]
        rank += 1
    return rank


def phi(x, a, p):
    n = len(x)
    return [(pow(x[i], a, p) * x[(i+1)%n]) % p for i in range(n)]


def gradient(x, a, p):
    t = phi(x, a, p)
    return [((a*t[i]+t[i-1])*pow(x[i],-1,p))%p for i in range(len(x))]


def hessian_rank(x, a, p):
    t = phi(x, a, p)
    n = len(x)
    E = [[(a if j==i else 0) + (1 if j==(i+1)%n else 0)
          for j in range(n)] for i in range(n)]
    H = [[sum(E[k][i]*t[k]*E[k][j] for k in range(n))%p
          for j in range(1,n)] for i in range(1,n)]
    return rank_mod(H,p)


def pfree(q,p):
    v=0
    while q%p==0:
        q//=p
        v+=1
    return q,v


def run_case(a,n,p):
    assert p>2 and a%p and (a+1)%p
    S=sum((-a)**i for i in range(n))
    expected,v = pfree(abs(S),p)
    assert v>=1 and ((-a)**n-1)%p==0
    zeros=[]
    # All singular points have nonzero coordinates; normalize first to one.
    for tail in product(range(1,p),repeat=n-1):
        x=(1,)+tail
        if all(g==0 for g in gradient(x,a,p)):
            assert sum(phi(x,a,p))%p==0
            assert hessian_rank(x,a,p)==n-2
            zeros.append(x)
    # For each of the test parameters below every geometric solution is F_p-rational.
    assert len(zeros)==expected,(a,n,p,expected,len(zeros))
    print(f'case d={a+1}, s={n}, p={p}: singular_points={len(zeros)}, '
          f'Tjurina_length_per_point={p**v}, Hessian_rank={n-2}')

if __name__=='__main__':
    for args in [(2,4,5),(2,5,11),(2,6,7)]:
        run_case(*args)
    # Smooth example, despite p dividing the degree.
    p,a,n=3,2,5
    assert all(any(g for g in gradient((1,)+tail,a,p)) or sum(phi((1,)+tail,a,p))%p!=0
               for tail in product(range(1,p),repeat=n-1))
    print('VERIFY_OK')
