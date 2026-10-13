#!/usr/bin/env python3
"""Exact rational check of two-site exclusion current identities (Python stdlib)."""
from fractions import Fraction as F
from itertools import product

def solve_linear(matrix, rhs):
    n=len(rhs)
    A=[[F(z) for z in row]+[F(rhs[i])] for i,row in enumerate(matrix)]
    for i in range(n):
        q=next(j for j in range(i,n) if A[j][i])
        A[i],A[q]=A[q],A[i]
        t=A[i][i]
        A[i]=[z/t for z in A[i]]
        for j in range(n):
            if j!=i:
                t=A[j][i]
                A[j]=[x-t*y for x,y in zip(A[j],A[i])]
    return [row[-1] for row in A]

def stationary(a,b,k,u,v):
    states=[(0,0),(1,0),(0,1),(1,1)]
    Q=[[F(0) for _ in states] for _ in states]
    def transition(src,dst,rate):
        Q[dst][src]+=rate;Q[src][src]-=rate
    for i,(x,y) in enumerate(states):
        transition(i,states.index((1-x,y)),k*u if not x else a*(1-u))
        transition(i,states.index((x,1-y)),k*v if not y else b*(1-v))
        if (x,y)==(1,0):transition(i,2,a)
        if (x,y)==(0,1):transition(i,1,b)
    Q[-1]=[F(1) for _ in states]
    pi=solve_linear(Q,[0,0,0,1])
    assert sum(pi)==1 and all(z>=0 for z in pi)
    return a*pi[1]-b*pi[2]

def exact(a,b,k,u,v):
    L=a*(1-u)+k*u; R=b*(1-v)+k*v; S=L+R
    D=S*(L*R+a*R+b*L)+(a-b)*k*(u*L-v*R)
    assert D>0
    return a*b*k*(u-v)*S/D,D

def assert_all():
    rates=[F(1,3),F(1),F(3,2),F(3)]
    p=[F(0),F(1,4),F(1,2),F(3,4),F(1)]
    runs=0; asym=0
    for a,b,k,u,v in product(rates,rates,rates,p,p):
        exactj,D=exact(a,b,k,u,v)
        assert exactj==stationary(a,b,k,u,v)
        swapped,Dt=exact(a,b,k,v,u)
        P=(a-b)**2*(1-u)*(1-v)+2*a*b*(2-u-v)+k*(a+b)*(u+v)
        even=a*b*k*k*(a-b)*(u-v)**2*P/(D*Dt)
        assert exactj+swapped==even
        assert (exactj>0)==(u>v)
        assert (exactj<0)==(u<v)
        if a!=b and u!=v:
            assert (even>0)==(a>b)
            asym+=1
        else: assert even==0
        runs+=1
    a,b,k,u,v=F(2),F(1),F(1),F(3,4),F(1,4)
    print('CHECK_OK', 'stationary_chain_cases',runs,'nonzero_rectification_cases',asym,
          'example_current',exact(a,b,k,u,v)[0],
          'example_reverse',exact(a,b,k,v,u)[0])

if __name__=='__main__':assert_all()
