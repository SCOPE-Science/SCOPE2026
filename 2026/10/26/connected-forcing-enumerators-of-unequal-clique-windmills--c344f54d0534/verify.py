"""Self-contained exhaustive checks for connected k-forcing sets in clique bouquets.
Usage: python verify.py
Requires Python standard library only.
"""
from itertools import product
from math import comb


def graph(sizes):
    count = 1 + sum(sizes)
    adj = [set() for _ in range(count)]
    blade = []
    pos = 1
    for m in sizes:
        b = list(range(pos, pos+m))
        blade.append(b)
        for a in b:
            adj[0].add(a); adj[a].add(0)
            for c in b:
                if a != c: adj[a].add(c)
        pos += m
    return adj,blade


def connected(sel, adj):
    if not sel: return False
    reach = {next(iter(sel))}
    while True:
        newer = reach | set().union(*(adj[u] for u in reach)) & sel
        if newer == reach: break
        reach = newer
    return reach == sel


def kforces(sel, adj, k):
    colored = set(sel)
    while True:
        newer = set(colored)
        for u in colored:
            unseen = adj[u] - colored
            if 0 < len(unseen) <= k: newer.update(unseen)
        if newer == colored: break
        colored = newer
    return len(colored) == len(adj)


def predicted(sel, blades, k):
    if 0 in sel:
        empty_mass = 0
        for b in blades:
            s = sum(u in sel for u in b)
            if not s: empty_mass += len(b)
            elif len(b)-s > k: return False
        return empty_mass <= k
    hits = [i for i,b in enumerate(blades) if any(u in sel for u in b)]
    if len(hits) != 1: return False
    j = hits[0]
    b = blades[j]
    s = sum(u in sel for u in b)
    return len(b)-s+1 <= k and sum(map(len,blades)) - len(b) <= k


def poly_analytic(sizes, k):
    # Exact convolution of blade factors; no graph search.
    def convolution(a,b):
        out={}
        for i,x in a.items():
            for j,y in b.items(): out[i+j]=out.get(i+j,0)+x*y
        return out
    r=len(sizes)
    ans={}
    for empty_mask in range(1<<r):
        if sum(sizes[i] for i in range(r) if (empty_mask>>i)&1)>k: continue
        p={1:1} # hub selected
        for i,m in enumerate(sizes):
            if empty_mask>>i&1: continue
            factor={s:comb(m,s) for s in range(max(1,m-k),m+1)}
            p=convolution(p,factor)
        for d,v in p.items(): ans[d]=ans.get(d,0)+v
    for j,m in enumerate(sizes):
        if sum(sizes)-m>k: continue
        for s in range(max(1,m-k+1),m+1):
            ans[s]=ans.get(s,0)+comb(m,s)
    return ans


def test():
    tested=0
    settings=0
    for r in (2,3,4):
        for sizes in product((2,3,4),repeat=r):
            if sum(sizes)>11: continue
            adj,blades=graph(sizes)
            for k in range(1,sum(sizes)+2):
                count={}
                for mask in range(1<<len(adj)):
                    sel={u for u in range(len(adj)) if mask>>u&1}
                    baseline=connected(sel,adj) and kforces(sel,adj,k)
                    expected=predicted(sel,blades,k)
                    if baseline != expected:
                        raise AssertionError((sizes,k,mask,baseline,expected))
                    if baseline: count[len(sel)]=count.get(len(sel),0)+1
                    tested+=1
                formula=poly_analytic(sizes,k)
                if count!=formula:
                    raise AssertionError((sizes,k,count,formula))
                settings+=1
    print('VERIFIED', settings, 'parameter tuples and', tested, 'vertex-subset comparisons')
    print('Includes heterogeneous blade sizes, all k from 1 to N_blades+1, and connectivity.')

if __name__=='__main__': test()
