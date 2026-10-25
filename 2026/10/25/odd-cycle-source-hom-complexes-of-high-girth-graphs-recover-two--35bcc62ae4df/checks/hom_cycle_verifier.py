"""Finite reproducibility checks for odd-cycle-source graph Hom complexes.
Only the Python standard library is required. These checks do not replace the all-parameter proof.
"""
from collections import Counter, defaultdict
from itertools import combinations
from math import comb

def add_edge(E,u,v): E.add(tuple(sorted((u,v))))
def cycle(n,offset=0):
    E=set()
    for i in range(n): add_edge(E,offset+i,offset+(i+1)%n)
    return E

def target_graphs():
    petersen=cycle(5)
    for i in range(5):add_edge(petersen,i,5+i)
    for i in range(5):add_edge(petersen,5+i,5+(i+2)%5)
    a=cycle(5);add_edge(a,0,5)
    b=cycle(5);add_edge(b,0,5); add_edge(b,5,6)
    c=cycle(5)|cycle(7,5);add_edge(c,0,5)
    d=cycle(5)|cycle(7,4) # share one common vertex 4
    e=cycle(7)
    f=cycle(9)
    return [('pentagon',cycle(5),5),('pentagon_plus_leaf',a,5),('pentagon_plus_two_leaves',b,5),
            ('petersen',petersen,5),('pentagon_heptagon_bridge',c,5),('pentagon_heptagon_wedge',d,5),
            ('heptagon',e,5),('nonagon',f,7)]

def adj_of(E):
    n=1+max(max(e) for e in E)
    A=[set() for _ in range(n)]
    for a,b in E:A[a].add(b);A[b].add(a)
    return A

def cycles_of_length(A,k):
    found=set(); n=len(A)
    for v in range(n):
        def rec(path,seen):
            if len(path)==k:
                if v in A[path[-1]]:
                    q=path
                    candidates=[]
                    for t in range(k):
                        u=q[t:]+q[:t];candidates.append(tuple(u));candidates.append(tuple(reversed(u)))
                    found.add(min(candidates))
                return
            for w in A[path[-1]]:
                if w not in seen and w>=v:
                    rec(path+[w],seen|{w})
        rec([v],{v})
    return found

def homomorphisms(A,m):
    n=len(A); out=[];cur=[-1]*m
    def rec(i):
        if i==m:
            if cur[0] in A[cur[-1]]: out.append(tuple(cur))
            return
        if i==0: options=range(n)
        else: options=A[cur[i-1]]
        for v in options:cur[i]=v;rec(i+1)
    rec(0)
    return out

def analyze(name,E,g):
    A=adj_of(E);m=g+2; vs=homomorphisms(A,m);idx={v:i for i,v in enumerate(vs)}
    flex={};grouped={}
    for i,walk in enumerate(vs):
        for j in range(m):
            choices=A[walk[(j-1)%m]] & A[walk[(j+1)%m]]
            if len(choices)>1:
                key=(j,walk[:j]+walk[j+1:]);grouped[key]=choices
    maxcells=set()
    for (j,other),choices in grouped.items():
        ids=[]
        for x in sorted(choices):
            walk=other[:j]+(x,)+other[j:]
            ids.append(idx[walk])
        maxcells.add(tuple(sorted(ids)))
    # Confirm no multi-coordinate prodsimplicial cell exists.
    for walk in vs:
        candidates=[i for i in range(m) if len(A[walk[(i-1)%m]] & A[walk[(i+1)%m]])>1]
        for i,j in combinations(candidates,2):
            B=A[walk[(i-1)%m]] & A[walk[(i+1)%m]]
            C=A[walk[(j-1)%m]] & A[walk[(j+1)%m]]
            if abs(i-j)%m not in (1,m-1):
                raise AssertionError((name,'disjoint flexible positions',walk,i,j))
            assert not all(y in A[x] for x in B for y in C), (name,walk,i,j)
    one=[frozenset((j,k)) for cell in maxcells for j,k in combinations(cell,2)]
    neighbors=[set() for _ in vs]
    for j,k in one: neighbors[j].add(k);neighbors[k].add(j)
    visited=set();cc=[]
    for i in range(len(vs)):
        if i in visited: continue
        todo=[i];visited.add(i);co=[]
        while todo:
            u=todo.pop();co.append(u)
            for v in neighbors[u]:
                if v not in visited: visited.add(v);todo.append(v)
        cc.append(set(co))
    chi=[]
    for co in cc:
        cells=[cell for cell in maxcells if cell[0] in co]
        # Include zero-dimensional vertices as a separate term, then higher faces in each simplex
        # (no two maximal simplices share an edge in these examples).
        shared=[frozenset((u,v)) for cell in cells for u,v in combinations(cell,2)]
        assert len(shared)==len(set(shared)),(name,'duplicate edge')
        val=len(co)+sum((-1)**(k-1)*sum(comb(len(cell),k) for cell in cells) for k in range(2,max(map(len,cells),default=1)+1))
        chi.append(val)
    c_g=len(cycles_of_length(A,g)); c_gp2=len(cycles_of_length(A,g+2)); expected_circles=2*c_g;expected_points=2*(g+2)*c_gp2
    got_circles=sum(z==0 for z in chi);got_points=sum(z==1 for z in chi)
    assert len(cc)==expected_circles+expected_points,(name,len(cc),expected_circles,expected_points)
    assert got_circles==expected_circles and got_points==expected_points,(name,Counter(chi),expected_circles,expected_points)
    # For this family every component is a point or collapses onto a polygon,
    # as established separately in the structural proof.
    return {'graph':name,'g':g,'V':len(A),'E':len(E),'hom_vertices':len(vs),'components':len(cc),
            'circle_components':got_circles,'isolated_components':got_points,
            'maximal_nontrivial_cells':len(maxcells),'max_simplex_vertices':max(map(len,maxcells),default=1),
            'component_sizes':sorted(Counter(map(len,cc)).items())}

if __name__=='__main__':
    import json
    for name,E,g in target_graphs(): print(json.dumps(analyze(name,E,g),sort_keys=True))
