from collections import Counter, deque

# Q_3 on {0,...,7}, with bit flips in coordinates 0,1,2.
edges=[]
for v in range(8):
    for bit in (1,2,4):
        w=v^bit
        if v<w:
            edges.append((v,w))
assert len(edges)==12

faces=[]
for mask in range(1,1<<len(edges)):
    used=0
    ok=True
    for i,(u,v) in enumerate(edges):
        if (mask>>i)&1:
            endpoints=(1<<u)|(1<<v)
            if used & endpoints:
                ok=False
                break
            used |= endpoints
    if ok:
        faces.append(mask)
F=set(faces)
fvec=[sum(m.bit_count()==k for m in faces) for k in range(1,5)]
assert fvec==[12,42,44,9]
assert len(faces)==107

order=[2,3,9,10,8,1,6,11,4,0,5,7]
unmatched=set(F)
pairs=[]
for i in order:
    bit=1<<i
    lows=sorted(m for m in unmatched if not (m&bit))
    for lo in lows:
        if lo not in unmatched:
            continue
        hi=lo|bit
        if hi in unmatched and hi in F:
            unmatched.remove(lo)
            unmatched.remove(hi)
            pairs.append((lo,hi,i))
assert len(pairs)==51
critical=sorted(unmatched, key=lambda m:(m.bit_count(),m))
assert [m.bit_count()-1 for m in critical]==[0,2,2,2,2]
critical_sets=[[i for i in range(12) if (m>>i)&1] for m in critical]
expected=[[2],[0,5,8],[0,7,8],[6,7,8],[1,4,11]]
assert critical_sets==expected

pairset={(lo,hi) for lo,hi,_ in pairs}
assert len(pairset)==len(pairs)
# Forman orientation: unmatched covers low->high, matched covers high->low.
indeg={m:0 for m in faces}
out={m:[] for m in faces}
cover_count=0
for hi in faces:
    t=hi
    while t:
        b=t & -t
        t-=b
        lo=hi^b
        if lo==0 or lo not in F:
            continue
        if (lo,hi) in pairset:
            a,c=hi,lo
        else:
            a,c=lo,hi
        out[a].append(c)
        indeg[c]+=1
        cover_count+=1
q=deque(m for m,d in indeg.items() if d==0)
seen=0
while q:
    x=q.popleft(); seen+=1
    for y in out[x]:
        indeg[y]-=1
        if indeg[y]==0:
            q.append(y)
assert seen==len(faces)
assert cover_count==252

# Independent mod-2 simplicial homology calculation, including augmentation.
bysize={k:[m for m in faces if m.bit_count()==k] for k in range(1,5)}
def rank_gf2(cols):
    piv={}
    rank=0
    for x in cols:
        while x:
            p=x.bit_length()-1
            if p in piv:
                x ^= piv[p]
            else:
                piv[p]=x
                rank+=1
                break
    return rank
ranks=[1]
for k in range(2,5):
    lower={m:i for i,m in enumerate(bysize[k-1])}
    cols=[]
    for m in bysize[k]:
        x=0
        t=m
        while t:
            b=t & -t; t-=b
            x ^= 1<<lower[m^b]
        cols.append(x)
    ranks.append(rank_gf2(cols))
assert ranks==[1,11,31,9]
betti=[]
for d in range(4):
    n=len(bysize[d+1])
    down=ranks[d]
    up=ranks[d+1] if d+1<len(ranks) else 0
    betti.append(n-down-up)
assert betti==[0,0,4,0]
chi=sum(((-1)**d)*fvec[d] for d in range(4))
assert chi==5

print('edges='+repr(edges))
print('faces=107')
print('f_vector=12,42,44,9')
print('matched_pairs=51')
print('hasse_covers=252')
print('critical_edge_index_sets='+repr(critical_sets))
print('augmented_boundary_ranks=1,11,31,9')
print('reduced_betti_mod2=0,0,4,0')
print('euler_characteristic=5')
print('ACYCLIC_MATCHING_OK')
print('VERIFY_OK')
