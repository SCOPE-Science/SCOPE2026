"""Exhaustive finite checks of rotation-character theorem for Mobius-ladder perfect-matching complexes.
Python standard library only. Edges are graph edges, facets are all perfect matchings.
"""
from collections import defaultdict


def construct(n):
    assert n % 2 == 0 and n >= 4
    m=2*n
    edges=[tuple(sorted((i,(i+1)%m))) for i in range(m)]
    edges += [(i,i+n) for i in range(n)]
    edges=[tuple(sorted(t)) for t in edges]
    assert len(edges)==3*n and len(set(edges))==3*n
    inv={e:i for i,e in enumerate(edges)}
    return edges,inv


def perfect_matchings(n,edges):
    byvertex=[[] for _ in range(2*n)]
    for j,(u,v) in enumerate(edges):
        byvertex[u].append((j,v));byvertex[v].append((j,u))
    result=[]
    def rec(unused, chosen):
        if not unused:
            result.append(chosen);return
        v=(unused & -unused).bit_length()-1
        for eid,w in byvertex[v]:
            if unused>>w & 1:
                rec(unused ^ (1<<v) ^ (1<<w),chosen|(1<<eid))
    rec((1<<(2*n))-1,0)
    assert len(set(result))==len(result)
    for f in result:assert f.bit_count()==n
    return result


def face_masks(facets):
    faces={0}
    for facet in facets:
        f=facet
        while f:
            faces.add(f)
            f=(f-1)&facet
    return faces


def orbit_partition(n,edges,inv,k):
    m=2*n
    perm=[]
    for (u,v) in edges:
        moved=tuple(sorted(((u+k)%m,(v+k)%m)))
        perm.append(inv[moved])
    orbs=[];seen=set()
    for i in range(len(edges)):
        if i in seen:continue
        orb=[];cur=i
        while cur not in seen:
            seen.add(cur);orb.append(cur);cur=perm[cur]
        assert cur==i
        orbs.append(sum(1<<j for j in orb))
    return orbs


def fixed_faces(faces,orbs):
    res=[]
    for face in faces:
        touched=[o for o in orbs if face&o]
        if all(face&o==o for o in touched):res.append((face,len(touched)))
    return res


def gf2_boundary_rank(domain,codomain):
    index={a:i for i,a in enumerate(codomain)}
    pivots={}
    for s in domain:
        x=0; b=s
        while b:
            bit=b&-b;b ^= bit
            x ^= 1 << index[s ^ bit]
        while x:
            p=x.bit_length()-1
            if p in pivots:x ^=pivots[p]
            else:
                pivots[p]=x;break
    return len(pivots)


def reduced_bettis(faces,n):
    levels=defaultdict(list)
    for f in faces:levels[f.bit_count()].append(f)
    ranks={}
    for k in range(1,n+1):
        ranks[k]=gf2_boundary_rank(levels[k], levels[k-1])
    return [len(levels[k])-ranks[k]-ranks.get(k+1,0) for k in range(1,n+1)]


def run():
    for n in (4,6,8,10):
        edges,inv=construct(n)
        facets=perfect_matchings(n,edges)
        faces=face_masks(facets)
        assert ((1 << (3*n)) - (1 << (2*n))) in faces  # all rungs constitute a perfect matching
        for k in (1,2):
            orbs=orbit_partition(n,edges,inv,k)
            fixed=fixed_faces(faces,orbs)
            orbit_sizes=sorted([o.bit_count() for o in orbs])
            predicted=(2,[n,2*n]) if k==1 else (6,[n//2,n//2,n,n])
            assert (len(fixed),orbit_sizes)==predicted, (n,k,len(fixed),orbit_sizes,predicted)
            orbit_sum=sum((-1)**count for face,count in fixed)
            assert orbit_sum==(0 if k==1 else -2), (n,k,orbit_sum)
            # Reduced Lefschetz (-1) times this weighted orbit sum.
            l_reduced=-orbit_sum
            trace=(-1)**(n//2-1)*l_reduced
            assert trace==(0 if k==1 else 2*(-1)**(n//2-1)),(n,k,trace)
        if n<=8:
            betti=reduced_bettis(faces,n)
            want=[0]*n
            want[n//2-1]=2
            assert betti==want,(n,betti,want)
            print('n',n,'perfect matchings',len(facets),'faces',len(faces),'mod2 reduced betti',betti)
        else:
            print('n',n,'perfect matchings',len(facets),'faces',len(faces),'checked fixed faces and traces')
    print('VERIFY_OK 4 perfect-matching enumerations; 8 complete fixed-simplex checks; 3 exact reduced mod-2 chain computations')

if __name__=='__main__':run()
