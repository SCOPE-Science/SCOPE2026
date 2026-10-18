#!/usr/bin/env python3
"""Algebraic and independent breadth-first checks of geodesic signatures."""
from collections import deque
from math import comb

def key(n,a,b):
    a,b=sorted((a,b));return a,b

def signature(n,a,b):
    h=n//2;d=a+b
    predecessor=int(a>0)+int(b>0)
    paths=comb(d,a)
    if n%2==0:
        if a==h:predecessor+=1;paths*=2
        if b==h:predecessor+=1;paths*=2
    return (d,predecessor,paths)

def direct(n):
    adj=[[] for _ in range(n*n)]
    for x in range(n):
        for y in range(n):
            v=x*n+y
            for z in [((x+1)%n)*n+y,((x-1)%n)*n+y,x*n+(y+1)%n,x*n+(y-1)%n]:adj[v].append(z)
    distances=[-1]*(n*n);counts=[0]*(n*n)
    distances[0]=0;counts[0]=1;q=deque([0])
    while q:
        v=q.popleft()
        for w in adj[v]:
            if distances[w]<0:distances[w]=distances[v]+1;q.append(w)
            if distances[w]==distances[v]+1:counts[w]+=counts[v]
    for v in range(n*n):
        x,y=divmod(v,n)
        a,b=min(x,n-x),min(y,n-y)
        pred=sum(distances[w]==distances[v]-1 for w in adj[v])
        assert signature(n,a,b)==(distances[v],pred,counts[v]),(n,v,signature(n,a,b),(distances[v],pred,counts[v]))
    return n*n

def main():
    order_checks=0
    for n in range(5,501):
        h=n//2
        observed={}
        for a in range(h+1):
            for b in range(a,h+1):
                s=signature(n,a,b)
                assert s not in observed,(n,observed[s],(a,b),s)
                observed[s]=(a,b)
        order_checks+=1
    tested=sum(direct(n) for n in range(5,31))
    print('PASS algebraic signature injectivity: 496 orders n=5..500')
    print('PASS independent BFS geodesic and predecessor counts: %d vertices, n=5..30' % tested)
if __name__=='__main__':main()
