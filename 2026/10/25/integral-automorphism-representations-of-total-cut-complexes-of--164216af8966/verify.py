"""Exact small-case independent checks for cluster-graph total cut homology."""
from itertools import permutations, product, combinations
from math import comb


def parity(a):
    inv=0
    for i in range(len(a)):
        for j in range(i+1,len(a)):
            inv+=(a[i]>a[j])
    return -1 if inv%2 else 1

def cyclic_poly_char(pi,k):
    seen=set(); poly=[1]+[0]*len(pi)
    for i in range(len(pi)):
        if i in seen:continue
        l=0;j=i
        while j not in seen:
            seen.add(j); l+=1;j=pi[j]
        factor=(-1)**(l+1)
        for d in range(len(pi)-l,-1,-1):
            poly[d+l]+=factor*poly[d]
    q=[]
    for i,v in enumerate(poly):
        q.append(v-(q[i-1] if i else 0))
    return q[k-1]

def vertex_perm(sizes,blockperm,flip=0):
    offsets=[];z=0
    for s in sizes: offsets.append(z);z+=s
    out=[]
    for b,s in enumerate(sizes):
        j=blockperm[b]
        assert sizes[j]==s
        for a in range(s):
            aa=(1-a) if (flip>>b&1 and a in (0,1)) else a
            out.append(offsets[j]+aa)
    return out

def top_hom_character_trace(sizes,k,perm):
    n=sum(sizes);d=n-k-1
    orbits=[];seen=set()
    for i in range(n):
        if i not in seen:
            m=0;j=i
            while j not in seen:
                seen.add(j);m|=1<<j;j=perm[j]
            orbits.append(m)
    # X faces: complement occupies at least k distinct cliques.
    blocks=[];start=0
    for s in sizes:
        blocks.append(((1<<s)-1)<<start);start+=s
    total=0
    for sel in range(1<<len(orbits)):
        face=0
        for i,o in enumerate(orbits):
            if sel>>i&1:face|=o
        complement=((1<<n)-1)^face
        if sum(bool(complement&b) for b in blocks)>=k:
            total+=(-1)**sel.bit_count()
    return ((-1)**(d+1))*total

def rank_gf2(rows):
    piv={}
    for x in rows:
        while x:
            i=x.bit_length()-1
            if i not in piv:
                piv[i]=x;break
            x^=piv[i]
    return len(piv)

def exact_mod2_betti(sizes,k):
    n=sum(sizes)
    blocks=[];p=0
    for s in sizes:
        blocks.append(((1<<s)-1)<<p);p+=s
    bysize={}
    for f in range(1<<n):
        if sum(bool((((1<<n)-1)^f) & b) for b in blocks)>=k:
            bysize.setdefault(f.bit_count(),[]).append(f)
    rank={}
    for size in range(1,n-k+1):
        high=bysize.get(size+1,[]);low=bysize.get(size,[])
        pos={f:i for i,f in enumerate(low)}
        col=[]
        for F in high:
            bb=0
            for i in range(n):
                if F>>i&1:bb^=1<<pos[F^(1<<i)]
            col.append(bb)
        rank[size]=rank_gf2(col)
    # reduced C_{-1} augment rank 1 when nonempty vertices
    betti={}
    for size,fs in bysize.items():
        if size==0:continue
        b=len(fs)-rank.get(size-1,0)-rank.get(size,0)
        if size==1: b-=1  # augmentation rank 1
        if b: betti[size-1]=b
    return betti

def check():
    instances=0
    for sizes,k in [([2,2,2],3),([2,2,2,2],3),([2,2,2,2],4),([2,2,2,2,2],3),([2,2,2,2,2],4),([2,3,2,3],3),([3,3,3],3),([2,2,3,3],3)]:
        c=len(sizes);n=sum(sizes)
        plist=[p for p in permutations(range(c)) if all(sizes[i]==sizes[p[i]] for i in range(c))]
        for pi in plist:
            for flip in range(1<<c):
                p=vertex_perm(sizes,pi,flip)
                target=parity(p)*cyclic_poly_char(pi,k)
                got=top_hom_character_trace(sizes,k,p)
                assert got==target,(sizes,k,pi,flip,target,got)
                instances+=1
    print('CLUSTER_GRAPH_EQUIVARIANT_CHARACTER_VERIFIED',instances)
    j=0
    for sizes,k in [([2,2,2],3),([2,2,2,2],3),([2,2,2,2],4),([2,3,2],3),([3,2,2],3)]:
        d=sum(sizes)-k-1
        got=exact_mod2_betti(sizes,k)
        want={d:comb(len(sizes)-1,k-1)}
        assert got==want, (sizes,k,got,want)
        j+=1
    print('CLUSTER_GRAPH_MOD2_HOMOLOGY_VERIFIED',j)

if __name__=='__main__':check()
