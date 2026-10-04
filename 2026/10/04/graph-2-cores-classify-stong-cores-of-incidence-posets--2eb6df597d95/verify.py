from itertools import combinations


def components(n, edges):
    adj=[set() for _ in range(n)]
    for a,b in edges:
        adj[a].add(b); adj[b].add(a)
    seen=set(); out=[]
    for s in range(n):
        if s in seen: continue
        stack=[s]; seen.add(s); vs=[]
        while stack:
            v=stack.pop(); vs.append(v)
            for w in adj[v]:
                if w not in seen:
                    seen.add(w); stack.append(w)
        es=[e for e in edges if e[0] in vs and e[1] in vs]
        out.append((set(vs),es))
    return out


def two_core(n, edges):
    adj=[set() for _ in range(n)]
    alive=[True]*n
    eset=set(tuple(sorted(e)) for e in edges)
    for a,b in eset:
        adj[a].add(b); adj[b].add(a)
    q=[v for v in range(n) if len(adj[v])<2]
    qi=0
    while qi < len(q):
        v=q[qi]; qi+=1
        if not alive[v] or len(adj[v])>=2: continue
        alive[v]=False
        for w in list(adj[v]):
            adj[w].remove(v)
            adj[v].remove(w)
            if alive[w] and len(adj[w])<2:
                q.append(w)
    vs={v for v in range(n) if alive[v]}
    es={e for e in eset if e[0] in vs and e[1] in vs}
    return vs,es


def tree_component_count(n, edges):
    t=0
    for vs,es in components(n, edges):
        # connected finite simple component is a tree iff |E|=|V|-1.
        if len(es)==len(vs)-1: t+=1
    return t


def incidence_poset(n, edges):
    edges=sorted(tuple(sorted(e)) for e in edges)
    elems=[('v',i) for i in range(n)] + [('e',e) for e in edges]
    le={(x,x) for x in elems}
    for e in edges:
        ee=('e',e)
        le.add((('v',e[0]),ee)); le.add((('v',e[1]),ee))
    return elems,le


def strict_upper(x, elems, le):
    return [y for y in elems if y!=x and (x,y) in le]

def strict_lower(x, elems, le):
    return [y for y in elems if y!=x and (y,x) in le]

def is_up_beat(x, elems, le):
    U=strict_upper(x,elems,le)
    return any(all((m,u) in le for u in U) for m in U)

def is_down_beat(x, elems, le):
    L=strict_lower(x,elems,le)
    return any(all((l,m) in le for l in L) for m in L)

def delete_poset(x, elems, le):
    e2=[z for z in elems if z!=x]
    l2={(a,b) for (a,b) in le if a!=x and b!=x}
    return e2,l2


def paired_leaf_reduction(n, edges):
    edges=set(tuple(sorted(e)) for e in edges)
    elems,le=incidence_poset(n,edges)
    alive=set(range(n))
    steps=0
    while True:
        deg={v:0 for v in alive}
        for a,b in edges:
            if a in alive and b in alive:
                deg[a]+=1; deg[b]+=1
        leaves=[v for v,d in deg.items() if d==1]
        if not leaves: break
        v=min(leaves)
        e=next(e for e in edges if v in e and e[0] in alive and e[1] in alive)
        vx=('v',v); ex=('e',e)
        assert is_up_beat(vx,elems,le), (n,edges,v,'vertex not up beat')
        elems,le=delete_poset(vx,elems,le)
        assert is_down_beat(ex,elems,le), (n,edges,e,'edge not down beat after leaf')
        elems,le=delete_poset(ex,elems,le)
        alive.remove(v); edges.remove(e); steps+=2
    return elems,le,alive,edges,steps


def verify_graph(n, edges):
    c_vs,c_es=two_core(n,edges)
    t=tree_component_count(n,edges)
    elems,le,alive,ered,steps=paired_leaf_reduction(n,edges)
    # Each cyclic component reduces to its graph 2-core; each tree component to one isolated vertex.
    expected_size=len(c_vs)+len(c_es)+t
    assert len(elems)==expected_size, (n,edges,len(elems),expected_size)
    # Result must be minimal.
    assert not any(is_up_beat(x,elems,le) or is_down_beat(x,elems,le) for x in elems)
    # Non-isolated vertices/edges in the reduced poset recover precisely the 2-core.
    nonisol=[x for x in elems if strict_upper(x,elems,le) or strict_lower(x,elems,le)]
    got_v={x[1] for x in nonisol if x[0]=='v'}
    got_e={x[1] for x in nonisol if x[0]=='e'}
    assert got_v==c_vs, (n,edges,got_v,c_vs)
    assert got_e==c_es, (n,edges,got_e,c_es)
    isolated=[x for x in elems if not strict_upper(x,elems,le) and not strict_lower(x,elems,le)]
    assert len(isolated)==t
    return steps


def main():
    total=0; reductions=0; max_steps=0
    by_n=[]
    for n in range(1,7):
        pairs=list(combinations(range(n),2))
        cnt=0
        for mask in range(1<<len(pairs)):
            edges={pairs[i] for i in range(len(pairs)) if (mask>>i)&1}
            st=verify_graph(n,edges)
            reductions += st
            max_steps=max(max_steps,st)
            total+=1; cnt+=1
        by_n.append((n,cnt))
    # Explicit contrast: C3 and C4 have graph homotopy type S^1, but minimal incidence-poset cores of sizes 6 and 8.
    for n in (3,4):
        cyc={(i,(i+1)%n) if i<(i+1)%n else ((i+1)%n,i) for i in range(n)}
        cyc={tuple(sorted(e)) for e in cyc}
        elems,le,_,_,_=paired_leaf_reduction(n,cyc)
        assert len(elems)==2*n
        assert not any(is_up_beat(x,elems,le) or is_down_beat(x,elems,le) for x in elems)
    print('VERIFY_OK')
    print('labeled_graphs_checked', total)
    print('graphs_by_order', by_n)
    print('beat_deletions_replayed', reductions)
    print('max_beat_deletions_single_graph', max_steps)
    print('cycle_core_sizes', {3:6,4:8})

if __name__=='__main__':
    main()
