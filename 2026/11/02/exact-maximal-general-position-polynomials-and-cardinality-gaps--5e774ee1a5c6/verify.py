#!/usr/bin/env python3
"""Independent exhaustive checks of terminal general-position enumerators.

No external packages. The defining shortest-path condition is evaluated from
BFS distances in the original graph; combinatorial counts are computed via an
unrelated labeled-block recurrence.
"""
from collections import Counter,deque
from math import comb, factorial

def onto_at_least_two(n,k):
    if not k:return int(n==0)
    # distribute n labeled objects among k labeled nonempty boxes with >=2
    dp=[0]*(n+1);dp[0]=1
    for _ in range(k):
        next_dp=[0]*(n+1)
        for used,v in enumerate(dp):
            if v:
                for q in range(2,n-used+1):
                    next_dp[used+q]+=v*comb(n-used,q)
        dp=next_dp
    return dp[n]

def formula(m,n):
    counts=Counter()
    for a in range(m+1):
        for b in range(n+1):
            for c in range(min(m-a,n-b)+1):
                # a row-centered stars, b column-centered stars,
                # c isolated edges, all m+n incidence vertices used
                ways=(comb(m,a)*comb(m-a,c)*comb(n,b)*comb(n-b,c)
                    *factorial(c)*onto_at_least_two(m-a-c,b)
                    *onto_at_least_two(n-b-c,a))
                if ways:counts[m+n-a-b-c]+=ways
    # all columns used, some rows unused; row-centered stars only
    for a in range(1,m):
        counts[n]+=comb(m,a)*onto_at_least_two(n,a)
    # all rows used, some columns unused; column-centered stars only
    for b in range(1,n):
        counts[m]+=comb(n,b)*onto_at_least_two(m,b)
    return +counts

def brute_from_graph_distances(m,n):
    vertices=[(i,j) for i in range(m) for j in range(n)]
    N=len(vertices)
    neighbors=[[v for v,(r,c) in enumerate(vertices)
                if u!=v and (r==i or c==j)] for u,(i,j) in enumerate(vertices)]
    d=[]
    for s in range(N):
        ds=[N+1]*N;ds[s]=0;queue=deque([s])
        while queue:
            u=queue.popleft()
            for v in neighbors[u]:
                if ds[v]>ds[u]+1:ds[v]=ds[u]+1;queue.append(v)
        d.append(ds)
    forbidden=set()
    for i in range(N):
        for j in range(i+1,N):
            for k in range(j+1,N):
                if (d[i][j]+d[j][k]==d[i][k]
                    or d[i][k]+d[k][j]==d[i][j]
                    or d[j][i]+d[i][k]==d[j][k]):
                    forbidden.add((1<<i)|(1<<j)|(1<<k))
    incident=[[] for _ in range(N)]
    for t in forbidden:
        for i in range(N):
            if t>>i & 1:incident[i].append(t)
    total=1<<N
    admissible=bytearray(total);admissible[0]=1
    for mask in range(1,total):
        b=mask&-mask; i=b.bit_length()-1
        remaining=mask^b
        if admissible[remaining] and not any(mask&t==t for t in incident[i]):
            admissible[mask]=1
    out=Counter()
    full=total-1
    for mask in range(total):
        if not admissible[mask]:continue
        unchosen=full^mask
        maximal=True
        while unchosen:
            b=unchosen&-unchosen; unchosen^=b
            if admissible[mask|b]: maximal=False;break
        if maximal:out[mask.bit_count()]+=1
    return +out,len(forbidden),total

def main():
    tested=0
    for m,n in [(2,2),(2,3),(2,4),(2,5),(3,3),(3,4),(3,5),(4,4),(4,5)]:
        observed,ntriples,masks=brute_from_graph_distances(m,n)
        expected=formula(m,n)
        assert observed==expected,(m,n,observed,expected)
        print('OK',m,n,'masks',masks,'geodesic triples',ntriples,'maximal',dict(sorted(observed.items())))
        tested+=masks
    print('VERIFIED',tested,'subsets against exact formulas and shortest-path predicate')
if __name__=='__main__':main()
