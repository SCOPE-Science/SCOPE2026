"""Exhaustive small-case checks of the proper-color-class pair-query rank theorem.

Usage: python3 verify_partition_rank.py
Standard library only. All graphs are finite, simple, and labelled.
"""
from functools import lru_cache
from itertools import combinations, product


def partitions(n):
    def rec(i, blocks):
        if i == n:
            yield tuple(tuple(b) for b in blocks)
            return
        for b in blocks:
            b.append(i)
            yield from rec(i+1, blocks)
            b.pop()
        blocks.append([i])
        yield from rec(i+1, blocks)
        blocks.pop()
    return list(rec(0, []))


def components(n, edges):
    parent = list(range(n))
    def root(v):
        while parent[v] != v:
            v = parent[v]
        return v
    for u,v in edges:
        u,v=root(u),root(v)
        parent[u]=v
    r=[root(i) for i in range(n)]
    labels={x:i for i,x in enumerate(sorted(set(r)))}
    return [labels[x] for x in r],len(labels)


def chromatic(n, edges):
    if n == 0: return 0
    # Exact chromatic number by independent-color classes, no heuristics.
    adj=[0]*n
    for u,v in edges:
        if u==v: return None
        adj[u]|=1<<v
        adj[v]|=1<<u
    @lru_cache(None)
    def f(mask):
        if not mask:return 0
        u=(mask&-mask).bit_length()-1
        rem=mask^(1<<u)
        best=n
        sub=rem
        while True:
            group=sub|(1<<u)
            independent=True
            for v in range(n):
                if (group>>v)&1 and adj[v]&group:
                    independent=False
                    break
            if independent:best=min(best,1+f(mask^group))
            if not sub:break
            sub=(sub-1)&rem
        return best
    return f((1<<n)-1)


def ldim(hypotheses, edge_count):
    if len(hypotheses)<=1:return 0
    masks=[sum(((h>>j)&1)<<i for i,h in enumerate(hypotheses)) for j in range(edge_count)]
    @lru_cache(None)
    def d(state):
        if state&(state-1)==0:return 0
        best=0
        for one in masks:
            a=state&one
            b=state&~one
            if a and b:
                best=max(best, 1+min(d(a),d(b)))
        return best
    return d((1<<len(hypotheses))-1)


def vc(hypotheses, edge_count):
    if len(hypotheses)<=1:return 0
    best=0
    for s in range(1<<edge_count):
        k=s.bit_count()
        if k<=best or 2**k>len(hypotheses):continue
        if len({h&s for h in hypotheses}) == 2**k:best=k
    return best


def main():
    base_count=0
    for n in range(1,6):
        es=list(combinations(range(n),2))
        ps=partitions(n)
        signatures=[]
        for p in ps:
            lab={v:k for k,b in enumerate(p) for v in b}
            signatures.append(sum((lab[u]==lab[v])<<j for j,(u,v) in enumerate(es)))
        E=len(es)
        for gmask in range(1<<E):
            g={j for j in range(E) if (gmask>>j)&1}
            h=[x for x in signatures if x&gmask==0]
            exp=n-chromatic(n,[es[j] for j in g])
            assert vc(h,E)==exp, (n,gmask,'VC')
            assert ldim(h,E)==exp, (n,gmask,'Ldim')
            base_count+=1
        print('ALL_GRAPH_BASE_CASES_PASS',n,(1<<E),flush=True)
        if n==4:
            condition_count=0
            for gmask in range(1<<E):
                for pat in product((-1,0,1),repeat=E):
                    plus=[es[j] for j,v in enumerate(pat) if v==1]
                    minus=[es[j] for j,v in enumerate(pat) if v==-1 or (gmask>>j)&1]
                    cls,m=components(n,plus)
                    hgraph={(cls[u],cls[v]) for u,v in minus}
                    if any(u==v for u,v in hgraph):
                        h=[x for x in signatures if x&gmask==0 and all(bool((x>>j)&1)==bool(pat[j]==1) for j in range(E) if pat[j]!=0)]
                        assert not h
                        continue
                    expected=m-chromatic(m,hgraph)
                    h=[x for x in signatures if x&gmask==0 and all(bool((x>>j)&1)==bool(pat[j]==1) for j in range(E) if pat[j]!=0)]
                    assert h
                    assert vc(h,E)==expected,(gmask,pat,'conditional-VC')
                    assert ldim(h,E)==expected,(gmask,pat,'conditional-Ldim')
                    condition_count+=1
            print('ALL_CONDITIONAL_FOUR_VERTEX_CASES_PASS',condition_count,flush=True)
    print('ALL_PARTITION_SHATTERING_CHECKS_PASS',base_count)

if __name__ == '__main__':main()
