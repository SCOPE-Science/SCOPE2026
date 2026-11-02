"""Independent finite-cover tests for shallow incidence-logic extension profiles.

The test constructs cyclic covers of the Fano incidence graph that contain no
cycles shorter than twelve. It compares exact one-quantifier extension types
of triples and induced two-quantifier types of representative pairs. Only
finite examples are checked; the accompanying proof handles infinite families.
"""
from collections import deque
from itertools import combinations
import random


def base_graph():
    points=range(1,8)
    lines=sorted({tuple(sorted((a,b,a^b))) for a,b in combinations(points,2)})
    assert len(lines)==7
    neighbors=[set() for _ in range(14)]
    edges=[]
    for j,line in enumerate(lines):
        for p in line:
            u=p-1; v=7+j
            neighbors[u].add(v); neighbors[v].add(u)
            edges.append((u,v))
    assert len(edges)==21
    return neighbors,edges


def simple_cycles(adj,max_length=10):
    result=set()
    def dfs(start,path):
        u=path[-1]
        for v in adj[u]:
            if v==start and len(path)>=6 and len(path)%2==0:
                seq=tuple(path)
                options=[seq[i:]+seq[:i] for i in range(len(seq))]
                rev=seq[::-1]
                options += [rev[i:]+rev[:i] for i in range(len(seq))]
                result.add(min(options))
            elif v not in path and len(path)<max_length:
                dfs(start,path+[v])
    for start in range(len(adj)):
        dfs(start,[start])
    return sorted(result)


