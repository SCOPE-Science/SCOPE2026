#!/usr/bin/env python3
"""Finite-field checks for the square image theorem for UT_5 in characteristic 2."""
from itertools import product
from collections import Counter

def table(q):
    if q==2: return [[a&b for b in range(q)] for a in range(q)]
    if q==4:
        def mul(a,b):
            v=0
            for i in range(2):
                for j in range(2):
                    if (a>>i)&1 and (b>>j)&1: v ^= 1<<(i+j)
            if v&4: v^=7  # x^2 = x+1
            return v
        return [[mul(a,b) for b in range(q)] for a in range(q)]
    raise ValueError(q)

def image(q):
    mult=table(q); image_set=set(); fibers=Counter(); qvals=range(q)
    for a,b,c,d,e,f,g,h,i,j in product(qvals, repeat=10):
        y=(mult[a][b], mult[b][c],mult[c][d], mult[a][f]^mult[e][c],mult[b][g]^mult[f][d],mult[a][i]^mult[e][g]^mult[h][d])
        fibers[y]+=1
    for y in product(qvals,repeat=6):
        u,v,w,r,s,t=y
        predicate=(not v and not (u and w)) or (v and ((u or w) or (mult[v][t] == mult[r][s])))
        assert (y in fibers)==bool(predicate), (q,y, predicate)
    expected=q**6-q**5+q**4+q**3-q**2
    assert len(fibers)==expected,(q,len(fibers),expected)
    assert sum(fibers.values())==q**10
    print('UT5 q=',q,'square_image_size=',len(fibers),'nonsquares_in_derived=',q**6-len(fibers),'total_inputs=',sum(fibers.values()),'fiber_sizes=',sorted(set(fibers.values())))
    return fibers

def product_in_derived(a,b,q):
    # Entries ordered (13,24,35,14,25,15), multiplication (I+X)(I+Y)=I+X+Y+XY.
    return tuple(a[k]^b[k]^(table(q)[a[0]][b[2]] if k==5 else 0) for k in range(6))

def width2(image_set,q):
    # optimized enumerate products only until all targets reached
    arr=list(image_set)
    all_targets=set(product(range(q),repeat=6))
    seen=set()
    mult=table(q)
    for a in arr:
        for b in arr:
            seen.add((a[0]^b[0],a[1]^b[1],a[2]^b[2],a[3]^b[3],a[4]^b[4],a[5]^b[5]^mult[a[0]][b[2]]))
        if len(seen)==q**6: break
    assert seen==all_targets,(q,len(seen),q**6)
    print('UT5 q=',q,'two-square product image=',len(seen))

def ut4(q):
    mul=table(q); vals=set()
    for a,b,c,d,e,f in product(range(q),repeat=6):
        vals.add((mul[a][b],mul[b][c],mul[a][e]^mul[d][c]))
    assert len(vals)==q**3
    print('UT4 q=',q,'square_image=',len(vals),'derived=',q**3)

if __name__=='__main__':
    for q in (2,4):
        im=image(q)
        width2(im,q)
        ut4(q)
    print('VERIFY_OK')
