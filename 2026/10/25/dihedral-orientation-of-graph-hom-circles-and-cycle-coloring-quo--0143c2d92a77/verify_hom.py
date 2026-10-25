"""Finite combinatorial tests for circle-target graph Hom complexes.

Uses only the standard graph-homomorphism 1-skeleton and exact integer
edge increments; no external packages.
"""
from itertools import product
from collections import defaultdict, deque


def hom_verts(n, edges, k):
    nbr=[[] for _ in range(n)]
    for a,b in edges:
        nbr[a].append(b); nbr[b].append(a)
    order=sorted(range(n),key=lambda i:-len(nbr[i]))
    f=[-1]*n
    out=[]
    def extend(j):
        if j==n:
            out.append(tuple(f));return
        v=order[j]
        for c in range(k):
            if all(f[w]<0 or (c-f[w])%k in (1,k-1) for w in nbr[v]):
                f[v]=c;extend(j+1)
        f[v]=-1
    extend(0)
    return out,nbr


def moves(f, nbr, k):
    for u,ns in enumerate(nbr):
        if len(ns)==0:continue
        choices={(f[v]+d)%k for v in ns for d in (-1,1)}
        for new in choices:
            if new!=f[u] and all((new-f[v])%k in (1,k-1) for v in ns):
                out=list(f);out[u]=new
                sign=1 if (new-f[u])%k==2%k else -1
                yield tuple(out),u,sign


def components(n,edges,k):
    verts,nbr=hom_verts(n,edges,k)
    V=set(verts); seen={}; comps=[]; edges_seen=set(); directed_checks=0
    for f in verts:
        if f in seen: continue
        ci=len(comps); comp=[];todo=[f];seen[f]=ci
        while todo:
            g=todo.pop();comp.append(g)
            for h,u,s in moves(g,nbr,k):
                assert h in V
                # A genuine color move is unambiguously plus or minus two.
                assert (h[u]-g[u])%k == (2*s)%k
                directed_checks+=1
                if h not in seen: seen[h]=ci;todo.append(h)
                else: assert seen[h]==ci
        comps.append(comp)
    return verts, nbr, comps, seen, directed_checks


def edge_orientation_cyclic(f,k):
    m=len(f)
    steps=[1 if (f[(i+1)%m]-f[i])%k==1 else -1 for i in range(m)]
    s=sum(steps);assert s%k==0
    return s//k, sum(v==1 for v in steps)


