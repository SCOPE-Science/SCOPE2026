"""Exact rational finite checks for the displayed F-stochastic counterexample.
Finite checks illustrate but do not replace the all-n analytical inequalities.
"""
from fractions import Fraction as Q

def matmul(A,B):
    return [[sum(A[i][k]*B[k][j] for k in range(len(B))) for j in range(len(B[0]))] for i in range(len(A))]

def P(n):
    u,v=Q(1,4),Q(3,4)
    a=Q(1,4)**n
    return [[1-u*a,u*a],[1-v*a,v*a]]

def delta(A):return abs(A[0][1]-A[1][1])

def run():
    Z=[[Q(1),Q(0)],[Q(1),Q(0)]]
    assert P(1)==[[Q(15,16),Q(1,16)],[Q(13,16),Q(3,16)]]
    for k in range(8):
        prod=P(k+1)
        for n in range(k+1,20):
            if n>k+1:prod=matmul(P(n),prod)
            assert matmul(P(n),Z)==Z
            assert all(Q(1,4)**(k+1)/4<=row[1]<=Q(3,4)**(k+1) for row in prod)
            expected=Q(1,2)**(n-k)*Q(1,4)**(n*(n+1)//2-k*(k+1)//2)
            assert delta(prod)==expected,(k,n,delta(prod),expected)
            assert all(sum(row)==1 for row in prod)
    print('PASS: 152 exact rational reverse-product checks, row positivity, Dobrushin product and P_n P=P.')
if __name__=='__main__':run()
