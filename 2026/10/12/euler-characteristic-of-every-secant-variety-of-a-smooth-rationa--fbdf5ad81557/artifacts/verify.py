from fractions import Fraction
from math import comb, factorial

def rank_matrix(A):
    A = [[Fraction(x) for x in row] for row in A]
    if not A:
        return 0
    m, n = len(A), len(A[0])
    rank = col = 0
    while rank < m and col < n:
        pivot = next((i for i in range(rank, m) if A[i][col]), None)
        if pivot is None:
            col += 1
            continue
        A[rank], A[pivot] = A[pivot], A[rank]
        p = A[rank][col]
        A[rank] = [x/p for x in A[rank]]
        for i in range(m):
            if i != rank and A[i][col]:
                f = A[i][col]
                A[i] = [a - f*b for a,b in zip(A[i], A[rank])]
        rank += 1
        col += 1
    return rank

def catalecticant_for_monomial(d,j,q):
    # Basis of differential operators: ds^(q-a) dt^a, a=0..q.
    # Basis of output monomials degree d-q, indexed by t-exponent.
    rows = q+1
    cols = d-q+1
    A = [[0]*cols for _ in range(rows)]
    for a in range(q+1):
        sx = q-a
        ty = a
        if sx <= d-j and ty <= j:
            coeff = 1
            for z in range(sx):
                coeff *= (d-j-z)
            for z in range(ty):
                coeff *= (j-z)
            out_t = j-ty
            A[a][out_t] = coeff
    return A

cat_checks = 0
for d in range(1,19):
    for j in range(d+1):
        q = min(j,d-j)
        got = rank_matrix(catalecticant_for_monomial(d,j,q))
        assert got == q+1, (d,j,q,got)
        cat_checks += 1

fd_checks = 0
for q in range(0,13):
    for a in range(q):
        s = sum((-1)**(q-h)*comb(q,h)*(h**a) for h in range(q+1))
        assert s == 0
        fd_checks += 1
    s = sum((-1)**(q-h)*comb(q,h)*(h**q) for h in range(q+1))
    assert s == factorial(q)
    fd_checks += 1

scroll_types = []
for k in range(2,6):
    for seed in range(1,33):
        ds = tuple(1 + ((seed*(i+2) + i*i) % 9) for i in range(k))
        scroll_types.append(ds)

fixed_checks = 0
coordinate_checks = 0
for ds in scroll_types:
    maxr = max(ds)+2
    for r in range(1,maxr+1):
        direct = 0
        for d in ds:
            for j in range(d+1):
                direct += int(min(j,d-j)+1 <= r)
                coordinate_checks += 1
        formula = sum(min(d+1,2*r) for d in ds)
        assert direct == formula, (ds,r,direct,formula)
        fixed_checks += 1

print("VERIFY_OK", cat_checks, fd_checks, fixed_checks, coordinate_checks)
