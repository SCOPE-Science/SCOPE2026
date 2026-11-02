"""Reproduce the finite exact tests for a one-edge augmentation of a biclique.

Standard-library only. Analytical quantifiers and asymptotics are proved in RESULT.md,
not by the finite tests in this file.
"""
from fractions import Fraction as Q
from collections import deque
from itertools import product
from random import Random
from math import sqrt, log2, log


def distances(m, n):
    N = m + n
    edges = [set() for _ in range(N)]
    for i in range(m):
        for j in range(m, N):
            edges[i].add(j)
            edges[j].add(i)
    edges[0].add(1)
    edges[1].add(0)
    out = []
    for a in range(N):
        d = [-1] * N
        d[a] = 0
        que = deque([a])
        while que:
            x = que.popleft()
            for y in edges[x]:
                if d[y] < 0:
                    d[y] = d[x] + 1
                    que.append(y)
        assert all(x >= 0 for x in d)
        out.append(d)
    return out


def polynomial(m, n, q):
    return ((4*m*n - 2*m - 6*n + 2)*q*q
            +(-6*m*n + m + 9*n - 2)*q
            +2*m*n - 4*n)


def root(m,n):
    a=4*m*n-2*m-6*n+2
    b=-6*m*n+m+9*n-2
    c=2*m*n-4*n
    return (-b+sqrt(b*b-4*a*c))/(2*a)


def exact_quadratic(D, q, z):
    return sum(z[i]*z[j] * (q if D[i][j] == 2 else D[i][j])
               for i in range(len(z)) for j in range(len(z)))


def completed_square(m,n,q,z):
    r=m-2
    s=sum(z[:m])
    assert s == -sum(z[m:])
    u=(z[0]+z[1])/2
    v=(z[0]-z[1])/2
    h=2*q*(m-1)-(m-2)
    A=4*q-2+4*q/r
    F=2*(q-1)-q/n-q*(2*q-1)/h
    return (F*s*s-A*(u-q*s/h)**2-2*v*v
            -q*sum((x-(s-2*u)/r)**2 for x in z[2:m])
            -q*sum((x+s/n)**2 for x in z[m:]))


def positive_definite(G):
    """Exact symmetric LDL pivots; only applied where positive definite is expected."""
    N=len(G)
    L=[[Q(0) for _ in range(N)] for _ in range(N)]
    d=[Q(0)]*N
    for j in range(N):
        d[j]=G[j][j]-sum(L[j][k]*L[j][k]*d[k] for k in range(j))
        if d[j] <= 0:
            return False
        for i in range(j+1,N):
            L[i][j]=(G[i][j]-sum(L[i][k]*L[j][k]*d[k] for k in range(j)))/d[j]
    return True


def gram_from_dist(D,q):
    N=len(D)
    M=[[Q(0) if D[i][j]==0 else Q(1) if D[i][j]==1 else q
        for j in range(N)] for i in range(N)]
    return [[-M[i][j]+M[i][-1]+M[-1][j] for j in range(N-1)]
            for i in range(N-1)]


def main():
    rng=Random(0xA17C)
    direct_checks=0
    pd_checks=0
    failure_witnesses=0
    root_checks=0
    for m in range(3,10):
        for n in range(2,9):
            N=m+n
            D=distances(m,n)
            assert all(D[i][j]==(0 if i==j else 1 if (i<m<=j or j<m<=i or {i,j}=={0,1}) else 2)
                       for i,j in product(range(N),repeat=2))
            qstar=root(m,n)
            q0=2*m*n/(2*m*n-m-n)
            assert 1<q0<qstar<2
            assert abs(float(polynomial(m,n,qstar)))<1e-8
            root_checks+=1
            for q in (Q(1),Q(6,5),Q(4,3),Q(3,2),Q(7,4),Q(2)):
                h=2*q*(m-1)-(m-2)
                F=2*(q-1)-q/n-q*(2*q-1)/h
                assert polynomial(m,n,q)==n*h*F
                for _ in range(10):
                    z=[Q(rng.randrange(-5,6),rng.randrange(1,5)) for _ in range(N-1)]
                    z.append(-sum(z))
                    assert exact_quadratic(D,q,z)==completed_square(m,n,q,z)
                    direct_checks+=1
                if polynomial(m,n,q)<0:
                    assert positive_definite(gram_from_dist(D,q))
                    pd_checks+=1
                elif polynomial(m,n,q)>0:
                    z=[q/h,q/h]+[(2*q-1)/h]*(m-2)+[-Q(1,n)]*n
                    assert sum(z)==0
                    assert exact_quadratic(D,q,z)==F and F>0
                    failure_witnesses+=1
    for n in (2,3,5,11):
        target=2*n/((4*n*n-1)*log(2))
        for m in (500,1000,2000):
            q=root(m,n)
            q0=2*m*n/(2*m*n-m-n)
            ratio=m*m*(log2(q)-log2(q0))
            assert abs(ratio-target)<0.012
    print('VERIFIED', 'exact_full_quadratic=',direct_checks,'exact_SPD=',pd_checks,
          'exact_fail_witnesses=',failure_witnesses,'root_brackets=',root_checks,
          'asymptotic_numeric_cases=',12)

if __name__=='__main__':
    main()
