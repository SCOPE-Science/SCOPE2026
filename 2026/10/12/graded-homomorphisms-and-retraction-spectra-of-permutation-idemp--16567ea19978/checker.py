"""Direct finite-field enumeration of graded retractions of a PBW quadratic algebra.

Algebra: k<x_1,...,x_n>/(x_i x_j-x_1 x_j: i,j).
For a degree-one matrix M, its multiplicativity conditions are tested directly
in the degree-two normal basis x_1 x_j, and idempotence directly as M^2=M.
"""
from itertools import product
from collections import Counter

def qbinom(n, k, q):
    if not 0 <= k <= n:
        return 0
    numerator = denominator = 1
    for i in range(k):
        numerator *= q**(n-i)-1
        denominator *= q**(k-i)-1
    assert numerator % denominator == 0
    return numerator//denominator

def rank(M,q):
    n = len(M)
    B=[list(row) for row in M]
    r=0
    for j in range(n):
        k=next((i for i in range(r,n) if B[i][j]%q),None)
        if k is None: continue
        B[r],B[k]=B[k],B[r]
        s=pow(B[r][j],-1,q)
        B[r]=[(x*s)%q for x in B[r]]
        for i in range(n):
            if i==r:continue
            s=B[i][j]
            B[i]=[(x-s*y)%q for x,y in zip(B[i],B[r])]
        r+=1
    return r

def multiply(A,B,q):
    n=len(A)
    return [[sum(A[i][k]*B[k][j] for k in range(n))%q for j in range(n)] for i in range(n)]

def is_multiplicative(A,q):
    n=len(A)
    sums=[sum(A[i][j] for i in range(n))%q for j in range(n)]
    # each defining relation x_i x_j - x_1 x_j must map to zero
    return all(not any(((sums[i]-sums[0])*A[k][j])%q
                           for k in range(n))
               for i in range(n) for j in range(n))

def is_hom_rect(A,q):
    # Matrix A is m by n: check the n(n-1) defining quadratic relations
    # in target degree 2, whose x_1 x_j normal coordinates have dimension m.
    m=len(A); n=len(A[0]); colsum=[sum(A[i][j] for i in range(m))%q for j in range(n)]
    return all(not any(((colsum[i]-colsum[0])*A[k][j])%q for k in range(m))
               for i in range(n) for j in range(n))

def direct_hom_count(n,m,q):
    return sum(is_hom_rect([list(z[i*n:(i+1)*n]) for i in range(m)],q)
               for z in product(range(q),repeat=m*n))

def direct_counts(n,q):
    out=Counter()
    for flat in product(range(q),repeat=n*n):
        A=[list(flat[i*n:(i+1)*n]) for i in range(n)]
        if multiply(A,A,q)!=A:continue
        if is_multiplicative(A,q):
            r=rank(A,q)
            c=sum(A[i][0] for i in range(n))%q
            out[(c,r)]+=1
    return out

def formula_counts(n,q):
    out={}
    for r in range(n+1):
        for c in (0,1):
            out[c,r]=(qbinom(n-1,r,q) if c==0 else qbinom(n-1,r-1,q))*q**(r*(n-r))
    return Counter({k:v for k,v in out.items() if v})

def run():
    for n,m,q in [(2,3,2),(3,2,2),(2,2,3),(3,2,3)]:
        got=direct_hom_count(n,m,q)
        assert got==q**(1+n*(m-1)), (n,m,q,got)
        print('hom',n,m,q,got)
    for n,q in [(2,2),(2,3),(2,5),(3,2),(3,3),(4,2)]:
        got=direct_counts(n,q)
        want=formula_counts(n,q)
        assert got==want,(n,q,got,want)
        profile={r:got.get((0,r),0)+got.get((1,r),0) for r in range(n+1)}
        assert [profile[i] for i in range(n+1)]==[profile[n-i] for i in range(n+1)]
        print('n=',n,'q=',q,'rank_counts=',profile,'types=',sorted(got.items()))
    print('VERIFY_OK')

if __name__=='__main__':run()
