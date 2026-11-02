#!/usr/bin/env python3
"""Exact 3- and 4-round FO types for finite Latin-square incidence graphs.

No external packages. Equality and symmetric adjacency are the entire signature.
The recursive 'one-point extension set' is the exact Ehrenfeucht--Fraisse
backward-induction type, not a graph-heuristic fingerprint.
"""
from itertools import permutations


def build(order, product):
    n=order
    cells=[(i,j,product(i,j)) for i in range(n) for j in range(n)]
    assert all(sorted(product(i,j) for j in range(n))==list(range(n)) for i in range(n))
    assert all(sorted(product(i,j) for i in range(n))==list(range(n)) for j in range(n))
    N=3*n+n*n
    G=[[0]*N for _ in range(N)]
    for k,(i,j,v) in enumerate(cells):
        b=3*n+k
        for p in (i,n+j,2*n+v):G[b][p]=G[p][b]=1
    return G


def atomic(G,points):
    out=0
    for i in range(len(points)):
        for j in range(i+1,len(points)):
            a,b=points[i],points[j]
            out=3*out+(0 if a==b else 1 if G[a][b] else 2)
    return out


def rank_type(G,r,pools):
    """Type after r rounds using complete extension sets at all prefixes."""
    N=len(G)
    def intern(table,values):
        t=frozenset(values)
        if t not in table:table[t]=len(table)
        return table[t]
    if r==3:
        one,two=pools
        B={(a,b):intern(one,(atomic(G,(a,b,c)) for c in range(N)))
           for a in range(N) for b in range(N)}
        A={a:intern(two,(B[a,b] for b in range(N))) for a in range(N)}
        return frozenset(A.values())
    assert r==4
    one,two,three=pools
    C={(a,b,c):intern(one,(atomic(G,(a,b,c,d)) for d in range(N)))
       for a in range(N) for b in range(N) for c in range(N)}
    B={(a,b):intern(two,(C[a,b,c] for c in range(N)))
       for a in range(N) for b in range(N)}
    A={a:intern(three,(B[a,b] for b in range(N))) for a in range(N)}
    return frozenset(A.values())


def main():
    s3=list(permutations(range(3)))
    inv={a:i for i,a in enumerate(s3)}
    def s3op(a,b):return inv[tuple(s3[a][s3[b][i]] for i in range(3))]
    names=[('order2',2,lambda a,b:(a+b)%2),
           ('order3',3,lambda a,b:(a+b)%3),
           ('cyclic4',4,lambda a,b:(a+b)%4),
           ('klein4',4,lambda a,b:a^b),
           ('cyclic5',5,lambda a,b:(a+b)%5)]
    pools3=[{},{}];pools4=[{},{},{}]
    out=[]
    for label,n,op in names:
        G=build(n,op)
        a=rank_type(G,3,pools3)
        b=rank_type(G,4,pools4)
        out.append((label,n,len(G),a,b))
    assert len({x[3] for x in out})==1
    assert out[0][4]!=out[1][4]
    assert out[1][4]!=out[2][4]
    assert out[0][4]!=out[2][4]
    assert all(x[4]==out[2][4] for x in out[2:])
    for label,n,N,a,b in out:
        group='2' if n==2 else '3' if n==3 else '4plus'
        print(f'{label}: n={n}, vertices={N}, rank3=common, rank4={group}')
    print('PASS: rank3 common; rank4 categories 2,3,4plus; sharp sizes 10,18,28')

if __name__=='__main__':main()
