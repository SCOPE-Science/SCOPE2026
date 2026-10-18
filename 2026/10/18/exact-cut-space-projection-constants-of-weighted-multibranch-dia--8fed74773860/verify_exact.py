"""Exact rational checks of weighted K_{2,m} cut-space projection formulas."""
from fractions import Fraction as F
from itertools import product


def data(r):
    assert len(r) >= 3 and all(t > 0 for t in r)
    m = len(r)
    W = sum(r)
    c = [t / (W-t) for t in r]
    Z = sum(c)
    alpha = [t/Z for t in c]
    lam = 1 + 1/Z
    return alpha, lam


def matrix(r):
    m = len(r)
    alpha,lam = data(r)
    P = [[F(0) for _ in range(2*m)] for __ in range(2*m)]
    # On input edge (j,b), the output on branch i has mean alpha_j/2.
    # Difference coordinates are retained only on branch j.
    for j in range(m):
        for b in range(2):
            for i in range(m):
                for a in range(2):
                    P[2*i+a][2*j+b] = alpha[j]/2 + (F(1) if i==j and a==b else F(-1) if i==j else F(0))/2
    return P,lam


def matmul(A,B):
    return [[sum(a*b for a,b in zip(row,col)) for col in zip(*B)] for row in A]


def run_case(r):
    P,lam = matrix(r)
    m=len(r); n=2*m
    assert matmul(P,P)==P
    # The image consists of edge vectors whose branchwise sums coincide.
    for col in zip(*P):
        sums=[col[2*j]+col[2*j+1] for j in range(m)]
        assert all(s==sums[0] for s in sums)
    # P fixes a basis: path-differences and the global common-sum vector.
    basis=[]
    for j in range(m):
        v=[F(0)]*n
        v[2*j]=F(1)
        v[2*j+1]=F(-1)
        basis.append(v)
    basis.append([F(1)]*n)
    for v in basis:
        assert [sum(P[i][j]*v[j] for j in range(n)) for i in range(n)]==v
    w=[v for t in r for v in (t,t)]
    colnorm=[sum(w[i]*abs(P[i][j]) for i in range(n))/w[j] for j in range(n)]
    assert max(colnorm)==lam
    assert all(z==lam for z in colnorm)
    alpha,_=data(r)
    assert sum(alpha)==1 and all(F(0)<x<F(1) for x in alpha)
    # Lower bound for every projection: min_a max_j c_j*|a_j| = 1/sum(1/c_j)
    W=sum(r)
    c=[(W-t)/t for t in r]
    assert max(c[j]*alpha[j] for j in range(m)) == lam-1
    return lam


if __name__=='__main__':
    count=0
    for m in range(3,9):
        for shift in range(15):
            r=[F(((3*i+5*shift)%17)+1, ((2*i+shift)%7)+1) for i in range(m)]
            run_case(r)
            count+=1
        assert run_case([F(1)]*m)==2-F(1,m)
        count+=1
        for t in [F(1,3),F(1),F(3),F(11,2)]:
            run_case([F(1)]*(m-1)+[t]); count+=1
    print(f"PASS: {count} exact cases, idempotence, full weighted column norms, range/fixing, sharp lower bounds")
