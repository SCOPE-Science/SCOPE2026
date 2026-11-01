"""Finite checks for the natural automorphism action on bipartite graph flex homology.

Run: python verify.py
Only Python standard library is required.
"""
from collections import deque, Counter
from itertools import combinations, permutations


def graph(n):
    return [(a, 2+i) for a in (0, 1) for i in range(n)]


def edges_data(n):
    edges=graph(n)
    incident=[[j for j,e in enumerate(edges) if v in e] for v in range(n+2)]
    return edges,incident


def flex(n, state, v, incident):
    idx=incident[v]
    if not idx:return None
    # For a hub: outgoing=1; for a leaf: outgoing=0.
    outbit=int(v<2)
    bits=[(state>>j)&1 for j in idx]
    if not (all(x==outbit for x in bits) or all(x!=outbit for x in bits)):
        return None
    return state ^ sum(1<<j for j in idx)


def components(n):
    edges,incident=edges_data(n)
    labels=[-1]*(1<<len(edges)); nc=0
    for start in range(len(labels)):
        if labels[start]>=0: continue
        labels[start]=nc; todo=[start]
        for x in todo:
            for v in range(n+2):
                y=flex(n,x,v,incident)
                if y is not None and labels[y]<0:
                    labels[y]=nc;todo.append(y)
        nc+=1
    return labels,nc


def rep(n,mask):
    # u is a sink; the other hub is a source at leaves in mask.
    return sum(1<<(n+i) for i in range(n) if mask & (1<<i))


def image_state(n,x,pi,swap):
    # Edges are stored (u,leaf_0)..(u,leaf_{n-1}),(v,leaf_0)..(v,leaf_{n-1}).
    y=0
    for a in (0,1):
        for i in range(n):
            if x & (1<<(a*n+i)):
                y |= 1<<((a^swap)*n+pi[i])
    return y


def subset_image(n,S,pi,swap):
    x=sum(1<<pi[i] for i in range(n) if S&(1<<i))
    if swap and x!=(1<<n)-1: return ((1<<n)-1)^x
    return x


def cells(n):
    edges,incident=edges_data(n)
    bydeg={}
    N=n+2
    for D in range(1<<N):
        if any((D>>u)&1 and (D>>v)&1 for u,v in edges):continue
        available=[j for j,(u,v) in enumerate(edges) if not ((D>>u)&1 or (D>>v)&1)]
        deg=D.bit_count();out=bydeg.setdefault(deg,[])
        for z in range(1<<len(available)):
            bits=sum(1<<available[k] for k in range(len(available)) if z>>k&1)
            out.append((D,bits))
    return bydeg


def signed_fixed_cell_trace(n,bydeg,pi,swap):
    edges=graph(n)
    V=n+2
    vertex_map=[1 if swap else 0,0 if swap else 1]+[2+pi[i] for i in range(n)]
    def img(d,b):
        e=sum(1<<vertex_map[v] for v in range(V) if d>>v&1)
        t=image_state(n,b,pi,swap)
        return e,t
    traces=[]
    for k in range(max(bydeg)+1):
        tr=0
        for d,b in bydeg.get(k,[]):
            if img(d,b)!=(d,b):continue
            verts=[v for v in range(V) if d>>v&1]
            perm=[vertex_map[v] for v in verts]
            inversions=sum(perm[i]>perm[j] for i in range(len(perm)) for j in range(i+1,len(perm)))
            tr+=(-1)**inversions
        traces.append(tr)
    return traces


def cycle_count(pi):
    used=set(); lengths=[]
    for i in range(len(pi)):
        if i in used:continue
        j=i;k=0
        while j not in used:
            used.add(j);j=pi[j];k+=1
        lengths.append(k)
    return lengths


def verify(n):
    labels,nc=components(n)
    exp_nc=3**n-2**n
    assert nc==exp_nc,(n,nc,exp_nc)
    rmap={}
    for m in range(1,1<<n):
        k=labels[rep(n,m)]
        assert k not in rmap,(n,m,k)
        rmap[k]=m
    assert len(rmap)==2**n-1
    bydeg=cells(n)
    assert len(bydeg[0])==2**(2*n)
    total=0
    for pi in permutations(range(n)):
        c=cycle_count(pi)
        for swap in (0,1):
            # direct action on nontrivial components via graph-state BFS, without using the proposed subset formula
            observed={}
            for k,m in rmap.items():
                img=labels[image_state(n,rep(n,m),pi,swap)]
                assert img in rmap
                observed[m]=rmap[img]
                assert observed[m]==subset_image(n,m,pi,swap),(n,pi,swap,m,observed[m])
            actual=sum(observed[m]==m for m in observed)
            expected=(2**len(c)-1 if not swap else 1+(2**len(c) if all(x%2==0 for x in c) else 0))
            assert actual==expected,(n,pi,swap,actual,expected)
            # Independently calculate the equivariant chain Lefschetz number from cubical cells.
            traces=signed_fixed_cell_trace(n,bydeg,pi,swap)
            L=sum((-1)**k * x for k,x in enumerate(traces))
            h0=sum(labels[image_state(n,x,pi,swap)]==labels[x]
                   for x in range(1<<(2*n)) if x==rep_component_min[labels[x]])
            assert h0-L==actual,(n,pi,swap,h0,L,actual,traces)
            total+=1
    return n,nc,len(bydeg),sum(map(len,bydeg.values())),total

if __name__=='__main__':
    for n in range(3,6):
        # Keep one representative per connected component, for an independent H_0 character count.
        labels,nc=components(n)
        rep_component_min=[1<<(2*n)]*nc
        for x,k in enumerate(labels): rep_component_min[k]=min(x,rep_component_min[k])
        print('TEST_OK',verify(n))
    print('VERIFY_OK')
