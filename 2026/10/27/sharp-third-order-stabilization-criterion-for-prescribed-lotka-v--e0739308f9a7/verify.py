#!/usr/bin/env python3
"""Exact-rational replay for a prescribed-abundance higher-order Lotka-Volterra theorem.

No external modules. The finite tests check algebraic identities, not an infinite existence claim;
the general existence and necessity arguments are in RESULT.md.
"""
from fractions import Fraction as F
from random import Random

def dot(a,b):
    return sum((x*y for x,y in zip(a,b)),F(0))

def mm(A,B):
    return [[sum((A[i][k]*B[k][j] for k in range(len(B))),F(0))
             for j in range(len(B[0]))] for i in range(len(A))]

def construct(r,S,z):
    n=len(r)
    B=[[S[i][j]*z[j] for j in range(n)] for i in range(n)]
    s=[-2*r[i]-sum(B[i]) for i in range(n)]
    eye=[[F(i==j) for j in range(n)] for i in range(n)]
    if all(si==s[0] for si in s):
        if s[0]>=0:
            return None,s
        J=[[s[0]*eye[i][j] for j in range(n)] for i in range(n)]
        mode='constant'
    else:
        p=next(j for j in range(1,n) if s[j]!=s[0]); q=0
        u=[F(0) for _ in range(n)]
        u[q]=(-1-s[p])/(s[q]-s[p]); u[p]=1-u[q]
        assert sum(u)==1 and dot(u,s)==-1
        J=[[-eye[i][j]+(s[i]+1)*u[j] for j in range(n)] for i in range(n)]
        N=[[J[i][j]+eye[i][j] for j in range(n)] for i in range(n)]
        assert all(x==0 for row in mm(N,N) for x in row)
        mode='nonconstant'
    C=[[J[i][j]-B[i][j] for j in range(n)] for i in range(n)]
    T=[[F(0) for _ in range(n)] for __ in range(n)]
    # T[i][j] is the coefficient of x_j^2 in the per-capita growth of species i.
    T=[[C[i][j]/(2*z[j]*z[j]) for j in range(n)] for i in range(n)]
    for i in range(n):
        # Evaluate the per-capita polynomial at the prescribed target.
        assert r[i]+dot(S[i],z)+sum((T[i][j]*z[j]*z[j] for j in range(n)),F(0))==0
        for j in range(n):
            # Derivative of actual x-vector field equals a diagonal similarity of J.
            direct=z[i]*(S[i][j]+2*T[i][j]*z[j])
            assert direct==z[i]*J[i][j]/z[j]
    assert [sum(row) for row in J]==s
    if mode=='constant':
        assert s[0]<0
    else:
        assert all(mm([[J[i][j]+eye[i][j] for j in range(n)] for i in range(n)],
                      [[J[i][j]+eye[i][j] for j in range(n)] for i in range(n)])[i][j] == 0
                   for i in range(n) for j in range(n))
    return (J,T,mode),s

def tests():
    rng=Random(20261018)
    count=0; blocked=0; nonconstant=0; constant=0
    for n in range(1,8):
        for _ in range(170):
            r=[F(rng.randint(-4,4),rng.randint(1,4)) for i in range(n)]
            S=[[F(rng.randint(-4,4),rng.randint(1,4)) for j in range(n)] for i in range(n)]
            z=[F(rng.randint(1,5),rng.randint(1,4)) for i in range(n)]
            result,s=construct(r,S,z)
            count+=1
            if result is None:
                blocked+=1
                assert len(set(s))==1 and s[0]>=0
            elif result[2]=='nonconstant': nonconstant+=1
            else: constant+=1
    # Construct explicit impossible and stabilizable examples, using fixed pairwise coefficients.
    negS=[[F(-1),F(0)],[F(0),F(-1)]]
    allowed,s=construct([F(-1),F(-2)],negS,[F(1),F(1)])
    assert s==[F(3),F(5)]
    assert allowed[0]==[[F(11),F(-8)],[F(18),F(-13)]]
    assert allowed[1]==[[F(6),F(-4)],[F(9),F(-6)]]
    excluded,s=construct([F(-1),F(-1)],negS,[F(1),F(1)])
    assert excluded is None and s==[F(3),F(3)]
    # The explicit fourth-order, per-capita cubic rescue for the excluded case:
    # g_i(x_i)=-1-x_i+6*x_i^2-4*x_i^3 has g_i(1)=0 and g_i'(1)=-1.
    assert -1-1+6-4==0
    assert -1+12-12==-1
    print('EXACT_REPLAY_OK', count, 'rational cases;',blocked,'forbidden;',
          nonconstant,'nonconstant stable;',constant,'constant-negative stable; plus sharp examples')

if __name__=='__main__':tests()
