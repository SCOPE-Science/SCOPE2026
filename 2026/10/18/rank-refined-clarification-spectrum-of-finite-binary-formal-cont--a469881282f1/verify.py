"""Independent finite checks for rank-refined clarification spectra.

Uses direct enumeration of incidence tables, not the factorization proof.
Requires only Python standard library.
"""
from collections import Counter
from itertools import product


def stirling_second(n, k):
    s = [[0] * (n + 1) for _ in range(n + 1)]
    s[0][0] = 1
    for i in range(1, n + 1):
        for j in range(1, i + 1):
            s[i][j] = s[i-1][j-1] + j*s[i-1][j]
    return s[n][k] if 0 <= k <= n else 0


def gaussian(n, k, q):
    if k < 0 or k > n:
        return 0
    out = 1
    # Exact Gaussian-binomial recurrence avoids intermediate division.
    row = [1]
    for v in range(1, n + 1):
        next_row = [1] + [0] * v
        next_row[v] = 1
        for j in range(1, v):
            next_row[j] = row[j] + q**(v-j)*row[j-1]
        row = next_row
    return row[k]


def falling(a, n):
    out = 1
    for i in range(n):
        out *= a-i
    return out if 0 <= n <= a else 0


def tuples_spanning(n, d, q=2):
    return sum(gaussian(d,j,q)*(-1)**(d-j)*q**((d-j)*(d-j-1)//2)*falling(q**j,n) for j in range(d+1))


def gl(d,q=2):
    out=1
    for i in range(d):
        out *= q**d-q**i
    return out


def number(r,m,a,b,d,q=2):
    num=(stirling_second(r,a)*stirling_second(m,b)*tuples_spanning(a,d,q)*tuples_spanning(b,d,q))
    assert num % gl(d,q)==0
    return num//gl(d,q)


def finite_rank(rows, ncol, q):
    a=[list(row) for row in rows]
    n=len(a)
    rank=0
    for col in range(ncol):
        pivot=next((u for u in range(rank,n) if a[u][col] % q),None)
        if pivot is None:
            continue
        a[rank],a[pivot]=a[pivot],a[rank]
        inv=pow(int(a[rank][col]),-1,q)
        for j in range(col,ncol):
            a[rank][j]=(a[rank][j]*inv)%q
        for i in range(n):
            if i==rank: continue
            f=a[i][col]
            if f:
                for j in range(col,ncol):
                    a[i][j]=(a[i][j]-f*a[rank][j])%q
        rank+=1
        if rank==n:break
    return rank


def spectrum_by_enumeration(r,m,q):
    counts=Counter()
    for flat in product(range(q),repeat=r*m):
        rows=[flat[i*m:(i+1)*m] for i in range(r)]
        cols=[tuple(rows[i][j] for i in range(r)) for j in range(m)]
        counts[(len(set(rows)),len(set(cols)),finite_rank(rows,m,q))]+=1
    return counts


def test():
    # Sum of every rank-profile equals the total number of incidence tables.
    for q in (2,3):
        for r in range(1,5 if q==2 else 3):
            for m in range(1,5 if q==2 else 3):
                exact=spectrum_by_enumeration(r,m,q)
                formula={}
                for a in range(1,r+1):
                    for b in range(1,m+1):
                        for d in range(min(a,b)+1):
                            val=number(r,m,a,b,d,q)
                            if val: formula[a,b,d]=val
                assert exact==formula,(q,r,m,exact,formula)
                assert sum(formula.values())==q**(r*m)
                print(f'CHECK q={q} rows={r} columns={m} profiles={len(exact)} total={q**(r*m)}')
    # Known unrefined OEIS baseline: A181230(3,3)=264, A088310(4)=33864.
    for n,counts in ((3,{2:96,3:168}), (4,{2:96,3:13608,4:20160})):
        got={d:number(n,n,n,n,d) for d in range(n+1)}
        got={k:v for k,v in got.items() if v}
        assert got==counts,(got,counts)
    # A rank-r clarified table can have at most q**r distinct rows/columns.
    for r in range(1,6):
        for a in range(1,2**r+2):
            assert (tuples_spanning(a,r)>0)==(r<=a<=2**r)
    # Independent rank-stratum normalization, known finite-field matrix count.
    for q in (2,3):
        for r in range(1,7):
            for m in range(1,7):
                for d in range(min(r,m)+1):
                    observed=sum(number(r,m,a,b,d,q) for a in range(1,r+1) for b in range(1,m+1))
                    target=gaussian(r,d,q)*gaussian(m,d,q)*gl(d,q)
                    assert observed==target,(q,r,m,d,observed,target)
    print('VERIFY_OK')

if __name__=='__main__':
    test()
