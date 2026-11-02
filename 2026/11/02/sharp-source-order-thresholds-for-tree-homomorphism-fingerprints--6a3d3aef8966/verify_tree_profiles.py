"""Exact bounded-tree-source homomorphism fingerprints (Python standard library)."""
from collections import defaultdict

def canonical(g):
    n=len(g)
    if n==1:return '()'
    deg=[len(x) for x in g]
    leaves=[i for i,d in enumerate(deg) if d<=1]
    remain=n
    while remain>2:
        remain-=len(leaves)
        new=[]
        for u in leaves:
            for v in g[u]:
                deg[v]-=1
                if deg[v]==1:new.append(v)
        leaves=new
    def rooted(u,parent):
        return '('+''.join(sorted(rooted(v,u) for v in g[u] if v!=parent))+')'
    centers=leaves
    return min(rooted(c,-1) for c in centers)

def alltrees(N):
    levels={1:[(tuple(),)]}
    for n in range(2,N+1):
        seen={}
        for t in levels[n-1]:
            for parent in range(n-1):
                g=[tuple(sorted(list(t[i])+([n-1] if i==parent else []))) for i in range(n-1)]
                g.append((parent,))
                key=canonical(g)
                if key not in seen:seen[key]=tuple(g)
        levels[n]=[seen[c] for c in sorted(seen)]
    return levels

def hom(s,t):
    m=len(s);n=len(t)
    par=[-2]*m;par[0]=-1;order=[0]
    for u in order:
        for v in s[u]:
            if par[v]==-2:par[v]=u;order.append(v)
    dp=[[0]*n for _ in range(m)]
    for u in reversed(order):
        for x in range(n):
            z=1
            for v in s[u]:
                if par[v]==u:z*=sum(dp[v][y] for y in t[x])
            dp[u][x]=z
    return sum(dp[0])

def edges(g):
    return [[u,v] for u in range(len(g)) for v in g[u] if u<v]

def run():
    levels=alltrees(13)
    counts=[0]+[len(levels[n]) for n in range(1,14)]
    assert counts == [0,1,1,1,2,3,6,11,23,47,106,235,551,1301], counts
    sources={k:levels[k] for k in range(1,9)}
    profiles={}
    classes_by_n={}
    for n in range(4,14):
        cls={}
        rows=[]
        for g in levels[n]:
            vs=[]
            for k in range(1,9):
                vs.extend(hom(src,g) for src in sources[k])
                cls.setdefault(k,defaultdict(list))[tuple(vs)].append(g)
            rows.append(vs)
        profiles[n]=[len(cls[k]) for k in range(1,9)]
        classes_by_n[n]=cls
    minsize={n:next(k for k in range(1,9) if profiles[n][k-1]==len(levels[n])) for n in range(4,14)}
    assert minsize=={4:3,5:3,6:4,7:4,8:5,9:5,10:6,11:6,12:7,13:8}
    failfirst={k:next(n for n in range(4,14) if profiles[n][k-1] < len(levels[n])) for k in range(3,8)}
    assert failfirst=={3:6,4:8,5:10,6:12,7:13}
    collisions=[v for v in classes_by_n[13][7].values() if len(v)>1]
    assert len(collisions)==1 and len(collisions[0])==2
    pair=collisions[0]
    split=[(i,hom(src,pair[0]),hom(src,pair[1])) for i,src in enumerate(sources[8]) if hom(src,pair[0]) != hom(src,pair[1])]
    assert len(split)==5
    assert len(classes_by_n[13][8])==1301
    # Small independent check against direct homomorphism maps.
    from itertools import product
    for n in range(2,6):
        for srcn in range(1,5):
            for src in levels[srcn]:
                for tgt in levels[n]:
                    brute=0
                    for mapping in product(range(n),repeat=srcn):
                        if all(mapping[v] in tgt[mapping[u]] for u,v in edges(src)):brute+=1
                    assert brute==hom(src,tgt)
    print('TREE_COUNTS',counts[1:]);print('K_MIN',minsize);print('FIRST_COLLISIONS',failfirst)
    print('N13_CLASSES_BY_K',profiles[13]);
    print('N13_WITNESS_A',edges(pair[0]));print('N13_WITNESS_B',edges(pair[1]));
    print('N13_ORDER8_SPLITTING_SOURCES',split)
    print('ALL_BOUNDED_TREE_SOURCE_PROFILE_CHECKS_PASS')
if __name__=='__main__':run()
