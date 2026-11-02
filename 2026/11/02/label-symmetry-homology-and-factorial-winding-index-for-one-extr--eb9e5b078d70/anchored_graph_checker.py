"""Finite reproducibility for the one-extra-label anchored graph theorem.
Usage: python3 anchored_graph_checker.py. Pure Python stdlib, no external input.
"""
from itertools import permutations,product
from collections import deque,defaultdict
from math import factorial,comb

def verify_graph(name,k,undirected_edges):
    n=k+1
    E=tuple(sorted(tuple(sorted(uv)) for uv in undirected_edges))
    assert len(E)==len(set(E)) and all(0<=u<v<k for u,v in E)
    assert len(E)>=k
    site_states=tuple(s for s in product(range(k),repeat=n) if len(set(s))==k)
    lookup={s:i for i,s in enumerate(site_states)}
    assert len(site_states)==k*factorial(n)//2
    edges=[]
    # An edge has one moving coordinate and k stationary labels assigned bijectively.
    for u,v in E:
        for active in range(n):
            others=[j for j in range(n) if j!=active]
            for arr in permutations(range(k)):
                st=[-1]*n
                for label,pos in zip(others,arr): st[label]=pos
                a=st.copy(); b=st.copy();a[active]=u;b[active]=v
                edges.append(((u,v),active,lookup[tuple(a)],lookup[tuple(b)]))
    assert len(edges)==len(E)*factorial(n)
    links=[[] for s in site_states]
    for _,_,a,b in edges:links[a].append(b);links[b].append(a)
    seen={0}; queue=deque([0])
    while queue:
        for j in links[queue.popleft()]:
            if j not in seen:seen.add(j);queue.append(j)
    assert len(seen)==len(site_states),(name,'not connected')
    def double_site(s):
        return next(j for j in range(k) if s.count(j)==2)
    # Orbit-sum invariant-chain boundary must be twice the ordinary graph incidence.
    for u,v in E:
        bd=defaultdict(int)
        for (uv,active,i,j) in edges:
            if uv==(u,v):bd[i]-=1;bd[j]+=1
        for ix,s in enumerate(site_states):
            expected=2*((double_site(s)==v)-(double_site(s)==u))
            assert bd[ix]==expected,(name,(u,v),ix,bd[ix],expected)
    # Exact fixed cellular trace for every permutation of particle labels.
    counts=defaultdict(int)
    for p in permutations(range(n)):
        inv=[p.index(i) for i in range(n)]
        def image(s):return tuple(s[inv[i]] for i in range(n))
        vf=sum(image(st)==st for st in site_states)
        ef=sum(image(site_states[a])==site_states[a] and image(site_states[b])==site_states[b] for _,_,a,b in edges)
        trace=1+ef-vf
        moved=sum(p[i]!=i for i in range(n))
        transposition=moved==2 and all(p[p[i]]==i for i in range(n))
        expected=(1+len(E)*factorial(n)-k*factorial(n)//2 if moved==0 else
                  1-k*factorial(n-2) if transposition else 1)
        assert trace==expected,(name,p,trace,expected)
        counts['id' if moved==0 else 'transposition' if transposition else 'other']+=1
    b1=len(edges)-len(site_states)+1
    assert b1==1+factorial(n)*(len(E)-k//2) if k%2==0 else b1==1+len(E)*factorial(n)-k*factorial(n)//2
    print(name,'vertices',len(site_states),'edges',len(edges),'b1',b1,'permutations_checked',sum(counts.values()),'invariant_orbit_boundary_2x_incidence','PASS')

verify_graph('triangle',3,[(0,1),(1,2),(0,2)])
verify_graph('square',4,[(0,1),(1,2),(2,3),(0,3)])
verify_graph('square_with_diagonal',4,[(0,1),(1,2),(2,3),(0,3),(0,2)])
verify_graph('complete_four',4,[(0,1),(0,2),(0,3),(1,2),(1,3),(2,3)])
verify_graph('five_cycle',5,[(0,1),(1,2),(2,3),(3,4),(0,4)])
verify_graph('triangle_with_two_pendants',5,[(0,1),(1,2),(0,2),(0,3),(3,4)])
print('ONE_EXTRA_ANCHORED_GRAPH_EQUIVARIANT_CHECKS_OK')
