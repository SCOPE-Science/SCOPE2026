#!/usr/bin/env python3
"""Finite independent corroboration for forest-order counting-refinement theorem.
No external packages. Exhausts all topologically labelled strict partial orders
of size <= 6, and all increasing labelled rooted forests of size <= 7.
Finite tests do not certify the theorem for arbitrary size.
"""
from itertools import combinations,product
from collections import defaultdict,Counter


def all_posets(n):
    pairs=list(combinations(range(n),2))
    for bits in range(1<<len(pairs)):
        r=[0]*n
        for k,(i,j) in enumerate(pairs):
            if (bits>>k)&1:r[i]|=1<<j
        if all((r[j]&~r[i])==0 for i in range(n) for j in range(i+1,n) if r[i]&(1<<j)):
            yield tuple(r)

def info(r):
    n=len(r); depth=[sum(bool(r[u]&(1<<v)) for u in range(n)) for v in range(n)]
    parents=[]
    for v in range(n):
        pre=[u for u in range(n) if r[u]&(1<<v)]
        if any(not (r[u]&(1<<w) or r[w]&(1<<u)) for u,w in combinations(pre,2)):
            return False,None,None
        parents.append(max(pre,key=lambda u:depth[u]) if pre else -1)
    return True,tuple(depth),tuple(parents)

def subtree_and_paths(par):
    n=len(par); kids=[[] for _ in par]
    for v,p in enumerate(par):
        if p>=0:kids[p].append(v)
    def code(v):return '('+''.join(sorted(code(w) for w in kids[v]))+')'
    sub=[code(v) for v in range(n)]
    paths=[]
    for v in range(n):
        trail=[];u=v
        while u>=0: trail.append(sub[u]);u=par[u]
        paths.append(tuple(reversed(trail)))
    return tuple(sorted(sub[v] for v,p in enumerate(par) if p<0)),tuple(paths)

def refine_many(rs,steps):
    n=len(rs[0]);cur=[tuple([0]*n) for _ in rs]
    out={0:cur}
    for t in range(1,steps+1):
        keys=[]
        for r,c in zip(rs,cur):
            keys.append([(c[v], tuple(sorted(Counter(c[w] for w in range(n) if r[w]&(1<<v)).items())),
                           tuple(sorted(Counter(c[w] for w in range(n) if r[v]&(1<<w)).items()))) for v in range(n)])
        universe=sorted({key for row in keys for key in row})
        enc={key:i for i,key in enumerate(universe)}
        cur=[tuple(enc[k] for k in row) for row in keys]
        out[t]=cur
    return out

def check_posets(n):
    ps=list(all_posets(n))
    cs=refine_many(ps,n+2)
    data=[]
    for p in ps:
        f,d,par=info(p)
        data.append((f,max(d) if f else -1,subtree_and_paths(par)[0] if f else None))
    for h in range(n):
        buckets=defaultdict(set)
        for i,c in enumerate(cs[max(1,h)]):
            buckets[tuple(sorted(c))].add(i)
        for i,(f,ht,form) in enumerate(data):
            if not f or ht!=h:continue
            for j in buckets[tuple(sorted(cs[max(1,h)][i]))]:
                assert data[j][0] and data[j][2]==form,('counterexample',n,h,ps[i],ps[j])
    forests=sum(z[0] for z in data)
    distinct=len({z[2] for z in data if z[0]})
    print(f'all-posets n={n}: topologically labelled={len(ps)}; forest-orders={forests}; forest isomorphism types={distinct}; rank bound verified')


def increased_forest(n):
    for choice in product(*(range(v+1) for v in range(1,n))):
        par=(-1,)+tuple((-1 if x==0 else x-1) for x in choice)
        # parent of v is -1 if 0, else x-1
        yield par

def from_par(par):
    n=len(par);rows=[]
    for v in range(n):
        k=0
        for u in range(n):
            x=par[u]
            while x>=0:
                if x==v:k|=1<<u;break
                x=par[x]
        rows.append(k)
    return tuple(rows)

def check_orbits(n):
    # use a single global colour system on the full enumerated forest family
    pars=list(increased_forest(n));rs=[from_par(p) for p in pars]
    C=refine_many(rs,n+2)
    seen=0
    for ix,p in enumerate(pars):
        depth=[]
        for v in range(n):
            d=0;u=p[v]
            while u>=0: d+=1;u=p[u]
            depth.append(d)
        h=max(depth)
        c=C[max(1,h)+1][ix]
        _,paths=subtree_and_paths(p)
        for i in range(n):
            for j in range(n):
                assert (c[i]==c[j])==(paths[i]==paths[j]),('orbit mismatch',n,p,i,j)
        seen+=1
    print(f'rooted-forests n={n}: increasing-labellings checked={seen}; max(1,height)+1 rounds equals orbit partition')

if __name__=='__main__':
    for n in range(1,7):check_posets(n)
    for n in range(1,8):check_orbits(n)
    print('PASS: no counterexamples in stated finite ranges')
