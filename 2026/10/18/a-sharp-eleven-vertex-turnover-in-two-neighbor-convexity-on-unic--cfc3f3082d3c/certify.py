"""Pure-Python exhaustive witness to the first non-cycle maximizer in unicyclic P3-convexity."""
from functools import lru_cache

# An unlabeled rooted tree is an ordered string of balanced parentheses with its child subtrees sorted.
@lru_cache(maxsize=None)
def rooted_shapes(n):
    if n==1:return ('()',)
    parts=sorted((s, code) for s in range(1,n) for code in rooted_shapes(s))
    out=[]
    def extend(start,rem,acc):
        if not rem:
            out.append('(' + ''.join(acc)+')');return
        for idx in range(start,len(parts)):
            size, code=parts[idx]
            if size>rem:break
            acc.append(code)
            extend(idx,rem-size,acc)
            acc.pop()
    extend(0,n-1,[])
    return tuple(sorted(out))

def decode(code):
    links=[];stack=[]
    for ch in code:
        if ch=='(':
            v=len(links);links.append(set())
            if stack:
                u=stack[-1];links[u].add(v);links[v].add(u)
            stack.append(v)
        else:stack.pop()
    return links

def unrooted_key(links):
    n=len(links);alive=set(range(n));degree=[len(q) for q in links]
    leaves=[v for v in alive if degree[v]<=1]
    while len(alive)>2:
        new=[]
        for v in leaves:
            alive.remove(v)
            for w in links[v]:
                if w in alive:
                    degree[w]-=1
                    if degree[w]==1:new.append(w)
        leaves=new
    def rooted(v,p):
        return '('+''.join(sorted(rooted(w,v) for w in links[v] if w!=p))+')'
    if len(alive)==1:return rooted(next(iter(alive)),-1)
    u,v=sorted(alive)
    return '('+''.join(sorted([rooted(u,v),rooted(v,u)]))+')'

def trees(n):
    d={}
    for shape in rooted_shapes(n):
        links=decode(shape)
        d[unrooted_key(links)]=links
    return list(d.values())

def noc(links):
    n=len(links)
    nbr=[sum(1<<u for u in nb) for nb in links]
    count=0
    for mask in range(1<<n):
        good=True
        for v,b in enumerate(nbr):
            if ((mask>>v)&1)==0 and (mask&b).bit_count()>1:
                good=False;break
        count+=good
    return count

def cycle(n):
    g=[set() for _ in range(n)]
    for v in range(n):
        w=(v+1)%n;g[v].add(w);g[w].add(v)
    return g

def pineapple(n):
    g=cycle(4)
    for i in range(4,n):
        g.append({0});g[0].add(i)
    return g

def census():
    known={3:1,4:2,5:3,6:6,7:11,8:23,9:47,10:106}
    table=[]
    for n in range(3,11):
        T=trees(n)
        assert len(T)==known[n],('tree count',n,len(T))
        best=0;noncycles=0;pairs=0;ties=0
        z=noc(cycle(n))
        for g in T:
            for a in range(n):
                for b in range(a+1,n):
                    if b in g[a]:continue
                    pairs+=1
                    g[a].add(b);g[b].add(a)
                    v=noc(g)
                    if v>best:best=v
                    if v==z:ties+=1
                    if v>z:noncycles+=1
                    g[a].remove(b);g[b].remove(a)
        assert best==z and noncycles==0,(n,best,z)
        table.append([n,len(T),pairs,z,best,ties])
    z11=noc(cycle(11))
    p11=noc(pineapple(11))
    assert(z11,p11)==(486,532)
    print('n trees attempts cycle_count max_value ties')
    for x in table:print(*x)
    print('11 cycle',z11,'C4+7leaves',p11,'difference',p11-z11)
    print('VERIFIED')

if __name__=='__main__':census()
