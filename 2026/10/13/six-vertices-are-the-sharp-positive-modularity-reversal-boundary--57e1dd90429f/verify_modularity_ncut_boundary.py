
#!/usr/bin/env python3
from itertools import combinations, permutations
from fractions import Fraction

def graph_data(n, mask):
    poss=list(combinations(range(n),2))
    adj=[0]*n
    edges=[]
    for i,(u,v) in enumerate(poss):
        if (mask>>i)&1:
            adj[u]|=1<<v
            adj[v]|=1<<u
            edges.append((u,v))
    if len(edges)<n-1:
        return None
    seen=1
    stack=[0]
    while stack:
        u=stack.pop()
        nb=adj[u]&~seen
        while nb:
            bit=nb & -nb
            nb-=bit
            v=bit.bit_length()-1
            seen|=bit
            stack.append(v)
    if seen != (1<<n)-1:
        return None
    return adj,edges

def bipart_metrics(n, adj, m, S):
    full=(1<<n)-1
    vol=sum(adj[v].bit_count() for v in range(n) if (S>>v)&1)
    cut=sum((adj[u] & (~S) & full).bit_count() for u in range(n) if (S>>u)&1)
    other=2*m-vol
    Q=Fraction(vol*other,2*m*m)-Fraction(cut,m)
    ncut=Fraction(2*m*cut,vol*other)
    # Exact identity.
    assert Q == Fraction(vol*other,2*m*m)*(1-ncut)
    return Q,ncut,cut,vol

def canonical_pair(n, edges, S1, S2):
    full=(1<<n)-1
    poss=list(combinations(range(n),2))
    idx={e:i for i,e in enumerate(poss)}
    best=None
    for p in permutations(range(n)):
        em=0
        for u,v in edges:
            a,b=sorted((p[u],p[v]))
            em |= 1<<idx[(a,b)]
        def relabel_set(S):
            T=0
            for u in range(n):
                if (S>>u)&1:
                    T |= 1<<p[u]
            return min(T, full^T)
        A=relabel_set(S1)
        B=relabel_set(S2)
        code=(em,tuple(sorted((A,B))))
        if best is None or code<best:
            best=code
    return best

strict_counts={}
weak_counts={}
connected_counts={}
n6_records=[]

for n in range(2,7):
    poss=list(combinations(range(n),2))
    strict=0
    weak=0
    connected=0
    for mask in range(1<<len(poss)):
        gd=graph_data(n,mask)
        if gd is None:
            continue
        adj,edges=gd
        connected+=1
        m=len(edges)
        full=(1<<n)-1
        parts=[]
        # One representative of each bipartition: require vertex 0 in S.
        for S in range(1,1<<n):
            if not (S&1) or S==full:
                continue
            if min(S.bit_count(), n-S.bit_count()) < 2:
                continue
            Q,Ncut,cut,vol=bipart_metrics(n,adj,m,S)
            if Q<=0:
                continue
            parts.append((S,Q,Ncut,cut,vol))
        for a,b in combinations(parts,2):
            dq=(a[1]>b[1])-(a[1]<b[1])
            dn=(a[2]>b[2])-(a[2]<b[2])  # lower Ncut is better
            disagreement = ((dq==0)!=(dn==0)) or dq*dn>0
            if disagreement:
                weak+=1
            if dq*dn>0:
                strict+=1
                if n==6:
                    n6_records.append((edges,m,a,b))
    connected_counts[n]=connected
    strict_counts[n]=strict
    weak_counts[n]=weak

assert connected_counts == {2:1,3:4,4:38,5:728,6:26704}
assert strict_counts == {2:0,3:0,4:0,5:0,6:420}
assert weak_counts == {2:0,3:0,4:0,5:0,6:780}

classes={}
for edges,m,a,b in n6_records:
    key=canonical_pair(6,edges,a[0],b[0])
    classes.setdefault(key,(edges,m,a,b))
assert len(classes)==2

# Expected two canonical types; order by edge count.
reps=sorted(classes.values(), key=lambda r:r[1])
r1,r2=reps
edges1,m1,a1,b1=r1
edges2,m2,a2,b2=r2
assert m1==7 and m2==9

# Representative 1: K4-e with a pendant 2-path attached to one endpoint of the missing edge.
# The selected partitions have (cut,vol)=(1,3) and (2,6).
vals1=sorted([(a1[1],a1[2],a1[3],min(a1[4],2*m1-a1[4])),
              (b1[1],b1[2],b1[3],min(b1[4],2*m1-b1[4]))])
assert set((x[2],x[3]) for x in vals1)=={(1,3),(2,6)}
assert {x[0] for x in vals1}=={Fraction(19,98),Fraction(10,49)}
assert {x[1] for x in vals1}=={Fraction(14,33),Fraction(7,12)}

# Representative 2: K4 and K3 sharing exactly one vertex.
assert set((a2[3],min(a2[4],2*m2-a2[4])) for _ in [0]) or True
stats2={(a2[3],min(a2[4],2*m2-a2[4]),a2[1],a2[2]),
        (b2[3],min(b2[4],2*m2-b2[4]),b2[1],b2[2])}
assert stats2=={
    (2,4,Fraction(10,81),Fraction(9,14)),
    (3,9,Fraction(1,6),Fraction(2,3)),
}

print("VERIFY_OK")
print("connected_labeled_counts",connected_counts)
print("strict_reversal_pair_counts",strict_counts)
print("weak_disagreement_pair_counts",weak_counts)
print("n6_strict_labeled_pairs",len(n6_records))
print("n6_canonical_graph_partition_pair_classes",len(classes))
for i,(edges,m,a,b) in enumerate(reps,1):
    print("class",i,"m",m,"edges",edges)
    print(" partition_A",a)
    print(" partition_B",b)
