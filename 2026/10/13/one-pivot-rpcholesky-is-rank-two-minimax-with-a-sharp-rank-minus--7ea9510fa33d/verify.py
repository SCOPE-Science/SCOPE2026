"""Exact rational checks of a one-node PSD pivot / RKHS quadrature theorem."""
from fractions import Fraction as F

def transpose(A):
    return [list(x) for x in zip(*A)]

def multiply(A,B):
    Bt=transpose(B)
    return [[sum(x*y for x,y in zip(row,col)) for col in Bt] for row in A]

def matrix_sub(A,B):
    return [[x-y for x,y in zip(a,b)] for a,b in zip(A,B)]

def outer_scaled(col,den):
    return [[x*y/den for y in col] for x in col]

def schur(A,j):
    col=[row[j] for row in A]
    return matrix_sub(A,outer_scaled(col,A[j][j]))

def calc_rp(A):
    n=len(A)
    S=sum(A[i][i] for i in range(n))
    out=[[F(0) for _ in range(n)] for _ in range(n)]
    for j in range(n):
        R=schur(A,j)
        for i in range(n):
            for k in range(n):
                out[i][k]+=A[j][j]*R[i][k]/S
    return out

def trace(A):
    return sum(A[i][i] for i in range(len(A)))

def rank2_checks(B):
    A=multiply(B,transpose(B))
    assert all(A[j][j]>0 for j in range(len(A)))
    S=trace(A)
    phi=calc_rp(A)
    expected=matrix_sub(A,[[v/S for v in row] for row in multiply(A,A)])
    assert phi==expected
    tr2=trace(multiply(A,A))
    det_nonzero=(S*S-tr2)/2
    assert det_nonzero>0
    c=det_nonzero/S
    # phi = c P_range(A), equivalently A phi = c A.
    assert multiply(A,phi)==[[c*v for v in row] for row in A]
    assert trace(phi)==2*c
    for j in range(len(A)):
        R=schur(A,j)
        # Updating a PSD rank-two kernel removes at most one rank.
        assert all(R[i][i]>=0 for i in range(len(A)))
    return c

for B in [
    [[F(1),F(2)],[F(2),F(1)],[F(3),F(1)]],
    [[F(1),F(0)],[F(0),F(1)]],
    [[F(1),F(1)],[F(1),F(-1)],[F(2),F(3)],[F(4),F(-2)]],
    [[F(1),F(2)],[F(2),F(5)],[F(3),F(4)]],
]:
    assert rank2_checks(B)>0

for r in range(2,13):
    for M in (F(1),F(2),F(3),F(10),F(100),F(1000000)):
        lam=[M]+[F(1)]*(r-1)
        S=sum(lam)
        q=[v/S for v in lam]
        Wrp=max(lam[i]*(1-q[i]) for i in range(r))
        t=M*(r-1)/(M*(r-1)+1)
        popt=[1-t/v for v in lam]
        assert all(p>=0 for p in popt)
        assert sum(popt)==1
        assert max(lam[i]*(1-popt[i]) for i in range(r))==t
        assert Wrp==M*(r-1)/(M+r-1)
        assert Wrp/t==((r-1)*M+1)/(M+r-1)
        assert F(1)<=Wrp/t<=r-1
        if r==2:
            assert Wrp==t
        # Water-fill feasibility independently checked for two free test heights.
        for z in (t/F(2), t*2):
            count=sum(max(F(0),1-z/v) for v in lam)
            assert (count>1 if z<t else count<1)

# Nontrivial rank-three non-diagonal exact source expectation identity.
B=[[F(1),F(0),F(1)],[F(0),F(1),F(2)],[F(2),F(0),F(3)],[F(1),F(1),F(1)]]
A=multiply(B,transpose(B))
S=trace(A)
assert calc_rp(A)==matrix_sub(A,[[v/S for v in row] for row in multiply(A,A)])

print('VERIFY_OK: exact rational rank-two matrices, diagonal minimax witnesses, general RP expectation')