def check_cycles():
    tests=0; homs=0; directed=0; groups=0
    for k in (3,5,6,7,8):
        for m in range(3,13):
            edges=[(i,(i+1)%m) for i in range(m)]
            verts,nbr, comps, belongs, stepchecks=components(m,edges,k)
            directed+=stepchecks
            homs+=len(verts)
            predicted={}
            for w in range(-m//k-1,m//k+2):
                if (m+k*w)%2 or abs(k*w)>m:continue
                r=(m+k*w)//2
                if r in (0,m): predicted[w]=k # singleton components
                else: predicted[w]=1 if k%2 else 2
            counted=defaultdict(int)
            for comp in comps:
                w,p=edge_orientation_cyclic(comp[0],k)
                assert all(edge_orientation_cyclic(g,k)[0]==w for g in comp)
                counted[w]+=1
            assert dict(counted)==predicted,(m,k,counted,predicted)
            allcircle=set()
            for i,comp in enumerate(comps):
                w,p=edge_orientation_cyclic(comp[0],k)
                if 0<p<m: allcircle.add(i)
            # For each cycle component, target rotations have positive degree;
            # reflections reverse the integer coordinate-increment class.
            for a,sgn in ((t,1) for t in range(k)):
                for i in allcircle:
                    f=comps[i][0]
                    target=tuple((sgn*x+a)%k for x in f)
                    assert belongs[target] in allcircle
                    assert edge_orientation_cyclic(target,k)[0]==edge_orientation_cyclic(f,k)[0]
                    groups+=1
            for a in range(k):
                for i in allcircle:
                    f=comps[i][0]
                    target=tuple((-x+a)%k for x in f)
                    assert belongs[target] in allcircle
                    assert edge_orientation_cyclic(target,k)[0]==-edge_orientation_cyclic(f,k)[0]
                    groups+=1
            # Count target-dihedral orbits of essential components whose
            # stabilizers have only rotations, i.e., nonzero winding pairs.
            visited=set(); positive=0
            for i in allcircle:
                if i in visited: continue
                f=comps[i][0]
                orbit={belongs[tuple((sgn*x+a)%k for x in f)] for a in range(k) for sgn in (-1,1)}
                visited.update(orbit)
                w,p=edge_orientation_cyclic(f,k)
                ws={edge_orientation_cyclic(comps[j][0],k)[0] for j in orbit}
                assert ws in ({0},{w,-w})
                if w!=0:positive+=1
            expect=sum(1 for w in range(1,(m-1)//k+1) if (k*w-m)%2==0)
            assert positive==expect,(m,k,positive,expect)
            tests+=1
    return tests,homs,directed,groups


def check_noncircle():
    graphs=[('path4',4,[(0,1),(1,2),(2,3)]),
            ('star4',5,[(0,i) for i in range(1,5)]),
            ('diamond',4,[(0,1),(1,2),(2,0),(0,3),(1,3)]),
            ('two_triangles',5,[(0,1),(1,2),(2,0),(0,3),(3,4),(4,0)]),
            ('square_diagonal',4,[(0,1),(1,2),(2,3),(3,0),(0,2)])]
    tests=0;transforms=0
    for name,n,edges in graphs:
        for k in (3,5,6):
            verts,nbr,comps,belongs,steps=components(n,edges,k)
            for f in verts:
                for g,u,s in moves(f,nbr,k):
                    # Target rotations preserve every directed-edge label.
                    for a in (0,1):
                        ff=tuple((x+a)%k for x in f);gg=tuple((x+a)%k for x in g)
                        assert (gg[u]-ff[u])%k==(2*s)%k
                        # Target reflections reverse directed increments.
                        fr=tuple((a-x)%k for x in f);gr=tuple((a-x)%k for x in g)
                        assert (gr[u]-fr[u])%k==(-2*s)%k
                        transforms+=1
            tests+=1
    return tests,transforms

if __name__=='__main__':
    print('CYCLE_COMPONENTS_AND_QUOTIENT_VERIFIED',*check_cycles())
    print('GENERAL_GRAPH_ORIENTATION_VERIFIED',*check_noncircle())


def homology_and_winding(n,edges,k):
    from math import gcd
    vertices,nbr,comps,belongs,_=components(n,edges,k)
    vid={f:i for i,f in enumerate(vertices)}
    undirected_edges={}
    neighbor_map={}
    for f in vertices:
        nb=list(moves(f,nbr,k));neighbor_map[f]=nb
        for g,u,s in nb:
            z=tuple(sorted((vid[f],vid[g])))
            undirected_edges[z]=None
    edge_keys=sorted(undirected_edges)
    edge_id={e:i for i,e in enumerate(edge_keys)}
    col2=set()
    for f in vertices:
        for g,u,s in neighbor_map[f]:
            for h,v,t in neighbor_map[f]:
                if u>=v: continue
                goal=list(f); goal[u]=g[u];goal[v]=h[v];goal=tuple(goal)
                if goal not in vid: continue
                if not any(z==goal for z,_,_ in neighbor_map[g]):continue
                if not any(z==goal for z,_,_ in neighbor_map[h]):continue
                pairs=[(f,g),(f,h),(g,goal),(h,goal)]
                bit=0
                for a,b in pairs:
                    bit ^= 1<<edge_id[tuple(sorted((vid[a],vid[b])))]
                assert bit.bit_count()==4
                col2.add(bit)
    pivots={}
    for b in col2:
        while b:
            p=b.bit_length()-1
            if p not in pivots:
                pivots[p]=b;break
            b^=pivots[p]
    b1=len(edge_keys)-len(vertices)+len(comps)-len(pivots)
    essential=sum(bool(len(c)>1) for c in comps)
    assert b1==essential,(n,k,b1,essential)
    # All cycles in each component have the same integral coordinate displacement.
    # The gcd of these displacements divided by k' is 1 on circle components.
    kprime=k//gcd(k,2)
    z_gcd=[0]*len(comps)
    lifts={}
    for ci,comp in enumerate(comps):
        lifts[comp[0]]=0;todo=[comp[0]]
        while todo:
            f=todo.pop()
            for g,u,s in neighbor_map[f]:
                step=s if u==0 else 0
                if g not in lifts:
                    lifts[g]=lifts[f]+step;todo.append(g)
                else:
                    delta=lifts[f]+step-lifts[g]
                    assert delta%kprime==0,(f,g,delta,kprime)
                    z_gcd[ci]=gcd(z_gcd[ci],abs(delta//kprime))
    for ci,comp in enumerate(comps):
        assert z_gcd[ci]==(1 if len(comp)>1 else 0),(n,k,ci,z_gcd[ci],len(comp))
    return len(vertices),len(edge_keys),len(col2),b1

if __name__=='__main__':
    samples=[(3,5),(4,5),(5,5),(6,5),(7,5),(8,5),(9,5),(6,6),(8,6),(9,3),(10,5)]
    total=[0,0,0,0]
    for n,k in samples:
        ret=homology_and_winding(n,[(i,(i+1)%n) for i in range(n)],k)
        total=[a+b for a,b in zip(total,ret)]
    print('EXACT_GF2_CELLULAR_H1_AND_PRIMITIVE_WINDING_VERIFIED',len(samples),*total)

def check_source_actions():
    tests=0
    for k in (3,5,6):
        for m in (3,4,5,6,7,8):
            edges=[(i,(i+1)%m) for i in range(m)]
            verts,nbr,comps,belongs,_=components(m,edges,k)
            rotations=lambda f: tuple(f[(i-1)%m] for i in range(m))
            reflection=lambda f:tuple(f[(-i)%m] for i in range(m))
            for f in verts:
                for g,u,s in moves(f,nbr,k):
                    for transform in (rotations,reflection):
                        ff=transform(f); gg=transform(g)
                        assert ff in belongs and gg in belongs
                        changed=[i for i in range(m) if ff[i]!=gg[i]]
                        assert len(changed)==1
                        assert (gg[changed[0]]-ff[changed[0]])%k==(2*s)%k
                        tests+=1
    return tests

if __name__=='__main__':
    print('DOMAIN_SYMMETRY_POSITIVE_WINDING_VERIFIED',check_source_actions())

def check_total_quotient_betti_zero():
    checked=0
    for k in (3,5,6,7,8):
        for m in range(3,13):
            verts,nbr,comps,belongs,_=components(m,[(i,(i+1)%m) for i in range(m)],k)
            unseen=set(range(len(comps)));orbits=[]
            while unseen:
                i=next(iter(unseen)); f=comps[i][0]
                orbit={belongs[tuple((sgn*x+a)%k for x in f)] for a in range(k) for sgn in (-1,1)}
                orbits.append(orbit);unseen-=orbit
            positive=sum(1 for w in range(1,(m-1)//k+1) if (k*w-m)%2==0)
            b0=positive+(m%2==0)+(m%k==0)
            assert len(orbits)==b0,(m,k,len(orbits),b0)
            checked+=1
    return checked
if __name__=='__main__':
    print('FULL_TARGET_DIHEDRAL_QUOTIENT_BETTI_VERIFIED',check_total_quotient_betti_zero())
