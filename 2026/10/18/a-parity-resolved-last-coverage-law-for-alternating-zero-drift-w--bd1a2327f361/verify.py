"""Exact checks for the last-coverage law under complementary alternating drift.
Python 3.10+; standard library only. The direct solver retains visited masks,
walker positions, and clock parity, and does not assume the analytic scale law.
"""
from fractions import Fraction as F


def closed_form(n, k, p):
    assert n >= 3 and 1 <= k < n and 0 < p < 1
    q = 1-p
    if n % 2:
        m = (n-1)//2
        return (q if k % 2 else p)/m
    m = n//2
    A = q/(m-p)
    B = p/(m-q)
    if k % 2:
        j = (k-1)//2
        return ((m-1-j)*A+j*B)/(m-1)
    j = k//2
    return ((j-p)*A+(m-j-q)*B)/(m-1)


def scale(x, p):
    # s(0)=0, s(2j)=j, s(2j+1)=j+1-p for negative j too.
    j = x//2
    return F(j) if x%2 == 0 else F(j)+1-p


def analytic_hitting(n, k, p):
    aa = k-n+1
    bb = k-1
    s = lambda x: scale(x, p)
    return ((s(bb)-s(0))/(s(bb)-s(aa)) * (s(aa)-s(aa-1))/(s(bb)-s(aa-1))
           + (s(0)-s(aa))/(s(bb)-s(aa)) * (s(bb+1)-s(bb))/(s(bb+1)-s(aa)))


def linear_solve(A, B):
    """Solve AX=B over exact rational fractions by Gauss-Jordan elimination."""
    d=len(A); w=len(B[0])
    M=[list(A[i])+list(B[i]) for i in range(d)]
    for col in range(d):
        piv=next(i for i in range(col,d) if M[i][col])
        M[col],M[piv]=M[piv],M[col]
        v=M[col][col]
        M[col]=[x/v for x in M[col]]
        for row in range(d):
            if row==col or not M[row][col]: continue
            v=M[row][col]
            M[row]=[x-v*y for x,y in zip(M[row],M[col])]
    return [row[d:d+w] for row in M]


def independent_absorption(n, p):
    """Exact absorbing-chain solution for the original time-dependent cycle walk."""
    masks=sorted((m for m in range(1,1<<n,2) if m!=(1<<n)-1),key=lambda m:-m.bit_count())
    value={}
    for mask in masks:
        states=[(pos,phase) for pos in range(n) if mask>>pos&1 for phase in (0,1)]
        where={state:i for i,state in enumerate(states)}
        d=len(states)
        A=[[F(int(i==j)) for j in range(d)] for i in range(d)]
        B=[[F(0) for j in range(n)] for i in range(d)]
        for i,(pos,phase) in enumerate(states):
            pp=p if phase==0 else 1-p
            for step,prob in ((1,pp),(-1,1-pp)):
                nxt=(pos+step)%n
                mm=mask | (1<<nxt)
                if mm==(1<<n)-1:
                    B[i][nxt]+=prob
                elif mm!=mask:
                    prior=value[(mm,nxt,1-phase)]
                    for j in range(n): B[i][j]+=prob*prior[j]
                else:
                    A[i][where[(nxt,1-phase)]]-=prob
        X=linear_solve(A,B)
        for i,(pos,phase) in enumerate(states):value[(mask,pos,phase)]=X[i]
    return value[(1,0,0)]


def main():
    count=0
    for n in range(3,65):
        for p in (F(1,5),F(2,5),F(1,2),F(3,4),F(9,10)):
            tot=F(0)
            for k in range(1,n):
                prediction=closed_form(n,k,p)
                assert prediction==analytic_hitting(n,k,p),(n,k,p,prediction,analytic_hitting(n,k,p))
                assert 0<prediction<1
                tot+=prediction
                count+=2
            assert tot==1,(n,p,tot)
            count+=1
    for n in range(3,8):
        for p in (F(1,4), F(2,5), F(1,2), F(3,4)):
            result=independent_absorption(n,p)
            assert result[0]==0
            assert sum(result)==1
            count+=2
            for k in range(1,n):
                expected=closed_form(n,k,p)
                assert result[k]==expected,(n,p,k,result[k],expected)
                count+=1
    print('VERIFIED',count,'exact rational checks')

if __name__=='__main__': main()
