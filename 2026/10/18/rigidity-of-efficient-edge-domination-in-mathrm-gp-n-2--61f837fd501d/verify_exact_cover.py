"""Exact-cover enumeration of dominating induced matchings in GP(n,2).

A chosen edge covers its closed edge-neighborhood; exact cover is equivalent
 to efficient edge domination. No external dependencies.
"""
import json

def graph_edges(n):
    return sorted({tuple(sorted(e)) for i in range(n) for e in ((i,(i+1)%n),(i,n+i),(n+i,n+(i+2)%n))})

def dim_sets(n):
    edges=graph_edges(n)
    m=len(edges)
    assert m==3*n
    adj_masks=[]
    for a,b in edges:
        mask=sum((1<<j) for j,(c,d) in enumerate(edges) if a==c or a==d or b==c or b==d)
        assert mask.bit_count()==5
        adj_masks.append(mask)
    candidates=[[] for _ in range(m)]
    for j,mask in enumerate(adj_masks):
        for i in range(m):
            if mask>>i&1:candidates[i].append(j)
    result=[]
    def visit(covered,chosen):
        if covered==(1<<m)-1:
            result.append(frozenset(edges[j] for j in chosen));return
        chosen_opts=None
        for i in range(m):
            if covered>>i&1:continue
            opts=[j for j in candidates[i] if not (adj_masks[j]&covered)]
            if not opts:return
            if chosen_opts is None or len(opts)<len(chosen_opts):chosen_opts=opts
            if len(chosen_opts)==1:break
        for j in chosen_opts:
            visit(covered|adj_masks[j],chosen+[j])
    visit(0,[])
    assert len(set(result))==len(result)
    return edges,set(result)

def expected(n):
    if n%5:return set()
    fam=set()
    for r in range(5):
        es=set()
        for i in range(n):
            if i%5==(r+3)%5:es.add(tuple(sorted((i,(i+1)%n))))
            if i%5==(r+1)%5:es.add(tuple(sorted((i,n+i))))
            if i%5==r:es.add(tuple(sorted((n+i,n+(i+2)%n))))
        assert len(es)==3*n//5
        fam.add(frozenset(es))
    return fam

out=[]
for n in range(5,41):
    edges,found=dim_sets(n)
    want=expected(n)
    assert found==want,(n,len(found),len(want))
    if n%5==0:
        assert set.union(*(set(x) for x in found))==set(edges)
        assert sum(len(x) for x in found)==len(edges)
    out.append({'n':n,'dominating_induced_matchings':len(found),'expected':len(want)})
print(json.dumps({'status':'PASS','method':'edge-neighborhood exact cover, all solutions','orders':out,'verified_construction':'all five classes partition edges, n multiple of five'},sort_keys=True,separators=(',',':')))
