#!/usr/bin/env python3
# Exact verifier for the mod-2 homology of the matching complex of G(10,2).
edges=[]
for i in range(10):
    edges.append(tuple(sorted((i,(i+1)%10))))
for i in range(10):
    edges.append((i,10+i))
for i in range(10):
    edges.append(tuple(sorted((10+i,10+((i+2)%10)))))
edges=sorted(set(edges))
assert len(edges)==30
assert set(range(20))=={v for e in edges for v in e}
deg=[0]*20
for a,b in edges:
    deg[a]+=1; deg[b]+=1
assert deg==[3]*20

mats=[[] for _ in range(11)]
def rec(start, used, tup):
    mats[len(tup)].append(tup)
    for j in range(start,len(edges)):
        a,b=edges[j]; bit=(1<<a)|(1<<b)
        if used & bit: continue
        rec(j+1, used|bit, tup+(j,))
rec(0,0,())
counts=[len(x) for x in mats]
expected_counts=[1,30,375,2540,10155,24474,34805,27300,10260,1400,36]
assert counts==expected_counts

def rank_gf2(cols):
    piv={}
    for x in cols:
        while x:
            p=x.bit_length()-1
            if p in piv: x ^= piv[p]
            else:
                piv[p]=x; break
    return len(piv)

ranks=[]
for k in range(1,11):
    lower={m:i for i,m in enumerate(mats[k-1])}
    cols=[]
    for m in mats[k]:
        x=0
        for t in range(k):
            x ^= 1 << lower[m[:t]+m[t+1:]]
        cols.append(x)
    ranks.append(rank_gf2(cols))
expected_ranks=[1,29,346,2194,7961,16513,18287,8896,1364,36]
assert ranks==expected_ranks

betti=[]
for k in range(1,11):
    betti.append(counts[k]-ranks[k-1]-(ranks[k] if k<10 else 0))
expected_betti=[0,0,0,0,0,5,117,0,0,0]
assert betti==expected_betti
red_euler=sum(((-1)**(k-1))*counts[k] for k in range(1,11))-1
assert red_euler==112==sum(((-1)**d)*b for d,b in enumerate(betti))
print('MATCHING_COUNTS',counts)
print('AUGMENTED_BOUNDARY_RANKS',ranks)
print('REDUCED_BETTI_DIMS_0_TO_9',betti)
print('REDUCED_EULER',red_euler)
print('DODECAHEDRAL_MATCHING_F2_VERIFY_OK')
