#!/usr/bin/env python3
"""Exact finite simplicial Morse certificate for first 2-stable Kneser graphs."""
import collections
import functools

ORDERS = {4: [1, 0], 5: [1, 0, 4, 3, 2], 6: [5, 2, 4, 6, 1, 3, 0, 7, 8], 7: [2, 13, 6, 12, 10, 9, 8, 5, 0, 7, 1, 4, 3, 11], 8: [3, 4, 14, 7, 12, 17, 18, 10, 2, 11, 16, 5, 15, 0, 19, 1, 13, 6, 9, 8], 9: [4, 3, 21, 18, 20, 12, 8, 11, 16, 9, 14, 2, 25, 13, 26, 7, 5, 19, 1, 23, 15, 6, 24, 17, 0, 10, 22], 10: [15, 16, 9, 12, 13, 25, 0, 26, 32, 23, 27, 31, 11, 3, 24, 34, 19, 20, 4, 10, 33, 28, 7, 2, 29, 6, 30, 17, 8, 5, 1, 22, 21, 14, 18]}
# Non-sensitive public reproducibility data: total orders of graph vertices.
# Every vertex is a stable chord (i,j) with 0 <= i < j < n.
EXPECTED = {4:{},5:{1:1},6:{2:1},7:{2:6},8:{2:13},9:{2:20},10:{2:26,3:2}}

def graph(n):
    vv=[(i,j) for i in range(n) for j in range(i+1,n) if (j-i) not in (1,n-1)]
    ed=[(i,j) for i,a in enumerate(vv) for j,b in enumerate(vv[:i]) if set(a).isdisjoint(b)]
    return vv,ed

def faces(n,edges):
    adj=[0]*n
    for a,b in edges:adj[a]|=1<<b;adj[b]|=1<<a
    out=[0]
    for x in out:
        for k in range(x.bit_length(),n):
            neighbors=adj[k]&x
            if neighbors.bit_count()>1:continue
            if neighbors and (adj[neighbors.bit_length()-1]&x):continue
            out.append(x | 1<<k)
    assert len(set(out))==len(out)
    return out

def pair(faces,order):
    remain=set(faces);pairs=[]
    for j in order:
        bit=1<<j
        for face in faces:
            if face not in remain or face&bit:continue
            larger=face|bit
            if larger in remain:
                remain.remove(face);remain.remove(larger)
                pairs.append((face,larger))
    return pairs, sorted(remain)

def boundary(face):
    out=[];sign=1;bits=face
    while bits:
        b=bits&-bits;bits^=b;out.append((face^b,sign));sign=-sign
    return out

def acyclicity(faces,pairs):
    reverse={g:l for l,g in pairs}
    indeg={x:0 for x in faces};out=collections.defaultdict(list);arcs=0
    for face in faces:
        for sub,_ in boundary(face):
            if reverse.get(face)==sub:u,v=sub,face
            else:u,v=face,sub
            out[u].append(v);indeg[v]+=1;arcs+=1
    q=collections.deque(x for x,d in indeg.items() if d==0)
    seen=0
    while q:
        x=q.popleft();seen+=1
        for y in out[x]:
            indeg[y]-=1
            if indeg[y]==0:q.append(y)
    assert seen==len(faces), ('cyclic',seen,len(faces))
    return arcs

def morse_boundary(pairs,critical):
    up={a:b for a,b in pairs};down={b:a for a,b in pairs};c=set(critical)
    @functools.lru_cache(None)
    def projection(face):
        if face in c:return {face:1}
        if face in down:return {}
        top=up[face];b=boundary(top)
        sign=next(sign for sub,sign in b if sub==face)
        acc=collections.defaultdict(int)
        for sub,ss in b:
            if sub==face:continue
            for h,v in projection(sub).items():acc[h]-=sign*ss*v
        return {h:v for h,v in acc.items() if v}
    result={}
    for f in critical:
        if not f:continue
        acc=collections.defaultdict(int)
        for sub,sgn in boundary(f):
            for h,v in projection(sub).items():acc[h]+=sgn*v
        result[f]={h:v for h,v in acc.items() if v}
    for f,bd in result.items():
        comp=collections.defaultdict(int)
        for sub,coef in bd.items():
            for h,v in result.get(sub,{}).items():comp[h]+=coef*v
        assert not any(comp.values()),'Morse d squared nonzero'
    return result

def integral_unit_rank(A):
    """Integer row/column elimination at only +-1 pivots; zero remainder required."""
    A=[list(map(int,row)) for row in A]
    if not A:return 0
    if not A[0]:return 0
    rank=0
    while A and A[0]:
        pivot=next(((i,j) for i,row in enumerate(A) for j,x in enumerate(row) if abs(x)==1),None)
        if pivot is None:
            assert all(not any(row) for row in A), ('nonzero Smith remainder',A)
            break
        i,j=pivot
        A[0],A[i]=A[i],A[0]
        for row in A:row[0],row[j]=row[j],row[0]
        q=A[0][0];assert abs(q)==1
        for ii in range(1,len(A)):
            k=A[ii][0]//q
            for jj in range(len(A[ii])):A[ii][jj]-=k*A[0][jj]
        A=[row[1:] for row in A[1:]]
        rank+=1
    return rank

def ranks_mod2(faces):
    bydim=collections.defaultdict(list)
    for f in faces:
        if f:bydim[f.bit_count()-1].append(f)
    ranks={0:1} if bydim[0] else {}
    for k in sorted(bydim):
        if k==0:continue
        rowid={f:i for i,f in enumerate(bydim[k-1])}
        piv={}
        for f in bydim[k]:
            x=0
            for h,_ in boundary(f):x^=1<<rowid[h]
            while x:
                b=x.bit_length()-1
                if b in piv:x^=piv[b]
                else:piv[b]=x;break
        ranks[k]=len(piv)
    return {k:len(v)-ranks.get(k,0)-ranks.get(k+1,0) for k,v in bydim.items() if len(v)-ranks.get(k,0)-ranks.get(k+1,0)}

def test(n):
    vertices,edges=graph(n);f=faces(len(vertices),edges)
    assert sorted(ORDERS[n])==list(range(len(vertices)))
    pairs,c=pair(f,ORDERS[n])
    incidence=acyclicity(f,pairs)
    M=morse_boundary(pairs,c)
    bydim=collections.defaultdict(list)
    for x in c:bydim[x.bit_count()-1].append(x)
    rank={}
    for d in [1,2,3]:
        upper=bydim[d];lower=bydim[d-1]
        A=[[M.get(f,{}).get(g,0) for f in upper] for g in lower]
        rank[d]=integral_unit_rank(A)
        assert rank[d]<=min(len(lower),len(upper))
    betti={d:len(bydim[d])-rank.get(d,0)-rank.get(d+1,0) for d in [1,2,3]}
    betti={d:r for d,r in betti.items() if r}
    # When an empty face is paired, a base point is implicit in reduced Morse theory.
    assert len(bydim[0])==0
    assert betti==EXPECTED[n]
    assert ranks_mod2(f)==EXPECTED[n]
    print('SG(2,%d)'%(n-4),'vertices=%d'%len(vertices),'faces=%d'%len(f),'pairs=%d'%len(pairs),'incidences=%d'%incidence,'critical='+repr({d:len(x) for d,x in bydim.items()}),'integer_ranks='+repr(rank),'reduced_betti='+repr(betti))

if __name__=='__main__':
    for n in range(4,11):test(n)
    print('STABLE_KNESER_TWO_INDEPENDENCE_TRANSITION_VERIFIED')
