#!/usr/bin/env python3
"""Self-contained reproducibility checks for the circular numerical-range projection theorem.

Requires only Python 3.9+ standard library. Exact rational identities and
deterministic numerical candidate comparisons supplement the analytic proof.
"""
from fractions import Fraction as F
from math import sqrt, pi, cos, sin
import random


def add(A, B):
    return [[A[i][j] + B[i][j] for j in range(2)] for i in range(2)]


def scale(z, A):
    return [[z * A[i][j] for j in range(2)] for i in range(2)]


def adj(A):
    return [[A[j][i].conjugate() for j in range(2)] for i in range(2)]


def mul(A, B):
    return [[sum(A[i][k]*B[k][j] for k in range(2)) for j in range(2)] for i in range(2)]


def trace(A):
    return A[0][0] + A[1][1]


def fro2(A):
    return sum(abs(A[i][j])**2 for i in range(2) for j in range(2))


def vecnorm(v):
    return sqrt(abs(v[0])**2 + abs(v[1])**2)


def mv(A, v):
    return [sum(A[i][j]*v[j] for j in range(2)) for i in range(2)]


def inner(x, y):
    return sum(x[i].conjugate() * y[i] for i in range(2))


def outer(u, v):
    return [[u[i]*v[j].conjugate() for j in range(2)] for i in range(2)]


def closest(A, c, r):
    a = trace(A)/2
    T = add(A, scale(-a, [[1,0],[0,1]]))
    H = mul(adj(T), T)
    h00, h11, h01 = H[0][0].real, H[1][1].real, H[0][1]
    discr = sqrt(max(0., (h00-h11)**2 + 4*abs(h01)**2))
    s = sqrt(max(0., (h00+h11+discr)/2))
    assert discr > 1.e-9, 'Routine branch is for nonnormal test cases'
    if abs(h01) > 1.e-10:
        v = [h01, (h00+h11+discr)/2-h00]
    else:
        v = [1., 0.] if h00 > h11 else [0., 1.]
    v = [z/vecnorm(v) for z in v]
    u = [z/s for z in mv(T,v)]
    N = scale(2*r,outer(u,v))
    X = add(scale(c,[[1,0],[0,1]]),N)
    predicted = fro2(add(A,scale(-c,[[1,0],[0,1]]))) + 4*r*r-4*r*s
    return X,N,T,s,u,v,predicted


def exact_tests():
    count=0
    for a in range(-5,6):
        for b in range(-4,5):
            for c in range(-3,4):
                a,b,c = F(a),F(b),F(c)
                T = [[a,b],[c,-a]]
                H=add(mul(adj(T),T),mul(T,adj(T)))
                factor=fro2(T)
                assert H==[[factor, F(0)],[F(0),factor]]
                assert mul(T,T)==scale(a*a+b*c,[[1,0],[0,1]])
                count+=2
    return count


def numeric_tests():
    rng=random.Random(20261031)
    count=0
    for sample in range(400):
        A=[[complex(rng.uniform(-2,2),rng.uniform(-2,2)) for _ in range(2)] for _ in range(2)]
        c=complex(rng.uniform(-1,1),rng.uniform(-1,1))
        r=rng.uniform(0.03,2.)
        X,N,T,s,u,v,predicted=closest(A,c,r)
        assert abs(inner(u,v))<1.e-9
        assert abs(vecnorm(u)-1)<1.e-9
        assert abs(vecnorm(v)-1)<1.e-9
        assert abs(trace(N))<1.e-9
        assert max(abs(z) for row in mul(N,N) for z in row)<1.e-8
        assert abs(fro2(N)-4*r*r)<1.e-8
        actual=fro2(add(A,scale(-1.,X)))
        assert abs(actual-predicted)<1.e-8*(1+abs(predicted))
        count+=7
        # Compare independent random scaled square-zero competitors, not a global proof.
        for j in range(75):
            w=[complex(rng.gauss(0,1),rng.gauss(0,1)) for _ in range(2)]
            w=[x/vecnorm(w) for x in w]
            phase=rng.uniform(0,2*pi)
            q=[-w[1].conjugate(),w[0].conjugate()]
            q=[z*complex(cos(phase),sin(phase)) for z in q]
            competitor=add(scale(c,[[1,0],[0,1]]),scale(2*r,outer(q,w)))
            candidate_cost=fro2(add(A,scale(-1,competitor)))
            assert candidate_cost + 1.e-9 >= predicted
            count+=1
    # Two distinct minimizers on a normal tracefree input.
    A=[[1.+0j,0j],[0j,-1.+0j]]
    r=.7
    minimizers=[]
    for phase in [0.,.7,1.8]:
        v=[1/sqrt(2),complex(cos(phase),sin(phase))/sqrt(2)]
        u=mv(A,v)
        N=scale(2*r,outer(u,v))
        assert abs(inner(u,v))<1.e-12
        assert abs(fro2(add(A,scale(-1,N))) - (fro2(A)+4*r*r-4*r))<1.e-12
        minimizers.append(N)
        count+=2
    assert all(fro2(add(minimizers[i],scale(-1,minimizers[i+1])))>1.e-3 for i in (0,1))
    count+=1
    # Scalar input: every radius-r disk center c has the same distance.
    A=[[3+2j,0],[0,3+2j]]
    for r in [.2,1.,2.]:
        v=[1.+0j,0j]; u=[0j,1.+0j]
        N=scale(2*r,outer(u,v))
        assert abs(fro2(add(A,scale(-1,add(A,N))))-4*r*r)<1.e-12
        count+=1
    return count


if __name__=='__main__':
    n1=exact_tests()
    n2=numeric_tests()
    print(f'PASS: {n1} exact-rational matrix identities; {n2} deterministic complex-matrix and competing-orbit checks; total {n1+n2}')
    print('Checks are supplementary: infinite optimization and disk equivalence are established in RESULT.md.')
