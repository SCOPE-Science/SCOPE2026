#!/usr/bin/env python3
import itertools, math
from collections import Counter, defaultdict

def abstract_graph(ells):
    r=len(ells); V=[]; support={}
    for a in itertools.product(*[range(e+1) for e in ells]):
        if all(x==0 for x in a): continue
        if all(a[i]==ells[i] for i in range(r)): continue
        S=tuple(i for i in range(r) if a[i]<ells[i])
        V.append(a); support[a]=S
    V=sorted(V); idx={v:i for i,v in enumerate(V)}
    adj=[[False]*len(V) for _ in V]
    for i in range(len(V)):
        for j in range(i+1,len(V)):
            if set(support[V[i]]) & set(support[V[j]]):
                adj[i][j]=adj[j][i]=True
    return V,adj,support

def cell_weights(ells):
    r=len(ells); out={}
    for mask in range(1,1<<r):
        S=tuple(i for i in range(r) if (mask>>i)&1)
        w=math.prod(ells[i] for i in S)
        if len(S)==r: w-=1
        out[S]=w
    return out

def is_auto(adj,p):
    n=len(adj)
    return all(adj[i][j]==adj[p[i]][p[j]] for i in range(n) for j in range(i+1,n))

def brute_autos(adj):
    n=len(adj)
    return [p for p in itertools.permutations(range(n)) if is_auto(adj,p)]

def structural_autos(ells,V,adj,support):
    r=len(ells); cells=defaultdict(list)
    for i,v in enumerate(V): cells[support[v]].append(i)
    coords=[]
    for p in itertools.permutations(range(r)):
        if all(ells[p[i]]==ells[i] for i in range(r)): coords.append(p)
    autos=set()
    # Small verification cases only: expand internal permutations and coordinate permutations.
    cell_keys=sorted(cells)
    internal_lists=[list(itertools.permutations(cells[S])) for S in cell_keys]
    for choices in itertools.product(*internal_lists):
        base={}
        for S,perm in zip(cell_keys,choices):
            for old,new in zip(cells[S],perm): base[old]=new
        for cp in coords:
            # coordinate permutation maps each exponent tuple and hence its support; values move with coordinates
            mapped=[None]*len(V); index={v:i for i,v in enumerate(V)}
            for old in range(len(V)):
                mid=base[old]; a=V[mid]
                b=[None]*r
                for i in range(r): b[cp[i]]=a[i]
                mapped[old]=index[tuple(b)]
            p=tuple(mapped)
            assert is_auto(adj,p)
            autos.add(p)
    return sorted(autos)

def brute_det(autos,n):
    nonid=[p for p in autos if any(p[i]!=i for i in range(n))]
    for k in range(n+1):
        for S in itertools.combinations(range(n),k):
            if all(any(p[v]!=v for v in S) for p in nonid): return k,S
    raise AssertionError

def build_coloring(ells,V,support):
    r=len(ells); W=math.prod(ells)-1; full=tuple(range(r)); cells=defaultdict(list)
    for i,v in enumerate(V): cells[support[v]].append(i)
    color={}
    for c,i in enumerate(sorted(cells[full])): color[i]=c
    bysize=defaultdict(list)
    for S,L in cells.items():
        if S!=full: bysize[len(L)].append(S)
    for k,SL in bysize.items():
        choices=iter(itertools.combinations(range(W),k))
        for S in sorted(SL):
            C=next(choices)
            for c,i in zip(C,sorted(cells[S])): color[i]=c
    return color,W

def check_distinguishing(autos,color,n):
    for p in autos:
        if all(color[i]==color[p[i]] for i in range(n)):
            assert all(p[i]==i for i in range(n))

def direct_Zn(n,factors):
    ds=[d for d in range(2,n) if n%d==0]
    edges=set()
    for i,d in enumerate(ds):
        for e in ds[i+1:]:
            if math.lcm(d,e)<n: edges.add(tuple(sorted((d,e))))
    exps={}
    for d in ds:
        a=[]
        for p,ell in factors:
            x=d;c=0
            while x%p==0: c+=1;x//=p
            a.append(c)
        exps[d]=tuple(a)
    V,adj,supp=abstract_graph(tuple(e for _,e in factors)); idx={v:i for i,v in enumerate(V)}
    assert set(exps.values())==set(V)
    for i,d in enumerate(ds):
        for e in ds[i+1:]:
            pred=adj[idx[exps[d]]][idx[exps[e]]]
            assert ((d,e) in edges)==pred
    return len(ds)

for ells in [(2,), (3,), (2,2), (2,3)]:
    V,adj,support=abstract_graph(ells); r=len(ells)
    N=math.prod(e+1 for e in ells)-2; P=math.prod(ells); weights=cell_weights(ells)
    assert len(V)==N
    assert sorted(Counter(support.values()).values())==sorted(weights.values())
    autos=structural_autos(ells,V,adj,support)
    mult=Counter(ells)
    expected=math.prod(math.factorial(w) for w in weights.values())*math.prod(math.factorial(c) for c in mult.values())
    assert len(autos)==expected,(ells,len(autos),expected)
    if len(V)<=7:
        b=brute_autos(adj)
        assert set(b)==set(autos)
    det,S=brute_det(autos,len(V))
    assert det==N-(2**r-1),(ells,det)
    color,W=build_coloring(ells,V,support); check_distinguishing(autos,color,len(V))
    assert W==P-1==max(weights.values())
    print(f"ells={ells}: N={N}, |Aut|={len(autos)}, Det={det}, distinguishing witness uses {W} colors")

assert direct_Zn(36,[(2,2),(3,2)])==7
assert direct_Zn(108,[(2,2),(3,3)])==10
print('Z/36Z and Z/108Z direct ideal-intersection reconstructions OK')
print('VERIFY_OK')
