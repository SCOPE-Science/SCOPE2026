"""Independent finite-field enumeration of annihilating square-zero matrix-pair rank spectra.
Run with Python 3; standard library only. Exhaustive fields here are prime fields.
"""
from itertools import product
from math import prod

def gauss(n,k,q):
    if k<0 or k>n:return 0
    return prod(q**(n-i)-1 for i in range(k))//prod(q**(k-i)-1 for i in range(k))

def gl(r,q):
    return prod(q**r-q**i for i in range(r))

def matrix_rank_count(b,k,r,q):
    return gauss(b,r,q)*gauss(k,r,q)*gl(r,q)

def count_stratum(n,q,r,s,k):
    a=n-k
    return gauss(n,k,q)*sum(
        (-1)**j*q**(j*(j-1)//2)*gauss(a,j,q)*
        matrix_rank_count(a-j,k,r,q)*matrix_rank_count(a-j,k,s,q)
        for j in range(a+1))

def total_stratum(n,q,k):
    return gauss(n,k,q)*prod(q**(2*k)-q**i for i in range(n-k))

def mult(A,B,n,q):
    return tuple(sum(A[i*n+t]*B[t*n+j] for t in range(n))%q
                 for i in range(n) for j in range(n))

def rank(rows,q):
    rows=[list(row) for row in rows]
    if not rows:return 0
    r=0
    for col in range(len(rows[0])):
        p=next((i for i in range(r,len(rows)) if rows[i][col]%q),None)
        if p is None:continue
        rows[r],rows[p]=rows[p],rows[r]
        inv=pow(rows[r][col],-1,q) # q is prime for brute tests
        rows[r]=[(v*inv)%q for v in rows[r]]
        for i in range(len(rows)):
            if i!=r and rows[i][col]%q:
                t=rows[i][col]
                rows[i]=[(u-t*v)%q for u,v in zip(rows[i],rows[r])]
        r+=1
        if r==len(rows):break
    return r

def test(n,q):
    zero=(0,)*(n*n)
    matrices=list(product(range(q),repeat=n*n))
    sq=[A for A in matrices if mult(A,A,n,q)==zero]
    hist={}
    for A in sq:
        rows_a=[A[i*n:(i+1)*n] for i in range(n)]
        r=rank(rows_a,q)
        for B in sq:
            if mult(A,B,n,q)!=zero or mult(B,A,n,q)!=zero:continue
            rows_b=[B[i*n:(i+1)*n] for i in range(n)]
            s=rank(rows_b,q)
            k=n-rank(rows_a+rows_b,q)
            hist[(r,s,k)]=hist.get((r,s,k),0)+1
    expected={(r,s,k):count_stratum(n,q,r,s,k)
              for k in range(n+1) for r in range(n+1) for s in range(n+1)}
    expected={key:v for key,v in expected.items() if v}
    assert hist==expected,(n,q,hist,expected)
    assert all(sum(v for (r,s,l),v in hist.items() if l==k)==total_stratum(n,q,k)
               for k in range(n+1))
    print('n=%d,q=%d: %d pairs, %d rank/kernel strata, kernel distribution %s' %
          (n,q,sum(hist.values()),len(hist),
           {k:sum(v for (r,s,l),v in hist.items() if l==k) for k in range(n+1)}))

if __name__=='__main__':
    for n,q in [(1,2),(2,2),(2,3),(3,2)]:test(n,q)
    for n in range(1,9):
        for q in (2,3,4,5):
            for k in range(n+1):
                assert sum(count_stratum(n,q,r,s,k)
                           for r in range(n+1) for s in range(n+1))==total_stratum(n,q,k)
                assert all(count_stratum(n,q,r,s,k)>=0
                           for r in range(n+1) for s in range(n+1))
    print('VERIFY_OK_ANNIHILATING_RANK_STRATA')
