#!/usr/bin/env python3
"""Exact independent enumerator for conditional edge moments in K_(3,n).
Usage: python verify_connected_k3n.py
"""
from fractions import Fraction
from itertools import product


def connected(n, mask):
    parent=list(range(n+3))
    def root(x):
        while parent[x]!=x:
            x=parent[x]
        return x
    for j in range(n):
        for i in range(3):
            if mask & (1<<(3*j+i)):
                parent[root(i)]=root(j+3)
    return len({root(v) for v in range(n+3)})==1


def predicted(n,t):
    x=1+t
    f=x*x+x+1
    g=x+2
    h=3
    P=f**n-3*g**n+2*h**n
    E=x*x*f**(n-1)-(2*x+1)*g**(n-1)+2*h**(n-1)
    Cc=t*(x*f**(n-1)-g**(n-1))
    Cr=x**4*f**(n-2)-(1+2*x*x)*g**(n-2)+2*h**(n-2)
    Cd=x**4*f**(n-2)-x*(x+2)*g**(n-2)+2*h**(n-2)
    return P,E,Cc,Cr,Cd


def independent_enumeration(n,t):
    Z=E=Cc=Cr=Cd=0
    for mask in range(1<<(3*n)):
        if not connected(n,mask):
            continue
        v=t**mask.bit_count()
        Z+=v
        a=bool(mask&1)
        if a:
            E+=v
            if mask&2: Cc+=v      # (1,0) same column
            if mask&8: Cr+=v      # (0,1) same left vertex
            if mask&16: Cd+=v     # (1,1) vertex disjoint
    return Z,E,Cc,Cr,Cd


def check():
    count=0
    for n in range(2,6):
        for t in (1,2,3):
            actual=independent_enumeration(n,t)
            expected=tuple(t**n*a for a in predicted(n,t))
            assert actual==expected,(n,t,actual,expected)
            count+=5
            P,E,Cc,Cr,Cd=predicted(n,t)
            assert P>0 and 0<E<P
            assert all(P*C-E*E<0 for C in (Cc,Cr,Cd)), (n,t)
            count+=5
    # The analytic Rayleigh difference factorization and Bernoulli comparison
    # are checked at many exact integer parameter values, not used as proof.
    for n in range(2,52):
        k=n-2
        for t in (1,2,3,5,10,100):
            x=t+1; f=x*x+x+1; g=x+2; h=3
            P,E,Cc,Cr,Cd=predicted(n,t)
            delta=P*Cd-E*E
            A=x*g*(2*x+1)
            B=2*(2*x+1)**2
            C=g*g
            rhs=t*t*(f**k*g**k)*(-A*f**0*g**0+B*Fraction(h,g)**k-C*Fraction(g,f)**k)
            assert delta==rhs,(n,t,delta,rhs)
            assert all(P*Cj-E*E<0 for Cj in (Cc,Cr,Cd))
            count+=4
    print(f'PASS: {count} exact assertions; direct connected-graph enumeration on K_(3,n), 2<=n<=5.')

if __name__=='__main__':
    check()
