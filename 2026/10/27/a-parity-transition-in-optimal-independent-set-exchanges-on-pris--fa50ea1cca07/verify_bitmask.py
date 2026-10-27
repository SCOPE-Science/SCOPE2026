"""Exhaustive independent-set/token-jump check for prism graphs, n=3,...,10.

Vertices are numbered 0,...,n-1 in layer zero and n,...,2n-1 in layer one.
The program uses bit masks, set intersections, and breadth-first component tests.
"""
from itertools import combinations
from collections import deque


def independent_sets(n,k):
    N=2*n
    edge_masks=[]
    for i in range(n):
        j=(i+1)%n
        for a,b in [(i,j),(n+i,n+j),(i,n+i)]:
            edge_masks.append((1<<a)|(1<<b))
    result=[]
    for comb in combinations(range(N),k):
        m=sum(1<<j for j in comb)
        if all((m&e)!=e for e in edge_masks):
            result.append(m)
    return result


def components(states,k):
    adj=[set() for _ in states]
    for i in range(len(states)):
        for j in range(i+1,len(states)):
            if ((states[i]^states[j]).bit_count()==2):
                adj[i].add(j); adj[j].add(i)
    groups=[]; seen=set()
    for i in range(len(states)):
        if i in seen: continue
        q=[i]; seen.add(i); group=[]
        while q:
            u=q.pop();group.append(u)
            for v in adj[u]:
                if v not in seen:seen.add(v);q.append(v)
        groups.append(group)
    return adj, sorted([len(g) for g in groups]), sum(map(len,adj))//2


def main():
    for n in range(3,11):
        kmax=n if n%2==0 else n-1
        maximal=independent_sets(n,kmax)
        assert len(maximal)==(2 if n%2==0 else 2*n)
        # The one-per-column restriction gives an upper bound of n.
        if n%2: assert len(independent_sets(n,n))==0
        adj, sizes, edges=components(maximal,kmax)
        if n%2:
            assert sizes==[2*n] and edges==2*n
            assert all(len(v)==2 for v in adj)
        else:
            assert sizes==[1,1] and edges==0
            one_less=independent_sets(n,n-1)
            a,s,e=components(one_less,n-1)
            assert len(one_less)==2*n and s==[n,n]
            assert e==n*(n-1) and all(len(v)==n-1 for v in a)
        states=independent_sets(n,n-2)
        a,s,e=components(states,n-2)
        assert len(states)==2*n*(n-2) and s==[2*n*(n-2)]
        print('n=%d alpha=%d maxima=%d maximal_exchange_edges=%d near2=%d near2_exchange_edges=%d near2_components=%d' %
              (n,kmax,len(maximal),edges,len(states),e,len(s)))

if __name__=='__main__':main()
