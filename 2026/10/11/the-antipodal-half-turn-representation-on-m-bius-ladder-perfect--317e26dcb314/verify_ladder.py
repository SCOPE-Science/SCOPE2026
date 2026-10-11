#!/usr/bin/env python3
"""Independent finite-chain checks for symmetry of perfect-matching complexes."""
from functools import lru_cache
from itertools import combinations

def graph(n):
    N=2*n
    edges=[tuple(sorted((i,(i+1)%N))) for i in range(N)]
    edges += [(i,i+n) for i in range(n)]
    loc={edge:i for i,edge in enumerate(edges)}
    p=[loc[tuple(sorted((((a+n)%N),((b+n)%N))))] for a,b in edges]
    assert sorted(p)==list(range(3*n))
    return edges,p

def perfect_matchings(n,edges):
    N=2*n
    incident=[[] for _ in range(N)]
    for e,(a,b) in enumerate(edges):
        incident[a].append((b,e));incident[b].append((a,e))
    @lru_cache(None)
    def solve(unused):
        if unused==0:return (0,)
        a=(unused & -unused).bit_length()-1
        result=[]
        for b,e in incident[a]:
            if (unused>>b)&1:
                result.extend((1<<e)|F for F in solve(unused ^ (1<<a) ^ (1<<b)))
        return tuple(result)
    return solve((1<<N)-1)

def all_faces(pms):
    faces={0}
    for pm in pms:
        subset=pm
        while subset:
            faces.add(subset)
            subset=(subset-1)&pm
    return faces

def gf2_boundary_ranks(n,faces):
    layers=[sorted(F for F in faces if F.bit_count()==k) for k in range(n+1)]
    rank=[0]*(n+1)
    for k in range(1,n+1):
        row={F:i for i,F in enumerate(layers[k-1])}
        pivots={}
        for F in layers[k]:
            vec=0
            g=F
            while g:
                bit=g&-g
                g^=bit
                vec ^= 1<<row[F^bit]
            while vec:
                lead=vec.bit_length()-1
                if lead not in pivots:
                    pivots[lead]=vec
                    break
                vec^=pivots[lead]
        rank[k]=len(pivots)
    betti=[len(layers[k])-rank[k]- (rank[k+1] if k<n else 0) for k in range(n)]
    return betti,len(faces),rank

def tau_on_face(F,p):
    mapped=0
    g=F
    while g:
        bit=g&-g
        i=bit.bit_length()-1
        mapped|=1<<p[i]
        g^=bit
    return mapped

def direct_trace(n,faces,p):
    signed=0;count=0
    for F in faces:
        if tau_on_face(F,p)!=F:continue
        count+=1
        t=sum(((F>>i)&1) and (p[i]!=i) for i in range(len(p)))//2
        signed+= (-1)**(F.bit_count()+t)
    return -signed,count

def packing_trace(n):
    # n spokes covering single positions; n paired rim edges covering consecutive positions.
    # n=2 uses two different parallel cycle edges, as in the graph itself.
    out=[0,0]
    def go(i,used,s,t):
        if i==2*n:
            out[0]+=(-1)**(s+t)
            out[1]+=1
            return
        go(i+1,used,s,t)
        if i<n: cover=1<<i
        else: cover=(1<<(i-n))|(1<<((i-n+1)%n))
        if used&cover==0:
            go(i+1,used|cover,s+(i<n),t+(i>=n))
    go(0,0,0,0)
    return -out[0],out[1]

def expected(n):
    if n%2==0:
        return {(n-2)//2:2}
    if n%6==3:
        return {(n//3):4}
    # n mod 6 in {1,5}; n=1 excluded
    return {((n+1)//3):2} if n%6==5 else {((n-1)//3):2}

if __name__=='__main__':
    for n in range(2,10):
        e,p=graph(n)
        pms=perfect_matchings(n,e)
        faces=all_faces(pms)
        L1,c1=direct_trace(n,faces,p)
        L2,c2=packing_trace(n)
        formula=-2*(-1)**(n//2) if n%2==0 else 0
        assert (L1,c1)==(L2,c2), (n,L1,c1,L2,c2)
        assert L1==formula,(n,L1,formula)
        if n<=8:
            bv,nfaces,ranks=gf2_boundary_ranks(n,faces)
            exp=expected(n)
            assert all(bv[k]==exp.get(k-1,0) for k in range(len(bv))), (n,bv,exp)
            # For n>=3 connected, H0=1, and top rational Betti expected.
            print('n',n,'PM',len(pms),'faces',nfaces,'reduced-L',L1,'fixed',c1,'betti_F2',bv,flush=True)
        else:
            print('n',n,'PM',len(pms),'faces',len(faces),'reduced-L',L1,'fixed',c1,flush=True)
    print('VERIFY_OK')
