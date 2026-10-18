#!/usr/bin/env python3
"""Independent F_p chain-rank checks for the full higher-independence filtration of KG(5,2)."""
from itertools import combinations
from collections import defaultdict
verts=list(combinations(range(5),2))
N=len(verts)
e=set(frozenset((i,j)) for i in range(N) for j in range(i) if not(set(verts[i])&set(verts[j])))
assert len(e)==15

def comp_bound(S):
    S=set(S)
    big=0
    while S:
        x=S.pop();seen={x};todo=[x]
        while todo:
            y=todo.pop()
            for z in list(S):
                if frozenset((y,z)) in e:
                    S.remove(z);seen.add(z);todo.append(z)
        big=max(big,len(seen))
    return big

buckets=defaultdict(list)
for j in range(N+1):
    for combo in combinations(range(N),j):
        b=max(1,comp_bound(combo))
        buckets[b].append(tuple(combo))
assert sum(map(len,buckets.values()))==1024

def rank_mod(columns,p):
    echelon={}
    for c in columns:
        c=dict(c)
        while c:
            k=max(c)
            if k not in echelon:
                echelon[k]=c
                break
            pp=echelon[k]
            factor=c[k]*pow(pp[k],-1,p)%p
            for row,num in pp.items():
                nextv=(c.get(row,0)-factor*num)%p
                if nextv:c[row]=nextv
                else:c.pop(row,None)
    return len(echelon)

EXPECTED={1:{2:4},2:{3:1},3:{3:1},4:{3:11},5:{4:61},
          6:{5:74},7:{6:36},8:{7:9},9:{8:1},10:{}}
for r in range(1,11):
    allowed={face for t in range(1,r+1) for face in buckets[t]}
    assert len(allowed)==sum(len(buckets[t]) for t in range(1,r+1))
    bydim={d:[f for f in allowed if len(f)==d+1] for d in range(N)}
    bydim[-1]=[()]
    for p in (2,3,5,7):
        rank={}
        for d in range(N):
            cs=[]
            for face in bydim[d]:
                v={}
                for j in range(len(face)):
                    sub=face[:j]+face[j+1:]
                    v[sub]=((-1)**j)%p
                cs.append(v)
            rank[d]=rank_mod(cs,p)
        bv={d:len(bydim[d])-rank[d]-rank.get(d+1,0) for d in range(N)}
        bv={d:k for d,k in bv.items() if k}
        assert bv==EXPECTED[r],(r,p,bv,EXPECTED[r])
    print('level',r,'faces',len(allowed)-1,'ranks',EXPECTED[r],'primes 2,3,5,7: PASS')
print('INDEPENDENT Fp CHECKS PASSED')
# Independently measure the only nontrivial long-lived class. We compute
# the rank of H_3(Ind_2) -> H_3(Ind_4) directly as a vector-space image,
# rather than relying on the persistence pairing algorithm.

def rank_f2(vectors):
    pivot={}
    for vector in vectors:
        while vector:
            h=vector.bit_length()-1
            if h not in pivot:
                pivot[h]=vector
                break
            vector ^= pivot[h]
    return len(pivot)

def kernel_vectors(columns):
    piv={}
    ker=[]
    for j,column in enumerate(columns):
        v=column;comb=1<<j
        while v:
            h=v.bit_length()-1
            if h not in piv:
                piv[h]=(v,comb)
                break
            w,c=piv[h];v^=w;comb^=c
        if not v:ker.append(comb)
    return ker

K2={face for t in range(1,3) for face in buckets[t]}
K4={face for t in range(1,5) for face in buckets[t]}
third2=sorted(f for f in K2 if len(f)==4)
second2=sorted(f for f in K2 if len(f)==3)
third4=sorted(f for f in K4 if len(f)==4)
fourth4=sorted(f for f in K4 if len(f)==5)
idx2={f:i for i,f in enumerate(second2)}
idx3={f:i for i,f in enumerate(third4)}
cols=[]
for tet in third2:
    b=0
    for j in range(4):b^=1<<idx2[tet[:j]+tet[j+1:]]
    cols.append(b)
ker=kernel_vectors(cols)
cycles=[]
for z in ker:
    vec=0
    for j,tet in enumerate(third2):
        if z>>j & 1:vec ^= 1<<idx3[tet]
    cycles.append(vec)
boundaries=[]
for cell in fourth4:
    v=0
    for j in range(5):v ^= 1<<idx3[cell[:j]+cell[j+1:]]
    boundaries.append(v)
rank_image=rank_f2(boundaries+cycles)-rank_f2(boundaries)
assert rank_image==1,(rank_image, len(ker))
print('Direct inclusion rank H3(Ind2) -> H3(Ind4) over F2:',rank_image)
print('ALL INDEPENDENT CHECKS PASSED')
