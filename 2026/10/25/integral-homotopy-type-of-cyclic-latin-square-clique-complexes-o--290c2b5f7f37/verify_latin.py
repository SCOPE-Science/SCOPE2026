#!/usr/bin/env python3
"""Finite checks of flag cliques and translation Lefschetz characters."""
from itertools import combinations, product
from cmath import exp, pi


def make_data(p):
    points = list(product(range(p), repeat=2))
    vertex = {v: i for i,v in enumerate(points)}
    def line_key(v, d):
        x,y=v
        return (d, (x if d==0 else y if d==1 else (x+y)%p))
    lines = {}
    for d in range(3):
        for v in points:
            lines.setdefault(line_key(v,d), set()).add(vertex[v])
    adj = {i: set() for i in range(p*p)}
    for i,j in combinations(range(p*p), 2):
        if any(line_key(points[i],d)==line_key(points[j],d) for d in range(3)):
            adj[i].add(j)
            adj[j].add(i)
    return points,vertex,list(lines.values()),adj

def bron_kerbosch(R,P,X,adj,output):
    if not P and not X:
        output.append(frozenset(R));return
    u=max(P|X,key=lambda i:len(P & adj[i])) if P or X else None
    for v in list(P-(adj[u] if u is not None else set())):
        bron_kerbosch(R|{v},P&adj[v],X&adj[v],adj,output)
        P.remove(v);X.add(v)

def clique_faces(adj):
    maximal=[]
    bron_kerbosch(set(),set(adj),set(),adj,maximal)
    faces=set()
    for cl in maximal:
        a=sorted(cl)
        for k in range(1,len(a)+1):
            faces.update(combinations(a,k))
    return faces,maximal

def decomp_faces(p, lines, vertex):
    faces=set()
    for line in lines:
        a=sorted(line)
        for k in range(1,len(a)+1):
            faces.update(combinations(a,k))
    for x,y in product(range(p), repeat=2):
        for a in range(1,p):
            tri=tuple(sorted((vertex[(x,y)],vertex[((x+a)%p,y)],vertex[(x,(y+a)%p)])))
            faces.add(tri)
    return faces

def mod2rank(vectors):
    pivots={}
    for v in vectors:
        while v:
            b=v.bit_length()-1
            if b in pivots: v^=pivots[b]
            else:
                pivots[b]=v
                break
    return len(pivots)

def hmod2(faces):
    layers={k:sorted(f for f in faces if len(f)==k) for k in range(1,max(map(len,faces))+1)}
    dimensions={}
    ranks={}
    for k, basis in layers.items():
        dimensions[k-1]=len(basis)
        if k==1:
            ranks[0]=0;continue
        index={f:i for i,f in enumerate(layers[k-1])}
        columns=[]
        for f in basis:
            v=0
            for omitted in range(k):
                sub=f[:omitted]+f[omitted+1:]
                v^=1<<index[sub]
            columns.append(v)
        ranks[k-1]=mod2rank(columns)
    return {dim:dimensions[dim]-ranks[dim]-ranks.get(dim+1,0) for dim in dimensions}, dimensions

def sign_of_permutation(seq):
    return (-1)**sum(seq[i]>seq[j] for i in range(len(seq)) for j in range(i+1,len(seq)))

def lefschetz(faces, points, vertex,p, g):
    gx,gy=g
    perm=[vertex[((x+gx)%p,(y+gy)%p)] for x,y in points]
    answer=0
    for f in faces:
        moved=[perm[v] for v in f]
        if tuple(sorted(moved))==f:
            answer += (-1)**(len(f)-1)*sign_of_permutation(moved)
    return answer

def Fourier_multiplicities(p, traces):
    result={}
    for u,v in product(range(p),repeat=2):
        value=sum(t*exp(-2j*pi*((u*a+v*b)%p)/p) for (a,b),t in traces.items())/(p*p)
        assert abs(value.imag)<1e-7 and abs(value.real-round(value.real))<1e-7,(p,(u,v),value)
        value=round(value.real)
        kernel=(u,v)==(0,0) and 'trivial' or 'special' if (u==0 or v==0 or u==v) else 'other'
        expected=p-1 if (u,v)==(0,0) else p-2 if kernel=='special' else p-3
        assert value==expected,(p,(u,v),kernel,value,expected)
        result[(u,v)]=value
    return {k:sum(1 for (u,v),m in result.items() if m==k) for k in sorted(set(result.values()))}

def main():
    for p in (3,5,7,9):
        points,vertex,lines,adj=make_data(p)
        allfaces,maximal=clique_faces(adj)
        explicit=decomp_faces(p,lines,vertex)
        assert allfaces==explicit,(p,len(allfaces-explicit),len(explicit-allfaces))
        assert len([c for c in maximal if c in [frozenset(line) for line in lines]])==3*p
        assert len([c for c in maximal if len(c)==3 and not any(c<=line for line in lines)])==p*p*(p-1)
        assert len(lines)==3*p
        betti,fd=hmod2(allfaces)
        assert betti=={k:(1 if k==0 else (p-1)**3 if k==2 else 0) for k in fd}
        traces={}
        for g in product(range(p),repeat=2):
            L=lefschetz(allfaces,points,vertex,p,g)
            special=(g!=(0,0) and (g[0]==0 or g[1]==0 or (g[0]+g[1])%p==0))
            expected=1+(p-1)**3 if g==(0,0) else p if special else 0
            assert L==expected,(p,g,L,expected)
            traces[g]=L-1
        # Ancillary check of previously studied rational translation characters (not a new claim):
        # Special Fourier kernels are the annihilators of x=0, y=0, x+y=0:
        # u=0, v=0, and u=v respectively.
        mult=Fourier_multiplicities(p,traces)
        print('p=%d vertices=%d edges=%d faces=%d maximal=%d mixed_triangles=%d F2_betti=%s fixed_traces=%s Fourier_multiplicities=%s' % (
            p,p*p,sum(len(v) for v in adj.values())//2,len(allfaces),len(maximal),p*p*(p-1),betti,
            {i:sum(1 for v in traces.values() if v==i) for i in sorted(set(traces.values()))},mult))
    print('ALL CHECKS PASSED')

if __name__=='__main__':main()
