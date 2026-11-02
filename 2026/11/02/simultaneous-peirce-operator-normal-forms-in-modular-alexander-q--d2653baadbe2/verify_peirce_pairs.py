"""Exact small-field checks for Peirce-pair conjugacy in Alexander quandle algebras.

Only the standard library is needed. The multiplication is evaluated from the
quandle's basis table, independently of the proposed ring-linear identities.
"""
from itertools import product


def test(p, d, phi):
    points = list(product(range(p), repeat=d))
    n = len(points)
    number = {v: i for i, v in enumerate(points)}
    def image(matrix, v):
        return tuple(sum(row[k] * v[k] for k in range(d)) % p for row in matrix)
    psi = [[(int(i == j) - phi[i][j]) % p for j in range(d)] for i in range(d)]
    P = [number[image(phi, v)] for v in points]
    Q = [number[image(psi, v)] for v in points]
    plus = [[number[tuple((points[i][k]+points[j][k]) % p for k in range(d))] for j in range(n)] for i in range(n)]
    table = [[plus[P[i]][Q[j]] for j in range(n)] for i in range(n)]
    zero = [0]*n
    one = tuple([1]+[0]*(n-1))
    def prod(a,b,mult):
        out=[0]*n
        for i,ai in enumerate(a):
            if ai:
                for j,bj in enumerate(b):
                    if bj:
                        k=mult[i][j]
                        out[k]=(out[k]+ai*bj)%p
        return tuple(out)
    def star(a,b): return prod(a,b,table)
    def conv(a,b): return prod(a,b,plus)
    e=[]
    for i in range(n):
        z=zero.copy();z[i]=1;e.append(tuple(z))
    idempotents=[]
    for u in product(range(p),repeat=n):
        if star(u,u)==u:
            idempotents.append(u)
            if any(u) and sum(u)%p !=1:
                raise AssertionError('Nonzero idempotent not augmented one')
    assert len(idempotents)>1
    for u in idempotents:
        if not any(u): continue
        upow=one
        for _ in range(p):upow=conv(upow,u)
        assert upow==one, 'Unit-power check failed'
        for j in range(n):
            uj=conv(u,e[j])
            assert star(uj,u)==conv(u,e[P[j]]), 'Right intertwining failed'
            assert star(u,uj)==conv(u,e[Q[j]]), 'Left intertwining failed'
    # A functional map on basis elements has rank equal to the number of images.
    ranks=[]
    for k in range(d+2):
        mapping=list(range(n))
        for _ in range(k):mapping=[Q[j] for j in mapping]
        ranks.append(len(set(mapping)))
    blocks=[ranks[j-1]-2*ranks[j]+ranks[j+1] for j in range(1,d+1)]
    assert all(b>=0 for b in blocks)
    assert sum(j*b for j,b in enumerate([0]+blocks) if j)>0 or ranks[0]==ranks[-1]
    print(f'PASS p={p} d={d} phi={phi} idempotents={len(idempotents)} left-ranks={ranks} zero-Jordan-blocks={blocks}')


if __name__=='__main__':
    test(2,1,[[1]])
    test(2,2,[[0,1],[1,1]])
    test(2,2,[[1,1],[0,1]])
    test(3,1,[[2]])
    test(3,2,[[2,0],[0,2]])
    test(3,2,[[1,1],[0,1]])
    test(5,1,[[2]])
    print('VERIFY_OK')
