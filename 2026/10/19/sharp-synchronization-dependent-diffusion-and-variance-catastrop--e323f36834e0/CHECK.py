#!/usr/bin/env python3
"""Exact rational checks for the partially synchronized, nonreciprocal Brownian dimer.
Only the Python standard library is needed. This is corroboration, not an infinite proof.
"""
from fractions import Fraction as F
from itertools import product


def inverse_solve(A,b):
    n=len(A)
    z=[list(map(F,row))+[F(b[i])] for i,row in enumerate(A)]
    for j in range(n):
        k=next(i for i in range(j,n) if z[i][j])
        z[j],z[k]=z[k],z[j]
        pivot=z[j][j]
        z[j]=[v/pivot for v in z[j]]
        for i in range(n):
            if i != j:
                t=z[i][j]
                z[i]=[z[i][m]-t*z[j][m] for m in range(n+1)]
    return [row[-1] for row in z]


def generator(lam, alpha):
    beta=lam-alpha
    # States (++), (+-), (--), (-+); two neighboring transitions at alpha,
    # and the opposite transition at beta.
    Q=[[F(0) for j in range(4)] for i in range(4)]
    for i in range(4):
        for j in range(4):
            if i != j:
                Q[i][j]=beta if abs(i-j)==2 else alpha
        Q[i][i]=-sum(Q[i][j] for j in range(4) if j!=i)
    return Q


def check(K,lam,a,alpha,D=F(1)):
    A=a*a; B=K*(K+lam)*(K+2*alpha)-A*(K+alpha)
    if B <= 0: return 0
    Q=generator(lam,alpha)
    phi=[a,F(0),-a,F(0)]
    psi=[F(0),a,F(0),-a]
    H=[[2*(K+phi[i])*(i==j)-Q[i][j] for j in range(4)] for i in range(4)]
    w=inverse_solve(H,[D]*4) # forcing 4D*pi_i=D
    wn=D*((K+lam)*(K+2*alpha)-A)/(2*B)
    assert w[1]==w[3]==wn
    assert all(v>0 for v in w)
    U=D/(K-A*(K+alpha)/((K+lam)*(K+2*alpha)))
    assert w[0]+w[2]==U
    # The autocorrelation mode is a simultaneous eigenvector of the killed chain.
    tau=K+2*lam
    assert all(sum((Q[i][j]-(K+phi[i])*(i==j))*psi[j]
                   for j in range(4))==-tau*psi[i] for i in range(4))
    green=sum(psi[i]*w[i]*psi[i] for i in range(4))/(4*tau)
    Deff=D/F(2)+A*wn/(2*tau)
    assert green==Deff-D/F(2)
    # Derivative with respect to alpha, computed independently from quotient rule.
    N=(K+lam)*(K+2*alpha)-A
    Nprime=2*(K+lam)
    Bprime=2*K*(K+lam)-A
    derivative=D*(Nprime*B-N*Bprime)/(2*B*B)
    assert derivative==D*A*(K*(K+lam)-A)/(2*B*B)
    return 1


def main():
    ct=0
    for K,lam,ar,frac,D in product([F(1),F(2),F(3),F(5)],
                                     [F(1,2),F(1),F(2),F(3)],
                                     [F(1,4),F(1,2),F(1),F(3,2),F(2),F(3),F(4),F(5)],
                                     [F(1,8),F(1,4),F(1,2),F(3,4),F(1)],
                                     [F(1,2),F(1),F(3)]):
        a=K*ar; alpha=lam*frac
        ct+=check(K,lam,a,alpha,D)
    assert ct>400
    # At the exact compensation surface, wn is independent of mixing rate.
    for K,lam in product([F(1),F(2),F(3)], [F(1),F(2),F(4)]):
        A=K*(K+lam)
        for alpha in [lam/F(7),lam/F(2),lam]:
            B=K*(K+lam)*(K+2*alpha)-A*(K+alpha)
            N=(K+lam)*(K+2*alpha)-A
            assert N* K == 2*B
    print('PASSED:',ct,'independent exact 4-state moment / Green-Kubo / derivative checks; 27 compensation checks')

if __name__=='__main__': main()
