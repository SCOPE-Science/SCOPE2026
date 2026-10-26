#!/usr/bin/env python3
"""Exact supplementary checks of the finite Gaussian Berezin polynomial blocks.

Only the Python standard library is used.  This finite checker supplements,
but does not replace, the proof for every polynomial degree and complex parameters.
"""
from fractions import Fraction as Q
from math import factorial


def monomials(degree):
    return [(j, d-j) for d in range(degree+1) for j in range(d+1)]


def operator_matrix(degree, a, b, mixed=True):
    basis = monomials(degree)
    index = {mon: i for i, mon in enumerate(basis)}
    mat = [[Q(0) for _ in basis] for _ in basis]
    for col, (j, k) in enumerate(basis):
        for target, weight in [((j-1,k), b*j), ((j,k-1), a*k)]:
            if min(target)>=0:
                mat[index[target]][col] += weight
        if mixed and j and k:
            mat[index[(j-1,k-1)]][col] += j*k
    return mat


def multiply(A,B):
    rows, between, cols = len(A), len(B), len(B[0])
    return [[sum((A[i][t]*B[t][j] for t in range(between)), Q(0))
             for j in range(cols)] for i in range(rows)]


def rank(M):
    A = [row[:] for row in M]
    h, w = len(A), len(A[0])
    i = 0
    for j in range(w):
        pivot = next((t for t in range(i,h) if A[t][j]), None)
        if pivot is None: continue
        A[i],A[pivot] = A[pivot],A[i]
        c = A[i][j]
        for k in range(j,w): A[i][k] /= c
        for t in range(i+1,h):
            c=A[t][j]
            if c:
                for k in range(j,w): A[t][k] -= c*A[i][k]
        i += 1
        if i == h: break
    return i


def main():
    count=0
    for degree in range(0,8):
        for a,b in [(Q(1),Q(1)),(Q(2),Q(-1)),(Q(-3),Q(2))]:
            basis=monomials(degree)
            size=len(basis)
            D=operator_matrix(degree,a,b)
            L=operator_matrix(degree,a,b,mixed=False)
            DP=[[Q(int(i==j)) for j in range(size)] for i in range(size)]
            LP=[[Q(int(i==j)) for j in range(size)] for i in range(size)]
            for k in range(degree+2):
                expected = (degree-k+1)*(degree-k+2)//2 if k<=degree else 0
                assert rank(DP)==expected,(degree,a,b,k,'rank')
                count+=1
                if k==degree:
                    for r in range(size):
                        assert DP[r]==LP[r],(degree,a,b,k,'highest power')
                        count+=1
                DP=multiply(DP,D)
                LP=multiply(LP,L)
            actual_norm_squared = sum((Q(factorial(degree)**2, factorial(j)*factorial(degree-j))
                                       * b**(2*j) * a**(2*(degree-j))
                                       for j in range(degree+1)),Q(0))
            desired=Q(factorial(degree)) * (a*a+b*b)**degree
            assert actual_norm_squared==desired
            count+=1
    print('VERIFY_OK: {} exact rational assertions'.format(count))


if __name__=='__main__': main()

# Supplemental exact tests for the physical Gaussian L2 norm: the exponential
# weight shifts the Gaussian and the common normalization cancels in the
# rank-one limiting operator.


def _moment(j, k, c):
    from math import comb
    return sum((Q(comb(j,r)*comb(k,r)*factorial(r))*c**(j+k-2*r)
                for r in range(min(j,k)+1)), Q(0))


def _solve(A, b):
    A=[row[:]+[y] for row,y in zip(A,b)]
    n=len(b)
    for i in range(n):
        p=next(t for t in range(i,n) if A[t][i])
        A[p],A[i]=A[i],A[p]
        x=A[i][i]
        for t in range(i,n+1):A[i][t]/=x
        for j in range(n):
            if j==i: continue
            x=A[j][i]
            if x:
                for t in range(i,n+1):A[j][t]-=x*A[i][t]
    return [row[-1] for row in A]


def check_physical_gaussian_l2():
    count=0
    for m in range(5):
        for alpha,beta in [(Q(1),Q(1)), (Q(1),Q(2)), (Q(2),Q(-1))]:
            c=alpha+beta
            base=monomials(m)
            G=[[_moment(j+t,k+l,c) for l,t in base] for j,k in base]
            L=[Q(factorial(m))*beta**j*alpha**k if j+k==m else Q(0)
               for j,k in base]
            x=_solve(G,L)
            dual_squared=sum((u*v for u,v in zip(L,x)),Q(0))
            assert dual_squared==Q(factorial(m))*(alpha*alpha+beta*beta)**m
            count+=1
    print('PHYSICAL_L2_VERIFY_OK: {} exact shifted-Gaussian Gram checks'.format(count))


if __name__=='__main__': check_physical_gaussian_l2()
