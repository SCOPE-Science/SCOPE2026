"""Compute mod-two simplicial Betti numbers directly from full orbit compatibility."""
from itertools import combinations
from orbit_fixed_checker import direct_orbit_graph

def faces_of_clique_graph(labels,edges):
    n=len(labels)
    idx={x:i for i,x in enumerate(labels)}
    adj=[set() for _ in range(n)]
    for a,b in edges:
        i,j=idx[a],idx[b];adj[i].add(j);adj[j].add(i)
    faces=[]
    def visit(face,candidates):
        faces.append(face)
        for j in sorted(candidates):
            visit(face+(j,), {k for k in candidates if k>j and k in adj[j]})
    for i in range(n):visit((i,), {j for j in adj[i] if j>i})
    bydim={}
    for x in faces:bydim.setdefault(len(x)-1,[]).append(x)
    return bydim

def rank(columns):
    pivots={}
    for v in columns:
        while v:
            p=v.bit_length()-1
            if p not in pivots:
                pivots[p]=v;break
            v^=pivots[p]
    return len(pivots)

def homology_betti(labels,edges):
    bydim=faces_of_clique_graph(labels,edges)
    dmax=max(bydim)
    ranks=[0]*(dmax+2)
    for d in range(1,dmax+1):
        earlier={s:i for i,s in enumerate(bydim[d-1])}
        cols=[]
        for simplex in bydim[d]:
            b=0
            for j in range(len(simplex)):
                b^=1<<earlier[simplex[:j]+simplex[j+1:]]
            cols.append(b)
        ranks[d]=rank(cols)
    return [len(bydim[d])-ranks[d]-ranks[d+1] for d in range(dmax+1)]

if __name__=='__main__':
    for k,f in [(4,0),(4,1),(4,2),(4,3),(5,0),(5,1),(5,2),(5,3)]:
        vertices,edges=direct_orbit_graph(k,f)
        betti=homology_betti(vertices,edges)
        b1=(2*(1<<f)-1) if k==4 else 0
        expected=[1,b1] if k==4 else [2,0]
        assert betti[:2]==expected and all(t==0 for t in betti[2:]),(k,f,betti,expected)
        print('PASS',k,f,'mod-two betti',betti)
