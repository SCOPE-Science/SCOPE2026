#!/usr/bin/env python3
"""Exact-integer finite diagnostics for the metallic-cat Fourier escape theorem.

These checks test a bounded collection of parameters and frequencies;
the all-parameter theorem is proved separately by a sign argument.
"""

def matmul(A,B):
    return [[sum(A[i][q]*B[q][j] for q in range(2)) for j in range(2)] for i in range(2)]

def power(A,n):
    R=[[1,0],[0,1]]
    for _ in range(n): R=matmul(R,A)
    return R

def mul(A,x):
    return (A[0][0]*x[0]+A[0][1]*x[1], A[1][0]*x[0]+A[1][1]*x[1])

def l1(x):
    return abs(x[0])+abs(x[1])

def G(s,n):
    a,b=0,1
    for _ in range(n): a,b=b,s*b+a
    return a

def check():
    checks=0
    for s in range(1,7):
        M=[[s,1],[1,0]]
        A=matmul(M,M)
        for n in range(1,8):
            Mn=power(M,n)
            Mn_inv=[[(-1)**n*Mn[1][1],(-1)**(n+1)*Mn[0][1]],
                    [(-1)**(n+1)*Mn[1][0],(-1)**n*Mn[0][0]]]
            t=G(s,n+1)+2*G(s,n)+G(s,n-1)
            assert Mn==[[G(s,n+1),G(s,n)],[G(s,n),G(s,n-1)]]
            checks+=1
            assert matmul(Mn,Mn_inv)==[[1,0],[0,1]]
            checks+=1
            assert power(A,n)==matmul(Mn,Mn)
            checks+=1
            best=t
            equality=set()
            # v=M^n k. Enumerate v, not k, to retain small exact minimizers.
            for x in range(-9,10):
                for y in range(-9,10):
                    if (x,y)==(0,0):continue
                    v=(x,y)
                    value=l1(mul(Mn_inv,v))+l1(mul(Mn,v))
                    assert value>=best,(s,n,v,value,best)
                    checks+=1
                    if value==best:equality.add(v)
            assert equality=={(1,0),(-1,0),(0,1),(0,-1)},(s,n,equality)
            checks+=1
            for v in equality:
                k=mul(Mn_inv,v)
                assert l1(k)+l1(mul(power(A,n),k))==best
                checks+=1
    print('PASS:',checks,'exact-integer assertions over s=1..6,n=1..7, nonzero v in [-9,9]^2')

if __name__=='__main__':check()
