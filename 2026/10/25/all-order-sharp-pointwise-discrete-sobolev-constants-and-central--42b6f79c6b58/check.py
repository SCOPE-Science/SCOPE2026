"""Exact rational spot checks of the discrete difference Green identity.
Finite checks supplement rather than establish the all-order theorem.
"""
from fractions import Fraction as F
from math import comb, factorial

def rise(x,k):
    z=1
    for r in range(k): z*=x+r
    return z

def inverse(A):
    n=len(A)
    M=[[F(x) for x in A[i]]+[F(i==j) for j in range(n)] for i in range(n)]
    for i in range(n):
        t=M[i][i]
        assert t
        M[i]=[x/t for x in M[i]]
        for j in range(n):
            if j==i:continue
            t=M[j][i]
            if t: M[j]=[x-t*y for x,y in zip(M[j],M[i])]
    return [row[n:] for row in M]

def run():
    assertions=0
    for a in range(1,6):
        for d in range(1,12):
            H=[[(-1)**(i-j)*comb(2*a,a+i-j) if abs(i-j)<=a else 0 for j in range(d)] for i in range(d)]
            G=inverse(H)
            den=rise(d+a,a)
            c=[F(rise(j,a-1)*rise(d-j+1,a),factorial(a-1)*den) for j in range(1,d+1)]
            for j in range(d):
                assert G[j][0]==c[j]; assertions+=1
            prod=rise(d+1,2*a-1)*factorial(a-1)**2
            for j in range(d):
                g=F(0)
                for k in range(j+1):
                    g+=F((d-2*k)*rise(k+1,a-1)**2*rise(d-k+1,a-1)**2,prod)
                assert G[j][j]==g; assertions+=1
            assert G[(d-1)//2][(d-1)//2]==max(G[j][j] for j in range(d));assertions+=1
    print('EXACT_CHECK_OK', assertions)
if __name__=='__main__':run()
