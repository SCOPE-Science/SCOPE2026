#!/usr/bin/env python3
"""Reproduce the integral multipath homology of the bidirected Petersen graph.

Only Python 3 standard library is needed. The digraph is defined with the outer
and inner pentagons and five spokes. Full reduced chains include the empty face.
"""
from collections import defaultdict, Counter, deque
from functools import lru_cache
import hashlib,json,sys,time

def graph_and_arcs():
    edges=sorted({tuple(sorted(e)) for e in
                  ([(i,(i+1)%5) for i in range(5)]+
                   [(i+5,5+(i+2)%5) for i in range(5)]+
                   [(i,i+5) for i in range(5)])})
    assert len(edges)==15
    arcs=tuple(x for u,v in edges for x in ((u,v),(v,u)))
    return edges,arcs

def valid(mask, arcs, n=10):
    parent=list(range(n)); indeg=[0]*n;outdeg=[0]*n
    def root(v):
        while v!=parent[v]:v=parent[v]
        return v
    b=mask
    while b:
        bit=b&-b;b^=bit;u,v=arcs[bit.bit_length()-1]
        indeg[v]+=1;outdeg[u]+=1
        if indeg[v]>1 or outdeg[u]>1:return False
        x,y=root(u),root(v)
        if x==y:return False
        parent[x]=y
    return True

def enumerate_faces(arcs):
    faces={0};frontier=[0]
    for k in range(1,10):
        nex=[]
        for f in frontier:
            for i in range(f.bit_length(),len(arcs)):
                g=f|(1<<i)
                if valid(g,arcs):nex.append(g)
        frontier=list(set(nex));faces.update(frontier)
        if not frontier:break
    return faces

def independent_path_orientation_counts(edges, n=10):
    # Different enumeration: 2^15 undirected edge subsets, not arc faces.
    # An undirected degree-at-most-two forest is a union of nontrivial
    # paths; each path has precisely two consistent orientations.
    result=Counter({0:1})
    for mask in range(1,1<<len(edges)):
        degree=[0]*n
        parent=list(range(n))
        def root(v):
            while parent[v]!=v:v=parent[v]
            return v
        valid_forest=True
        components=0
        b=mask
        while b:
            bit=b&-b;b^=bit
            u,v=edges[bit.bit_length()-1]
            degree[u]+=1;degree[v]+=1
            if degree[u]>2 or degree[v]>2:
                valid_forest=False;break
            x,y=root(u),root(v)
            if x==y:
                valid_forest=False;break
            parent[x]=y
        if not valid_forest:continue
        active={root(i) for i in range(n) if degree[i]}
        components=len(active)
        result[mask.bit_count()]+=1<<components
    return dict(sorted(result.items()))

def matching(faces,m):
    # Repeated elementary acyclic pivot matchings.
    unmatched=set(faces);partner={}
    for i in range(m):
        bit=1<<i
        for f in sorted(unmatched,key=lambda x:(x.bit_count(),x)):
            g=f|bit
            if not f&bit and f in unmatched and g in unmatched:
                unmatched.remove(f);unmatched.remove(g)
                partner[f]=g;partner[g]=f
    return unmatched,partner

def acyclic_check(faces,partner):
    indeg={f:0 for f in faces};out=defaultdict(list);inc=0
    for f in faces:
        b=f
        while b:
            bit=b&-b;b^=bit;lower=f^bit
            if partner.get(lower)==f:
                out[lower].append(f);indeg[f]+=1
            else:
                out[f].append(lower);indeg[lower]+=1
            inc+=1
    queue=deque(f for f,c in indeg.items() if c==0);processed=0
    while queue:
        f=queue.popleft();processed+=1
        for v in out[f]:
            indeg[v]-=1
            if indeg[v]==0:queue.append(v)
    assert processed==len(faces),(processed,len(faces))
    return inc

def delete_bit_boundary(mask):
    b=mask;j=0
    while b:
        bit=b&-b;b^=bit
        yield mask^bit, (-1 if j&1 else 1)
        j+=1

def morse_matrices(crit,partner):
    critical={k:sorted(f for f in crit if f.bit_count()-1==k) for k in range(-1,10)}
    assert not critical[-1] and not critical[0]
    matrices={}
    stats=[]
    for k in range(0,10):
        if not critical[k] or not critical[k-1]:continue
        index={f:i for i,f in enumerate(critical[k-1])}
        building=set()
        @lru_cache(maxsize=None)
        def proj(f):
            if f in crit:
                return {index[f]:1}
            g=partner[f]
            if g.bit_count()<f.bit_count():
                return {}  # a matched upper face dies in the Morse projection
            if f in building:raise RuntimeError('gradient cycle')
            building.add(f)
            c=next(s for a,s in delete_bit_boundary(g) if a==f)
            ans=Counter()
            for a,s in delete_bit_boundary(g):
                if a==f:continue
                for index_i,t in proj(a).items():ans[index_i]+=-c*s*t
            building.remove(f)
            return {j:v for j,v in ans.items() if v}
        M=[[0]*len(critical[k]) for _ in critical[k-1]]
        for j,f in enumerate(critical[k]):
            ans=Counter()
            for g,s in delete_bit_boundary(f):
                for i,t in proj(g).items():ans[i]+=s*t
            for i,a in ans.items():M[i][j]=a
        matrices[k]=M
        stats.append((k,len(critical[k-1]),len(critical[k]),len(proj.cache_info().__str__())))
    return critical,matrices

