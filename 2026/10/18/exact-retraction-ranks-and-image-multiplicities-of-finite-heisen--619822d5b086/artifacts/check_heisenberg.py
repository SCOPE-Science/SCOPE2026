"""Exact finite-field checks for the Heisenberg Lie retraction formulas.

Run with Python 3.11 or later; no third-party dependencies.
"""
from itertools import combinations, product
from math import prod


def gf_mul(a, b, q):
    if q == 4:
        u = 0
        while b:
            if b & 1:
                u ^= a
            b >>= 1
            a <<= 1
            if a & 4:
                a ^= 7  # x^2 + x + 1
        return u
    return (a*b) % q


def add(a, b, q):
    return a ^ b if q == 4 or q == 2 else (a+b) % q


def neg(a, q):
    return a if q in (2,4) else (-a) % q


def mul_mat(A, B, q):
    n = len(A)
    return tuple(tuple(sum_field((gf_mul(A[i][k],B[k][j],q) for k in range(n)),q) for j in range(n)) for i in range(n))


def sum_field(vals, q):
    acc = 0
    for v in vals:
        acc = add(acc,v,q)
    return acc


def rank(A, q):
    T = [list(row) for row in A]
    n = len(T); m = len(T[0]) if n else 0
    r = 0
    for c in range(m):
        p = next((j for j in range(r,n) if T[j][c]), None)
        if p is None: continue
        T[r],T[p] = T[p],T[r]
        inv = next(x for x in range(1,q) if gf_mul(x,T[r][c],q)==1)
        T[r] = [gf_mul(v,inv,q) for v in T[r]]
        for j in range(n):
            if j!=r and T[j][c]:
                b=T[j][c]
                T[j] = [add(T[j][h],neg(gf_mul(b,T[r][h],q),q),q) for h in range(m)]
        r += 1
    return r


def omega(x,y,q):
    n=len(x)//2
    return sum_field((add(gf_mul(x[i],y[n+i],q), neg(gf_mul(x[n+i],y[i],q),q),q) for i in range(n)),q)


def iso_count(n,r,q):
    if r==0:return 1
    num=prod(q**(2*n-2*i)-1 for i in range(r))
    den=prod(q**(r-i)-1 for i in range(r))
    assert num%den==0
    return num//den


def pred(n,q):
    return {**{r:iso_count(n,r,q)*q**(r*(2*n-r+1)) for r in range(n+1)},2*n+1:1}


def verify_all_matrices(n,q):
    d=2*n; got={r:0 for r in list(range(n+1))+[d+1]}
    vectors=list(product(range(q),repeat=d))
    tested=0
    for seq in product(range(q),repeat=d*d):
        A=tuple(tuple(seq[d*i:d*(i+1)]) for i in range(d))
        if mul_mat(A,A,q)!=A: continue
        # Direct endomorphism test on a symplectic basis.
        cols=[tuple(A[i][j] for i in range(d)) for j in range(d)]
        for lam in range(q):
            if any(omega(cols[i],cols[j],q)!=(lam if omega(tuple(1 if k==i else 0 for k in range(d)),tuple(1 if k==j else 0 for k in range(d)),q)==1 else neg(lam,q) if omega(tuple(1 if k==i else 0 for k in range(d)),tuple(1 if k==j else 0 for k in range(d)),q)==neg(1,q) else 0) for i in range(d) for j in range(d)):
                continue
            for c in vectors:
                # F(v+tz)=A(v)+(c(v)+lam*t)z.
                ok=(lam*lam-lam)%q==0 if q not in (2,4) else gf_mul(lam,lam,q)==lam
                if not ok: continue
                if any(add(sum_field((gf_mul(c[k],A[k][i],q) for k in range(d)),q),gf_mul(lam,c[i],q),q)!=c[i] for i in range(d)):
                    continue
                r=rank(A,q)+(1 if lam else 0)
                got[r]=got.get(r,0)+1
                tested+=1
    assert got==pred(n,q),(n,q,got,pred(n,q))
    print('DIRECT_MATRIX_CHECK',n,q,got,'total',tested)


def enumerate_subspaces(m,r,q):
    for pivots in combinations(range(m),r):
        available=[]
        for i,p in enumerate(pivots):
            for j in range(p+1,m):
                if j not in pivots:
                    available.append((i,j))
        for vals in product(range(q),repeat=len(available)):
            rows=[[1 if j==p else 0 for j in range(m)] for p in pivots]
            for (i,j),v in zip(available,vals):
                rows[i][j]=v
            yield tuple(tuple(v for v in row) for row in rows)


def verify_subspace_counts(n,q):
    d=2*n
    for r in range(n+1):
        got=sum(1 for rows in enumerate_subspaces(d,r,q) if all(omega(u,v,q)==0 for u in rows for v in rows))
        exp=iso_count(n,r,q)
        assert got==exp,(n,q,r,got,exp)
        print('ISOTROPIC_SUBSPACES',n,q,r,got)




def verify_full_lie_matrices(q):
    # Exhaustively enumerate every linear self-map of the 3-dimensional Lie algebra.
    counts = {0:0,1:0,2:0,3:0}
    for flat in product(range(q), repeat=9):
        F=tuple(tuple(flat[3*i:3*(i+1)]) for i in range(3))
        bracket = add(gf_mul(F[0][0],F[1][1],q), neg(gf_mul(F[0][1],F[1][0],q),q),q)
        if F[0][2] or F[1][2] or F[2][2]!=bracket:
            continue
        if mul_mat(F,F,q)!=F:
            continue
        counts[rank(F,q)]+=1
    expected={i:pred(1,q).get(i,0) for i in range(4)}
    assert counts==expected,(q,counts,expected)
    print('FULL_LIE_LINEAR_MAPS',q,counts)

if __name__=='__main__':
    for q in (2,3,4,5):verify_all_matrices(1,q)
    verify_all_matrices(2,2)
    for q in (2,3,4):verify_full_lie_matrices(q)
    for n,q in ((2,3),(3,2)):verify_subspace_counts(n,q)
    print('ALL_EXACT_CHECKS_PASSED')
