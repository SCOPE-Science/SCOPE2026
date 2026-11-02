"""Exact finite-field verification of projective-paired quantum Lee codes.

Uses only Python's standard library. The all-parameter theorem is proved
separately; this script checks reproducible finite examples exactly.
"""
from itertools import product


def rank_mod(mat, p):
    if not mat:
        return 0
    a = [[x % p for x in row] for row in mat]
    nrows, ncols = len(a), len(a[0])
    rank = 0
    for j in range(ncols):
        pivot = next((i for i in range(rank, nrows) if a[i][j]), None)
        if pivot is None:
            continue
        a[rank], a[pivot] = a[pivot], a[rank]
        scale = pow(a[rank][j], -1, p)
        a[rank] = [(scale * x) % p for x in a[rank]]
        for i in range(nrows):
            if i != rank and a[i][j]:
                scale = a[i][j]
                a[i] = [(x - scale * y) % p for x, y in zip(a[i], a[rank])]
        rank += 1
        if rank == nrows:
            break
    return rank


def columns(p, r):
    projective = set()
    for v in product(range(p), repeat=r):
        if not any(v):
            continue
        j = next(j for j, x in enumerate(v) if x)
        a = pow(v[j], -1, p)
        projective.add(tuple((a * x) % p for x in v))
    result = []
    for v in sorted(projective):
        for a in range(1, (p - 1)//2 + 1, 2):
            result.append((tuple(a*x % p for x in v),
                           tuple((a+1)*x % p for x in v)))
    return result


def check(p, r):
    assert p % 4 == 1
    cs = columns(p,r)
    n = len(cs)
    assert n == (p**r - 1)//4
    X = [c[0] for c in cs]
    Z = [c[1] for c in cs]
    H = [[X[j][i] for j in range(n)] + [Z[j][i] for j in range(n)] for i in range(r)]
    assert rank_mod(H,p) == r
    for i in range(r):
        for j in range(r):
            assert sum((H[i][k]*H[j][k+n] - H[i][k+n]*H[j][k]) for k in range(n))%p == 0
    one_error_syndromes = []
    for x,z in cs:
        for v in (x, z):
            one_error_syndromes.append(v)
            one_error_syndromes.append(tuple(-a % p for a in v))
    assert len(one_error_syndromes)==4*n==p**r-1
    assert len(set(one_error_syndromes)) == p**r-1
    assert all(any(s) for s in one_error_syndromes)
    # Directly check no pair of elementary errors can have zero syndrome,
    # unless their composition is the zero Pauli operator.
    for i, s in enumerate(one_error_syndromes):
        for j in range(i+1,len(one_error_syndromes)):
            if all((x+y)%p==0 for x,y in zip(s,one_error_syndromes[j])):
                # Each such pair comprises mutually inverse elementary
                # errors at the same physical coordinate.
                assert i//4==j//4 and i//2==j//2 and (i^j)==1
    x,z=cs[0]
    assert all((2*a-b)%p==0 for a,b in zip(x,z))
    # The nontrivial weight-three undetectable local Pauli is not a
    # stabilizer: the columns excluding its coordinate span F_p^r.
    assert rank_mod([[c[0][i] for c in cs[1:]] + [c[1][i] for c in cs[1:]] for i in range(r)],p)==r
    print(f'PASS p={p}, r={r}, n={n}, k={n-r}; distinct nonzero syndromes={4*n}; commuting rank={r}; Lee distance=3')


if __name__=='__main__':
    for p,r in ((5,2),(5,3),(5,4),(13,2),(17,2)):
        check(p,r)
    print('PROJECTIVE_QUANTUM_LEE_VERIFICATION_OK')
