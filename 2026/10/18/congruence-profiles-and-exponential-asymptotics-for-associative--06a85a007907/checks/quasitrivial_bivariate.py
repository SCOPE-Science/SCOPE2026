"""Coefficient-domain recurrence for the bivariate EGF, independent of direct operation enumeration."""
from math import comb, factorial

def mulpoly(a,b):
    c=[0]*(len(a)+len(b)-1)
    for i,v in enumerate(a):
        for j,w in enumerate(b):c[i+j]+=v*w
    return c

def bellpoly(n):
    # Stirling recurrence avoids partition enumeration
    a=[1]
    for k in range(n):
        b=[0]*(len(a)+1)
        for j,v in enumerate(a):
            b[j]+=j*v
            b[j+1]+=v
        a=b
    return a

def solve(N):
    # ordered block arrangements of a labeled s-set = operations q_s; sum over
    # at least two source blocks = q_s - w_s.
    b=[0]+[1]+[2]*max(0,N-1)
    q=[1]+[0]*N
    for n in range(1,N+1):
        q[n]=sum(comb(n,s)*b[s]*q[n-s] for s in range(1,n+1))
    R=[[0] for _ in range(N+1)]
    for n in range(1,N+1):
        R[n]=[v*b[n] for v in bellpoly(n)]
        if len(R[n])<2:R[n]+=[0]*(2-len(R[n]))
        R[n][1] += q[n]-b[n]  # A multi-block interval contributes one congruence class.
    H=[[1]]+[[0] for _ in range(N)]
    for n in range(1,N+1):
        result=[0]*(n+1)
        for s in range(1,n+1):
            p=mulpoly(R[s],H[n-s])
            for j,v in enumerate(p):result[j]+=comb(n,s)*v
        H[n]=result
    return q,H

if __name__=='__main__':
    q,H=solve(10)
    for n in range(1,9):print('n=',n,'ops=',q[n],'profile=',H[n],'total=',sum(H[n]))
    assert H[4]==[0,138,270,300,138]
    assert [sum(H[n]) for n in range(1,10)]==[1,8,70,846,12784,232238,4923734,119325224,3253497786]
    print('BIVARIATE_OK')
