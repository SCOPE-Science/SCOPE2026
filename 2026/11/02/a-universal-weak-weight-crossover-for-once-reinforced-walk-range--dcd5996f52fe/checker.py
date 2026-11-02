#!/usr/bin/env python3
"""Exact finite-state and transform checks for a vanishing-weight once-reinforced walk."""
from fractions import Fraction as F
from collections import defaultdict
from math import acosh, exp, log, sqrt, tanh, isclose, erf


def evolve_direct(n, c, half):
    mass = {(0, 0) if half else (0, 0, 0): F(1)}
    for _ in range(n):
        nxt = defaultdict(F)
        for st, weight in mass.items():
            if half:
                x, hi = st
                if x == 0:
                    next_states = [(1, F(1))]
                elif x == hi:
                    next_states = [(x+1, 1/(1+c)), (x-1, c/(1+c))]
                else:
                    next_states = [(x+1, F(1,2)), (x-1, F(1,2))]
                for y, pr in next_states:
                    nxt[(y, max(hi,y))] += weight*pr
            else:
                x, lo, hi = st
                if lo == hi:
                    next_states = [(x+1,F(1,2)), (x-1,F(1,2))]
                elif x == lo:
                    next_states = [(x-1,1/(1+c)), (x+1,c/(1+c))]
                elif x == hi:
                    next_states = [(x+1,1/(1+c)), (x-1,c/(1+c))]
                else:
                    next_states = [(x+1,F(1,2)), (x-1,F(1,2))]
                for y,pr in next_states:
                    nxt[(y,min(lo,y),max(hi,y))] += weight*pr
        mass = dict(nxt)
        assert sum(mass.values()) == 1
    out=defaultdict(F)
    for st,weight in mass.items():
        k=st[1] if half else st[2]-st[1]
        out[k]+=weight
    return dict(out)


def time_increment_pmf(i, c, half, max_time):
    active={i:F(1)}
    exit_mass=defaultdict(F)
    for t in range(1,max_time+1):
        nxt=defaultdict(F)
        for x,w in active.items():
            if x == i:
                exit_mass[t]+=w/(1+c)
                nxt[x-1]+=w*c/(1+c)
            elif x == 0:
                if half:
                    nxt[1]+=w
                else:
                    exit_mass[t]+=w/(1+c)
                    nxt[1]+=w*c/(1+c)
            else:
                nxt[x-1]+=w/2
                nxt[x+1]+=w/2
        active=dict(nxt)
    assert sum(exit_mass.values())+sum(active.values())==1
    return dict(exit_mass)


def convolution(a,b,tmax):
    z=defaultdict(F)
    for i,x in a.items():
        for j,y in b.items():
            if i+j<=tmax:z[i+j]+=x*y
    return dict(z)


def solve_linear(a,b):
    n=len(b);m=[list(a[i])+[b[i]] for i in range(n)]
    for col in range(n):
        piv=next(k for k in range(col,n) if m[k][col])
        m[col],m[piv]=m[piv],m[col]
        d=m[col][col]
        m[col]=[v/d for v in m[col]]
        for row in range(n):
            if row!=col:
                d=m[row][col]
                if d:m[row]=[m[row][k]-d*m[col][k] for k in range(n+1)]
    return [row[-1] for row in m]


def discrete_discounted_increment(i,c,q,half):
    a=[[F(int(j==k)) for k in range(i+1)] for j in range(i+1)]
    b=[F(0)]*(i+1)
    for j in range(i+1):
        if j==i:
            a[j][i-1]-=q*c/(1+c)
            b[j]=q/(1+c)
        elif j==0:
            if half:
                a[0][1]-=q
            else:
                a[0][1]-=q*c/(1+c)
                b[0]=q/(1+c)
        else:
            a[j][j-1]-=q/2
            a[j][j+1]-=q/2
    return solve_linear(a,b)[i]


def discounted_ruin(i,q,half):
    # g_j = E_j[q^tau], tau first hitting i (reflected) or {0,i} (full)
    a=[[F(int(j==k)) for k in range(i+1)] for j in range(i+1)]
    b=[F(0)]*(i+1)
    for j in range(i+1):
        if j==i or (j==0 and not half):
            b[j]=F(1)
        elif j==0:
            a[0][1]-=q
        else:
            a[j][j-1]-=q/2
            a[j][j+1]-=q/2
    return solve_linear(a,b)[i-1]


def log_inverse_transform(m,c,half,s,n):
    theta=acosh(exp(s/n))
    fac=c*tanh(theta)
    coeff=1 if half else .5
    return -s*m/n - sum(log(1+fac*tanh(coeff*i*theta)) for i in range(1,m))


def run():
    checks=0
    # Independent direct-state versus independent record-holding-time calculations.
    for half in (False,True):
        for c in (F(1,5),F(1,2),F(1),F(3,2)):
            for n in range(1,11):
                direct=evolve_direct(n,c,half)
                sdist={1:F(1)}
                for k in range(1,n+1):
                    if k>1:
                        sdist=convolution(sdist,time_increment_pmf(k-1,c,half,n),n)
                    observed=sum(p for size,p in direct.items() if size>=k)
                    obtained=sum(p for time,p in sdist.items() if time<=n)
                    assert observed==obtained, (half,c,n,k,observed,obtained)
                    checks+=1
    # Exact rational resolvent independently checked against renewal excursion factor.
    for half in (False,True):
        for c in (F(1,5),F(1),F(5,3)):
            for q in (F(1,3),F(2,3),F(3,4)):
                for i in range(1,9):
                    f=discrete_discounted_increment(i,c,q,half)
                    g=discounted_ruin(i,q,half)
                    rhs=q/(1+c*(1-q*g))
                    assert f==rhs,(half,c,q,i,f,rhs)
                    checks+=1
    # Critical scaling: exact generating product approaches the drift-plus-Levy Laplace law.
    numeric=[]
    for half in (False,True):
        for gamma in (0.25,1.0,2.0):
            for s in (0.5,1.0,2.0):
                r=0.6
                errors=[]
                for n in (400,1600,6400):
                    c=gamma/sqrt(n)
                    obs=log_inverse_transform(int(r*n),c,half,s,n)
                    limit=-r*(s+gamma*sqrt(2*s))
                    errors.append(abs(obs-limit))
                assert errors[2] < errors[0],(half,gamma,s,errors)
                numeric.append((half,gamma,s,errors[0],errors[-1]))
                checks+=1
    # Supercritical vanishing reinforcement, Brownian 1/2-stable hitting-time transform.
    for half in (False,True):
        for s in (0.5,1,2):
            r=0.7
            errors=[]
            for n in (2500,10000,40000):
                c=n**(-0.17)
                m=round(r*sqrt(n)/c)
                obs=log_inverse_transform(m,c,half,s,n)
                limit=-r*sqrt(2*s)
                errors.append(abs(obs-limit))
            assert errors[-1] < errors[0],(half,s,errors)
            checks+=1
    print('PASS finite-state, exact-rational and asymptotic numerical checks:',checks)
    print('Critical convergence examples (half, gamma, s, error n=400, error n=6400):')
    for row in numeric[:6]:print(row)
    print('Limit at gamma=1, r=1/2:',erf(0.5/sqrt(1.0)))

if __name__=='__main__':run()
