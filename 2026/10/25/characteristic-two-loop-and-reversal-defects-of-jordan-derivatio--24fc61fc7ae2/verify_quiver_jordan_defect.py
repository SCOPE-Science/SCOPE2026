#!/usr/bin/env python3
from collections import Counter


def rank_mod_p(rows,p):
    if not rows:return 0
    work=[[z%p for z in row] for row in rows]
    pivot=0
    for col in range(len(work[0])):
        r=next((t for t in range(pivot,len(work)) if work[t][col]),None)
        if r is None:continue
        work[pivot],work[r]=work[r],work[pivot]
        inv=pow(work[pivot][col],-1,p)
        work[pivot]=[(inv*y)%p for y in work[pivot]]
        for i in range(pivot+1,len(work)):
            if work[i][col]:
                scale=work[i][col]
                work[i]=[(a-scale*b)%p for a,b in zip(work[i],work[pivot])]
        pivot+=1
        if pivot==len(work):break
    return pivot


def run_case(name,n,arrows):
    basis=[('e',i,i) for i in range(n)]+[('a',i,j) for i,j in arrows]
    d=len(basis)
    def prod(a,b):
        k,i,j=basis[a]; h,u,v=basis[b]
        if k=='e' and h=='e':return b if i==u else None
        if k=='e' and h=='a':return b if i==u else None
        if k=='a' and h=='e':return a if j==u else None
        return None
    def cons(a,b):
        mat=[[0]*(d*d) for _ in range(d)]
        c=prod(a,b)
        if c is not None:
            for t in range(d):mat[t][c*d+t]+=1
        for t in range(d):
            c=prod(t,b)
            if c is not None:mat[c][a*d+t]-=1
            c=prod(a,t)
            if c is not None:mat[c][b*d+t]-=1
        return mat
    jordan=[]; deriv=[]
    for a in range(d):
        for b in range(d):
            ab=cons(a,b)
            deriv+=ab
            if b<a:continue
            if a==b:jordan+=ab
            else:
                ba=cons(b,a)
                jordan.extend([[s+t for s,t in zip(r,rr)] for r,rr in zip(ab,ba)])
    c=Counter(arrows); loops=[c[(u,u)] for u in range(n)]
    reverse=sum(c[(u,v)]*c[(v,u)] for u in range(n) for v in range(n) if u!=v)
    adj=[set() for _ in range(n)]
    for u,v in arrows:
        if u!=v:adj[u].add(v);adj[v].add(u)
    components=[];seen=set()
    for u in range(n):
        if u in seen:continue
        stack=[u];seen.add(u);comp=[]
        while stack:
            k=stack.pop();comp.append(k)
            for v in adj[k]:
                if v not in seen:seen.add(v);stack.append(v)
        components.append(comp)
    numcomp=len(components)
    L=sum(loops)
    singleton_loop=sum(loops[u]==1 and not adj[u] for u in range(n))
    cross=sum(loops[u]*loops[v] for u in range(n) for v in range(n) if u!=v)
    expected={2:reverse+cross+L*numcomp-singleton_loop,3:reverse,5:reverse}
    for p in (2,3,5):
        delta=rank_mod_p(deriv,p)-rank_mod_p(jordan,p)
        assert delta==expected[p],(name,p,delta,expected[p])
    print(name,'dim',d,'diff-char2',expected[2],'diff-odd',reverse)

cases=[
 ('one_vertex_no_loop',1,[]),('one_vertex_one_loop',1,[(0,0)]),('one_vertex_two_loops',1,[(0,0),(0,0)]),
 ('two_isolated_loops',2,[(0,0),(1,1)]),('single_arrow',2,[(0,1)]),
 ('double_arrow',2,[(0,1),(1,0)]),('double_arrow_multiplicity',2,[(0,1),(0,1),(1,0)]),
 ('loop_arrow',2,[(0,0),(0,1)]),('loop_arrow_reverse',2,[(0,0),(0,1),(1,0)]),
 ('loop_other_isolated',3,[(0,0),(0,1)]),('one_edge_and_loop_isolated',3,[(0,1),(2,2)]),
 ('two_loops_with_edge',2,[(0,0),(1,1),(0,1)]),
 ('cycle_three',3,[(0,1),(1,2),(2,0)]),
 ('cycle_three_one_loop',3,[(0,0),(0,1),(1,2),(2,0)]),
 ('two_cycles_disjoint',4,[(0,1),(1,0),(2,3),(3,2)]),
 ('chain_three_two_loops',3,[(0,0),(2,2),(0,1),(1,2)]),
]
for name,n,arrows in cases:run_case(name,n,arrows)
print('QUIVER_JORDAN_DEFECT_OK',len(cases),'examples')
