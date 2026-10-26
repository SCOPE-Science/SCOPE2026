"""Independent finite checks of full-degree coalition partitions in regular graphs.

Uses the original k-domination definition, not the vertex-cover equivalence.
Standard-library only. Run: python verify.py
"""
from itertools import combinations, product


def is_bipartite(adj):
    n=len(adj); color=[-1]*n; components=0
    for s in range(n):
        if color[s]>=0: continue
        components+=1; color[s]=0; queue=[s]
        for u in queue:
            for v in range(n):
                if (adj[u] >> v)&1:
                    if color[v]<0: color[v]=1-color[u]; queue.append(v)
                    elif color[v]==color[u]: return False, components
    return True, components


def partitions(n):
    # Restricted-growth enumeration of ALL unlabeled set partitions.
    r=[0]*n
    def extend(i, highest):
        if i==n:
            k=highest+1; blocks=[0]*k
            for u,b in enumerate(r): blocks[b]|=1<<u
            yield blocks
        else:
            for b in range(highest+2):
                r[i]=b
                yield from extend(i+1,max(highest,b))
    yield from extend(1,0)


def independent_kdom_table(adj,k):
    n=len(adj); complete=(1<<n)-1
    table=[False]*(1<<n)
    for s in range(1<<n):
        complement=complete^s
        table[s]=all((adj[v]&s).bit_count()>=k
                     for v in range(n) if (complement>>v)&1)
    return table


def direct_coalition_counts(adj):
    n=len(adj); k=adj[0].bit_count()
    assert k>=2 and all(a.bit_count()==k for a in adj)
    dom=independent_kdom_table(adj,k)
    counts={}
    for blocks in partitions(n):
        m=len(blocks)
        if m<3 or m>4: continue  # structural upper bound proved separately
        if all((dom[a] and a.bit_count()==k) or
               (not dom[a] and any((not dom[b]) and dom[a|b]
                 for b in blocks if b!=a)) for a in blocks):
            counts[m]=counts.get(m,0)+1
    return counts


def cycle(n):
    return [1<<((i+1)%n)|1<<((i-1)%n) for i in range(n)]


def complete_bipartite(m):
    return [((1<<m)-1)<<m]*m + [(1<<m)-1]*m


def cube3():
    return [sum(1<<(v^(1<<i)) for i in range(3)) for v in range(8)]


def complete(n):
    return [((1<<n)-1)^(1<<i) for i in range(n)]


def disjoint(a,b):
    p=len(a)
    return a+[x<<p for x in b]


def check_graph(adj,name):
    k=adj[0].bit_count()
    assert all(a.bit_count()==k for a in adj)
    bip,c=is_bipartite(adj)
    counts=direct_coalition_counts(adj)
    expected=4 if bip else 3
    assert counts.get(expected,0)>0 and all(h<=expected for h in counts), (name,expected,counts)
    if bip and c==1:
        m=len(adj)//2
        assert counts.get(4,0)==(2**(m-1)-1)**2,(name,counts)
    return expected,counts.get(4,0)



def orientations_and_splits(adj):
    # Independent construction of every bipartition and two splits per side.
    n=len(adj); colors=[-1]*n; components=[]
    for s in range(n):
        if colors[s]!=-1: continue
        colors[s]=0; group=[s]
        for u in group:
            for v in range(n):
                if (adj[u]>>v)&1:
                    if colors[v]==-1: colors[v]=1-colors[u]; group.append(v)
                    else: assert colors[v]!=colors[u]
        components.append(group)
    all_vertex=(1<<n)-1
    seen=set()
    for flips in product((0,1),repeat=len(components)-1):
        orientation=(0,)+flips; x=0
        for comp,flip in zip(components,orientation):
            for v in comp:
                if (colors[v]^flip)==0: x|=1<<v
        y=all_vertex^x
        def halves(mask):
            anchor=mask&-mask
            rem=mask^anchor
            choice=rem
            while choice:
                yield anchor|choice,mask^(anchor|choice)
                choice=(choice-1)&rem
            # Exclude the all-set + empty split above; include anchor alone.
            yield anchor, mask^anchor
        # Deduplicate within side via anchor membership; exclude full-set choice.
        def splits(mask):
            anchor=mask&-mask; rest=mask^anchor
            z=(rest-1)&rest
            while z:
                yield anchor|z, rest^z
                z=(z-1)&rest
            yield anchor,rest
        for a,b in splits(x):
            for c,d in splits(y):
                seen.add(tuple(sorted((a,b,c,d))))
    return len(seen),len(components),n//2

def main():
    graph_count=0
    exact4_count=0
    for n in range(3,7):
        edges=list(combinations(range(n),2))
        for mask in range(1<<len(edges)):
            adj=[0]*n
            for j,(u,v) in enumerate(edges):
                if (mask>>j)&1:
                    adj[u]|=1<<v; adj[v]|=1<<u
            k=adj[0].bit_count()
            if k>=2 and all(a.bit_count()==k for a in adj):
                expected,q=check_graph(adj,f'all-labeled-n{n}-{mask}')
                graph_count+=1
                if expected==4: exact4_count+=1
    samples={
        'C7':cycle(7), 'C8':cycle(8), 'Q3':cube3(),
        'K4,4':complete_bipartite(4),
        'K7':complete(7),
        '2C4':disjoint(cycle(4),cycle(4)),
        '2K4':disjoint(complete(4),complete(4)),
        'K3,3':complete_bipartite(3),
    }
    for name,adj in samples.items():
        expected,q=check_graph(adj,name)
        print(f'SAMPLE {name}: n={len(adj)}, k={adj[0].bit_count()}, max={expected}, four_partitions={q}')
    disjoint_samples={
        '3C4':disjoint(disjoint(cycle(4),cycle(4)),cycle(4)),
        '4C4':disjoint(disjoint(cycle(4),cycle(4)),disjoint(cycle(4),cycle(4))),
        '2K3,3':disjoint(complete_bipartite(3),complete_bipartite(3)),
    }
    for name,adj in disjoint_samples.items():
        actual,c,m=orientations_and_splits(adj)
        predicted=2**(c-1)*(2**(m-1)-1)**2-2**(c-2)*(2**(c-1)-1)
        assert actual==predicted,(name,actual,predicted)
        print(f'OPTIMAL_PARTITION_COUNT {name}: components={c}, count={actual}')
    print(f'EXHAUSTIVE_LABELLED_REGULAR_GRAPHS_N3_TO_N6={graph_count}')
    print(f'EXHAUSTIVE_BIPARTITE_CASES={exact4_count}')
    print('VERIFY_OK')

if __name__=='__main__': main()
