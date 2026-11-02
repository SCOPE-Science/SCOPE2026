"""Direct zero-forcing and token-jump enumeration on gear graphs."""
import itertools
from collections import deque

def graph(m):
    n=2*m+1
    g=[set() for _ in range(n)]
    def edge(a,b):g[a].add(b);g[b].add(a)
    for i in range(m):
        edge(2*m,i);edge(i,m+i);edge(m+i,(i+1)%m)
    return g

def forcing(g,S):
    blue=set(S)
    while True:
        growth=set()
        for a in blue:
            white=g[a]-blue
            if len(white)==1:growth.update(white)
        if not growth:return len(blue)==len(g)
        blue.update(growth)

def family(m):
    h=2*m; d={}
    for i in range(m):
        u=lambda j:j%m
        v=lambda j:m+j%m
        d['A',i]=frozenset((h,u(i),v(i)))
        d['B',i]=frozenset((h,u(i+1),v(i)))
        d['C',i]=frozenset((u(i),v(i),v(i+1)))
        d['D',i]=frozenset((u(i+1),v(i),v(i+1)))
        d['E',i]=frozenset((u(i+2),v(i),v(i+1)))
    return d

def test(m):
    g=graph(m)
    assert not any(forcing(g,x) for x in itertools.combinations(range(len(g)),2))
    actual={frozenset(x) for x in itertools.combinations(range(len(g)),3) if forcing(g,x)}
    d=family(m); assert len(d)==5*m and actual==set(d.values())
    adj={s:set() for s in d}
    for s,t in itertools.combinations(d,2):
        if len(d[s]&d[t])==2:adj[s].add(t);adj[t].add(s)
    assert sum(map(len,adj.values()))//2==11*m
    assert all(len(adj[s])==(6 if s[0]=='D' else 4) for s in adj)
    rad=(3*m+3)//4;dia=(3*m+6)//4
    for s in adj:
        dst={s:0};q=deque([s])
        while q:
            x=q.popleft()
            for y in adj[x]:
                if y not in dst:dst[y]=dst[x]+1;q.append(y)
        assert len(dst)==5*m
        typ=s[0]
        target=dia if typ in 'AB' else rad if typ=='D' or m%4 else rad+1
        assert max(dst.values())==target,(m,s,target,max(dst.values()))
    tri=sum(sum(y in adj[z] for y,z in itertools.combinations(adj[x],2)) for x in adj)//3
    assert tri==4*m

if __name__=='__main__':
    for m in range(4,11):test(m)
    print('DIRECT_ZERO_FORCING_ALL_TRIPLES_PASS m=4..10')
    print('DIRECT_TOKEN_JUMP_ALL_PAIRS_PASS m=4..10')
