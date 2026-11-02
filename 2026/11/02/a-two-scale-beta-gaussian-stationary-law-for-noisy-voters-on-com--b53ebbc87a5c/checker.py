"""Independent finite-state verification for bipartite noisy-voter equilibrium.

Usage: python checker.py
Requires only Python's standard library.
"""
from fractions import Fraction as F
from math import isclose


def solve(A, b):
    n = len(b)
    A = [list(A[i]) + [b[i]] for i in range(n)]
    for k in range(n):
        r = next((i for i in range(k, n) if A[i][k] != 0), None)
        assert r is not None
        A[k], A[r] = A[r], A[k]
        pivot = A[k][k]
        A[k] = [v / pivot for v in A[k]]
        for i in range(n):
            if i == k or A[i][k] == 0:
                continue
            s = A[i][k]
            A[i] = [A[i][j] - s * A[k][j] for j in range(n + 1)]
    return [A[i][-1] for i in range(n)]


def stationary(a, b, theta):
    states = [(i, j) for i in range(a+1) for j in range(b+1)]
    index = {s:k for k,s in enumerate(states)}
    N = len(states)
    Q = [[F(0) for _ in range(N)] for _ in range(N)]
    for k,(i,j) in enumerate(states):
        transitions = [
            (i+1,j,(a-i)*(F(j,b)+theta/2)) if i<a else None,
            (i-1,j,i*(F(b-j,b)+theta/2)) if i>0 else None,
            (i,j+1,(b-j)*(F(i,a)+theta/2)) if j<b else None,
            (i,j-1,j*(F(a-i,a)+theta/2)) if j>0 else None,
        ]
        for event in transitions:
            if event is not None:
                ii,jj,rate=event
                Q[index[(ii,jj)]][k] += rate
                Q[k][k] -= rate
    Q[-1] = [F(1)]*N
    y = [F(0)]*(N-1)+[F(1)]
    return states,solve(Q,y)


def verify():
    assertions = 0
    for a in range(1,5):
        for b in range(1,5):
            for theta in [F(1,3),F(1),F(5,2)]:
                states,pi=stationary(a,b,theta)
                h=F(1,a)+F(1,b)
                x=h/(h+2*theta*(2+theta))
                z=(1+theta)*x
                def exp(f):
                    return sum((p*f(i,j) for (i,j),p in zip(states,pi)),F(0))
                assert all(p>0 for p in pi); assertions+=1
                assert sum(pi)==1; assertions+=1
                assert exp(lambda i,j:F(i,a))==F(1,2);assertions+=1
                assert exp(lambda i,j:F(j,b))==F(1,2);assertions+=1
                if a>=2:
                    assert exp(lambda i,j:F((2*i-a)**2-a,a*(a-1)))==x;assertions+=1
                if b>=2:
                    assert exp(lambda i,j:F((2*j-b)**2-b,b*(b-1)))==x;assertions+=1
                assert exp(lambda i,j:F((2*i-a)*(2*j-b),a*b))==z;assertions+=1
                expect_variance=h*theta*(1+theta)/(2*(h+2*theta*(2+theta)))
                vvar=exp(lambda i,j:(F(i,a)-F(j,b))**2)
                assert vvar==expect_variance;(assertions:=assertions+1)
                assert z>x;assertions+=1
    # A precise stationary moment calculation at a moderate size,
    # independent of the proof's limiting approximation.
    a,b,theta=4,3,F(1,10)
    states,pi=stationary(a,b,theta)
    u4=sum(p*((F(i,a)+F(j,b))/2)**4 for (i,j),p in zip(states,pi))
    assert F(0)<u4<F(1);assertions+=1
    print(f"PASS: {assertions} exact-rational assertions; "+
          f"{4*4*3+1} independent stationary systems. Sample fourth moment: {u4}")

if __name__=='__main__':
    verify()
