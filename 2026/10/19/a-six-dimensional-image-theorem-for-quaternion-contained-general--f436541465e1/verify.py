"""Exact finite-field spot-checks for generalized commutators in split octonions.

Only simple modular integer arithmetic is used; no external packages.
"""
from itertools import product


def matmul(a, b, p):
    return [(a[0]*b[0]+a[1]*b[2]) % p,
            (a[0]*b[1]+a[1]*b[3]) % p,
            (a[2]*b[0]+a[3]*b[2]) % p,
            (a[2]*b[1]+a[3]*b[3]) % p]


def adj(a, p):
    return [a[3] % p, (-a[1]) % p, (-a[2]) % p, a[0] % p]


def plus(a, b, p):
    return [(u+v) % p for u, v in zip(a, b)]


def octmul(a, b, p):
    return plus(matmul(a[:4], b[:4], p),
                matmul(adj(b[4:], p), a[4:], p), p) + plus(
        matmul(b[4:], a[:4], p), matmul(a[4:], adj(b[:4], p), p), p)


def phi(a, b, x, y, p):
    return [(u-v) % p for u, v in zip(
        octmul(a, octmul(x, y, p), p),
        octmul(b, octmul(y, x, p), p))]


def rank(m, p):
    a = [[z % p for z in r] for r in m]
    n, nc, k = len(a), len(a[0]), 0
    for j in range(nc):
        pivot = next((i for i in range(k, n) if a[i][j]), None)
        if pivot is None:
            continue
        a[k], a[pivot] = a[pivot], a[k]
        inv = pow(a[k][j], -1, p)
        a[k] = [(v*inv) % p for v in a[k]]
        for i in range(n):
            if i != k and a[i][j]:
                r = a[i][j]
                a[i] = [(u-r*v) % p for u,v in zip(a[i], a[k])]
        k += 1
        if k == n:
            break
    return k


def check_prime(p):
    vectors = [(a,b) for a in range(p) for b in range(p)]
    units = [(u,v) for u in vectors for v in vectors
             if (u[0]*v[1]-u[1]*v[0]) % p]
    basis = [[int(i == j) for i in range(8)] for j in range(8)]
    for kind in ('same_image', 'same_kernel'):
        for u, v in units:
            a,b=u; c,d=v
            if kind=='same_image':
                A=[a,b,0,0,0,0,0,0]; B=[c,d,0,0,0,0,0,0]
                t=next(t for t in range(1,p) if ((a+b*t-c)%p,(b-d)%p)!=(0,0))
                x=[1,0,t,1,0,0,0,0]
            else:
                A=[a,0,b,0,0,0,0,0]; B=[c,0,d,0,0,0,0,0]
                x=[0,1,1,0,0,0,0,0]
            images=[phi(A,B,x,y,p) for y in basis]
            T=[list(row) for row in zip(*images)]
            assert rank(T,p)==6, (p,kind,u,v)
            if kind=='same_image':
                assert all(T[i][j]==0 for i in (2,3) for j in range(8))
            else:
                assert all(T[i][j]==0 for i in (5,7) for j in range(8))
    return len(units)

if __name__=='__main__':
    for prime in (3,5,7):
        count=check_prime(prime)
        print(f'GF({prime}): {count} pairs in each of two incidence types; all fixed-slice ranks 6')
    print('VERIFY_OK')
