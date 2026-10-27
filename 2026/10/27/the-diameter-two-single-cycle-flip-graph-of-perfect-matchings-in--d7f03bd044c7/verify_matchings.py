"""Independent perfect-matching enumeration and symmetric-difference test."""
import itertools,collections

def verify(n):
    base=sorted({tuple(sorted(p)) for i in range(n) for p in
                 ((i,(i+1)%n),(n+i,n+(i+1)%n),(i,n+i))})
    incident=[[] for _ in range(2*n)]
    for j,(u,v) in enumerate(base):incident[u].append(j);incident[v].append(j)
    socket={(v,j):k for k,(v,j) in enumerate((v,j) for v in range(2*n)
                                                  for j in incident[v])}
    tri_edges={tuple(sorted((socket[v,i],socket[v,j]))) for v in range(2*n)
               for i,j in itertools.combinations(incident[v],2)}
    long_edges={tuple(sorted((socket[u,j],socket[v,j]))) for j,(u,v) in enumerate(base)}
    edges=sorted(tri_edges|long_edges)
    adj=[[] for _ in range(6*n)]
    for j,(u,v) in enumerate(edges):adj[u].append((v,j));adj[v].append((u,j))
    matchings=[]
    def visit(unmatched,selected):
        if unmatched==0:matchings.append(selected);return
        low=unmatched&-unmatched;u=low.bit_length()-1
        for v,j in adj[u]:
            if (unmatched>>v)&1:visit(unmatched^low^(1<<v),selected|(1<<j))
    visit((1<<(6*n))-1,0)
    assert len(matchings)==2**(n+1)
    # In each matching, count absent long edges; these give an even subgraph.
    base_to_long={j:edges.index(tuple(sorted((socket[u,j],socket[v,j]))))
                  for j,(u,v) in enumerate(base)}
    edge_index={e:j for j,e in enumerate(base)}
    rim_top=[edge_index[tuple(sorted((i,(i+1)%n)))] for i in range(n)]
    rim_bottom=[edge_index[tuple(sorted((n+i,n+(i+1)%n)))] for i in range(n)]
    coords=[]
    for m in matchings:
        F=sum((1<<j) for j,e in base_to_long.items() if not((m>>e)&1))
        bottom=[(F>>j)&1 for j in rim_bottom]
        top=[(F>>j)&1 for j in rim_top]
        a=top[0]^bottom[0]
        assert all((top[i]^bottom[i])==a for i in range(n))
        coords.append((a,sum(t<<i for i,t in enumerate(bottom))))
    assert len(set(coords))==len(matchings)
    def cycle_xor(a,b):
        mask=a^b;local=collections.defaultdict(set)
        for j,(u,v) in enumerate(edges):
            if mask>>j&1:local[u].add(v);local[v].add(u)
        if not local:return False
        assert all(len(x)==2 for x in local.values())
        seen=set();stack=[next(iter(local))]
        while stack:
            v=stack.pop()
            if v not in seen:
                seen.add(v);stack.extend(local[v]-seen)
        return len(seen)==len(local)
    def cyclic_interval(bits):
        if bits==0 or bits==(1<<n)-1:return False
        return sum(((bits>>i)&1)!=((bits>>((i-1)%n))&1) for i in range(n))==2
    count=0
    for i in range(len(matchings)):
        for j in range(i+1,len(matchings)):
            a,x=coords[i];b,y=coords[j]
            prediction=(a!=b) or cyclic_interval(x^y)
            observed=cycle_xor(matchings[i],matchings[j])
            assert prediction==observed,(n,i,j)
            count+=int(observed)
    assert count==len(matchings)*(2**n+n*(n-1))//2
    print('n=%d matchings=%d verified_edges=%d verified_join=yes' %
          (n,len(matchings),count))
for n in range(3,8):verify(n)
