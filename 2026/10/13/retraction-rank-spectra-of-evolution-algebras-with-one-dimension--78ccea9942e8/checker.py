"""Finite-prime-field checks for retraction spectra of rank-one-square algebras.

Run: python3 checker.py. Uses only the Python standard library.
"""
from collections import Counter
from itertools import combinations, product


def rank(mat, p):
    rows = [list(row) for row in mat]
    if not rows:
        return 0
    m, n = len(rows), len(rows[0]); k = 0
    for j in range(n):
        h = next((i for i in range(k, m) if rows[i][j] % p), None)
        if h is None: continue
        rows[h], rows[k] = rows[k], rows[h]
        v = pow(rows[k][j] % p, -1, p)
        rows[k] = [v*x % p for x in rows[k]]
        for i in range(m):
            if i != k:
                w = rows[i][j]
                rows[i] = [(a - w*b) % p for a,b in zip(rows[i], rows[k])]
        k += 1
        if k == m: break
    return k


def subspaces(n, r, p):
    for piv in combinations(range(n),r):
        free = [(i,j) for i in range(r) for j in range(piv[i]+1,n) if j not in piv]
        for vals in product(range(p),repeat=len(free)):
            a = [[0]*n for _ in range(r)]
            for i,j in enumerate(piv): a[i][j] = 1
            for (i,j),v in zip(free,vals): a[i][j] = v
            yield a


def is_isotropic(a, diag,p):
    return all(sum(diag[t]*u[t]*v[t] for t in range(len(diag))) % p == 0 for u in a for v in a)


def in_span(c, a, p):
    return rank(a+[list(c)], p) == len(a)


def isometric_subspace_count(n,r,p,diag,c):
    return sum(is_isotropic(a,diag,p) and not in_span(c,a,p) for a in subspaces(n,r,p))


def n_iso(d,p,eps):
    if d < 1: return 0
    if d%2: return p**(d-1)-1
    return p**(d-1)-1+(p-1)*eps*p**(d//2-1)


def witt_index(n,eps):
    if n%2: return (n-1)//2
    return n//2 if eps==1 else n//2-1


def iso_count(n,r,p,eps):
    if r<0 or r>witt_index(n,eps): return 0
    ans = p**(r*(r-1)//2)
    for j in range(r): ans *= n_iso(n-2*j,p,eps)
    denominator=1
    for i in range(r): denominator *= p**r-p**i
    assert ans%denominator==0
    return ans//denominator


def chi(a,p):
    if not a%p: return 0
    return 1 if pow(a%p,(p-1)//2,p)==1 else -1


def formula(n,p,diag,c):
    d=1
    for b in diag: d=d*b%p
    eps=chi(((-1)**(n//2))*d,p) if n%2==0 else 1
    iso_c=sum(diag[i]*c[i]*c[i] for i in range(n))%p==0
    ans=Counter({0:1,n:1})
    for r in range(1,n):
        if r>witt_index(n,eps): continue
        tot=iso_count(n,r,p,eps)
        # For isotropic c, its orthogonal quotient loses a hyperbolic plane.
        reduced=iso_count(n-2,r-1,p,eps) if iso_c else 0
        nr=tot-reduced
        assert nr>=0
        ans[r]=nr*p**(r*(n-r-1))
    return ans


def count_idempotent_homs(n,p,diag,c):
    ans=Counter()
    for flat in product(range(p),repeat=n*n):
        a=[list(flat[i*n:(i+1)*n]) for i in range(n)]
        if any(sum(a[i][k]*a[k][j] for k in range(n)) % p != a[i][j]
               for i in range(n) for j in range(n)): continue
        # Directly test preservation of products e_i*e_j.
        ac=[sum(a[i][j]*c[j] for j in range(n))%p for i in range(n)]
        ok=True
        for i in range(n):
            for j in range(n):
                left=[(diag[i] if i==j else 0)*v%p for v in ac]
                bij=sum(diag[k]*a[k][i]*a[k][j] for k in range(n))%p
                right=[bij*v%p for v in c]
                if left!=right: ok=False;break
            if not ok:break
        if ok: ans[rank(a,p)]+=1
    return ans


def test():
    matrix_tests=[
      (2,3,[1,1],[1,0]),(2,3,[1,2],[1,0]),(2,3,[1,2],[1,1]),
      (2,5,[1,1],[1,0]),(2,5,[1,4],[1,1]),
      (3,3,[1,1,1],[1,0,0]),(3,3,[1,1,2],[1,0,1]),
    ]
    for n,p,diag,c in matrix_tests:
        actual=count_idempotent_homs(n,p,diag,c)
        expected=formula(n,p,diag,c)
        assert actual==expected,(n,p,diag,c,actual,expected)
        print('matrix',n,p,diag,c,dict(sorted(actual.items())))
    geometric_tests=[
       (3,3,[1,1,1],[1,0,0]),(3,3,[1,1,2],[1,0,1]),
       (4,3,[1,1,1,1],[1,0,0,0]),(4,3,[1,1,1,2],[1,0,0,0]),
       (4,5,[1,1,1,4],[1,0,0,0]),(4,5,[1,1,1,4],[1,0,0,1]),
       (5,3,[1,1,1,1,1],[1,0,0,0,0]),
    ]
    for n,p,diag,c in geometric_tests:
        computed=formula(n,p,diag,c)
        for r in range(1,n):
            geo=isometric_subspace_count(n,r,p,diag,c)
            assert computed.get(r,0)==geo*p**(r*(n-r-1)),(n,p,diag,c,r,computed,geo)
        print('isotropic',n,p,diag,c,dict(sorted(computed.items())))
    print('VERIFY_OK')

if __name__=='__main__': test()
