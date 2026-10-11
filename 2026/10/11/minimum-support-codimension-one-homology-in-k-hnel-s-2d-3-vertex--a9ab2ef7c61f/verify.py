from itertools import combinations

def gf2_rank(rows):
    piv = {}
    for x in rows:
        while x:
            p = x.bit_length()-1
            if p in piv:
                x ^= piv[p]
            else:
                piv[p]=x
                break
    return len(piv)

def all_faces(facets, k):
    s=set()
    for F in facets:
        for c in combinations(F,k): s.add(tuple(sorted(c)))
    return sorted(s)

def build(d):
    n=2*d+3
    B=[tuple(sorted(((i+j)%n for j in range(d+2)))) for i in range(n)]
    # d-faces of B and cofacet counts; boundary d-faces are those in exactly one B facet.
    counts={}
    for F in B:
        for G in combinations(F,d+1):
            G=tuple(sorted(G)); counts[G]=counts.get(G,0)+1
    Kfac=sorted(G for G,c in counts.items() if c==1)
    return n,B,Kfac,counts

def check(d):
    n,B,Kfac,counts=build(d)
    faces_dm1=set(all_faces(Kfac,d))       # (d-1)-simplices, d vertices
    faces_d=set(Kfac)                      # d-simplices, d+1 vertices
    cyclic_blocks={tuple(sorted((i+j)%n for j in range(d+1))) for i in range(n)}
    missing=[]
    for Q in combinations(range(n),d+1):
        if Q in faces_d: continue
        if all(tuple(sorted(R)) in faces_dm1 for R in combinations(Q,d)):
            missing.append(Q)
    assert set(missing)==cyclic_blocks and len(missing)==n
    # Boundary rank computation over F2: H_{d-1} = ker d_{d-1}/im d_d.
    faces_dm2=all_faces(Kfac,d-1)
    idx_dm2={f:i for i,f in enumerate(faces_dm2)}
    rows_dm1=[]
    for F in sorted(faces_dm1):
        x=0
        for R in combinations(F,d-1): x ^= 1<<idx_dm2[tuple(sorted(R))]
        rows_dm1.append(x)
    rank_dm1=gf2_rank(rows_dm1)
    idx_dm1={f:i for i,f in enumerate(sorted(faces_dm1))}
    rows_d=[]
    for F in Kfac:
        x=0
        for R in combinations(F,d): x ^= 1<<idx_dm1[tuple(sorted(R))]
        rows_d.append(x)
    rank_d=gf2_rank(rows_d)
    h=(len(faces_dm1)-rank_dm1)-rank_d
    assert h==1
    # Each missing boundary is not in im d_d: rank increases by one.
    base=rank_d
    for Q in missing:
        x=0
        for R in combinations(Q,d): x ^= 1<<idx_dm1[tuple(sorted(R))]
        assert gf2_rank(rows_d+[x])==base+1
    # Gap proof conditions on all missing candidates are also directly checked.
    return n,len(Kfac),len(faces_dm1),rank_dm1,rank_d,len(missing)

out=[]
for d in range(3,8): out.append((d,)+check(d))
print('VERIFY_OK ' + ' ; '.join('d=%d n=%d fd=%d fdm1=%d rdm1=%d rd=%d missing=%d'%t for t in out))
