"""Finite checks for scale-two graph-Rips complexes of narrow rectangular tori.
Python 3, standard library only. General n is established by the accompanying proof.
"""
from itertools import combinations
from collections import Counter, defaultdict

def graph(m,n):
    vertices=[(a,b) for b in range(n) for a in range(m)]
    idx={v:i for i,v in enumerate(vertices)}
    neighbors=[set() for _ in vertices]
    for i,(a,b) in enumerate(vertices):
        for j in range(i):
            c,d=vertices[j]
            delta=min((a-c)%m,(c-a)%m)+min((b-d)%n,(d-b)%n)
            if delta<=2:
                neighbors[i].add(j);neighbors[j].add(i)
    return vertices,idx,neighbors

def maximal_cliques(adj):
    # Bron--Kerbosch with pivot, represented as Python integer sets.
    masks=[sum(1<<v for v in nbrs) for nbrs in adj]
    result=[]
    def rec(R,P,X):
        if not(P|X):
            result.append(frozenset(R));return
        U=P|X
        pivot=max((u for u in range(len(masks)) if (U>>u)&1),key=lambda u:(P&masks[u]).bit_count())
        avail=P&~masks[pivot]
        while avail:
            bit=avail&-avail;v=bit.bit_length()-1
            rec(R+(v,),P&masks[v],X&masks[v])
            P^=bit;X|=bit;avail^=bit
    rec((),(1<<len(adj))-1,0)
    return set(result)

def predicted_facets(m,n,idx):
    D,Q,E=set(),set(),set()
    for j in range(n):
        for i in range(m):
            D.add(frozenset(idx[p] for p in [(i,j),((i+1)%m,j),((i-1)%m,j),(i,(j+1)%n),(i,(j-1)%n)]))
            Q.add(frozenset(idx[p] for p in [(i,j),((i+1)%m,j),(i,(j+1)%n),((i+1)%m,(j+1)%n)]))
    for j in range(n):
        if m==5:
            E.add(frozenset(idx[(i,j)] for i in range(m)))
        elif m==6:
            for parity in (0,1):
                E.add(frozenset(idx[(i,j)] for i in range(parity,m,2)))
    for i in range(m):
        if n==5:
            E.add(frozenset(idx[(i,j)] for j in range(n)))
        elif n==6:
            for parity in (0,1):
                E.add(frozenset(idx[(i,j)] for j in range(parity,n,2)))
    return D,Q,E

def faces_from_facets(facets):
    fs=defaultdict(set)
    for facet in facets:
        seq=tuple(sorted(facet))
        for k in range(1,len(seq)+1):
            fs[k-1].update(combinations(seq,k))
    return dict(fs)

def binary_rank(columns):
    basis={}
    for x in columns:
        while x:
            p=x.bit_length()-1
            if p in basis:x ^= basis[p]
            else:
                basis[p]=x;break
    return len(basis)

def betti_mod_two(faces):
    boundary_rank={}
    for d in range(1,max(faces)+1):
        prev={f:i for i,f in enumerate(sorted(faces[d-1]))}
        col=[]
        for face in sorted(faces[d]):
            mask=0
            for k in range(len(face)):
                mask ^= 1<<prev[face[:k]+face[k+1:]]
            col.append(mask)
        boundary_rank[d]=binary_rank(col)
    out={d:len(c)-boundary_rank.get(d,0)-boundary_rank.get(d+1,0) for d,c in faces.items()}
    out[0]-=1
    return out

