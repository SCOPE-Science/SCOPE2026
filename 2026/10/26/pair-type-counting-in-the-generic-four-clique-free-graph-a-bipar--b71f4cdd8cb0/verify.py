"""Exact finite checks of paired extension profiles of K4-free graphs.
Run: python3 verify.py (Python 3.9+ standard library only).
"""
from itertools import combinations
from fractions import Fraction


def edges_of_graph(n, bits):
    pairs=list(combinations(range(n),2))
    return {(a,b) for i,(a,b) in enumerate(pairs) if (bits>>i)&1}


def is_clique(vertices, edges):
    return all((min(a,b),max(a,b)) in edges for a,b in combinations(vertices,2))


def is_free(n, edges, size):
    return not any(is_clique(c,edges) for c in combinations(range(n),size))


def independent_polynomial(n, edges):
    c=[0]*(n+1)
    for mask in range(1<<n):
        if all(not((mask>>a)&1 and (mask>>b)&1) for a,b in edges):
            c[mask.bit_count()]+=1
    return c


def tri_free_subset(mask,edges):
    return not any(all(mask>>v & 1 for v in tri) for tri in combinations(sorted(set(sum(([a,b] for a,b in edges), []))),3) if is_clique(tri,edges))


def formula_general(n,edges):
    good=[]
    triangles=[c for c in combinations(range(n),3) if is_clique(c,edges)]
    for a in range(1<<n):
        good.append(not any(all((a>>v)&1 for v in tr) for tr in triangles))
    total=sum(good)**2
    for a in range(1<<n):
        if not good[a]:continue
        for b in range(1<<n):
            if good[b] and all(not ((a&b)>>u &1 and (a&b)>>v &1) for u,v in edges):
                total+=1
    return total


def direct_types(n,edges):
    ans=0
    for xy in (0,1):
        for a in range(1<<n):
            for b in range(1<<n):
                ext=set(edges)
                ext.update((u,n) for u in range(n) if (a>>u)&1)
                ext.update((u,n+1) for u in range(n) if (b>>u)&1)
                if xy:ext.add((n,n+1))
                if is_free(n+2,ext,4):ans+=1
    return ans


def weighted_bipartite(n,edges):
    c=independent_polynomial(n,edges)
    return 4**n + sum(v*3**(n-k) for k,v in enumerate(c))


def is_bipartite(n,edges):
    adj=[[] for _ in range(n)]
    for a,b in edges:adj[a].append(b);adj[b].append(a)
    color={}
    for u in range(n):
        if u in color:continue
        color[u]=0; q=[u]
        for v in q:
            for w in adj[v]:
                if w in color:
                    if color[w]==color[v]:return False
                else:color[w]=1-color[v];q.append(w)
    return True


def evaluate_poly(c,z):
    return sum(v*z**i for i,v in enumerate(c))


def interpolate_at_one(xs,ys):
    ans=Fraction()
    for i,x in enumerate(xs):
        term=ys[i]
        for j,y in enumerate(xs):
            if j!=i:term*= (1-y)/(x-y)
        ans+=term
    return ans


def clone_graph(n,edges,t):
    return n*t,{(u*t+i,v*t+j) for u,v in edges for i in range(t) for j in range(t)}


def run():
    checked_all=0; checked_bip=0
    for n in range(0,5):
        for m in range(1<<(n*(n-1)//2)):
            edges=edges_of_graph(n,m)
            if not is_free(n,edges,4):continue
            a=direct_types(n,edges)
            assert a==formula_general(n,edges),(n,m,'general',a,formula_general(n,edges))
            checked_all+=1
            if is_bipartite(n,edges):
                b=weighted_bipartite(n,edges)
                assert a==b,(n,m,'bipartite',a,b)
                checked_bip+=1
    # Clone interpolation uses the polynomial identity; direct extension counting
    # is separately checked above on smaller instances.
    checked_interp=0
    for n in range(1,5):
        for m in range(1<<(n*(n-1)//2)):
            e=edges_of_graph(n,m)
            if not is_bipartite(n,e):continue
            original=independent_polynomial(n,e)
            xs=[];ys=[]
            for t in range(1,n+2):
                nn,ee=clone_graph(n,e,t)
                assert is_bipartite(nn,ee)
                xs.append(Fraction(4**t-3**t,3**t))
                weighted=weighted_bipartite(nn,ee)
                y=Fraction(weighted-4**nn,3**nn)
                assert y==evaluate_poly(original,xs[-1]),('clone',n,m,t)
                ys.append(y)
            assert interpolate_at_one(xs,ys)==sum(original),('interpolation',n,m)
            checked_interp+=1
    print('GENERAL_K4_FREE_PAIRS',checked_all)
    print('BIPARTITE_PAIRS',checked_bip)
    print('INTERPOLATION_INSTANCES',checked_interp)
    print('ALL_TESTS_PASS')

if __name__=='__main__':run()
