"""Standalone exact checks for power domination of GP(n,2); Python 3 stdlib only."""
from itertools import combinations
from collections import deque, Counter

def graph(n):
    # Vertices 0..n-1 are a_i, n..2*n-1 are b_i.
    g = [set() for _ in range(2*n)]
    def e(x,y):
        if x == y: raise AssertionError('loop')
        g[x].add(y);g[y].add(x)
    for i in range(n):
        e(i,(i+1)%n)
        e(i,n+i)
        e(n+i,n+(i+2)%n)
    assert all(len(t)==3 for t in g)
    return g

def synchronous(g,S,with_rounds=False):
    obs=set(S)
    for i in S: obs.update(g[i])
    frames=[frozenset(obs)]
    while True:
        nxt=obs.copy()
        for v in obs:
            w=g[v]-obs
            if len(w)==1: nxt.update(w)
        if len(nxt)==len(obs): break
        obs=nxt
        frames.append(frozenset(obs))
    return (frozenset(obs),frames) if with_rounds else len(obs)==len(g)

def sequential(g,S):
    # Independent implementation: use mutable Boolean states and make one force per pass.
    seen=[False]*len(g)
    for v in S:
        seen[v]=True
        for j in g[v]:seen[j]=True
    while True:
        moved=False
        for v in range(len(g)):
            if not seen[v]:continue
            missing=[w for w in g[v] if not seen[w]]
            if len(missing)==1:
                seen[missing[0]]=True
                moved=True
                break
        if not moved: return all(seen)

def edge_monitoring(g,S):
    # Directly implement the edge-monitoring rules in Barrera--Ferrero (2010):
    # initially observe each edge incident to a sensor, then close under
    # (i) endpoints of observed edges; (ii) edges with both ends observed;
    # (iii) a last unobserved incident edge at an observed vertex.
    edges={tuple(sorted((a,b))) for a in range(len(g)) for b in g[a]}
    obs_edges={e for e in edges if any(x in S for x in e)}
    obs_vertices=set(S)
    while True:
        changed=False
        vertices=set(obs_vertices)
        for a,b in obs_edges:
            vertices.add(a); vertices.add(b)
        if len(vertices)>len(obs_vertices): changed=True
        obs_vertices=vertices
        new=set(obs_edges)
        for a,b in edges:
            if a in obs_vertices and b in obs_vertices: new.add((a,b))
        for a in obs_vertices:
            unmonitored=[tuple(sorted((a,b))) for b in g[a] if tuple(sorted((a,b))) not in obs_edges]
            if len(unmonitored)==1: new.add(unmonitored[0])
        if len(new)>len(obs_edges): changed=True
        obs_edges=new
        if not changed: return len(obs_vertices)==len(g) and len(obs_edges)==len(edges)

def expected(n):
    ans=set()
    def put(x,y):ans.add(tuple(sorted((x,y))))
    for i in range(n):
        put(i,(i+3)%n)
        put(n+i,n+(i+1)%n)
        for d in (-4,-3,3,4):put(i,n+(i+d)%n)
    assert len(ans)==6*n
    return ans

def dist(g,x):
    out=[-1]*len(g);out[x]=0;q=deque([x])
    while q:
        v=q.popleft()
        for w in g[v]:
            if out[w]<0:out[w]=out[v]+1;q.append(w)
    return out

def run():
    for n in range(9,21):
        g=graph(n)
        success=set();
        for S in combinations(range(2*n),2):
            a=synchronous(g,S);b=sequential(g,S);c=edge_monitoring(g,S)
            assert a==b==c,(n,S,a,b,c)
            if a:success.add(S)
        want=expected(n)
        assert success==want,(n,len(success),len(want),sorted(success^want)[:15])
        for x in range(2*n):assert not synchronous(g,(x,)),(n,x)
        deg=Counter()
        exchange=set()
        for pair in success:
            for x in pair:deg[x]+=1
            for x in pair:
                for y in range(2*n):
                    other=tuple(sorted((set(pair)-{x})|{y}))
                    if len(other)==2 and other in success and other !=pair: exchange.add(tuple(sorted((pair,other))))
        assert len(exchange)==30*n,(n,len(exchange))
        assert set(deg.values())=={6},(n,deg)
        # Connectedness of the line graph via pair-exchange adjacency.
        adj={x:set() for x in success}
        for a,b in exchange: adj[a].add(b);adj[b].add(a)
        assert all(len(t)==10 for t in adj.values()),(n,Counter(map(len,adj.values())))
        reached=set();todo=[next(iter(success))]
        while todo:
            x=todo.pop()
            if x in reached:continue
            reached.add(x);todo.extend(adj[x]-reached)
        assert len(reached)==6*n
        if n>=13:
            threes=set()
            for v in range(2*n):
                ds=dist(g,v)
                threes.update(tuple(sorted((v,w))) for w,d in enumerate(ds) if d==3)
            failures={tuple(sorted((n+i,n+(i+6)%n))) for i in range(n)}
            assert len(threes)==7*n,(n,len(threes))
            assert threes-success==failures,(n,len(threes-success),len(failures))
            assert len(failures)==n
        print('PAIR_EXHAUSTIVE_OK',n,'minimum_sets',len(success),'exchange_edges',len(exchange))
    for n in (21,22,23,29,37,61):
        g=graph(n)
        want=expected(n)
        success={S for S in combinations(range(2*n),2) if synchronous(g,S)}
        assert success==want,(n,success^want)
        print('PAIR_GENERAL_STRESS_OK',n,'minimum_sets',len(success))
    # The bad alleged distance-three example at n=13.
    n=13;g=graph(n);x=n;y=n+6
    observed,frames=synchronous(g,(x,y),True)
    assert dist(g,x)[y]==3
    assert len(frames)==2 and len(observed)==10 and len(observed)<2*n
    assert all(sum(w not in observed for w in g[v])!=1 for v in observed)
    print('DISTANCE_THREE_COUNTEREXAMPLE_OK n=13 inner_pair=(0,6) observed=10/26 stalled')
    # Local symbolic forcing footprints stabilize for n >= 21.
    bad={
       ('OO',1):(0,6),('OO',2):(1,10),
       ('OI',0):(0,6),('OI',1):(1,10),('OI',2):(1,10),
       ('II',2):(0,6),('II',4):(1,8),('II',6):(1,10),
    }
    good={('OO',3):1,('OI',3):2,('OI',4):3,('II',1):1}
    for n in (21,22,49,97):
        g=graph(n)
        for (typ,d),(rounds,size) in bad.items():
            a=0 if typ!='II' else n
            b=(d if typ=='OO' else n+d) if typ!='II' else n+d
            done,frames=synchronous(g,(a,b),True)
            assert len(frames)-1==rounds and len(done)==size,(n,typ,d,len(frames)-1,len(done))
            assert all(sum(w not in done for w in g[v])!=1 for v in done)
        for (typ,d),rounds in good.items():
            a=0 if typ!='II' else n
            b=(d if typ=='OO' else n+d) if typ!='II' else n+d
            done,frames=synchronous(g,(a,b),True)
            assert len(done)==2*n
            assert any(all(i%n in frame and n+i%n in frame for i in range(j,j+4)) for frame in frames[:rounds+1] for j in range(n)),(n,typ,d)
    print('LOCAL_PROOF_FOOTPRINTS_OK')
    print('ALL_VERIFY_OK')
if __name__=='__main__':run()
