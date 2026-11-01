#!/usr/bin/env python3
"""Reproduce a finite check of an open-neighborhood theorem for line graphs."""
from itertools import product, combinations
from collections import Counter

def projective_incidence(q):
    assert q in (2, 3)
    def normalize(v):
        for x in v:
            if x:
                return tuple((a * pow(x, -1, q)) % q for a in v)
        raise ValueError
    pts = sorted({normalize(v) for v in product(range(q), repeat=3) if any(v)})
    v = len(pts)
    return 2*v, [(i, v+j) for i,p in enumerate(pts)
                 for j,l in enumerate(pts) if sum(a*b for a,b in zip(p,l))%q == 0]

def petersen():
    P = list(combinations(range(5),2))
    return len(P),[(i,j) for i in range(len(P)) for j in range(i+1,len(P))
                   if not(set(P[i]) & set(P[j]))]

def bridge_copies(n,E):
    return 2*n, sorted(E+[(u+n,v+n) for u,v in E]+[(0,n)])

def subsets(mask,include_empty=True):
    s=mask
    while s:
        yield s
        s=(s-1)&mask
    if include_empty: yield 0

def rank_mod2(faces, k):
    if k==0: return 0
    cols = faces[k]; idx = {s:j for j,s in enumerate(faces[k-1])}; piv={}
    for s in cols:
        q=s; b=0
        while q:
            x=q & -q; q-=x
            b ^= 1 << idx[s ^ x]
        while b:
            h=b.bit_length()-1
            if h in piv:b ^=piv[h]
            else:
                piv[h]=b
                break
    return len(piv)

def verify(name,n,edges):
    E=sorted(tuple(sorted(e)) for e in edges)
    assert len(E)==len(set(E)) and all(0<=u<v<n for u,v in E)
    assert len(E)>0
    adj=[set() for _ in range(n)]
    for u,v in E:adj[u].add(v);adj[v].add(u)
    assert min(map(len,adj))>=3
    for u in range(n):
        for v in adj[u]:
            assert len(adj[u]&adj[v])==0, 'triangle'
    for u in range(n):
        for v in range(u+1,n):
            assert len(adj[u]&adj[v])<=1, 'quadrilateral'
    m=len(E)
    E_at=[set() for _ in range(n)]
    for i,(u,v) in enumerate(E):E_at[u].add(i);E_at[v].add(i)
    nbr=[set() for _ in E]
    for i,(u,v) in enumerate(E):nbr[i]=(E_at[u]|E_at[v])-{i}
    # Exact local intersection identities, including disjoint attachment faces.
    for i,(u,v) in enumerate(E):
        X,Y=E_at[u]-{i},E_at[v]-{i}
        assert X.isdisjoint(Y)
        assert X|Y==nbr[i]
        for w in range(n):
            if w in (u,v):continue
            assert not (X & E_at[w] and Y & E_at[w])
        for j,(a,b) in enumerate(E):
            if j==i:continue
            common=nbr[i]&nbr[j]
            if {u,v}&{a,b}:
                w=next(iter({u,v}&{a,b}))
                assert common == E_at[w]-{i,j}
            else:
                assert len(common)<=1
    face_set={0}
    for S in nbr:
        bits=sum(1<<i for i in S)
        face_set.update(subsets(bits))
    faces_by_degree={k:sorted(s for s in face_set if s.bit_count()==k+1)
                     for k in range(max(z.bit_count() for z in face_set))}
    dmax=max(faces_by_degree)
    ranks=[0]+[rank_mod2(faces_by_degree,k) for k in range(1,dmax+1)]+[0]
    betti=[len(faces_by_degree[k])-ranks[k]-ranks[k+1] for k in range(dmax+1)]
    b=m-n+1
    expected={1:m+b}
    for d,cnt in Counter(map(len,adj)).items():expected[d-2]=expected.get(d-2,0)+cnt
    assert betti[0]==1,(name,betti)
    for k in range(1,dmax+1):
        assert betti[k]==expected.get(k,0),(name,k,betti,expected)
    print(name,'vertices',n,'edges',m,'simplex_counts',
          [len(faces_by_degree[k]) for k in range(dmax+1)],'ranks',ranks,
          'reduced_mod2_betti',[betti[0]-1]+betti[1:],
          'predicted_degrees',dict(sorted(expected.items())))

if __name__=='__main__':
    p2=projective_incidence(2)
    p3=projective_incidence(3)
    pet=petersen()
    verify('Fano incidence graph',*p2)
    verify('ternary projective-plane incidence graph',*p3)
    verify('Petersen graph',*pet)
    verify('two Petersen graphs joined by a bridge',*bridge_copies(*pet))
    print('VERIFY_OK')
