"""Independent finite orbit-pair checks for coordinate-symmetric Hamming Rips fixed loci.

Run with Python 3. No external packages required.
"""
from itertools import combinations
from collections import deque


def orbit_masks(k, z, w):
    return [sum(1 << j for j in inds) | (z << k)
            for inds in combinations(range(k), w)]


def hdist(u, v):
    return (u ^ v).bit_count()


def direct_orbit_graph(k, f):
    orbits = {}
    for w in range(k + 1):
        for z in range(1 << f):
            vs = orbit_masks(k, z, w)
            if all(hdist(a, b) <= 3 for a in vs for b in vs):
                orbits[(w, z)] = vs
    edges = set()
    labels = sorted(orbits)
    for a,b in combinations(labels,2):
        if all(hdist(x,y) <= 3 for x in orbits[a] for y in orbits[b]):
            edges.add((a,b))
    return labels, edges


def expected(k, f):
    good_weights = {0,1,k-1,k}
    labels=[(w,z) for w in sorted(good_weights) for z in range(1<<f)]
    E=set()
    for a,b in combinations(labels,2):
        w,z=a; v,u=b; delta=(z^u).bit_count()
        if w==v:
            okay=delta <= (1 if w in (1,k-1) else 3)
        elif {w,v}=={0,1} or {w,v}=={k-1,k}:
            okay=delta<=2
        elif k==4 and ({w,v}=={0,k-1} or {w,v}=={1,k}):
            okay=delta==0
        else:
            okay=False
        if okay:E.add((a,b))
    return labels,E


def clique_count_and_components(labels, edges):
    idx={v:i for i,v in enumerate(labels)}
    adj=[0]*len(labels)
    for a,b in edges:
        i,j=idx[a],idx[b];adj[i]|=1<<j;adj[j]|=1<<i
    component=[]; seen=set()
    for start in range(len(labels)):
        if start in seen:continue
        queue=deque([start]);seen.add(start);comp=[]
        while queue:
            t=queue.popleft();comp.append(t)
            for j in range(len(labels)):
                if (adj[t]>>j)&1 and j not in seen:
                    seen.add(j);queue.append(j)
        component.append(comp)
    fvec=[]
    # each clique generated exactly once using its least vertex
    def visit(mask, dim):
        while len(fvec)<=dim:fvec.append(0)
        fvec[dim]+=1
        nxt=mask
        while nxt:
            bit=nxt&-nxt;next_i=bit.bit_length()-1;nxt^=bit
            visit(nxt&adj[next_i],dim+1)
    for i in range(len(labels)):
        visit(adj[i]&~((1<<(i+1))-1),0)
    chi=sum((-1)**j*v for j,v in enumerate(fvec))
    return len(component),chi,fvec


def check(k,f):
    labels,E=direct_orbit_graph(k,f)
    ex,EE=expected(k,f)
    assert labels==ex,(k,f,'vertices',labels,ex)
    assert E==EE,(k,f,'edges',E^EE)
    comp,chi,fvec=clique_count_and_components(labels,E)
    if k==4:
        # χ(X_f) for f<=3 is 1, for f=4 is 0 (cross-polytope S^7)
        chiX=1 if f<=3 else 0
        expectation=(1,2*chiX-(2*(1<<f)))
    else:
        expectation=(2,2*(1 if f<=3 else 0))
    assert (comp,chi)==expectation,(k,f,comp,chi,expectation)
    print('PASS', 'k',k,'f',f,'orbit_vertices',len(labels), 'edges',len(E),
          'components',comp,'Euler',chi,'fvec',fvec)

if __name__=='__main__':
    for k in range(4,8):
        for f in range(4):
            check(k,f)
    check(4,4)
    check(5,4)