def voltage_cover(p,seed):
    adj,edges=base_graph()
    cycles=simple_cycles(adj)
    assert len(cycles)==133
    rng=random.Random(seed)
    arcs={(u,v):i for i,(u,v) in enumerate(edges)}
    def cycle_sum(c,volts):
        total=0
        for a,b in zip(c,c[1:]+c[:1]):
            if (a,b) in arcs:total+=volts[arcs[a,b]]
            else:total-=volts[arcs[b,a]]
        return total%p
    for attempt in range(5000):
        volts=[rng.randrange(p) for _ in edges]
        if all(cycle_sum(c,volts)!=0 for c in cycles): break
    else:raise AssertionError('No voltage assignment')
    N=14*p
    nbr=[[] for _ in range(N)]
    for (u,v),dv in zip(edges,volts):
        for k in range(p):
            a=u*p+k; b=v*p+(k+dv)%p
            nbr[a].append(b);nbr[b].append(a)
    assert all(len(ns)==3 for ns in nbr)
    col=[0 if i//p<7 else 1 for i in range(N)]
    print('COVER_OK',p,'vertices',N,'base_short_cycles',len(cycles),'attempts',attempt+1)
    return nbr,col


def bfs(nbr,src):
    D=[-1]*len(nbr)
    D[src]=0
    q=deque([src])
    while q:
        u=q.popleft()
        for v in nbr[u]:
            if D[v]<0:D[v]=D[u]+1;q.append(v)
    assert all(d>=0 for d in D)
    return D


def exact_q1_triple(a,b,c, nbr, col, universe_masks,neighbor_masks):
    params=(a,b,c)
    n=len(nbr)
    equal=tuple(i==j for i,j in ((a,b),(a,c),(b,c)))
    q0=(tuple(col[v] for v in params), equal,
        tuple(int(y in nbr[x]) for x,y in ((a,b),(a,c),(b,c))))
    # Include exact atomic forms of every possible fourth parameter assignment.
    ext=[]
    for sort in (0,1):
        allmask=universe_masks[sort]
        for i,x in enumerate(params):
            if col[x]==sort:
                eq=tuple(int(y==x) for y in params)
                links=tuple(int(y in nbr[x]) for y in params)
                ext.append((sort,eq,links))
        free=allmask
        for x in set(params):free &= ~(1<<x)
        masks=[neighbor_masks[x] & allmask for x in params]
        for pattern in range(8):
            subset=free
            for i,nmask in enumerate(masks):
                subset &= nmask if (pattern>>i)&1 else ~nmask
                if not subset:break
            if subset:
                ext.append((sort,(0,0,0),tuple((pattern>>i)&1 for i in range(3))))
    return (q0,tuple(sorted(set(ext))))


def signatures(nbr,col,selected):
    n=len(nbr)
    masks=[sum(1<<v for v in ns) for ns in nbr]
    universe=(sum(1<<i for i in range(n) if col[i]==0),sum(1<<i for i in range(n) if col[i]==1))
    results={}
    for a,b in selected:
        D=bfs(nbr,a)
        d=D[b]
        s=set()
        for x in range(n):
            s.add(exact_q1_triple(a,b,x,nbr,col,universe,masks))
        results[(col[a],col[b],d)]=frozenset(s)
    return results


def pick(nbr,col,max_distance=10):
    root=[0,next(i for i,c in enumerate(col) if c==1)]
    selected=[]
    for a in root:
        D=bfs(nbr,a)
        for d in range(max_distance+1):
            for sort in (0,1):
                options=[v for v in range(len(col)) if col[v]==sort and D[v]==d]
                if options:selected.append((a,options[0]))
    return selected



def quadrangle_2_2():
    """Symplectic generalized quadrangle W(3,2) on fifteen F_2 points."""
    pts=list(range(1,16))
    def sym(x,y):
        bits=lambda z,i:(z>>i)&1
        return (bits(x,0)*bits(y,2)+bits(x,2)*bits(y,0)+
                bits(x,1)*bits(y,3)+bits(x,3)*bits(y,1))%2
    lines=sorted({tuple(sorted((x,y,x^y))) for x,y in combinations(pts,2) if not sym(x,y)})
    assert len(lines)==15
    nbr=[[] for _ in range(30)]
    for j,line in enumerate(lines):
        for x in line:
            a=x-1;b=15+j
            nbr[a].append(b);nbr[b].append(a)
    assert all(len(x)==3 for x in nbr)
    col=[0]*15+[1]*15
    for u in range(30):
        D=bfs(nbr,u)
        assert max(D)==4
    print('SYMPLECTIC_QUADRANGLE_2_2_OK vertices=30 diameter=4 degree=3')
    return nbr,col


def q1_pair_type(a,b,nbr,col,allmask,neighmask):
    params=(a,b)
    atom=(col[a],col[b],int(a==b),int(b in nbr[a]))
    ext=[]
    for sort in (0,1):
        for x in params:
            if col[x]==sort:
                ext.append((sort,tuple(int(x==v) for v in params),
                            tuple(int(v in nbr[x]) for v in params)))
        free=allmask[sort]
        for x in set(params):free &= ~(1<<x)
        masks=[neighmask[x]&allmask[sort] for x in params]
        for pattern in range(4):
            m=free
            for k,bitmask in enumerate(masks):
                m &= bitmask if (pattern>>k)&1 else ~bitmask
                if not m:break
            if m:ext.append((sort,(0,0),tuple((pattern>>k)&1 for k in range(2))))
    return atom,tuple(sorted(set(ext)))


def one_point_q2_type(nbr,col,a):
    n=len(col)
    allmask=(sum(1<<i for i in range(n) if col[i]==0),
             sum(1<<i for i in range(n) if col[i]==1))
    nm=[sum(1<<x for x in row) for row in nbr]
    return frozenset(q1_pair_type(a,b,nbr,col,allmask,nm) for b in range(n))


def test():
    models={p:voltage_cover(p,seed) for p,seed in ((211,2448),(223,5448))}
    result={}
    for p,(nbr,col) in models.items():
        sel=pick(nbr,col,10)
        sig=signatures(nbr,col,sel)
        print('EXACT_PAIR_Q2_CLASSES',p,len(sig),'signature_count',len(set(sig.values())))
        def trunc(key):
            ca,cb,d=key
            return ca,cb,(d if d<=4 else 6) if ca==cb else (d if d<=3 else 5)
        by={}
        for key,s in sig.items():
            t=trunc(key)
            if t in by:
                assert by[t]==s,(p,'nonuniform within class',key)
            else:by[t]=s
        print('TRUNCATED_DISTANCE_SIGNATURES_OK',p,len(by))
        result[p]=by
    assert result[211]==result[223], 'Cross-cover mismatch'
    qnbr,qcol=quadrangle_2_2()
    for sort in (0,1):
        qa=next(i for i,c in enumerate(qcol) if c==sort)
        qu=one_point_q2_type(qnbr,qcol,qa)
        for p,(cnbr,ccol) in models.items():
            ca=next(i for i,c in enumerate(ccol) if c==sort)
            assert qu==one_point_q2_type(cnbr,ccol,ca), (p,sort,'rank-three disagreement')
    print('QUADRANGLE_TO_HIGH_GIRTH_RANK_THREE_TYPES_OK')
    print('CROSS_COVER_EXACT_RANK_TWO_PAIR_PROFILES_OK',len(result[211]))
    print('VERIFY_OK')

if __name__=='__main__':test()
