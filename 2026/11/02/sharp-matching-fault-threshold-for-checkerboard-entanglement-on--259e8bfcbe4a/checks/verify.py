#!/usr/bin/env python3
"""Integer-only rank checks for hypercube graph-state matching omissions."""
from itertools import combinations
from random import Random


def rank2(rows):
    pivots={}
    for r in rows:
        while r:
            low=r&-r;p=low.bit_length()-1
            if p in pivots:r^=pivots[p]
            else:pivots[p]=r;break
    return len(pivots)


def cube(d):
    even=[x for x in range(1<<d) if x.bit_count()%2==0]
    odd=[x for x in range(1<<d) if x.bit_count()%2==1]
    oi={x:i for i,x in enumerate(odd)}
    ei={x:i for i,x in enumerate(even)}
    rows=[];edges=[]
    for i,a in enumerate(even):
        bits=0
        for j in range(d):
            b=a^(1<<j);k=oi[b];bits|=1<<k
            edges.append((i,k,a,b))
        rows.append(bits)
    return rows,edges,ei,oi


def deletion_rank(rows,edges):
    rr=rows.copy()
    for i,j,_,_ in edges:rr[i]^=1<<j
    return rank2(rr)


def coordinate_matching(edges,ei,oi,d,replace):
    j=0;c=1<<j
    U=[c^(1<<i) for i in range(d)]
    if replace:
        U.remove(c^(1<<(d-1)))
        U.append((1<<1)^(1<<2))
    assert len(set(U))==d
    ans=[(ei[a],oi[a^(1<<j)],a,a^(1<<j)) for a in U]
    assert len({x[2] for x in ans})==len({x[3] for x in ans})==d
    return ans


def main():
    random=Random(20261029)
    examined=0
    for d in (4,6,8):
        rows,edges,ei,oi=cube(d)
        initial=rank2(rows)
        assert initial==1<<(d-2)
        hist={}
        if d==4:
            # ALL k=1,2,3 matchings among 32 edges: exhaustive, not sampled.
            for k in (1,2,3):
                count=0
                for inds in combinations(range(len(edges)),k):
                    chosen=[edges[i] for i in inds]
                    if len({e[2] for e in chosen})<k or len({e[3] for e in chosen})<k:continue
                    assert deletion_rank(rows,chosen)==initial+k
                    count+=1;examined+=1
                hist[k]=count
        else:
            for k in range(1,d):
                count=0
                for rep in range(120 if d==6 else 55):
                    selected=[];used_a=set();used_b=set()
                    for e in random.sample(edges,len(edges)):
                        if e[2] not in used_a and e[3] not in used_b:
                            selected.append(e);used_a.add(e[2]);used_b.add(e[3])
                            if len(selected)==k:break
                    assert len(selected)==k
                    assert deletion_rank(rows,selected)==initial+k
                    count+=1;examined+=1
                hist[k]=count
        bad=coordinate_matching(edges,ei,oi,d,False)
        good=coordinate_matching(edges,ei,oi,d,True)
        assert deletion_rank(rows,bad)==initial+d-1
        assert deletion_rank(rows,good)==initial+d
        examined+=2
        print('d=%d initial=%d matchings_by_size=%s threshold_neighbor=%d threshold_modified=%d'%(d,initial,hist,deletion_rank(rows,bad),deletion_rank(rows,good)))
    for d in (3,5,7):
        rows,edges,ei,oi=cube(d)
        initial=rank2(rows)
        assert initial==1<<(d-1)
        for e in edges[:min(len(edges),50)]:
            assert deletion_rank(rows,[e])==initial-1
            examined+=1
        print('odd_d=%d initial=%d single_edge_checks=%d'%(d,initial,min(len(edges),50)))
    print('ALL_VERIFIED total_ranks=%d'%examined)

if __name__=='__main__':main()
