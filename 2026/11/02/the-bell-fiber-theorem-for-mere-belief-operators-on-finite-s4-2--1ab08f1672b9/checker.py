#!/usr/bin/env python3
"""Independent finite checks for the finite S4.2 mere-belief reconstruction theorem.
Requires only the Python standard library. All finite enumerations are labelled.
"""
from itertools import product
from math import comb

def bell(n):
    table = [[0]*(n+1) for _ in range(n+1)]
    table[0][0] = 1
    for i in range(1,n+1):
        for k in range(1,i+1):
            table[i][k] = table[i-1][k-1] + k*table[i-1][k]
    return sum(table[n])

def check_s42(rows,n):
    if any(not (row & (1<<w)) for w,row in enumerate(rows)):
        return False
    for w,r in enumerate(rows):
        for u in range(n):
            if r & (1<<u) and rows[u] & ~r:
                return False
    for w,r in enumerate(rows):
        for u in range(n):
            if not (r & (1<<u)):continue
            for v in range(n):
                if r & (1<<v) and not (rows[u] & rows[v]):
                    return False
    return True

def operator_direct(rows,n):
    """Truth table of (diamond box X) and (not box X), for ALL subsets X."""
    full=(1<<n)-1
    table=[]
    for x in range(1<<n):
        values=0
        for w,r in enumerate(rows):
            if r&~x and any((r>>v)&1 and not (rows[v]&~x)
                           for v in range(n)):
                values |= 1<<w
        table.append(values)
    return tuple(table)

def terminal_cluster(rows,w,n):
    r=rows[w]
    # Identify the unique terminal SCC by its inclusion-minimal row.
    masks=[rows[u] for u in range(n) if r&(1<<u)]
    mn=min(masks,key=lambda m:m.bit_count())
    assert all((mn & ~x)==0 for x in masks)
    return mn

def validate_recovery(rows,table,n):
    full=(1<<n)-1
    transient=0; visible=0
    for w in range(n):
        positives=[x for x in range(1<<n) if table[x]&(1<<w)]
        t=terminal_cluster(rows,w,n)
        if not positives:
            assert rows[w]==t
            continue
        transient|=1<<w
        assert rows[w]!=t
        recovered_t=full
        for x in positives:
            recovered_t &= x
        recovered_outside=0
        for u in range(n):
            if table[full^(1<<u)]&(1<<w):
                recovered_outside|=1<<u
        assert recovered_t==t
        assert recovered_outside==(rows[w]&~t)
        assert recovered_t | recovered_outside == rows[w]
        visible|=t
    z=full & ~transient
    assert visible&~z==0
    invisible=(z & ~visible).bit_count()
    return invisible

def brute():
    expected_operators=[1,3,22,229]
    expected_frames=[1,4,26,255]
    for n in range(1,5):
        groups={}
        frames=0
        for rows in product(range(1<<n),repeat=n):
            if not check_s42(rows,n):
                continue
            frames +=1
            h=operator_direct(rows,n)
            u=validate_recovery(rows,h,n)
            if h in groups:
                assert groups[h][0]==u
                groups[h][1]+=1
            else:
                groups[h]=[u,1]
        assert frames==expected_frames[n-1],(n,frames)
        assert len(groups)==expected_operators[n-1],(n,len(groups))
        assert all(multiplicity==bell(u) for u,multiplicity in groups.values())
        print("n=%d frames=%d operators=%d fiber_Bell=PASS"%
              (n,frames,len(groups)))
    return True

def counting():
    # A000798, the established counts of labelled finite preorders.
    preorder=[1,1,4,29,355,6942,209527,9535241]
    visible=[0,0]
    for m in range(2,len(preorder)):
        visible.append(sum(comb(m,t)*preorder[m-t] for t in range(1,m)))
    connected=[0,1]+visible[2:]
    q=[1]
    for n in range(1,len(preorder)):
        q.append(sum(comb(n-1,k-1)*connected[k]*q[n-k]
                     for k in range(1,n+1)))
    assert q == [1,1,3,22,229,3361,71444,2233351],q
    print("Q_0..Q_7 = ",q)
    return True

if __name__=="__main__":
    assert brute()
    assert counting()
    print("ALL_CHECKS_OK")
