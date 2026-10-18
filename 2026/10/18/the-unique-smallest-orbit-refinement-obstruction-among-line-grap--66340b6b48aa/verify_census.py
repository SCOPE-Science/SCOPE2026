#!/usr/bin/env python3
"""Exact census of orbit-refinement gaps in line graphs of unlabelled trees <=9 vertices.
Uses no external packages. Run: python3 line_tree_verify_draft.py
"""

def canonical_tree(edges, n):
    adj=[[] for _ in range(n)]
    for a,b in edges:adj[a].append(b);adj[b].append(a)
    def rootcode(u, parent):
        return '('+''.join(sorted(rootcode(v,u) for v in adj[u] if v!=parent))+')'
    return min(rootcode(u,-1) for u in range(n))

def edge_orbits(edges, n, marked=()):
    adj=[[] for _ in range(n)]
    for idx,(a,b) in enumerate(edges):adj[a].append((b,idx));adj[b].append((a,idx))
    marks={x:i+1 for i,x in enumerate(marked)}
    def branch(x, parent):
        return '('+''.join(sorted(str(marks.get(j,0))+branch(y,x)
                   for y,j in adj[x] if y!=parent))+')'
    out=[]
    for idx,(a,b) in enumerate(edges):
        out.append((marks.get(idx,0),tuple(sorted((branch(a,b),branch(b,a))))))
    return out

def color_refinement(edges, n, marked=()):
    m=len(edges)
    nbr=[[] for _ in range(m)]
    for i in range(m):
        for j in range(i):
            if (set(edges[i]) & set(edges[j])):
                nbr[i].append(j);nbr[j].append(i)
    marks={x:i+1 for i,x in enumerate(marked)}
    colors=[marks.get(i,0) for i in range(m)]
    for t in range(m+1):
        descriptors=[(colors[i],tuple(sorted(colors[j] for j in nbr[i]))) for i in range(m)]
        dictionary={desc:i for i,desc in enumerate(sorted(set(descriptors)))}
        update=[dictionary[desc] for desc in descriptors]
        if len(set(update))==len(set(colors)):
            return update,t+1
        colors=update
    raise AssertionError('colour refinement exceeds vertex bound')

def all_trees(upto):
    layer=[tuple()]
    yield 1,layer
    for n in range(2,upto+1):
        d={}
        for e in layer:
            for vertex in range(n-1):
                f=e+((vertex,n-1),)
                code=canonical_tree(f,n)
                d.setdefault(code,f)
        layer=list(d.values())
        yield n,layer

TOTAL=[];bad=[]
for n,trees in all_trees(9):
    for e in trees:
        orbit=edge_orbits(e,n) if e else []
        colors,_=color_refinement(e,n) if e else ([],0)
        image={}
        for c,o in zip(colors,orbit):
            if c in image and image[c]!=o:
                bad.append((n,e,len(set(colors)),len(set(orbit))))
                break
            image[c]=o
    TOTAL.append((n,len(trees),sum(x[0]==n for x in bad)))
assert TOTAL==[(1,1,0),(2,1,0),(3,1,0),(4,2,0),(5,3,0),(6,6,0),(7,11,0),(8,23,0),(9,47,1)],TOTAL
assert len(bad)==1
n,exception,wl_count,orbit_count=bad[0]
assert (wl_count,orbit_count)==(2,3)
for e in range(8):
    colors,_=color_refinement(exception,9,(e,))
    orbit=edge_orbits(exception,9,(e,))
    assert all(not (colors[i]==colors[j] and orbit[i]!=orbit[j])
               for i in range(8) for j in range(8))
print('CENSUS',TOTAL)
print('EXCEPTION',exception)
print('UNMARKED_WL_ORBITS',wl_count,orbit_count)
print('ALL_EIGHT_SINGLE_MARKINGS_RECOVER_ORBITS',True)
print('VERIFY_OK')
