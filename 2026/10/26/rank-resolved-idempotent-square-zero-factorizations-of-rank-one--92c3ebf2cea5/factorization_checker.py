"""Direct finite-field check for minimal-rank idempotent--square-zero factorizations.

Run: python factorization_checker.py
All cases enumerate matrices directly; the general theorem is proved separately.
"""
from itertools import product


def mul(a, b, q):
    if q == 4:
        # GF(4) = GF(2)[z]/(z^2+z+1), 0,1,z,z+1 encoded as 0..3.
        p = 0
        for i in range(2):
            for j in range(2):
                if ((a >> i) & 1) and ((b >> j) & 1):
                    p ^= 1 << (i+j)
        if p & 4:
            p ^= 7
        return p
    return a * b % q


def add(a, b, q):
    return (a ^ b) if q == 4 else ((a+b) % q)


def dot(a,b,q):
    s = 0
    for x,y in zip(a,b):
        s = add(s,mul(x,y,q),q)
    return s


def matmul(A,B,n,q):
    return tuple(dot(A[i*n:(i+1)*n],B[j::n],q)
                 for i in range(n) for j in range(n))


def gauss(n,k,q):
    if not 0 <= k <= n:return 0
    x=y=1
    for j in range(k):
        x *= q**(n-j)-1
        y *= q**(k-j)-1
    return x//y


def formula(n,q):
    C={r:q**(r*(n-r)-1)*gauss(n-2,r-1,q) for r in range(1,n)}
    D={r:q**(r*(n-r))*gauss(n-1,r-1,q) for r in range(1,n+1)}
    return {trace:{r: (q**(n-1)-(1 if trace else q))*C.get(r,0)
                         +(0 if trace else D.get(r,0)) for r in range(1,n+1)}
            for trace in (0,1)}


def rank(A,n,q):
    M=[list(A[i*n:(i+1)*n]) for i in range(n)]
    d=0
    for c in range(n):
        row=next((i for i in range(d,n) if M[i][c]),None)
        if row is None:continue
        M[d],M[row]=M[row],M[d]
        inv=next(z for z in range(1,q) if mul(z,M[d][c],q)==1)
        M[d]=[mul(z,inv,q) for z in M[d]]
        for i in range(n):
            if i!=d and M[i][c]:
                t=M[i][c]
                M[i]=[add(a,mul(t,b,q),q) if q==4 else (a-mul(t,b,q))%q
                      for a,b in zip(M[i],M[d])]
        d+=1
    return d


def exhaustive(n,q):
    targets={0: tuple((1 if i==0 and j==1 else 0) for i in range(n) for j in range(n)),
             1: tuple((1 if i==j==0 else 0) for i in range(n) for j in range(n))}
    counts={a:{r:0 for r in range(1,n+1)} for a in targets}
    checked=0
    for E in product(range(q),repeat=n*n):
        if matmul(E,E,n,q)!=E:continue
        checked+=1
        r=rank(E,n,q)
        # Enumerate rank-one N = u psi, with normalized psi fixed by target's row.
        for trace,A in targets.items():
            psi=[A[j] for j in range(n)]
            for u in product(range(q),repeat=n):
                if not any(u):continue
                N=tuple(mul(u[i],psi[j],q) for i in range(n) for j in range(n))
                if matmul(N,N,n,q)!=(0,)*(n*n):continue
                if matmul(E,N,n,q)==A:
                    counts[trace][r]+=1
    return checked,counts


def main():
    for n,q in ((2,2),(2,3),(2,4),(2,5),(3,2),(3,3),(4,2)):
        e,actual=exhaustive(n,q)
        expected=formula(n,q)
        assert actual == expected, (n,q,actual,expected)
        print('dimension=%d field=%d idempotents=%d trace_zero=%d trace_nonzero=%d: PASS' %
              (n,q,e,sum(actual[0].values()),sum(actual[1].values())),flush=True)
    print('MINIMAL_RANK_FACTOR_EXHAUSTIVE_OK')

if __name__=='__main__':main()
