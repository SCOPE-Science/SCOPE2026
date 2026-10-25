"""Exact checks for square-root-to-uniform chains under alternating switching.
Run with Python >=3.9; only standard library is required.
"""
from fractions import Fraction as F
from itertools import product

def multiply(A,B):
    n=len(A)
    return tuple(tuple(sum(A[i][k]*B[k][j] for k in range(n)) for j in range(n)) for i in range(n))

def matpow(A,m):
    n=len(A)
    V=tuple(tuple(F(i==j) for j in range(n)) for i in range(n))
    for _ in range(m): V=multiply(V,A)
    return V

def blend(A,B,c):
    n=len(A)
    return tuple(tuple((1-c)*A[i][j]+c*B[i][j] for j in range(n)) for i in range(n))

def transpose(A):return tuple(zip(*A))

def max_tv(A):
    n=len(A)
    return max(sum(abs(v-F(1,n)) for v in row)/2 for row in A)

def check():
    P=tuple(tuple(F(a,2) for a in row) for row in ((1,1,0,0),(0,0,1,1),(1,1,0,0),(0,0,1,1)))
    Q=transpose(P)
    J=tuple(tuple(F(1,4) for j in range(4)) for i in range(4))
    assert multiply(P,P)==J==multiply(Q,Q)
    assert multiply(P,Q)!=J and multiply(Q,P)!=J
    R=multiply(P,Q)
    assert multiply(R,R)==R
    assert max_tv(R)==F(1,2)
    count=0
    for epsilon in (F(0),F(1,10),F(1,5),F(1,2),F(3,4),F(9,10),F(1)):
        A=blend(P,J,epsilon); B=blend(Q,J,epsilon)
        assert multiply(A,A)==J==multiply(B,B)
        assert all(sum(row)==1 for row in A+B)
        assert all(sum(A[i][j] for i in range(4))==1 for j in range(4))
        if epsilon>0: assert all(a>0 for row in A+B for a in row)
        for phase in (0,1):
            M=matpow(A,0)
            for t in range(1,21):
                M=multiply(M, (A,B)[(t-1+phase)%2])
                assert max_tv(M)==F(1,2)*(1-epsilon)**t, (epsilon,t,phase,max_tv(M))
                assert max(abs(M[i][j]*4-1) for i in range(4) for j in range(4))==(1-epsilon)**t
                count+=1
    print('EXACT_FOUR_STATE_ALGEBRA_PASS',count,'switching cases')
    # Enumerate rational 3-state P with denominator up to 6, including all feasible rows.
    # This finite test does not replace the analytic compactness proof.
    mats=0
    for den in range(1,7):
        rows=[(F(a,den),F(b,den),F(den-a-b,den)) for a in range(den+1) for b in range(den-a+1)]
        J3=tuple(tuple(F(1,3) for j in range(3)) for i in range(3))
        for rowset in product(rows, repeat=3):
            if any(sum(rowset[i][j] for i in range(3))!=1 for j in range(3)): continue
            if multiply(rowset,rowset)!=J3:continue
            mats+=1
            # Approximate Gram largest eigenvalue via exact positivity of I-A^T A, using all 2x2 principal minors
            D=tuple(tuple(rowset[i][j]-F(1,3) for j in range(3)) for i in range(3))
            G=multiply(transpose(D),D)
            H=tuple(tuple(F(i==j)-G[i][j] for j in range(3)) for i in range(3))
            assert all(H[i][i]>0 for i in range(3))
            assert all(H[i][i]*H[j][j]-H[i][j]*H[j][i]>0 for i in range(3) for j in range(i+1,3))
            # determinant is zero? A kills ones, on ones eigenvalue 0, I-A^TA has eigenvalue 1: det strictly positive
            det=(H[0][0]*(H[1][1]*H[2][2]-H[1][2]*H[2][1])-H[0][1]*(H[1][0]*H[2][2]-H[1][2]*H[2][0])+H[0][2]*(H[1][0]*H[2][1]-H[1][1]*H[2][0]))
            assert det>0
    print('THREE_STATE_FINITE_GRID_PASS',mats,'feasible rational kernels (denominator at most 6)')
    print('VERIFY_OK')
if __name__=='__main__':check()