def smith_unit_reduction(M):
    # Exact integral elementary row and column operations using unit pivots.
    if not M:return (0,True,0,0)
    A=[row.copy() for row in M];m=len(A);n=len(A[0]);k=0
    maxabs=max(abs(x) for row in A for x in row)
    while k<min(m,n):
        pos=next(((i,j) for i in range(k,m) for j in range(k,n) if abs(A[i][j])==1),None)
        if pos is None:break
        i,j=pos
        A[k],A[i]=A[i],A[k]
        if j!=k:
            for row in A:row[k],row[j]=row[j],row[k]
        p=A[k][k]
        assert abs(p)==1
        for i in range(k+1,m):
            c=A[i][k]*p
            if c:
                for j in range(k,n):A[i][j]-=c*A[k][j]
        for j in range(k+1,n):
            c=A[k][j]*p
            if c:
                for i in range(k,m):A[i][j]-=c*A[i][k]
        k+=1
        maxabs=max(maxabs,max((abs(A[i][j]) for i in range(k,m) for j in range(k,n)), default=0))
    residual=sum(1 for i in range(k,m) for j in range(k,n) if A[i][j])
    return k,residual==0,residual,maxabs

def rank_mod(M,p):
    if not M:return 0
    A=[[x%p for x in row] for row in M];m=len(A);n=len(A[0]);r=0
    for j in range(n):
        pivot=next((i for i in range(r,m) if A[i][j]),None)
        if pivot is None:continue
        A[r],A[pivot]=A[pivot],A[r]
        inv=pow(A[r][j],-1,p)
        for i in range(r+1,m):
            if A[i][j]:
                c=A[i][j]*inv%p
                for q in range(j,n):A[i][q]=(A[i][q]-c*A[r][q])%p
        r+=1
        if r==m:break
    return r

def direct_mod2_betti(faces):
    # Independent cellular computation, without Morse matching or cancellations.
    levels=defaultdict(list)
    for f in faces:levels[f.bit_count()].append(f)
    ranks={}
    for k in range(1,max(levels)+1):
        lower={g:i for i,g in enumerate(levels[k-1])}
        piv={};rank=0
        for f in levels[k]:
            mask=0
            for g,_ in delete_bit_boundary(f): mask^=1<<lower[g]
            while mask:
                i=mask.bit_length()-1
                if i in piv:mask^=piv[i]
                else:piv[i]=mask;rank+=1;break
        ranks[k]=rank
    return {k-1:len(levels[k])-ranks.get(k,0)-ranks.get(k+1,0)
            for k in range(0,max(levels)+1)
            if len(levels[k])-ranks.get(k,0)-ranks.get(k+1,0)}

def main():
    edges,arcs=graph_and_arcs();faces=enumerate_faces(arcs)
    assert len(faces)==59203,len(faces)
    fcounts=dict(sorted(Counter(f.bit_count()-1 for f in faces).items()))
    independent_counts=independent_path_orientation_counts(edges)
    assert independent_counts=={k+1:v for k,v in fcounts.items()},(independent_counts,fcounts)
    critical,partner=matching(faces,len(arcs))
    counts=dict(sorted(Counter(f.bit_count()-1 for f in critical).items()))
    incidences=acyclic_check(faces,partner)
    criticals,matrices=morse_matrices(critical,partner)
    ranks={};snf={}
    for k,M in matrices.items():
        r,done,left,maxabs=smith_unit_reduction(M)
        assert done,('nonunit Smith remainder',k,r,left,maxabs)
        assert rank_mod(M,2)==r and rank_mod(M,1000003)==r
        ranks[k]=r;snf[k]={'rows':len(M),'columns':len(M[0]),'unit_factors':r,'remainder_nonzero':left,'max_intermediate_abs':maxabs}
    betas={k:len(c)-ranks.get(k,0)-ranks.get(k+1,0) for k,c in criticals.items() if c}
    assert betas=={4:12,5:1,6:44,7:94},betas
    direct_betti=direct_mod2_betti(faces)
    assert direct_betti==betas, (direct_betti,betas)
    # Squared boundary matrices vanish integrally.
    for k,A in matrices.items():
        B=matrices.get(k-1)
        if B:
            assert len(B[0])==len(A)
            assert all(sum(B[i][a]*A[a][j] for a in range(len(A)))==0
                        for i in range(len(B)) for j in range(len(A[0])))
    print(json.dumps({'graph':'bidirected Petersen graph GP(5,2)','vertices':10,
          'undirected_edges':edges,'directed_arcs':arcs,
          'augmented_faces':len(faces),'f_vector':fcounts,
          'independent_undirected_oriented_counts':independent_counts,
          'face_poset_incidences':incidences,'matching_pairs':len(partner)//2,
          'critical_cells':counts,'morse_smith':snf,'reduced_betti':betas,
          'integral_torsion':'none','direct_mod2_betti':direct_betti},sort_keys=True))
    print('VERIFIED_BIDIRECTED_PETERSEN_INTEGRAL_HOMOLOGY')
if __name__=='__main__':main()
