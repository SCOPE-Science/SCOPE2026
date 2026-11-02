"""Direct enumerator for independent dominating sets of two-token bicliques."""
from itertools import combinations
from math import comb
from collections import Counter
import networkx as nx


def theoretical(m,n):
    out=Counter({comb(m,2)+comb(n,2):1})
    for s in range(m):
        if s==1: continue
        for t in range(n):
            if t==1: continue
            out[comb(s,2)+comb(t,2)+(m-s)*(n-t)] += comb(m,s)*comb(n,t)
    return out


def token_graph(m,n):
    vertices=list(combinations(range(m+n),2))
    g=nx.Graph()
    g.add_nodes_from(vertices)
    for a,b in combinations(vertices,2):
        common=set(a)&set(b)
        if len(common)!=1: continue
        u=next(iter(set(a)-common));v=next(iter(set(b)-common))
        if (u<m)!=(v<m):g.add_edge(a,b)
    return g


def predicted_min(m,n):
    a,b=sorted((m,n),reverse=True)
    if a==b==2: return 2
    if b==2:return 2*a-3
    return a+comb(b-1,2)-1


def check(m,n):
    g=token_graph(m,n)
    size_hist=Counter(map(len,nx.find_cliques(nx.complement(g))))
    exp=theoretical(m,n)
    assert size_hist==exp,(m,n,size_hist,exp)
    assert min(size_hist)==predicted_min(m,n)
    p=comb(m,2)+comb(n,2);q=m*n
    assert max(size_hist)==max(p,q)
    assert size_hist[max(p,q)] == (2 if p==q else 1)
    assert sum(size_hist.values())==1+(2**m-m-1)*(2**n-n-1)
    print(f'PRIMARY_OK m={m} n={n} maximal={sum(size_hist.values())} min={min(size_hist)} max={max(size_hist)} top={size_hist[max(size_hist)]} histogram={dict(sorted(size_hist.items()))}')


if __name__=='__main__':
    for pair in [(2,2),(2,3),(2,5),(3,3),(3,4),(3,5),(3,6),(4,4),(4,5),(5,5),(3,6)]:
        check(*pair)
    print('PRIMARY_COMPLETE_OK')
