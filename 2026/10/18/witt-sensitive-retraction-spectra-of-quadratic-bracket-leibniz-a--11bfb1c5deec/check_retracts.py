"""Direct finite computations for retractions of quadratic-bracket Leibniz algebras.

Requires only Python 3. All arithmetic here is over prime fields; the
mathematical statement also covers fields of odd prime-power order.
"""
from itertools import combinations, product
from math import prod


def matrix_vector(A, x, p):
    return tuple(sum(a*b for a, b in zip(row, x)) % p for row in A)


def matmul(A, B, p):
    return tuple(tuple(sum(A[i][k]*B[k][j] for k in range(len(B))) % p
                       for j in range(len(B[0])))
                 for i in range(len(A)))


def form(x, y, D, p):
    return sum(a*b*d for a, b, d in zip(x, y, D)) % p


def rank(A, p):
    A = [list(row) for row in A]
    if not A:
        return 0
    m, n, r = len(A), len(A[0]), 0
    for col in range(n):
        pivot = next((i for i in range(r, m) if A[i][col] % p), None)
        if pivot is None:
            continue
        A[r], A[pivot] = A[pivot], A[r]
        u = pow(A[r][col], -1, p)
        A[r] = [v*u % p for v in A[r]]
        for i in range(m):
            if i != r and A[i][col]:
                a = A[i][col]
                A[i] = [(v-a*w) % p for v, w in zip(A[i], A[r])]
        r += 1
        if r == m:
            break
    return r


def rref_spaces(n, r, p):
    for pivots in combinations(range(n), r):
        free = [(i, j) for i in range(r) for j in range(pivots[i]+1, n)
                if j not in pivots]
        for entries in product(range(p), repeat=len(free)):
            A = [[0]*n for _ in range(r)]
            for i, pivot in enumerate(pivots):
                A[i][pivot] = 1
            for (i, j), a in zip(free, entries):
                A[i][j] = a
            yield tuple(tuple(row) for row in A)


def isotropic_spaces(n, r, p, D):
    return sum(1 for A in rref_spaces(n, r, p)
               if all(form(A[i], A[j], D, p) == 0
                      for i in range(r) for j in range(r)))


