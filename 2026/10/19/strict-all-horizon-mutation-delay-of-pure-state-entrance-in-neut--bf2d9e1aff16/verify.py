#!/usr/bin/env python3
"""Exact finite checks for symmetric-mutation Moran pure-state stopping times.

Run: python3 verify.py
These checks illustrate finite cases; the general theorem rests on the proof.
"""
from fractions import Fraction as F


def transition(n, mu):
    assert n >= 2 and F(0) <= mu <= F(1)
    m = n // 2
    Q = [[F(0) for _ in range(m)] for _ in range(m)]
    for r in range(1, m + 1):
        x = F(r, n)
        p = (1-x)*(x+mu*(1-2*x))
        q = x*(1-x-mu*(1-2*x))
        if r < m:
            Q[r-1][r] = p
            if r > 1:
                Q[r-1][r-2] = q
            Q[r-1][r-1] = 1-p-q
        elif n % 2 == 0:
            if r > 1:
                Q[r-1][r-2] = p+q
            Q[r-1][r-1] = 1-p-q
        else:
            if r > 1:
                Q[r-1][r-2] = q
            Q[r-1][r-1] = 1-q
    return Q


def matvec(a,x):
    return [sum((q*v for q,v in zip(row,x)),F(0)) for row in a]


def sub(a,b):
    return [[u-v for u,v in zip(x,y)] for x,y in zip(a,b)]


def trajectories(n,mu,T):
    Q=transition(n,mu)
    D=sub(transition(n,F(1)),transition(n,F(0)))
    u=[F(1)]* (n//2)
    du=[F(0)]* (n//2)
    out=[]
    for t in range(T+1):
        out.append((u[:],du[:]))
        du=[a+b for a,b in zip(matvec(Q,du),matvec(D,u))]
        u=matvec(Q,u)
    return out


def test():
    comparisons=0
    deriv_tests=0
    monotone_in_state=0
    for n in range(3,17):
        for j in range(5):
            mu=F(j,4)
            states=trajectories(n,mu,20)
            for t,(u,du) in enumerate(states):
                assert all(F(0)<=v<=1 for v in u)
                assert all(u[i]<=u[i+1] for i in range(len(u)-1))
                monotone_in_state+=max(0,len(u)-1)
                for r in range(1,len(u)+1):
                    assert du[r-1] == 0 if t<r else du[r-1]>0, (n,mu,t,r,du[r-1])
                    deriv_tests+=1
            if j>0:
                prior=trajectories(n,F(j-1,4),20)
                for t in range(21):
                    for r in range(1,len(u)+1):
                        L=states[t][0][r-1]
                        R=prior[t][0][r-1]
                        assert L == R if t<r else L>R,(n,mu,t,r,L,R)
                        comparisons+=1
    for mu in [F(0),F(1,2),F(1)]:
        assert transition(2,mu)==[[F(1,2)]]
    for j in range(5):
        mu=F(j,4)
        for t,(u,du) in enumerate(trajectories(3,mu,25)):
            assert u == [((F(7)+mu)/9)**t]
    print(f'PASS n=3..16 mu=0,1/4,1/2,3/4,1: {comparisons} stochastic-order comparisons, {deriv_tests} exact derivative-sign tests, {monotone_in_state} exact state comparisons.')
    print('PASS n=2 exception and n=3 geometric closed form.')

if __name__=='__main__':
    test()