def check(m,n):
    verts,idx,adj=graph(m,n)
    mx=maximal_cliques(adj)
    D,Q,E=predicted_facets(m,n,idx)
    assert mx==D|Q|E,('facet classification',m,n,len(mx),len(D|Q|E),len(mx-(D|Q|E)),len((D|Q|E)-mx))
    assert len(D)==m*n and len(Q)==m*n
    s=lambda t:1 if t==5 else 2 if t==6 else 0
    A=n*s(m);B=m*s(n)
    assert len(E)==A+B
    M=faces_from_facets(D|Q)
    full=faces_from_facets(mx)
    for coord,period,fiber_count in ((0,m,n),(1,n,m)):
        if period<5 or period>6:continue
        for fixed in range(fiber_count):
            row={idx[(i,fixed)] for i in range(m)} if coord==0 else {idx[(fixed,i)] for i in range(n)}
            U_faces={dim:{f for f in fs if set(f)<=row} for dim,fs in M.items()}
            tri=U_faces[2]
            get=lambda i:idx[(i,fixed)] if coord==0 else idx[(fixed,i)]
            expected={tuple(sorted([get(i),get((i+1)%period),get((i+2)%period)])) for i in range(period)}
            assert tri==expected and len(tri)==period
            diagonal=[tuple(sorted((get(i),get((i+2)%period)))) for i in range(period)]
            assert len(set(diagonal))==period
            assert all(sum(set(edge)<=set(t) for t in tri)==1 for edge in diagonal)
            assert len(U_faces[0])==period and len(U_faces[1])==2*period
            if period==6:assert len({f for f in full[2] if set(f)<=row})==8
    bt=betti_mod_two(full)
    expected={0:0,1:2 if not(A or B) else 1 if not (A and B) else 0,
              2:1 if not(A or B) else A+B if not (A and B) else A+B-1,3:0,4:0}
    assert bt==expected,(m,n,bt,expected)
    return [len(full[d]) for d in sorted(full)],bt,len(mx)

if __name__=='__main__':
    for m,n in [(5,5),(5,6),(6,6),(5,7),(6,7),(7,7),(5,8),(6,8),(7,8),(8,8),(5,9),(6,9),(7,9),(5,10),(6,10)]:
        f,b,facets=check(m,n)
        print('m=%d n=%d facets=%d face_vector=%s reduced_mod2_betti=%s'%(m,n,facets,f,b),flush=True)
    print('VERIFY_OK')

def verify_surface_collapse(m,n):
    _,idx,_=graph(m,n)
    D,Q,_=predicted_facets(m,n,idx)
    allfaces=set(f for fam in faces_from_facets(D|Q).values() for f in fam)
    count=0
    def pair(low,upper):
        nonlocal count
        lo=tuple(sorted(low));up=tuple(sorted(upper))
        assert lo in allfaces and up in allfaces and len(up)==len(lo)+1,(m,n,'missing',lo,up)
        co=[f for f in allfaces if set(lo)<set(f)]
        assert co==[up],(m,n,'not_free',lo,up,co[:5])
        allfaces.remove(lo);allfaces.remove(up);count+=1
    for j in range(n):
        for i in range(m):
            v=idx[(i,j)]
            E=idx[((i+1)%m,j)];W=idx[((i-1)%m,j)]
            N=idx[(i,(j+1)%n)];S=idx[(i,(j-1)%n)]
            pair([E,W,N,S],[v,E,W,N,S])
    for j in range(n):
        for i in range(m):
            v=idx[(i,j)]
            nbr=[idx[((i+1)%m,j)],idx[((i-1)%m,j)],idx[(i,(j+1)%n)],idx[(i,(j-1)%n)]]
            for t in combinations(nbr,3):pair(t,(*t,v))
    for j in range(n):
        for i in range(m):
            a=idx[(i,j)];b=idx[((i+1)%m,j)]
            c=idx[((i+1)%m,(j+1)%n)];d=idx[(i,(j+1)%n)]
            pair([a,b,d],[a,b,c,d])
    for j in range(n):
        for i in range(m):
            a=idx[(i,j)];b=idx[((i+1)%m,j)]
            c=idx[((i+1)%m,(j+1)%n)];d=idx[(i,(j+1)%n)]
            pair([b,d],[b,c,d])
    for j in range(n):
        for i in range(m):
            v=idx[(i,j)];E=idx[((i+1)%m,j)];W=idx[((i-1)%m,j)]
            N=idx[(i,(j+1)%n)];S=idx[(i,(j-1)%n)]
            pair([E,W],[v,E,W]);pair([N,S],[v,N,S])
    T=set()
    for j in range(n):
        for i in range(m):
            a=idx[(i,j)];b=idx[((i+1)%m,j)]
            c=idx[((i+1)%m,(j+1)%n)];d=idx[(i,(j+1)%n)]
            for tri in [(a,b,c),(a,c,d)]:
                for size in (1,2,3):T.update(tuple(sorted(f)) for f in combinations(tri,size))
    assert allfaces==T,(m,n,'wrong_survivor',len(allfaces),len(T))
    assert count==9*m*n,(m,n,count)
    return count

if __name__=='__main__':
    for m,n in [(5,5),(5,6),(6,6),(5,7),(6,7),(7,7),(5,8),(6,8)]:
        print('surface_collapse',m,n,verify_surface_collapse(m,n),flush=True)
    print('COLLAPSE_VERIFY_OK')
