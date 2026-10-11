from itertools import combinations

def bits(mask,n):
    return {i for i in range(n) if mask>>i & 1}

def powerset_nonempty(vals):
    vals=tuple(vals); m=len(vals)
    for z in range(1,1<<m):
        yield frozenset(vals[i] for i in range(m) if z>>i & 1)

def connected(adj):
    n=len(adj); seen={0}; stack=[0]
    while stack:
        v=stack.pop()
        for w in adj[v]:
            if w not in seen: seen.add(w); stack.append(w)
    return len(seen)==n

def bipartition(adj):
    n=len(adj); col=[-1]*n; col[0]=0; q=[0]
    for v in q:
        for w in adj[v]:
            if col[w]<0: col[w]=1-col[v]; q.append(w)
            elif col[w]==col[v]: return None
    return ({i for i,c in enumerate(col) if c==0},{i for i,c in enumerate(col) if c==1})

def square_free(adj):
    n=len(adj)
    for u in range(n):
        for v in range(u+1,n):
            if len(adj[u]&adj[v])>=2: return False
    return True

def neighborhood_complex(adj):
    K=set()
    for N in adj:
        K.update(powerset_nonempty(sorted(N)))
    return K

def target(adj, side, centers):
    faces={frozenset((v,)) for v in side}
    for c in centers:
        N=sorted(adj[c])
        r=N[0]
        for x in N:
            if x!=r:
                faces.add(frozenset((r,x)))
    return faces

def collapse_side(K,adj,side,centers):
    pairs=[]
    for c in centers:
        N=sorted(adj[c]); r=N[0]; rest=[x for x in N if x!=r]
        for k in range(len(rest),1,-1):
            for comb in combinations(rest,k):
                s=frozenset(comb); t=frozenset((*comb,r)); pairs.append((s,t,c))
    # Global decreasing lower-face size; center order only breaks ties.
    pairs.sort(key=lambda p:(-len(p[0]),p[2],tuple(sorted(p[0]))))
    count=0
    for s,t,c in pairs:
        if s not in K or t not in K:
            raise AssertionError(('missing pair',s,t,c))
        cofaces=[f for f in K if s < f]
        if cofaces != [t] and set(cofaces)!={t}:
            raise AssertionError(('not free',s,t,c,cofaces))
        K.remove(s); K.remove(t); count+=1
    return count

def check(adj):
    part=bipartition(adj); assert part is not None
    A,B=part; K=neighborhood_complex(adj)
    # Bipartite neighborhood faces must not cross sides.
    assert all(f<=A or f<=B for f in K)
    expected=target(adj,A,B)|target(adj,B,A)
    work=set(K)
    c=collapse_side(work,adj,A,B)+collapse_side(work,adj,B,A)
    assert work==expected, (work^expected)
    # Target edge uniqueness and connectedness/rank on each side.
    e=sum(len(N) for N in adj)//2; n=len(adj); beta=e-n+1
    for side,centers in ((A,B),(B,A)):
        E=[f for f in expected if len(f)==2 and f<=side]
        assert len(E)==e-len(centers)
        tadj={v:set() for v in side}
        for uv in E:
            u,v=tuple(uv); tadj[u].add(v); tadj[v].add(u)
        root=next(iter(side)); seen={root}; stack=[root]
        while stack:
            v=stack.pop()
            for w in tadj[v]:
                if w not in seen: seen.add(w); stack.append(w)
        assert seen==side
        assert len(E)-len(side)+1==beta
    return len(K),c,beta

def pg2_incidence(q):
    reps=[]
    seen=set()
    for x in range(q):
      for y in range(q):
       for z in range(q):
        if (x,y,z)==(0,0,0): continue
        v=(x,y,z)
        i=next(i for i,a in enumerate(v) if a%q)
        inv=pow(v[i],-1,q)
        r=tuple((a*inv)%q for a in v)
        if r not in seen: seen.add(r); reps.append(r)
    reps.sort(); m=len(reps); adj=[set() for _ in range(2*m)]
    for i,pv in enumerate(reps):
      for j,lv in enumerate(reps):
        if sum(a*b for a,b in zip(pv,lv))%q==0:
          adj[i].add(m+j); adj[m+j].add(i)
    return adj

def main():
    total=0; collapses=0; faces=0; beta_max=0; by_n={}
    for n in range(2,7):
        edges=list(combinations(range(n),2)); good=0
        for mask in range(1,1<<len(edges)):
            adj=[set() for _ in range(n)]
            for j,(u,v) in enumerate(edges):
                if mask>>j & 1: adj[u].add(v); adj[v].add(u)
            if not connected(adj): continue
            if bipartition(adj) is None or not square_free(adj): continue
            F,C,b=check(adj)
            total+=1; good+=1; collapses+=C; faces+=F; beta_max=max(beta_max,b)
        by_n[n]=good
    pg=[]
    for q in (2,3,5):
        adj=pg2_incidence(q)
        assert connected(adj) and bipartition(adj) is not None and square_free(adj)
        F,C,b=check(adj)
        assert b==q**3
        pg.append((q,len(adj),sum(map(len,adj))//2,F,C,b))
    print('VERIFY_OK')
    print('connected_labeled_bipartite_square_free_graphs_n2_to_n6=',total)
    print('by_n=',by_n)
    print('neighborhood_faces_checked=',faces)
    print('elementary_collapses_checked=',collapses)
    print('maximum_cycle_rank_seen=',beta_max)
    print('projective_plane_checks_q_v_e_faces_collapses_beta=',pg)
if __name__=='__main__': main()
