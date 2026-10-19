"""Independent finite verification of opposing-direction record covariance.
Run: python3 verify.py. Uses only the Python standard library.
"""
from fractions import Fraction
from math import factorial, comb
from itertools import permutations

def exact_joint(n, i, j):
    if i < j:
        return Fraction(1, i * (n-j+1))
    if i == j:
        return Fraction(factorial(i-1)*factorial(n-i), factorial(n))
    p, d = n-i, i-j
    return Fraction(factorial(p), factorial(n))*sum((Fraction(factorial(i+k-1), factorial(k)*(d+k)) for k in range(p+1)), Fraction())

def cov(n, i, j):
    return exact_joint(n,i,j)-Fraction(1,i*(n-j+1))

def determinant(A):
    # Independent Fraction-valued Gaussian elimination.
    B = [row[:] for row in A]
    m=len(B); out=Fraction(1)
    for col in range(m):
        pivot=next((r for r in range(col,m) if B[r][col]), None)
        if pivot is None: return Fraction()
        if pivot!=col:
            B[col],B[pivot]=B[pivot],B[col]
            out=-out
        v=B[col][col];out*=v
        for r in range(col+1,m):
            f=B[r][col]/v
            if f:
                for c in range(col+1,m):B[r][c]-=f*B[col][c]
                B[r][col]=Fraction()
    return out

def run():
    checked=0
    for n in range(2,8):
        joint_counts=[[0]*n for _ in range(n)]
        for w in permutations(range(n)):
            left=[w[i]==min(w[:i+1]) for i in range(n)]
            right=[w[j]==max(w[j:]) for j in range(n)]
            for i in range(n):
                for j in range(n):
                    joint_counts[i][j]+=int(left[i] and right[j])
        total=factorial(n)
        for i in range(1,n+1):
            for j in range(1,n+1):
                assert Fraction(joint_counts[i-1][j-1],total)==exact_joint(n,i,j),(n,i,j)
                checked+=1
    for n in range(2,13):
        M=[[cov(n,i,j) for j in range(1,n)] for i in range(2,n+1)]
        for r in range(n-1):
            for c in range(n-1):
                s=M[r][c]
                if c<=r: assert s>0,(n,r,c)
                elif c==r+1: assert s<0,(n,r,c)
                else: assert s==0,(n,r,c)
                checked+=1
        if n<=8:
            assert determinant(M)>0,n
            checked+=1
        D=[Fraction(1)]
        for k in range(1,n):
            D.append(sum((M[k-1][j]*D[j]*__import__('functools').reduce(lambda x,t: x*(-M[t][t+1]),range(j,k-1),Fraction(1)) for j in range(k)),Fraction()))
        if n<=8: assert D[-1]==determinant(M),n
        assert D[-1]>0,n
        checked+=1
    print('PASS: '+str(checked)+' exact probability/sign/determinant assertions; n<=7 exhaustive words, n<=12 formulas')

if __name__=='__main__':run()
