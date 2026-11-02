"""Direct small-prime-field checks of radical/socle rank-stratum formulas.

No third-party dependencies. Run: python verify.py
"""
from collections import Counter
from itertools import product
from math import comb


def gaussian(n, r, q):
    if not 0 <= r <= n:
        return 0
    numerator = 1
    denominator = 1
    for i in range(r):
        numerator *= q ** (n-i) - 1
        denominator *= q ** (r-i) - 1
    return numerator // denominator


def full_maps(t, h, ell, q):
    result = 0
    for a in range(h+1):
        for b in range(t+1):
            result += ((-1)**(a+b) * q**(comb(a, 2)+comb(b, 2))
                       * gaussian(h,a,q) * gaussian(t,b,q)
                       * q**(ell*(h-a)*(t-b)))
    return result


def expected(q, n, ell):
    return {(t,k): gaussian(n,k,q)*gaussian(k,t,q)*full_maps(t,n-k,ell,q)
            for k in range(n+1) for t in range(k+1)
            if gaussian(n,k,q)*gaussian(k,t,q)*full_maps(t,n-k,ell,q)}


def matrix_product(x,y,n,q):
    return tuple(sum(x[i*n+k]*y[k*n+j] for k in range(n)) % q
                 for i in range(n) for j in range(n))


def rank(rows,q):
    data = [list(r) for r in rows]
    if not data:
        return 0
    m, n = len(data),len(data[0])
    pivot = 0
    for j in range(n):
        ip = next((i for i in range(pivot,m) if data[i][j]%q),None)
        if ip is None: continue
        data[ip],data[pivot]=data[pivot],data[ip]
        v=pow(data[pivot][j],-1,q)
        data[pivot]=[(v*z)%q for z in data[pivot]]
        for i in range(pivot+1,m):
            z=data[i][j]%q
            if z:
                data[i]=[(u-z*w)%q for u,w in zip(data[i],data[pivot])]
        pivot+=1
        if pivot==m: break
    return pivot


def profile(mats,n,q):
    horizontal=[[M[i*n+j] for M in mats for j in range(n)] for i in range(n)]
    vertical=[[M[i*n+j] for j in range(n)] for M in mats for i in range(n)]
    return (rank(horizontal,q), n-rank(vertical,q))


def direct(q,n,ell):
    zeros=(0,)*(n*n)
    squares=[]
    for M in product(range(q),repeat=n*n):
        if matrix_product(M,M,n,q)==zeros: squares.append(M)
    compatibility=[[False]*len(squares) for _ in squares]
    for i,M in enumerate(squares):
        for j,N in enumerate(squares):
            if matrix_product(M,N,n,q)==zeros and matrix_product(N,M,n,q)==zeros:
                compatibility[i][j]=True
    c=Counter()
    def visit(prefix, candidates):
        if len(prefix)==ell:
            c[profile([squares[j] for j in prefix],n,q)]+=1
            return
        for j in candidates:
            visit(prefix+[j],[k for k in candidates if compatibility[j][k]])
    visit([],list(range(len(squares))))
    return c, len(squares)


def main():
    configs=[(2,2,2),(3,2,2),(2,3,2),(3,3,2),
             (2,4,2),(2,2,3),(2,3,3),(2,3,4)]
    for q,n,ell in configs:
        observed,sq=direct(q,n,ell)
        prediction=expected(q,n,ell)
        if observed!=prediction:
            print('MISMATCH',q,n,ell,observed,prediction)
            raise AssertionError('rank-stratum mismatch')
        total=sum(observed.values())
        assert all(t<=k for t,k in observed)
        if n%2==1:
            m=n//2
            assert observed.get((m,m),0)==observed.get((m+1,m+1),0)
        print(f'q={q} n={n} ell={ell}: square-zero generators={sq}, valid tuples={total}, strata={len(observed)}; OK')
    print('VERIFY_OK')


if __name__=='__main__':
    main()
