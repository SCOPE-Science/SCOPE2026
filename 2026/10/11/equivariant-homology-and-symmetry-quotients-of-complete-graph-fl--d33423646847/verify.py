"""Standalone exact checks for symmetric-group characters of complete-graph flex complexes.
No third-party dependencies. Enumerates edge orientations and source/sink flips.
"""
from itertools import combinations, permutations
from math import factorial, gcd
from collections import defaultdict


def cycle_types(n):
    def gen(r, lo=1):
        if not r:
            yield ()
        else:
            for a in range(lo, r+1):
                for b in gen(r-a,a): yield (a,)+b
    return list(gen(n))


def representative(parts):
    g=[]; p=0
    for z in parts:
        g += list(range(p+1,p+z))+[p]
        p+=z
    return tuple(g)


def B(parts):
    return sum(a//2 for a in parts)+sum(gcd(a,b) for a,b in combinations(parts,2))


def phi(parts):
    if any(a%2==0 for a in parts): return 0
    f=parts.count(1)
    def N(i):return 2**B(tuple(x for x in parts if x!=1)+(1,)*(f-i)) if i<=f else 0
    # Removing i *distinct* singleton cycles preserves all nontrivial cycles.
    return N(0)-2*f*N(1)+f*(f-1)*N(2)


def cycle_character(parts):
    n=sum(parts)
    if len(set(parts))!=1:return 0
    d=parts[0];k=len(parts)
    tot=sum(gcd(a,d)==1 for a in range(1,d+1))
    return tot*(d**k)*factorial(k)//n


def path_character(parts):
    f=parts.count(1); n=sum(parts)
    a=0;factor=1
    for t in range(min(f,n-3)+1):
        if t>0:factor*=f-t+1
        reduced=tuple(x for x in parts if x!=1)+(1,)*(f-t)
        a+=factor*phi(reduced)
    return a


def orientation_graph(n):
    edges=list(combinations(range(n),2)); inc=[]
    for v in range(n):
        z=0
        for i,(a,b) in enumerate(edges):
            if v==a or v==b:z|=(1<<i)
        inc.append(z)
    N=1<<len(edges); parent=list(range(N));size=[1]*N
    def root(a):
        while parent[a]!=a:
            parent[a]=parent[parent[a]];a=parent[a]
        return a
    def join(a,b):
        a=root(a);b=root(b)
        if a!=b:
            if size[a]<size[b]:a,b=b,a
            parent[b]=a;size[a]+=size[b]
    sinks=[[] for _ in range(N)]
    degrees=[0]*N
    for mask in range(N):
        for v in range(n):
            all_in=True;all_out=True
            for j,(a,b) in enumerate(edges):
                if v!=a and v!=b:continue
                out=bool(mask&(1<<j)) if v==a else not bool(mask&(1<<j))
                if out:all_in=False
                else:all_out=False
            if all_in:sinks[mask].append(v)
            if all_in or all_out:
                degrees[mask]+=1
                nxt=mask^inc[v]
                if nxt>mask:join(mask,nxt)
    groups=defaultdict(list)
    for mask in range(N):groups[root(mask)].append(mask)
    kinds={}
    for k,lst in groups.items():
        degs=[degrees[m] for m in lst]
        assert max(degs)<=2
        kinds[k]='cycle' if len(lst)>1 and all(d==2 for d in degs) else 'path'
        if kinds[k]=='cycle':assert len(lst)==n
    return edges,inc,root,groups,kinds,sinks


def action(mask, edges, g):
    n=len(g); table={ab:j for j,ab in enumerate(edges)}; z=0
    for j,(a,b) in enumerate(edges):
        x,y=g[a],g[b]
        if x>y:x,y=y,x; val=not bool(mask&(1<<j))
        else:val=bool(mask&(1<<j))
        if val:z|=1<<table[(x,y)]
    return z


def orbit_counts(n, edges, root, groups, kinds, generators):
    keys=list(groups)
    ix={key:i for i,key in enumerate(keys)}
    par=list(range(len(keys)))
    def find(i):
        while par[i]!=i:
            par[i]=par[par[i]];i=par[i]
        return i
    def union(i,j):par[find(i)]=find(j)
    for g in generators:
        for i,key in enumerate(keys):
            r=root(action(groups[key][0],edges,g))
            union(i,ix[r])
    orbits=defaultdict(list)
    for i,k in enumerate(keys):orbits[find(i)].append(k)
    profile=defaultdict(int)
    for v in orbits.values():
        key=v[0]
        k=(kinds[key],len(groups[key])-1 if kinds[key]=='path' else -1)
        profile[k]+=1
    return dict(profile)


def a(n):
    from collections import Counter
    z=0
    for parts in cycle_types(n):
        ct=Counter(parts); den=1
        for j,m in ct.items():den*=j**m*factorial(m)
        z+=factorial(n)//den*phi(parts)
    assert z%factorial(n)==0
    return z//factorial(n)


def swap(n,u,v):
    g=list(range(n));g[u],g[v]=g[v],g[u];return tuple(g)


def three(n,u,v,w):
    g=list(range(n));g[u],g[v],g[w]=v,w,u;return tuple(g)


def verify(n):
    edges,inc,root,groups,kinds,sinks=orientation_graph(n)
    cycles=sum(v=='cycle' for v in kinds.values()); paths=len(kinds)-cycles
    assert cycles==factorial(n-1), (n,cycles)
    assert paths==path_character((1,)*n),(n,paths,path_character((1,)*n))
    probes=0
    for parts in cycle_types(n):
        g=representative(parts)
        cp=cc=0
        for key,lst in groups.items():
            rep=lst[0]
            if root(action(rep,edges,g))==key:
                if kinds[key]=='cycle':
                    cc+=1
                    assert len(sinks[rep])==1
                    v=sinks[rep][0]
                    from_a=rep^inc[v]
                    to_a=action(rep,edges,g)
                    to_b=action(from_a,edges,g)
                    assert len(sinks[to_a])==1
                    assert to_b==to_a^inc[sinks[to_a][0]], 'orientation reversal found'
                else:cp+=1
        expcp=path_character(parts);expcc=cycle_character(parts)
        assert (cp,cc)==(expcp,expcc),(n,parts,(cp,cc),(expcp,expcc))
        probes+=1
    sg=[swap(n,i,i+1) for i in range(n-1)]
    ag=[three(n,0,1,i) for i in range(2,n)]
    for group,gen in [('S',sg),('A',ag)]:
        orbs=orbit_counts(n,edges,root,groups,kinds,gen)
        assert orbs.get(('cycle',-1))==(1 if group=='S' or n%2==0 else 2),(n,group,orbs)
        for m in range(3,n+1):
            assert orbs.get(('path',n-m))==(a(m)*(1 if group=='S' else 2)),(n,group,m,orbs)
    return n,len(groups),paths,cycles,probes

if __name__=='__main__':
    total=0
    for n in range(3,7):
        v=verify(n); total+=v[-1];print('n=%d components=%d paths=%d cycles=%d conjugacy_types=%d'%v)
    print('VERIFY_OK; all',total,'conjugacy classes checked against complete orientation-component enumeration')
