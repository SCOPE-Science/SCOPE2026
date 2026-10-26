#!/usr/bin/env python3
"""Exact rational checker for two-phase cycle last-discovery laws.

Uses an independent absorbing-chain computation that tracks the parity of
absolute time and which neighbors of a candidate last vertex were seen.
Requires only Python 3 standard library.
"""
from fractions import Fraction as F
from collections import deque


def proposed(n, p):
    q = 1-p
    ans = [F(0)]*n
    for k in range(1,n):
        s = n-k
        r = [(1/p if i%2==s%2 else 1/q) for i in range(n)]
        middle = sum(r[1:n-1])
        u = sum(r[s:n-1]) / middle
        ans[k] = u*r[0]/sum(r[:n-1])+(1-u)*r[n-1]/sum(r[1:])
    return ans


def explicit(n,p):
    q=1-p
    z=[F(0)]*n
    if n%2:
        m=(n-1)//2
        for k in range(1,n):z[k]=(q if k%2 else p)/m
    else:
        m=n//2
        a=p/(m-q); b=q/(m-p)
        for k in range(1,n):
            w=(F(k-1,n-2) if k%2 else F(n-k,n-2)-F(2,n-2)*q)
            z[k]=w*a+(1-w)*b
    return z


def solve_linear(A, b):
    n=len(b)
    for j in range(n):
        pivot=next((i for i in range(j,n) if A[i][j]), None)
        assert pivot is not None, ('singular',n,j)
        if pivot!=j:
            A[j],A[pivot]=A[pivot],A[j]
            b[j],b[pivot]=b[pivot],b[j]
        d=A[j][j]
        for t in range(j,n):A[j][t]/=d
        b[j]/=d
        for i in range(j+1,n):
            factor=A[i][j]
            if factor:
                for t in range(j,n):A[i][t]-=factor*A[j][t]
                b[i]-=factor*b[j]
    x=[F(0)]*n
    for i in range(n-1,-1,-1):
        x[i]=b[i]-sum(A[i][j]*x[j] for j in range(i+1,n))
    return x


def independent(n,p,k):
    q=1-p
    neighbors=((k-1)%n,(k+1)%n)
    def update(mask,x):
        if x==neighbors[0]:mask|=1
        if x==neighbors[1]:mask|=2
        return mask
    start=(0,0,update(0,0))
    states=[start]
    loc={start:0}
    transitions=[]
    for st in states:
        x,t,mask=st
        row=[]
        for direction,prob in [(+1,p if t==0 else q),(-1,q if t==0 else p)]:
            y=(x+direction)%n
            if y==k:
                row.append((None,prob,mask==3))
            else:
                nxt=(y,1-t,update(mask,y))
                if nxt not in loc:
                    loc[nxt]=len(states)
                    states.append(nxt)
                row.append((loc[nxt],prob,False))
        transitions.append(row)
    N=len(states)
    A=[[F(int(i==j)) for j in range(N)] for i in range(N)]
    b=[F(0)]*N
    for i,row in enumerate(transitions):
        for dest,prob,success in row:
            if dest is None:
                if success:b[i]+=prob
            else:A[i][dest]-=prob
    return solve_linear(A,b)[0],N


def run():
    cases=0
    total_states=0
    for n in range(3,8):
        for p in (F(1,3),F(2,5),F(3,4)):
            values=proposed(n,p)
            assert values == explicit(n,p), (n,p,values,explicit(n,p))
            assert sum(values)==1
            if n%2:
                m=(n-1)//2
                for k in range(1,n):
                    assert values[k] == ((1-p) if k%2 else p)/m
            else:
                for parity in (0,1):
                    v=[values[k] for k in range(1,n) if k%2==parity]
                    if len(v)>=3:
                        assert len({v[i+2]-2*v[i+1]+v[i] for i in range(len(v)-2)})==1
                        assert v[2]-2*v[1]+v[0]==0
            for k in range(1,n):
                independent_value, states=independent(n,p,k)
                assert independent_value==values[k], (n,p,k,independent_value,values[k])
                cases+=1;total_states+=states
    # Exact parity nonuniformity for odd cycles.
    for n in (3,5,7,11,29):
        p=F(7,10); z=proposed(n,p)
        tv=sum(abs(z[k]-F(1,n-1)) for k in range(1,n))/2
        assert tv==abs(p-F(1,2))
    for m in (10,20,40,80,160):
        z=explicit(2*m,F(7,10))
        tv=sum(abs(z[k]-F(1,2*m-1)) for k in range(1,2*m))/2
        assert abs(tv-F(1,10))<F(1,m)
    print('PASS',cases,'independent exact-rational absorbing-chain comparisons;',
          total_states,'states solved; odd-cycle total-variation identities PASS')

if __name__=='__main__':run()
