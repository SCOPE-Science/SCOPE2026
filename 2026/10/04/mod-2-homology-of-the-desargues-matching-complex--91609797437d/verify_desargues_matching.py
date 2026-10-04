#!/usr/bin/env python3
from collections import defaultdict

N=10
# Generalized Petersen graph G(10,3): outer u_i cycle, spokes, inner v_i-v_{i+3}.
edges=[]
for i in range(N):
    edges.append((i,(i+1)%N))
for i in range(N):
    edges.append((i,N+i))
for i in range(N):
    a,b=N+i,N+((i+3)%N)
    if a>b: a,b=b,a
    if (a,b) not in edges: edges.append((a,b))
edges=sorted({tuple(sorted(e)) for e in edges})
assert len(edges)==30
edge_masks=[(1<<a)|(1<<b) for a,b in edges]

by_size=defaultdict(list)

def rec(start, used, chosen):
    by_size[len(chosen)].append(tuple(chosen))
    for j in range(start,len(edges)):
        if used & edge_masks[j]:
            continue
        rec(j+1, used|edge_masks[j], chosen+[j])
rec(0,0,[])
counts={k:len(v) for k,v in sorted(by_size.items())}
expected={0:1,1:30,2:375,3:2540,4:10155,5:24486,6:34945,7:27840,8:11040,9:1720,10:60}
assert counts==expected,(counts,expected)

def gf2_rank_columns(cols):
    piv={}
    r=0
    for x in cols:
        while x:
            p=x.bit_length()-1
            if p in piv:
                x ^= piv[p]
            else:
                piv[p]=x
                r+=1
                break
    return r

def boundary_rank(k):
    # d_k: chains on k-edge matchings -> chains on (k-1)-edge matchings.
    if k==0: return 0
    low=by_size[k-1]
    idx={m:i for i,m in enumerate(low)}
    cols=[]
    for m in by_size[k]:
        x=0
        for t in range(k):
            face=m[:t]+m[t+1:]
            x ^= 1<<idx[face]
        cols.append(x)
    return gf2_rank_columns(cols)

ranks={k:boundary_rank(k) for k in range(1,11)}
expected_ranks={1:1,2:29,3:346,4:2194,5:7961,6:16525,7:18415,8:9380,9:1660,10:60}
assert ranks==expected_ranks,(ranks,expected_ranks)
# simplex dimension j corresponds to matchings of cardinality j+1.
betti={}
for j in range(0,10):
    c=len(by_size[j+1])
    rk_dj=ranks[j+1]
    rk_next=ranks.get(j+2,0)
    b=c-rk_dj-rk_next
    if b: betti[j]=b
assert betti=={5:5,6:45},betti
chi=sum(((-1)**j)*len(by_size[j+1]) for j in range(10))
assert chi==41
assert chi-1==(-5+45)==40
print('edges',len(edges))
print('matching_counts',counts)
print('boundary_ranks',ranks)
print('reduced_betti_F2',betti)
print('euler_characteristic',chi,'reduced',chi-1)
print('DESARGUES_MATCHING_VERIFY_OK')
