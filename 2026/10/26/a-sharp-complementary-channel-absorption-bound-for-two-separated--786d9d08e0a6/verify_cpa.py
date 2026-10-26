#!/usr/bin/env python3
"""Reproduce exact two-sheet coherent-absorption identities with independent matrix arithmetic."""
import cmath, math, random

def multiply(A,B):
    return [[sum(A[i][k]*B[k][j] for k in range(2)) for j in range(2)] for i in range(2)]

def scatter(a,b,theta):
    X=lambda u:[[1-u,-u],[u,1+u]]
    E=cmath.exp(1j*theta)
    M=multiply(X(b),multiply([[E,0],[0,1/E]],X(a)))
    z=M[1][1]
    assert abs(z)>=1+a+b-1e-8
    return M, [[-M[1][0]/z,1/z],[1/z,M[0][1]/z]]

def singular_values_sq(S):
    tr=sum(abs(v)**2 for row in S for v in row)
    det=S[0][0]*S[1][1]-S[0][1]*S[1][0]
    disc=max(0.,tr*tr-4*abs(det)**2)
    return ((tr+math.sqrt(disc))/2,(tr-math.sqrt(disc))/2)

def assert_close(x,y,tol=2e-10):
    assert abs(x-y)<tol*max(1,abs(x),abs(y)),(x,y)

checks=0
for a in [.05,.12,.25,.39,.5,.78,.9]:
    b=1-a
    for m in range(4):
        M,S=scatter(a,b,math.pi*m)
        assert_close(M[0][0],0)
        s1,s2=singular_values_sq(S)
        assert_close(s1,1);assert_close(s2,0)
        assert_close(abs(M[1][0])**2,1)
        checks+=4
for L in [1.001,1.02,1.2,1.5,2,2.5,3,4,10,50,100]:
    delta=math.hypot(L-1,1)
    for sgn in [-1,1]:
        a=(L+sgn*delta)/2
        b=L-a
        assert min(a,b)>0
        for m in range(4):
            th=math.pi*(m+.5)
            M,S=scatter(a,b,th)
            assert_close(M[0][0],0)
            assert_close(abs(M[1][1]),2*L)
            assert_close(abs(M[1][0])**2,(2*a-1)**2)
            s1,s2=singular_values_sq(S)
            assert_close(s1,((L-1)**2+1)/L**2)
            assert_close(s2,0)
            assert_close(1-s1,2*(L-1)/L**2)
            assert 1-s1<=.5000000001
            checks+=7
# Random ensembles validate transfer/S reciprocity/passivity and wave outgoing cancellation.
rng=random.Random(100613)
for _ in range(1000):
    a=10**rng.uniform(-2,1)
    b=10**rng.uniform(-2,1)
    theta=rng.uniform(-5,5)
    M,S=scatter(a,b,theta)
    assert_close(M[0][0]*M[1][1]-M[0][1]*M[1][0],1)
    assert_close(S[0][1],S[1][0])
    s1,s2=singular_values_sq(S)
    assert s1<=1+1e-10 and s2>=-1e-10 and s2<=s1+1e-10
    assert_close((S[0][0]*S[1][1]-S[0][1]*S[1][0]),-M[0][0]/M[1][1])
    checks+=4
for L in [1.05,1.7,2,5,100]:
    q=L-1
    a=(L+math.hypot(q,1))/2
    b=L-a
    # random non-phase-locked separations cannot be exact CPA
    for theta in [math.pi/4,math.pi/3,math.pi/7]:
        M,_=scatter(a,b,theta)
        assert abs(M[0][0])>1e-6
        checks+=1
print('PASS',checks,'independent scalar and matrix assertions')
