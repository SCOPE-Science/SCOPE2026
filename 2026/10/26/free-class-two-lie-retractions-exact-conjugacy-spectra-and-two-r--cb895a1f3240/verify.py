"""Standalone direct enumeration for retractions of free class-two Lie algebras.
No external dependencies. Run: python free2_retract_verify.py
"""
from itertools import product
from collections import Counter, defaultdict
from math import prod


def gaussian(n, r, q):
    if not 0 <= r <= n:
        return 0
    num = prod(q ** (n - j) - 1 for j in range(r))
    den = prod(q ** (r - j) - 1 for j in range(r))
    return num // den


def rank_rows(rows, p):
    if not rows:
        return 0
    a = [[v % p for v in row] for row in rows]
    pivrow = 0
    for col in range(len(a[0])):
        pivot = next((i for i in range(pivrow, len(a)) if a[i][col]), None)
        if pivot is None:
            continue
        a[pivrow], a[pivot] = a[pivot], a[pivrow]
        inv = pow(a[pivrow][col], -1, p)
        a[pivrow] = [(v * inv) % p for v in a[pivrow]]
        for j in range(len(a)):
            if j != pivrow and a[j][col]:
                c = a[j][col]
                a[j] = [(x-c*y) % p for x,y in zip(a[j], a[pivrow])]
        pivrow += 1
        if pivrow == len(a):
            break
    return pivrow


def rowspace_canonical(columns, p):
    if not columns:
        return ()
    a = [[v % p for v in c] for c in columns]
    pivrow = 0
    for col in range(len(a[0])):
        pivot = next((i for i in range(pivrow, len(a)) if a[i][col]), None)
        if pivot is None:
            continue
        a[pivrow], a[pivot] = a[pivot], a[pivrow]
        inv = pow(a[pivrow][col], -1, p)
        a[pivrow] = [(v * inv) % p for v in a[pivrow]]
        for j in range(len(a)):
            if j != pivrow and a[j][col]:
                c = a[j][col]
                a[j] = [(x-c*y) % p for x,y in zip(a[j], a[pivrow])]
        pivrow += 1
        if pivrow == len(a):
            break
    return tuple(tuple(row) for row in a[:pivrow])


def matmul(a,b,p):
    return [[sum(a[i][k]*b[k][j] for k in range(len(b))) % p
             for j in range(len(b[0]))] for i in range(len(a))]


def enumerate_case(n,p):
    pairs = [(i,j) for i in range(n) for j in range(i+1,n)]
    z = len(pairs)
    d = n+z
    counts = Counter()
    image_fibers = defaultdict(Counter)
    tested = 0
    for ae in product(range(p), repeat=n*n):
        A = [list(ae[i*n:(i+1)*n]) for i in range(n)]
        rank = rank_rows(A,p)
        # All degree-two images are forced by the Lie brackets.
        C = [[(A[i][a]*A[j][b]-A[j][a]*A[i][b])%p for (a,b) in pairs]
             for (i,j) in pairs]
        # center basis is ordered by pairs.
        # C entries above are row (i,j), column (a,b); correct row/column convention
        # C_{(i,j),(a,b)} = A_{i,a} A_{j,b} - A_{j,a} A_{i,b}
        for be in product(range(p), repeat=z*n):
            B = [list(be[i*n:(i+1)*n]) for i in range(z)]
            BA = matmul(B,A,p)
            CB = matmul(C,B,p)
            idem = all((BA[i][j]+CB[i][j]-B[i][j])%p == 0
                       for i in range(z) for j in range(n)) and matmul(A,A,p)==A
            tested += 1
            if not idem:
                continue
            counts[rank]+=1
            M = [A[i]+[0]*z for i in range(n)] + [B[i]+C[i] for i in range(z)]
            # independent direct check of F^2=F on the entire Lie algebra
            assert matmul(M,M,p)==M
            # direct brackets on generators: F([e_a,e_b])=[F(e_a),F(e_b)]
            for ix,(a,b) in enumerate(pairs):
                for zz,(i,j) in enumerate(pairs):
                    want=(A[i][a]*A[j][b]-A[i][b]*A[j][a])%p
                    assert M[n+zz][n+ix] == want
            if n==3 and p==2:
                cols = [tuple(M[i][j] for i in range(d)) for j in range(d)]
                canon = rowspace_canonical(cols,p)
                image_fibers[rank][canon]+=1
    N=n*(n-1)//2
    expected = {}
    for r in range(n+1):
        R=r*(r-1)//2
        expected[r] = gaussian(n,r,p)*p**(r*(n-r)+r*(N-R)+(n-r)*R)
    assert dict(counts) == expected, (n,p,counts,expected)
    if image_fibers:
        for r in range(n+1):
            R=r*(r-1)//2
            num=gaussian(n,r,p)*p**(r*(N-R))
            multiplicity=p**(r*(n-r)+(n-r)*R)
            assert len(image_fibers[r])==num
            assert set(image_fibers[r].values())=={multiplicity}
    print(f'PASS n={n} p={p} checked={tested} idempotents={sum(counts.values())} by-rank={[counts[r] for r in range(n+1)]}' +
          (f' distinct-images={[len(image_fibers[r]) for r in range(n+1)]}' if image_fibers else ''))


def main():
    for n,p in ((2,2),(2,3),(2,5),(3,2)):
        enumerate_case(n,p)
    print('VERIFY_OK free-two-step retracts')

if __name__=='__main__':
    main()
