#!/usr/bin/env python3
"""Exact finite-state checks for geometric resetting on reflected paths.

Requires only the Python standard library. It is a finite test, not a proof
of the all-size theorem or of asymptotic estimates.
"""
from fractions import Fraction as Q
from math import factorial, cosh, acosh


def cheb(l, x):
    a, b = Q(1), x
    if l == 0:
        return a
    for _ in range(1, l):
        a, b = b, 2*x*b-a
    return b


def formula(l, r):
    if r == 0:
        return Q(5*l*l)
    z = cheb(l, 1/(1-r))
    return (3*z - 1 - 2/z)/r


def solve(A, b):
    n=len(b)
    for i in range(n):
        v=next(k for k in range(i,n) if A[k][i])
        if v!=i:
            A[i],A[v]=A[v],A[i]
            b[i],b[v]=b[v],b[i]
        fac=A[i][i]
        for j in range(i,n):
            A[i][j]/=fac
        b[i]/=fac
        for k in range(i+1,n):
            w=A[k][i]
            if not w:
                continue
            for j in range(i,n):
                A[k][j]-=w*A[i][j]
            b[k]-=w*b[i]
    x=[Q(0)]*n
    for i in range(n-1,-1,-1):
        x[i]=b[i]-sum(A[i][j]*x[j] for j in range(i+1,n))
    return x


def state_solve(l,r):
    # (location, mask of boundary vertices reached); both => absorbed.
    start=(0,0)
    queue=[start]
    states=[start]
    transitions={}
    while queue:
        x,mask=queue.pop()
        step={}
        if r:
            step[(0,mask)]=step.get((0,mask),Q(0))+r
        neighbors=([-l+1] if x==-l else ([l-1] if x==l else [x-1,x+1]))
        for y in neighbors:
            nmask=mask | (1 if y==-l else 0) | (2 if y==l else 0)
            if nmask==3:
                continue
            key=(y,nmask)
            step[key]=step.get(key,Q(0))+(1-r)/len(neighbors)
        transitions[(x,mask)]=step
        for v in step:
            if v not in states:
                states.append(v)
                queue.append(v)
    pos={s:i for i,s in enumerate(states)}
    n=len(states)
    A=[[Q(int(i==j)) for j in range(n)] for i in range(n)]
    for s,row in transitions.items():
        for t,p in row.items():
            A[pos[s]][pos[t]]-=p
    b=[Q(1) for _ in states]
    return solve(A,b)[pos[start]],n


def check():
    count=0
    for l in range(1,6):
        for r in (Q(0),Q(1,7),Q(1,4),Q(1,2)):
            actual,n=state_solve(l,r)
            expected=formula(l,r)
            assert actual==expected,(l,r,actual,expected)
            count+=1
    for l in range(1,18):
        a=[Q(0)]*(l+1)
        a[0]=Q(1)
        for j in range(1,l+1):
            a[j]=Q(2**j *l*factorial(l+j-1), factorial(l-j)*factorial(2*j))
        for u in (Q(0),Q(1,7),Q(3,5),Q(7,2)):
            actual=sum(a[j]*u**j for j in range(l+1))
            assert actual==cheb(l,1+u),(l,u)
            count+=1
        assert all(v>0 for v in a)
        count+=1
    # Coefficient of u at zero is also coefficient of r at zero.
    for l in range(1,18):
        a=Q(l*l)
        b=a*(a-1)/6
        derivative=5*a+5*b-2*a*a
        assert derivative==a*(25-7*a)/6
        count+=1
    # Diffusive correction is checked numerically, at a nonoptimal
    # positive rate, independently of finite-state tests above.
    alpha=0.8
    t=(2*alpha)**0.5
    z=cosh(t)
    f=(3*z-1-2/z)/alpha
    h=5*t*(3+2/z**2)*__import__('math').sinh(t)/12
    for l in (80,120,200):
        r=alpha/l**2
        k=acosh(1/(1-r))
        zz=cosh(l*k)
        actual=(3*zz-1-2/zz)/r
        assert abs((actual-l*l*f)-h) < 90/l**2
        count+=1
    print('PASS: %d checks; 20 independent finite-state mean comparisons plus polynomial and asymptotic checks' %count)


if __name__=='__main__':
    check()
