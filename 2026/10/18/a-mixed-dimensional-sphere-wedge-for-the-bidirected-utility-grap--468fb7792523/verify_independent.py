#!/usr/bin/env python3
"""Independent direct-subset enumeration and finite-field homology check."""
from collections import defaultdict

# Deliberately construct arcs with a different pair-iteration order.
ARCS=[]
for j in range(3):
    for i in range(3):
        ARCS.append((i,j+3))
        ARCS.append((j+3,i))

def admissible(mask):
    targets={}; sources={}
    for index,(u,v) in enumerate(ARCS):
        if mask & (1<<index):
            if u in targets or v in sources:return False
            targets[u]=v;sources[v]=u
    for start in targets:
        current=start;seen=set()
        while current in targets:
            if current in seen:return False
            seen.add(current);current=targets[current]
    return True

def field_rank(faces_hi,faces_lo,modulus):
    loc={f:i for i,f in enumerate(faces_lo)};pivots={}
    for mask in faces_hi:
        indices=[i for i in range(len(ARCS)) if mask & (1<<i)]
        col={loc[mask^(1<<i)]:(1 if j%2==0 else modulus-1) for j,i in enumerate(indices)}
        while col:
            r=max(col);v=col[r]
            if r not in pivots:
                inv=pow(v,-1,modulus)
                pivots[r]={x:(a*inv)%modulus for x,a in col.items()}
                break
            for x,a in pivots[r].items():
                val=(col.get(x,0)-v*a)%modulus
                if val:col[x]=val
                else:col.pop(x,None)
    return len(pivots)

def main():
    f=defaultdict(list)
    for mask in range(1<<18):
        if mask.bit_count()<=5 and admissible(mask):f[mask.bit_count()].append(mask)
    counts=[len(f[k]) for k in range(6)]
    assert counts==[1,18,108,264,252,72],counts
    print('second_arc_order_first_four:',ARCS[:4])
    print('second_face_counts_including_empty:',counts)
    for prime in (2,3,5,101):
        ranks=[field_rank(f[k],f[k-1],prime) for k in range(1,6)]
        betti=[len(f[k])-ranks[k-1]-(ranks[k] if k<5 else 0) for k in range(1,6)]
        assert ranks==[1,17,91,173,60],(prime,ranks)
        assert betti==[0,0,0,19,12],(prime,betti)
        print('prime',prime,'boundary_ranks_augmented:',ranks,'reduced_betti_by_dimension_0_to_4:',betti)
    print('independent_checks_passed:',True)
if __name__=='__main__':main()
