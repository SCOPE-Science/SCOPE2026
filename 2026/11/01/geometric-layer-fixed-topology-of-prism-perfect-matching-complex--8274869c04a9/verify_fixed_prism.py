#!/usr/bin/env python3
"""Standalone finite checks for the layer-fixed prism perfect-matching theorem.

Pure Python; exact integer and GF(2) arithmetic. Verification examples do
not replace the general topological proof.
"""
from itertools import combinations, permutations
from collections import defaultdict

def canonical(u,v):
    return (u,v) if u<v else (v,u)

def cycle(n):
    return tuple(canonical(i,(i+1)%n) for i in range(n))

def complete(n):
    return tuple(combinations(range(n),2))

def path(n):
    return tuple((i,i+1) for i in range(n-1))

def all_perfect_matchings(n, edges):
    adj=[set() for _ in range(n)]
    for u,v in edges: adj[u].add(v); adj[v].add(u)
    def rec(left):
        if not left:
            yield frozenset()
            return
        v=min(left)
        for w in sorted(adj[v] & left):
            for rest in rec(left - {v,w}):
                yield rest | {canonical(v,w)}
    return list(rec(set(range(n)))) if n%2==0 else []

def prism_edge_orbits(n, edges):
    # Prism vertices are (layer, original) encoded layer*n+vertex.
    rung=[frozenset([canonical(v,v+n)]) for v in range(n)]
    horiz=[frozenset([canonical(u,v),canonical(n+u,n+v)]) for u,v in edges]
    return rung+horiz

def prism_edges(n, edges):
    return [canonical(i,i+n) for i in range(n)]+list(edges)+[(u+n,v+n) for u,v in edges]

def orbit_simplices(n, edges, crosscheck=True):
    orbits=prism_edge_orbits(n, edges)
    pms=all_perfect_matchings(2*n,prism_edges(n,edges)) if crosscheck else []
    faces=[]
    for mask in range(1<<len(orbits)):
        vertices=set(); faceset=set(); matching=True
        for i in range(len(orbits)):
            if (mask>>i)&1:
                for u,v in orbits[i]:
                    if u in vertices or v in vertices: matching=False
                    vertices.add(u); vertices.add(v); faceset.add(canonical(u,v))
        if crosscheck:
            is_real=any(faceset.issubset(P) for P in pms)
            if matching != is_real:
                raise AssertionError(('orbit realization mismatch',n,edges,mask,matching,is_real))
        if matching:
            faces.append(tuple(i for i in range(len(orbits)) if (mask>>i)&1))
    return faces,orbits,len(pms)

def rank_mod_two(columns):
    basis={}
    for col in columns:
        x=col
        while x:
            p=x.bit_length()-1
            if p in basis: x ^= basis[p]
            else: basis[p]=x;break
    return len(basis)

def reduced_betti(faces):
    bydim=defaultdict(list)
    for f in faces: bydim[len(f)-1].append(f)
    dmax=max(bydim)
    br={}
    for d in range(0,dmax+1):
        cod={f:i for i,f in enumerate(bydim[d-1])}
        columns=[]
        for f in bydim[d]:
            boundary = [f[:j]+f[j+1:] for j in range(len(f))]
            bit=0
            for sub in boundary: bit ^= (1<<cod[sub])
            columns.append(bit)
        br[d]=rank_mod_two(columns)
    betti={}
    for d in range(0,dmax+1):
        b=len(bydim[d])-br[d]-br.get(d+1,0)
        if b: betti[d]=b
    return betti

def sign_of_permutation(indexes):
    inv=sum(x>y for i,x in enumerate(indexes) for y in indexes[i+1:])
    return -1 if inv%2 else 1

def signed_homology_trace(n,edges,perm):
    edgelist=tuple(edges)
    perfects=all_perfect_matchings(n,edgelist)
    position={e:i for i,e in enumerate(sorted(edgelist))}
    trace=0
    for M in perfects:
        ordered=sorted(M)
        moved=[canonical(perm[u],perm[v]) for u,v in ordered]
        if set(moved)==set(ordered):
            trace+=sign_of_permutation([position[e] for e in moved]) * sign_of_permutation([position[e] for e in ordered])
    return trace

def lefschetz(n,edges,faces,perm):
    edgelist=tuple(edges)
    mov={i:perm[i] for i in range(n)}
    pos={e:i+n for i,e in enumerate(edgelist)}
    for i,(u,v) in enumerate(edgelist):mov[n+i]=pos[canonical(perm[u],perm[v])]
    # nonreduced Lefschetz sum over nonempty fixed simplices of signed action
    L=0
    for face in faces:
        if not face:continue
        moved=[mov[i] for i in face]
        if set(moved)==set(face):
            L+=(-1)**(len(face)-1)*sign_of_permutation(moved)
    return L

def verify_example(tag,n,edges,group_perms=()):
    edges=tuple(sorted(set(canonical(*e) for e in edges)))
    faces,orbits,pm_prism=orbit_simplices(n,edges)
    beta=reduced_betti(faces)
    basepm=len(all_perfect_matchings(n,edges))
    expected={n//2-1:basepm} if (n%2==0 and basepm>0) else {}
    assert beta==expected,(tag,beta,expected)
    for perm in group_perms:
        assert {canonical(perm[u],perm[v]) for u,v in edges}==set(edges)
        tr=signed_homology_trace(n,edges,perm) if n%2==0 else 0
        lefs=lefschetz(n,edges,faces,perm)
        pred=1+(((-1)**(n//2-1))*tr if n%2==0 else 0)
        assert lefs==pred, (tag,perm,lefs,pred)
    print('OK',tag,'n',n,'basePM',basepm,'prismPM',pm_prism,'faces',len(faces),'reducedH',beta,'symmetrychecks',len(group_perms))

if __name__=='__main__':
    for n in range(3,9):
        r=lambda shift:tuple((i+shift)%n for i in range(n))
        s=lambda offset:tuple((offset-i)%n for i in range(n))
        verify_example('cycle-'+str(n),n,cycle(n),[r(k) for k in range(n)]+[s(k) for k in range(n)])
    for n in range(2,7):
        pp=[tuple(range(n)),tuple(reversed(range(n)))]
        verify_example('path-'+str(n),n,path(n),pp)
    for n in (3,4,5):
        verify_example('complete-'+str(n),n,complete(n),list(permutations(range(n))) if n<=4 else [tuple(range(n))])
    n=6
    edges=[(i,j) for i in range(3) for j in range(3,6)]
    verify_example('K33',n,edges,[tuple(range(n)),(1,0,2,3,4,5),(3,4,5,0,1,2)])
    print('ALL_CHECKS_PASSED')