def predicted_isotropic(n, r, q, eps):
    if r == 0:
        return 1
    if r > n//2 or (n % 2 == 0 and eps == -1 and r == n//2):
        return 0
    num = 1
    for j in range(r):
        m = n - 2*j
        zeros = q**(m-1) if m % 2 else q**(m-1) + eps*(q-1)*q**(m//2-1)
        num *= zeros-1
    den = prod(q**i-1 for i in range(1, r+1))
    assert num % den == 0
    return num // den


def witt_sign_even(D, p):
    n = len(D)
    assert n % 2 == 0
    determinant = prod(D) % p
    character = pow(((-1)**(n//2) * determinant) % p, (p-1)//2, p)
    assert character in (1, p-1)
    return 1 if character == 1 else -1


def check_geometry():
    cases = [(3, (1,2)), (3, (1,1)), (5, (1,4)), (5, (1,2)),
             (3, (1,1,1)), (3, (1,1,1,1)), (3, (1,1,1,2)),
             (3, (1,1,1,1,1)), (5, (1,1,1,1)), (5, (1,1,1,2))]
    for p, D in cases:
        n = len(D)
        eps = witt_sign_even(D, p) if n%2==0 else None
        for r in range(n//2+1):
            found = isotropic_spaces(n, r, p, D)
            expected = predicted_isotropic(n, r, p, eps)
            assert found == expected, (p, D, r, found, expected)
        print('GEOMETRY_OK',p,D)


def check_full_endomorphisms(n, p, D):
    # Enumerates every homomorphism and every composition-idempotent map.
    # Every endomorphism must send the 1-dimensional derived ideal to itself.
    # Matrix columns, in order, are images of x_1,...,x_n,z.
    zero = (0,)*n
    eye = tuple(tuple(1 if i==j else 0 for j in range(n)) for i in range(n))
    recorded = [0]*(n+2)
    for entries in product(range(p), repeat=n*n):
        P = tuple(tuple(entries[i*n+j] for j in range(n)) for i in range(n))
        columns = tuple(tuple(P[i][j] for i in range(n)) for j in range(n))
        p_is_idempotent = matmul(P, P, p) == P
        im_rank = rank(P, p)
        for c in range(p):
            is_morphism = all(form(columns[i], columns[j], D, p)
                              == (c*D[i] if i==j else 0) % p
                              for i in range(n) for j in range(n))
            if not (is_morphism and p_is_idempotent and c*c % p == c):
                continue
            for f in product(range(p), repeat=n):
                fP = tuple(sum(f[k]*P[k][j] for k in range(n)) % p
                           for j in range(n))
                if all((fP[j]+c*f[j]) % p == f[j] for j in range(n)):
                    recorded[n+1 if c else im_rank] += 1
    eps = witt_sign_even(D, p) if n%2==0 else None
    expected = [0]*(n+2)
    expected[0] = expected[n+1] = 1
    for r in range(1,n//2+1):
        expected[r] = predicted_isotropic(n, r, p, eps) * p**(r*(n-r+1))
    assert recorded == expected, ('endomorphisms', p, D, recorded, expected)
    print('EXHAUSTIVE_ENDOMORPHISMS_OK',p,D,recorded)


def main():
    check_geometry()
    for p,D in [(3,(1,1)), (3,(1,2)), (5,(1,2)), (5,(1,4)), (3,(1,1,1))]:
        check_full_endomorphisms(len(D),p,D)
    print('ALL_QUADRATIC_LEIBNIZ_RETRACTION_CHECKS_PASSED')

if __name__ == '__main__':
    main()

# Rank-one conjugacy-orbit checks use explicit orthogonal similitudes.
def vectors(n,p):
    return list(product(range(p),repeat=n))


def nonzero_lines(n,p):
    reps=[]
    for x in vectors(n,p):
        if not any(x):
            continue
        lead=next(a for a in x if a)
        if lead == 1:
            reps.append(x)
    return reps


def flatten(A):
    return tuple(v for row in A for v in row)


def inverse_matrix(A,p):
    n=len(A)
    rows=[list(A[i])+[int(i==j) for j in range(n)] for i in range(n)]
    for j in range(n):
        k=next((i for i in range(j,n) if rows[i][j]%p),None)
        if k is None:
            return None
        rows[j],rows[k]=rows[k],rows[j]
        inv=pow(rows[j][j],-1,p)
        rows[j]=[(x*inv)%p for x in rows[j]]
        for i in range(n):
            if i!=j:
                v=rows[i][j]
                rows[i]=[(a-v*b)%p for a,b in zip(rows[i],rows[j])]
    return tuple(tuple(row[n:]) for row in rows)


def check_rank_one_orbits(p,D):
    n=len(D)
    reps=[u for u in nonzero_lines(n,p) if form(u,u,D,p)==0]
    if not reps:
        print('RANK_ONE_ORBITS_OK',p,D,'none')
        return
    Pset={}
    for u in reps:
        for lam in vectors(n,p):
            if sum(x*y for x,y in zip(u,lam))%p != 1:
                continue
            a=tuple((lam[i]*pow(D[i],-1,p))%p for i in range(n))
            t=form(a,a,D,p)
            A=tuple(tuple(u[i]*lam[j]%p for j in range(n)) for i in range(n))
            Pset[flatten(A)]=t
    similitudes=[]
    for entries in product(range(p), repeat=n*n):
        g=tuple(tuple(entries[i*n+j] for j in range(n)) for i in range(n))
        inv=inverse_matrix(g,p)
        if inv is None:continue
        c=form(matrix_vector(g,tuple(1 if i==0 else 0 for i in range(n)),p),
               matrix_vector(g,tuple(1 if i==0 else 0 for i in range(n)),p),D,p)*pow(D[0],-1,p)%p
        if c and all(form(tuple(g[k][i] for k in range(n)),tuple(g[k][j] for k in range(n)),D,p)==(c*D[i] if i==j else 0)%p for i in range(n) for j in range(n)):
            similitudes.append((g,inv))
    remaining=set(Pset)
    orbits=[]
    while remaining:
        x=next(iter(remaining))
        P=tuple(tuple(x[i*n+j] for j in range(n)) for i in range(n))
        orbit=set()
        for g,inv in similitudes:
            Pnew=matmul(matmul(g,P,p),inv,p)
            orbit.add(flatten(Pnew))
        assert orbit <= set(Pset)
        remaining-=orbit
        tt={Pset[y] for y in orbit}
        cats={'zero' if t==0 else ('square' if pow(t,(p-1)//2,p)==1 else 'nonsquare') for t in tt}
        orbits.append((len(orbit),cats))
    expected_num=2 if n%2==0 else 3
    assert len(orbits)==expected_num,(p,D,orbits)
    if n%2:
        assert sorted(size for size,_ in orbits)==sorted([len(reps)*p**(n-2),len(reps)*(p-1)//2*p**(n-2),len(reps)*(p-1)//2*p**(n-2)])
    else:
        assert sorted(size for size,_ in orbits)==sorted([len(reps)*p**(n-2),len(reps)*(p-1)*p**(n-2)])
    print('RANK_ONE_ORBITS_OK',p,D,sorted(orbits,key=lambda z:z[0]))

if __name__ == '__main__':
    for p,D in [(3,(1,2)),(3,(1,1,1)),(5,(1,4))]:
        check_rank_one_orbits(p,D)
    print('ALL_RANK_ONE_ORBIT_CHECKS_PASSED')
