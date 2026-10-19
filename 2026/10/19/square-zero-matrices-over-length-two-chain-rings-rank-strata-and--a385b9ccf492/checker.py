"""Reproducibility checks for square-zero matrices over length-two chain rings.

Python 3 standard library only. Run `python checker.py`.
The exhaustive matrix enumeration is performed independently of the counting formula.
"""
from fractions import Fraction
from itertools import product
from math import prod


def P(q, k):
    return prod((Fraction(q**i-1, q**i) for i in range(1, k+1)), start=Fraction(1))


def formula(q, n):
    gl = prod(q**n-q**j for j in range(n))
    return [int(Fraction(gl, 1) / (P(q,a)*P(q,n-2*a)))
            for a in range(n//2 + 1)]


def field_rank(flat, n, p):
    v = [[flat[n*i+j]%p for j in range(n)] for i in range(n)]
    r=0
    for col in range(n):
        pivot=next((i for i in range(r,n) if v[i][col]),None)
        if pivot is None:
            continue
        v[r],v[pivot]=v[pivot],v[r]
        inv=pow(v[r][col],-1,p)
        for j in range(col,n): v[r][j]=(v[r][j]*inv)%p
        for i in range(r+1,n):
            m=v[i][col]
            if m:
                for j in range(col,n): v[i][j]=(v[i][j]-m*v[r][j])%p
        r+=1
    return r


def multiplication_table(kind,p):
    k=p*p
    if kind=='unramified':
        # Ring F_p[epsilon]/epsilon^2; encode a+p*b.
        add=lambda u,v:(u%p+v%p)%p + p*((u//p+v//p)%p)
        mul=lambda u,v:((u%p)*(v%p))%p + p*(((u%p)*(v//p)+(u//p)*(v%p))%p)
    else:
        # Ring Z/p^2 Z; residue is F_p.
        add=lambda u,v:(u+v)%k
        mul=lambda u,v:(u*v)%k
    return [[add(i,j) for j in range(k)] for i in range(k)], [[mul(i,j) for j in range(k)] for i in range(k)]


def enumerate_square_zero(n,p,kind):
    add,mul=multiplication_table(kind,p)
    k=p*p
    counts=[0]*(n//2+1)
    for entries in product(range(k),repeat=n*n):
        zero=True
        for i in range(n):
            if not zero: break
            for j in range(n):
                s=0
                for h in range(n):
                    s=add[s][mul[entries[i*n+h]][entries[h*n+j]]]
                if s:
                    zero=False
                    break
        if zero:
            a=field_rank(entries,n,p)
            assert a<=n//2
            counts[a]+=1
    return counts


def matmul_modp(A,B,n,p):
    return [sum(A[i*n+k]*B[k*n+j] for k in range(n))%p
            for i in range(n) for j in range(n)]


def kernel_dim_anticommutant(A,n,p):
    # For each matrix unit E_uv, construct coordinates of AE_uv+E_uv A.
    m=n*n
    rows=[[0]*m for _ in range(m)]
    for u in range(n):
        for v in range(n):
            col=u*n+v
            for i in range(n):
                for j in range(n):
                    rows[i*n+j][col]=((A[i*n+u] if j==v else 0)
                                      +(A[v*n+j] if i==u else 0))%p
    rank=0
    for col in range(m):
        piv=next((i for i in range(rank,m) if rows[i][col]),None)
        if piv is None: continue
        rows[rank],rows[piv]=rows[piv],rows[rank]
        inv=pow(rows[rank][col],-1,p)
        rows[rank]=[(t*inv)%p for t in rows[rank]]
        for i in range(rank+1,m):
            fac=rows[i][col]
            if fac:
                rows[i]=[(x-fac*y)%p for x,y in zip(rows[i],rows[rank])]
        rank+=1
    return m-rank


def reduced_lift_check(n,p):
    seen=[0]*(n//2+1)
    reduction_counts=[0]*(n//2+1)
    for A in product(range(p),repeat=n*n):
        if any(matmul_modp(A,A,n,p)):
            continue
        a=field_rank(A,n,p)
        dim=kernel_dim_anticommutant(A,n,p)
        assert dim==(n-a)**2+a*a,(n,p,a,dim)
        reduction_counts[a]+=1
        seen[a]+=p**dim
    assert seen==formula(p,n),(seen,formula(p,n))
    return seen,reduction_counts


def run():
    for n,p,kind in [(2,2,'ramified'),(2,2,'unramified'),
                     (3,2,'ramified'),(3,2,'unramified'),
                     (2,3,'ramified'),(2,3,'unramified')]:
        actual=enumerate_square_zero(n,p,kind)
        expected=formula(p,n)
        assert actual==expected,(n,p,kind,actual,expected)
        print('EXHAUSTIVE',n,p,kind,actual)
    for n,p in [(2,2),(3,2),(4,2),(2,3),(3,3)]:
        got,reduced=reduced_lift_check(n,p)
        print('REDUCTION_KERNELS',n,p,reduced,got)
    assert formula(2,4)==[65536,107520,53760]
    print('VERIFY_OK')

if __name__=='__main__':run()
