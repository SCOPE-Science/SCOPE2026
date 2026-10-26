"""Independent exact checks for small prisms and selected constructive cases."""
from itertools import combinations
from collections import Counter
from construct import coloring

# A second graph representation: vertices (layer, column), edges as
# unordered pairs of tuples. It does not use the other program's graph().
def graph(n):
    e=[]
    for j in range(n):
        e.append(frozenset(((0,j),(1,j))))
        e.append(frozenset(((0,j),(0,(j+1)%n))))
        e.append(frozenset(((1,j),(1,(j+1)%n))))
    assert len(set(e))==3*n
    return e

def conflict_graph(n):
    edges=graph(n)
    adj={v:set() for e in edges for v in e}
    for e in edges:
        a,b=tuple(e);adj[a].add(b);adj[b].add(a)
    m=len(edges);conf=[0]*m
    for i in range(m):
        for j in range(i):
            p=edges[i];q=edges[j]
            if p&q or any(y in adj[x] for x in p for y in q):
                conf[i]|=1<<j;conf[j]|=1<<i
    return conf

def histogram(n):
    conf=conflict_graph(n);m=len(conf);hist=Counter()
    # An independent set of the edge-conflict graph is an induced matching.
    def dfs(available,size):
        hist[size]+=1
        while available:
            u=available&-available;v=u.bit_length()-1
            available ^=u
            dfs(available &~conf[v],size+1)
    dfs((1<<m)-1,0)
    return hist

def dsatur_decision(n,k):
    conf=conflict_graph(n);m=len(conf)
    used=[-1]*m; masks=[0]*m; deg=[a.bit_count() for a in conf]
    calls=0
    def dfs(depth,num):
        nonlocal calls
        calls+=1
        if depth==m:return True
        v=-1;best=(-1,-1)
        for i in range(m):
            if used[i]>=0:continue
            seen=masks[i].bit_count()
            if seen==k:return False
            if (seen,deg[i])>best:v=i;best=(seen,deg[i])
        for c in range(min(num+1,k)):
            if (masks[v]>>c)&1:continue
            used[v]=c;changes=[];z=conf[v]
            while z:
                bit=z&-z;j=bit.bit_length()-1;z-=bit
                if used[j]==-1 and not ((masks[j]>>c)&1):
                    masks[j]|=1<<c;changes.append(j)
            if dfs(depth+1,max(num,c+1)):return True
            for j in changes:masks[j]&=~(1<<c)
            used[v]=-1
        return False
    answer=dfs(0,0)
    return answer,calls

def verify_template(n):
    edges=graph(n);cols=coloring(n)
    # Input columns are (rung, upper, lower); map to the independently
    # enumerated edge order (rung, upper, lower) for each column.
    mapping={edges[3*i+k]:cols[i][k] for i in range(n) for k in range(3)}
    conf=conflict_graph(n)
    for i in range(3*n):
        for j in range(i):
            if (conf[i]>>j)&1:assert mapping[edges[i]]!=mapping[edges[j]],(n,i,j)
    return len(set(mapping.values()))

if __name__=='__main__':
    for n in (3,5,6):
        hist=histogram(n)
        print('n=',n,'induced matching size histogram=',dict(sorted(hist.items())),
              'max=',max(hist),'maximum_count=',hist[max(hist)])
        expected={3:{0:1,1:9},5:{0:1,1:15,2:25},6:{0:1,1:18,2:57,3:2}}[n]
        assert dict(hist)==expected,(n,hist)
    for n,k in ((3,8),(5,7),(6,7),(7,6),(9,6),(10,6)):
        exists,nodes=dsatur_decision(n,k)
        assert not exists,(n,k)
        print(f'exhaustive: prism n={n} is NOT strongly {k}-colorable; search nodes={nodes}')
    for n in (3,4,5,6,7,8,9,10,11,12,13,14,15,17,18,19,20,21,22,23,25,26,27,30,31,40,41,42,99):
        p=verify_template(n)
        print('independent graph check:',n,'colors=',p)
    print('INDEPENDENT_CHECKS_OK')
