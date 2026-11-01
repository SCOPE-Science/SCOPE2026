#!/usr/bin/env python3
"""Exact algebraic tests for the coupled Gumowski--Mira inverse-fiber theorem.

Uses the Python standard library. The universal statements are proved
analytically in RESULT.md; these finite tests independently check identities.
"""
from fractions import Fraction as Q
from itertools import product
import random


def g(t, mu):
    return mu*t + 2*(1-mu)*t/(1+t*t)


def gp(t, mu):
    return mu + 2*(1-mu)*(1-t*t)/(1+t*t)**2


def h(t, a, b):
    return (1+a)*t - a*b*t**3


def hp(t, a, b):
    return (1+a) - 3*a*b*t*t


def map_once(x, y, a, b, mu, eps):
    n = len(x)
    lam = 1-eps
    X = [lam*(h(y[i],a,b)+g(x[i],mu)) + eps*(x[(i-1)%n]+x[(i+1)%n])/2 for i in range(n)]
    Y = [-x[i]+g(X[i],mu) for i in range(n)]
    return X, Y


def target_coords(X,Y,a,b,mu,eps):
    n=len(X)
    lam=1-eps
    u=[g(X[i],mu)-Y[i] for i in range(n)]
    v=[(X[i]-lam*g(u[i],mu)-eps*(u[(i-1)%n]+u[(i+1)%n])/2)/lam for i in range(n)]
    return u,v


def det_exact(M):
    M=[row[:] for row in M]
    n=len(M)
    det=Q(1)
    for j in range(n):
        piv=next((i for i in range(j,n) if M[i][j]),None)
        if piv is None:return Q(0)
        if piv!=j:
            M[j],M[piv]=M[piv],M[j]
            det=-det
        pivot=M[j][j]
        det*=pivot
        for i in range(j+1,n):
            c=M[i][j]/pivot
            for k in range(j+1,n):
                M[i][k]-=c*M[j][k]
            M[i][j]=Q(0)
    return det


def jacobian(x,y,a,b,mu,eps):
    n=len(x)
    lam=1-eps
    X,_=map_once(x,y,a,b,mu,eps)
    A=[[Q(0) for _ in range(n)] for _ in range(n)]
    B=[[Q(0) for _ in range(n)] for _ in range(n)]
    for i in range(n):
        A[i][i]+=lam*gp(x[i],mu)
        A[i][(i-1)%n]+=eps/2
        A[i][(i+1)%n]+=eps/2
        B[i][i]=lam*hp(y[i],a,b)
    return [A[i]+B[i] for i in range(n)] + [[-int(i==j)+gp(X[i],mu)*A[i][j] for j in range(n)] + [gp(X[i],mu)*B[i][j] for j in range(n)] for i in range(n)]


def test():
    rng=random.Random(280011)
    algebra_count=0
    for n in (2,3,4):
        for trial in range(30):
            a,b,mu,eps=Q(33,100),Q(1,10),Q(2,5),Q(1,4)
            x=[Q(rng.randint(-7,7),rng.randint(2,8)) for _ in range(n)]
            y=[Q(rng.randint(-7,7),rng.randint(2,8)) for _ in range(n)]
            X,Y=map_once(x,y,a,b,mu,eps)
            u,v=target_coords(X,Y,a,b,mu,eps)
            assert u==x
            assert v==[h(t,a,b) for t in y]
            D=det_exact(jacobian(x,y,a,b,mu,eps))
            expected=(1-eps)**n
            for t in y: expected*=hp(t,a,b)
            assert D==expected,(n,trial,D,expected)
            algebra_count+=1
    print('Exact forward/inverse and full Jacobian identity cases:',algebra_count)

    # In this choice h(y)=2y-y**3/2; all three roots of h(y)=0
    # are rational and generate 3**N inverse images of one target.
    a,b,mu,eps=Q(1),Q(1,2),Q(1,2),Q(1,4)
    for n in (2,3,5):
        image_set=set()
        for y in product((Q(-2),Q(0),Q(2)),repeat=n):
            X,Y=map_once([Q(0)]*n,y,a,b,mu,eps)
            image_set.add((tuple(X),tuple(Y)))
        assert image_set=={((Q(0),)*n,(Q(0),)*n)}
        print('Exact zero-target preimage count: N=',n,'count=',3**n)

    # At h(y)=3/2 the roots are 1, (-1+sqrt(13))/2,
    # (-1-sqrt(13))/2. Two lie in [-3/2,3/2], one outside.
    assert h(Q(1),a,b)==Q(3,2)
    # For the other roots, use the defining quadratic y**2+y-3=0
    # to reduce h(y)-3/2, rather than floating-point approximations.
    # y**3=4*y-3 modulo y**2+y-3, making h(y)-3/2=0.
    # Coefficient identity for (y-1)(y^2+y-3)=y^3-4*y+3.
    def conv(a,b):
        c=[Q(0)]*(len(a)+len(b)-1)
        for i,v in enumerate(a):
            for j,w in enumerate(b):c[i+j]+=v*w
        return c
    assert conv([Q(-1),Q(1)],[Q(-3),Q(1),Q(1)]) == [Q(3),Q(-4),Q(0),Q(1)]
    # Square-root location conditions, justified entirely by integer inequalities:
    # 3 < sqrt(13) < 4 implies 1 < (sqrt(13)-1)/2 < 3/2,
    # while (1+sqrt(13))/2 > 3/2.
    assert 9 < 13 < 16 and 4 < 13
    for aa,bb in ((Q(1,100),Q(1,20)),(Q(33,100),Q(1,10))):
        assert 1+aa > 3*aa*bb # fold radii of both source regimes exceed one
    print('Two-in-box exact witness: L=3/2, h(y)=3/2; roots 1 and (-1+sqrt(13))/2')
    print('All checks passed')

if __name__=='__main__':test()
