from itertools import product
from collections import deque
from math import prod


def weak_order(level_sizes):
    level=[]
    for i,n in enumerate(level_sizes):
        level += [i]*n
    N=len(level)
    leq=[[False]*N for _ in range(N)]
    for a in range(N):
        for b in range(N):
            leq[a][b] = (a==b) or (level[a] < level[b])
    return level, leq


def monotone_maps(src_sizes, tgt_sizes):
    sl,sleq=weak_order(src_sizes)
    tl,tleq=weak_order(tgt_sizes)
    n,m=len(sl),len(tl)
    out=[]
    for vals in product(range(m), repeat=n):
        ok=True
        for a in range(n):
            for b in range(n):
                if sleq[a][b] and not tleq[vals[a]][vals[b]]:
                    ok=False; break
            if not ok: break
        if ok: out.append(vals)
    return out,sl,tl,tleq


def special(f, src_sizes, tgt_sizes, sl, tl):
    for i in range(len(src_sizes)):
        vals={f[x] for x,L in enumerate(sl) if L==i}
        if any(tl[v] != i for v in vals):
            return False
        if len(vals) < 2:
            return False
    return True


def comparable(f,g,tleq):
    le=all(tleq[a][b] for a,b in zip(f,g))
    ge=all(tleq[b][a] for a,b in zip(f,g))
    return le or ge


def components(maps,tleq):
    n=len(maps)
    adj=[[] for _ in range(n)]
    for i in range(n):
        for j in range(i+1,n):
            if comparable(maps[i],maps[j],tleq):
                adj[i].append(j); adj[j].append(i)
    seen=[False]*n
    comps=[]
    for i in range(n):
        if seen[i]: continue
        q=[i]; seen[i]=True; C=[]
        for u in q:
            C.append(u)
            for v in adj[u]:
                if not seen[v]:
                    seen[v]=True; q.append(v)
        comps.append(C)
    return comps,adj


def check_case(src,tgt):
    maps,sl,tl,tleq=monotone_maps(src,tgt)
    sp=[i for i,f in enumerate(maps) if special(f,src,tgt,sl,tl)]
    expected_special=prod(q**p-q for p,q in zip(src,tgt))
    assert len(sp)==expected_special
    comps,adj=components(maps,tleq)
    isolated={C[0] for C in comps if len(C)==1}
    assert isolated==set(sp), (src,tgt,len(isolated),len(sp))
    nonsp=[i for i in range(len(maps)) if i not in isolated]
    big=[C for C in comps if len(C)>1]
    assert len(big)==1 and set(big[0])==set(nonsp)
    assert len(comps)==1+expected_special
    # For special maps, the theorem's top-homology rank is the product of
    # (number of used target vertices on level i minus one).
    ranks=[]
    for i in sp:
        f=maps[i]
        r=1
        for L in range(len(src)):
            used={f[x] for x,sL in enumerate(sl) if sL==L}
            r*=len(used)-1
        assert r>0
        ranks.append(r)
    return len(maps),len(sp),len(comps),min(ranks),max(ranks)

cases=[
    ((2,2,2),(2,2,3)),
    ((2,2,3),(2,2,2)),
    ((2,3,2),(3,2,2)),
    ((2,2,3),(2,3,2)),
]
for src,tgt in cases:
    total,special_count,comp_count,rmin,rmax=check_case(src,tgt)
    print(f"src={src} tgt={tgt} maps={total} isolated={special_count} components={comp_count} rank_range={rmin}..{rmax}")
print("VERIFY_OK")
