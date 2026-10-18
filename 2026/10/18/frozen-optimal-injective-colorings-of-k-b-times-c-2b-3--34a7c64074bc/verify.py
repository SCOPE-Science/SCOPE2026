"""Independent finite checks of injective-colouring rigidity in cyclic complete direct products.

No third-party modules. Computes both canonical-independent-support witnesses
and palette transfer closed-walk counts, never interpreting finite tests as proof.
"""
from collections import Counter
from itertools import combinations
from math import factorial, comb


def independent_subsets(n, k):
    for ss in combinations(range(n), k):
        s = set(ss)
        if all((v+1) % n not in s for v in s):
            yield s


def full_support_check(b):
    n, q = 2*b+3, 2*b+1
    maximum = list(independent_subsets(n, b+1))
    assert len(maximum) == n
    by_edge = {}
    for s in maximum:
        uncovered = [e for e in range(n) if not ({e,(e+1)%n} & s)]
        assert len(uncovered)==1
        by_edge[uncovered[0]]=s
    assert len(by_edge)==n
    groups=Counter()
    for deficient in independent_subsets(n,b):
        missing = [e for e in range(n) if not ({e,(e+1)%n} & deficient)]
        assert len(missing)==3
        supports = [deficient]+[by_edge[e] for e in range(n) if e not in missing]
        assert len(supports)==q
        palettes = [set(j for j,s in enumerate(supports) if t in s) for t in range(n)]
        assert all(len(p)==b for p in palettes)
        assert all(not (palettes[t]&palettes[(t+1)%n]) for t in range(n))
        # Count literal allowable new colours for every one of the b labelled vertices at each layer.
        nrecolours=0
        for t in range(n):
            options = set(range(q)) - palettes[t-1] - palettes[t] - palettes[(t+1)%n]
            nrecolours += b*len(options)
        gap_excess=[]
        cyc=sorted(deficient)
        for i,t in enumerate(cyc):
            next_t=cyc[(i+1)%b]+(n if i==b-1 else 0)
            gap_excess.append(next_t-t-2)
        expected=b*sum(max(0,x-1) for x in gap_excess)
        assert nrecolours==expected,(b,cyc,expected,nrecolours)
        groups[nrecolours] += 1
    want={2*b:n,b:n*(b-1),0:n*(b-1)*(b-2)//6}
    assert groups==want,(b,groups,want)
    assert sum(groups.values())==n*(b+1)*(b+2)//6
    return dict(sorted(groups.items())), factorial(q)*factorial(b)**n*groups[0]


def transfer_closed_walk_count(b):
    n,q=2*b+3,2*b+1
    # Palette indices are q-bit masks of size b. Adjacent cycle palettes must be disjoint.
    masks=[sum(1<<x for x in sub) for sub in combinations(range(q),b)]
    adj=[[j for j,t in enumerate(masks) if s&t==0] for s in masks]
    walks=0
    for first in range(len(masks)):
        curr={first:1}
        for _ in range(n-1):
            nxt={}
            for i,ways in curr.items():
                for j in adj[i]:
                    nxt[j]=nxt.get(j,0)+ways
            curr=nxt
        walks+=sum(curr.get(last,0) for last in adj[first])
    assert walks==factorial(q)*n*(b+1)*(b+2)//6, (b,walks)
    return walks


def common_neighbor_graph_check(b):
    n=2*b+3
    vertex=[(a,i) for i in range(n) for a in range(b)]
    ns={(a,i):{(c,(i+di)%n) for di in (-1,1) for c in range(b) if c!=a} for a,i in vertex}
    for a,i in vertex:
        for z,j in vertex:
            if (a,i)==(z,j):continue
            common=bool(ns[(a,i)] & ns[(z,j)])
            predicted= i==j or (j-i)%n in (2,n-2)
            assert common==predicted,(b,(a,i),(z,j),common,predicted)
    return True


if __name__=='__main__':
    for b in range(3,9):
        d,f=full_support_check(b)
        print('b',b,'n',2*b+3,'canonical degree histogram',d,'frozen fully labelled',f)
    for b in (3,4):
        print('b',b,'independent transfer count',transfer_closed_walk_count(b),'common-neighbor test',common_neighbor_graph_check(b))
    print('ALL_CHECKS_PASSED')
