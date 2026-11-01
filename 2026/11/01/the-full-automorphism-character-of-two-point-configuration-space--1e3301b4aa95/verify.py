#!/usr/bin/env python3
"""Independent finite examples for the graph-automorphism character of two-point tree configurations.
Only the Python standard library is required. This is a finite check, not a proof of the universal theorem.
"""
import itertools
import collections

def vertices_edges(n, edges):
    ee=sorted(tuple(sorted(e)) for e in edges)
    assert len(ee)==n-1 and len(set(ee))==len(ee)
    return ee

def automorphisms(n, edges):
    E=set(edges)
    deg=[0]*n
    for a,b in E:deg[a]+=1;deg[b]+=1
    groups={d:[v for v in range(n) if deg[v]==d] for d in sorted(set(deg))}
    seq=list(groups.values())
    for choices in itertools.product(*(itertools.permutations(vs) for vs in seq)):
        mp={v:img for vs,images in zip(seq,choices) for v,img in zip(vs,images)}
        if {tuple(sorted((mp[a],mp[b]))) for a,b in E}==E:
            yield mp

def doubled(n,edges,mp):
    E=vertices_edges(n,edges); index={e:i for i,e in enumerate(E)}
    subdiv=[(v,n+i) for i,(v,w) in enumerate(E)]+[(w,n+i) for i,(v,w) in enumerate(E)]
    m=dict(mp)
    for i,(v,w) in enumerate(E):m[n+i]=n+index[tuple(sorted((mp[v],mp[w])))]
    return n+len(E),vertices_edges(n+len(E),subdiv),m

def c2_count(m,items):
    return sum(m[i]!=i and m[m[i]]==i for i in items)//2

def fixed_trace(N,E,m):
    V=range(N)
    def edgeimage(e):return tuple(sorted((m[e[0]],m[e[1]])))
    def sgn(e):return 1 if m[e[0]] < m[e[1]] else -1
    c0=sum({m[a],m[b]}=={a,b} for a,b in itertools.combinations(V,2))
    c1=sum(sgn(e) for v in V for e in E if v not in e and m[v]==v and edgeimage(e)==e)
    c2=0
    for a,b in itertools.combinations(E,2):
        if set(a).isdisjoint(b) and {edgeimage(a),edgeimage(b)}=={a,b}:
            c2+=sgn(a)*sgn(b)*(1 if edgeimage(a)==a else -1)
    return c0,c1,c2

def local_trace(N,E,m):
    nbr=[[] for _ in range(N)]
    for a,b in E:nbr[a].append(b);nbr[b].append(a)
    ret=0
    for v in range(N):
        if m[v]!=v:continue
        ds=nbr[v]
        f=sum(m[w]==w for w in ds)
        t=c2_count(m,ds)
        ret+=(f-1)*(f-2)//2-t
    return ret

def boundary_check(N,E):
    # Impartial mod-2 rank of every two-dimensional cellular boundary.
    cells0=list(itertools.combinations(range(N),2));c0ids={c:i for i,c in enumerate(cells0)}
    cells1=[(v,e) for v in range(N) for e in E if v not in e];c1ids={c:i for i,c in enumerate(cells1)}
    cells2=[(e,f) for e,f in itertools.combinations(E,2) if set(e).isdisjoint(f)]
    graph=[[] for _ in cells0]
    for v,e in cells1:
        a,b=e
        x=c0ids[tuple(sorted((v,a)))];y=c0ids[tuple(sorted((v,b)))];graph[x].append(y);graph[y].append(x)
    seen={0}; todo=[0]
    while todo:
        for v in graph[todo.pop()]:
            if v not in seen:seen.add(v);todo.append(v)
    assert len(seen)==len(cells0),(N,'disconnect',len(seen),len(cells0))
    pivots={}
    for e,f in cells2:
        coeffs=[(e[1],f),(e[0],f),(f[1],e),(f[0],e)]
        mask=0
        composition=0
        for v,ed in coeffs:
            a,b=ed
            composition^=1<<c0ids[tuple(sorted((v,a)))]
            composition^=1<<c0ids[tuple(sorted((v,b)))]
        assert composition==0, 'chain composition nonzero'
        for c in coeffs:mask^=1<<c1ids[c]
        while mask:
            p=mask.bit_length()-1
            if p not in pivots:pivots[p]=mask;break
            mask^=pivots[p]
        else:raise AssertionError('nonzero H2 modulo 2')
    beta1=len(cells1)-(len(cells0)-1)-len(cells2)
    return len(cells0),len(cells1),len(cells2),beta1

def test(label,n,edges):
    E=vertices_edges(n,edges); auto=list(automorphisms(n,E));assert auto
    N,EE,_=doubled(n,E,auto[0]);dims=boundary_check(N,EE)
    b=sum((d-1)*(d-2)//2 for d in [sum(v in e for e in E) for v in range(n)])
    assert dims[-1]==b,(label,dims,b)
    for m0 in auto:
        N,EE,m=doubled(n,E,m0)
        c=fixed_trace(N,EE,m);top=1-c[0]+c[1]-c[2]
        loc=local_trace(N,EE,m)
        assert top==loc,(label,m0,c,top,loc)
    print(f'{label}: |Aut|={len(auto)}, C0/C1/C2={dims[:3]}, beta1={b}, all signed traces match')

def main():
    test('star4',5,[(0,i) for i in range(1,5)])
    test('star5',6,[(0,i) for i in range(1,6)])
    test('double-star',8,[(0,1),(0,2),(0,3),(0,4),(1,5),(1,6),(1,7)])
    test('balanced-binary',7,[(0,1),(0,2),(1,3),(1,4),(2,5),(2,6)])
    test('path6',6,[(i,i+1) for i in range(5)])
    test('unequal-branches',9,[(0,1),(0,2),(0,3),(1,4),(1,5),(2,6),(2,7),(3,8)])
    print('VERIFY_OK')

if __name__=='__main__':main()
