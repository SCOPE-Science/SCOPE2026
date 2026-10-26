"""Finite identity checks for the three-state no-repeat mutation spine.

Run: python verify.py. All checks concern finite algebra; they do not prove the
large-deviation principle or certify originality.
"""
import math
import random


def dot(a, b):
    return sum(x*y for x,y in zip(a,b))


def kernel(q):
    return [[0.0 if i == j else q[j]/(1-q[i]) for j in range(3)] for i in range(3)]


def flow(nu):
    t12 = 0.5 - nu[2]
    t13 = 0.5 - nu[1]
    t23 = 0.5 - nu[0]
    return [[0.0,t12,t13],[t12,0.0,t23],[t13,t23,0.0]]


def entropy(q, nu, Q):
    P=kernel(q)
    return sum(Q[i][j]*math.log(Q[i][j]/(nu[i]*P[i][j]))
               for i in range(3) for j in range(3)
               if i!=j and Q[i][j]>0)


def explicit(q, nu):
    P=kernel(q)
    Q=flow(nu)
    return sum(Q[i][j]*math.log(Q[i][j]**2/(nu[i]*nu[j]*P[i][j]*P[j][i]))
               for i,j in [(0,1),(0,2),(1,2)] if Q[i][j]>0)


def run():
    rng=random.Random(20261018)
    checks=0
    u=[1/3]*3
    assert abs(explicit(u,u))<1e-13; checks+=1
    assert abs(explicit(u,[0.5,0.5,0.0])-math.log(2))<1e-13; checks+=1
    for _ in range(1500):
        weights=[rng.uniform(0.02,3) for _ in range(3)]
        q=[x/sum(weights) for x in weights]
        P=kernel(q)
        pi_raw=[q[i]*(1-q[i]) for i in range(3)]
        pi=[x/sum(pi_raw) for x in pi_raw]
        assert all(abs(sum(row)-1)<1e-12 for row in P);checks+=1
        assert all(abs(pi[i]*P[i][j]-pi[j]*P[j][i])<1e-12 for i in range(3) for j in range(3));checks+=1
        assert abs(entropy(q,pi,flow(pi)))<1e-12;checks+=1
        a=[rng.uniform(0.02,3) for _ in range(3)]
        w=[x/sum(a) for x in a]
        nu=[(1-w[i])/2 for i in range(3)]
        Q=flow(nu)
        assert all(abs(sum(Q[i])-nu[i])<1e-12 for i in range(3));checks+=1
        assert all(abs(sum(Q[i][j] for i in range(3))-nu[j])<1e-12 for j in range(3));checks+=1
        assert abs(entropy(q,nu,Q)-explicit(q,nu))<1e-11;checks+=1
        assert entropy(q,nu,Q)>-1e-11;checks+=1
        c=min(Q[0][1],Q[0][2],Q[1][2])*0.5
        for direction in (-1,1):
            R=[row[:] for row in Q]
            s=direction*c
            for i,j in [(0,1),(1,2),(2,0)]:
                R[i][j]+=s;R[j][i]-=s
            assert entropy(q,nu,R)>entropy(q,nu,Q)+1e-12
            checks+=1
    print('PASSED',checks,'finite algebraic/numeric assertions')

if __name__=='__main__':
    run()
