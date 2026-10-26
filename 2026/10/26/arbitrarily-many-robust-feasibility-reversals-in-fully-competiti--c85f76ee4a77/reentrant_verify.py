"""Exact finite witnesses for multiband feasibility in competitive Lotka-Volterra systems."""
from fractions import Fraction as F


def inverse(A):
    n = len(A)
    T = [[F(A[i][j]) for j in range(n)] + [F(int(i == j)) for j in range(n)] for i in range(n)]
    for i in range(n):
        k = next((k for k in range(i, n) if T[k][i]), None)
        if k is None:
            raise ValueError('singular witness matrix')
        T[i], T[k] = T[k], T[i]
        p = T[i][i]
        T[i] = [a / p for a in T[i]]
        for j in range(n):
            if j != i:
                p = T[j][i]
                T[j] = [a - p*b for a,b in zip(T[j], T[i])]
    return [row[n:] for row in T]


def matvec(A, v):
    return [sum((a*b for a,b in zip(row, v)), F(0)) for row in A]


def setup(k, odd):
    n = 2*k + odd
    B = [[F(0) for _ in range(n)] for _ in range(n)]
    for j in range(1, k+1):
        B[2*j-2][2*j-1] = F(4*j-2)
        B[2*j-1][2*j-2] = F(4*j-3)
    good = [F(1, 2)] + [F(8*j-1,2) for j in range(1,k)] + [F(4*k-1)]
    bad = [F(8*j-5,2) for j in range(1,k+1)]
    return B,good,bad


def A_at(B,a):
    return [[(a if i == j else F(0)) + B[i][j] for j in range(len(B))] for i in range(len(B))]


def check(k,odd):
    B,good,bad = setup(k,odd)
    n=len(B)
    witnesses= sorted(good+bad)
    M=F(0); d=None
    for a in witnesses:
        C=inverse(A_at(B,a))
        M=max(M,max(sum(map(abs,row)) for row in C))
        x=matvec(C,[F(1)]*n)
        if a in good:
            assert all(t>0 for t in x), (k,odd,a,x)
            q=min(x)
        else:
            j=bad.index(a)
            assert x[2*j]<0,(k,odd,a,x)
            q=-x[2*j]
        d=q if d is None else min(d,q)
    eps=min(F(1,8*M*(n-1)),d/(16*M*M*(n-1)),F(1,8*(n-1)))/2
    assert eps>0
    dense=[[B[i][j] if B[i][j] else (eps if i!=j else F(0)) for j in range(n)] for i in range(n)]
    assert all(dense[i][j]>0 for i in range(n) for j in range(n) if i!=j)
    for a in witnesses:
        C=inverse(A_at(dense,a))
        x=matvec(C,[F(1)]*n)
        if a in good:assert all(t>0 for t in x),(k,odd,a,x)
        else: assert x[2*bad.index(a)]<0,(k,odd,a,x)
    a=good[-1]
    assert all(a>sum((dense[i][j]+dense[j][i])/2 for j in range(n) if j!=i) for i in range(n))
    return n, k+1, eps


def main():
    cases=[check(k,odd) for k in range(1,6) for odd in (0,1)]
    for n,bands,eps in cases:
        print(f'n={n} feasible_witnesses={bands} epsilon={eps}')
    print(f'PASS: {len(cases)} exact-rational dense interaction cases, with positive/negative witnesses and final symmetric diagonal dominance.')

if __name__=='__main__':
    main()
