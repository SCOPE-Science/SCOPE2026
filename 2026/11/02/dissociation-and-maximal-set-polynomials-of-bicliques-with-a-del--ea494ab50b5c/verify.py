"""Exact independent checks of induced-degree-one (dissociation) enumerators.

Usage: python verify.py
No external packages; all graph checks use adjacency rather than theorem cases.
"""
from itertools import combinations
from math import comb


def graph(m, n, t):
    edges = []
    for i in range(m):
        for j in range(n):
            if i != j or i >= t:
                edges.append((i, m+j))
    return edges


def brute(m, n, t):
    vertices=m+n
    neigh=[0]*vertices
    for a,b in graph(m,n,t):
        neigh[a]|=1<<b
        neigh[b]|=1<<a
    diss=[False]*(1<<vertices)
    diss[0]=True
    all_count=[0]*(vertices+1)
    maximal_count=[0]*(vertices+1)
    for mask in range(1<<vertices):
        good=all((neigh[v]&mask).bit_count()<=1
                 for v in range(vertices) if mask>>v&1)
        diss[mask]=good
        if good:all_count[mask.bit_count()]+=1
    for mask, good in enumerate(diss):
        if good and all(not diss[mask|1<<v] for v in range(vertices) if not mask>>v&1):
            maximal_count[mask.bit_count()]+=1
    return all_count,maximal_count


def expected(m,n,t):
    all_count=[0]*(m+n+1)
    maximal_count=[0]*(m+n+1)
    for i in range(m+1):all_count[i]+=comb(m,i)
    for i in range(n+1):all_count[i]+=comb(n,i)
    all_count[0]-=1
    all_count[2]+=m*n
    all_count[3]+=t*(m+n-2)
    all_count[4]+=comb(t,2)
    maximal_count[m]+=1
    maximal_count[n]+=1
    maximal_count[2]+=(m-t)*(n-t)
    maximal_count[3]+=t*(m+n-2*t)
    maximal_count[4]+=comb(t,2)
    return all_count,maximal_count


def main():
    total=0
    for m in range(3,8):
        for n in range(3,8):
            for t in range(min(m,n)+1):
                a,b=brute(m,n,t)
                x,y=expected(m,n,t)
                assert a==x,(m,n,t,'all',a,x)
                assert b==y,(m,n,t,'maximal',b,y)
                # The only well-dissociated case in the tested domain.
                supported=[i for i,v in enumerate(b) if v]
                assert (len(supported)==1)==(m==n==t==4),(m,n,t,supported)
                total+=1
    print('VERIFY_OK',total,'graph parameter triples; all subsets checked')

if __name__=='__main__':main()
