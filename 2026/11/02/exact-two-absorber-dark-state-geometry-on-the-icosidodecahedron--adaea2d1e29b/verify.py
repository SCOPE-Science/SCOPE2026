#!/usr/bin/env python3
"""Exact finite certificate for spectral accessibility on the icosidodecahedral graph.

This standalone program needs only Python's standard library. It constructs the
line graph of the generalized Petersen graph GP(10,2), verifies a monic
annihilating polynomial, and exhausts all 435 unordered vertex pairs using
exact rational row reduction.
"""
from collections import Counter, deque
from fractions import Fraction


def graph():
    E = set()
    for i in range(10):
        for a, b in ((i, (i+1) % 10), (i, 10+i), (10+i, 10+(i+2) % 10)):
            E.add(tuple(sorted((a, b))))
    edge = sorted(E)
    assert len(edge) == 30
    A = [[int(i != j and bool(set(e) & set(f))) for j, f in enumerate(edge)]
         for i, e in enumerate(edge)]
    assert all(sum(row) == 4 for row in A)
    return edge, A


def mm(X, Y):
    n = len(X); m = len(Y[0]); p = len(Y)
    return [[sum(X[i][k] * Y[k][j] for k in range(p))
             for j in range(m)] for i in range(n)]


def powers(A, count):
    n = len(A)
    I = [[int(i == j) for j in range(n)] for i in range(n)]
    out = [I]
    for _ in range(count):
        out.append(mm(out[-1], A))
    return out


def poly(A, factors):
    n = len(A)
    P = [[int(i == j) for j in range(n)] for i in range(n)]
    for coefficients in factors:
        nxt = [[0]*n for _ in range(n)]
        pp = powers(A, len(coefficients)-1)
        for k,c in enumerate(coefficients):
            if c:
                for i in range(n):
                    for j in range(n):
                        nxt[i][j] += c * pp[k][i][j]
        P = mm(P, nxt)
    return P


def rank_exact(cols):
    # All columns are integer, with no floating-point threshold.
    n = len(cols[0]); m = len(cols)
    mat = [[Fraction(cols[j][i]) for j in range(m)] for i in range(n)]
    piv = 0
    for j in range(m):
        selected = next((i for i in range(piv, n) if mat[i][j]), None)
        if selected is None:
            continue
        mat[piv], mat[selected] = mat[selected], mat[piv]
        den = mat[piv][j]
        for k in range(j, m):
            mat[piv][k] /= den
        for i in range(piv+1, n):
            if mat[i][j]:
                factor = mat[i][j]
                for k in range(j, m):
                    mat[i][k] -= factor * mat[piv][k]
        piv += 1
        if piv == n:
            break
    return piv


def distance(A, origin):
    n=len(A)
    d=[-1]*n
    d[origin]=0
    q=deque([origin])
    while q:
        i=q.popleft()
        for j in range(n):
            if A[i][j] and d[j]<0:
                d[j]=d[i]+1
                q.append(j)
    assert -1 not in d
    return d


def main():
    edge,A=graph()
    assert len(edge)==30 and sum(map(sum,A))==120
    # (x-4)(x-2)(x-1)(x+1)(x+2)(x^2-2x-4)
    factors=((-4,1),(-2,1),(-1,1),(1,1),(2,1),(-4,-2,1))
    zero=poly(A, factors)
    assert all(z==0 for row in zero for z in row)
    Ap=powers(A,7)
    cols=[[Ap[k][i][u] for i in range(30)] for u in range(30) for k in range(7)]
    for u in range(30):
        assert rank_exact(cols[7*u:7*(u+1)]) == 7
    dist=[distance(A,u) for u in range(30)]
    counts=Counter()
    for u in range(30):
        for v in range(u+1,30):
            r=rank_exact(cols[7*u:7*(u+1)] + cols[7*v:7*(v+1)])
            d=dist[u][v]
            routes=Ap[3][u][v]
            counts[d,r,routes if d==3 else 0]+=1
            if d==5:
                assert r == 8
            elif d==3 and routes==2:
                assert r==12
            else:
                assert r==13, (u,v,d,r,routes)
    assert sum(counts.values()) == 435
    assert sum(v for (d,r,_),v in counts.items() if r==8)==15
    assert sum(v for (d,r,_),v in counts.items() if r==12)==60
    assert sum(v for (d,r,_),v in counts.items() if r==13)==360
    expected={(1,13,0):60,(2,13,0):120,(3,12,2):60,(3,13,1):60,(4,13,0):120,(5,8,0):15}
    assert dict(counts)==expected, counts
    print('Graph: line graph of GP(10,2), 30 vertices, 60 edges, all degree 4')
    print('Minimal annihilator m(A)=(A-4I)(A-2I)(A-I)(A+I)(A+2I)(A^2-2A-4I)=0')
    print('Each single-site seven-step Krylov rank: 7 for all 30 sites')
    print('All 435 unordered pairs:')
    for (d,r,paths),cnt in sorted(counts.items()):
        print(f'  distance={d}, A^3-paths={paths if d==3 else "n/a"}, bright_rank={r}: {cnt}')
    print('PASS: every matrix identity and rank is exact over rationals')


if __name__ == '__main__':
    main()
