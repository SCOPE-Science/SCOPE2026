#!/usr/bin/env python3
"""Exhaustive finite semantic certificate for two-world ternary modalities.

Usage: python3 verify.py
Only Python's standard library is required.
Triple-bit convention: bit 4u+2v+w represents R(u,v,w).
"""
from itertools import product


def holds(mask, u, v, w):
    return bool(mask & (1 << (4*u + 2*v + w)))


def admissible(mask, size, leq):
    """Check the two existential persistence conditions verbatim."""
    for u,v,w in product(range(size), repeat=3):
        if not holds(mask,u,v,w):
            continue
        for uu in range(size):
            if leq[u][uu] and not any(
                leq[v][vv] and leq[w][ww] and holds(mask,uu,vv,ww)
                for vv,ww in product(range(size),repeat=2)
            ):
                return False
        for vv,ww in product(range(size),repeat=2):
            if leq[v][vv] and leq[w][ww] and not any(
                leq[u][uu] and holds(mask,uu,vv,ww)
                for uu in range(size)
            ):
                return False
    return True


def upsets(size, leq):
    return tuple(A for A in range(1<<size) if all(
        not (A >> u & 1) or not leq[u][v] or (A >> v & 1)
        for u,v in product(range(size),repeat=2)
    ))


def operations(mask,size,leq,ups):
    cir,bul={},{}
    for A,B in product(ups,repeat=2):
        c,b=0,0
        for u in range(size):
            if any(holds(mask,u,v,w) and (A>>v&1) and (B>>w&1)
                   for v,w in product(range(size),repeat=2)):
                c |= 1<<u
            if all((not leq[u][uu]) or all(
                not holds(mask,uu,v,w) or (A>>v&1) or (B>>w&1)
                for v,w in product(range(size),repeat=2))
                for uu in range(size)):
                b |= 1<<u
        assert c in ups and b in ups
        cir[A,B]=c;bul[A,B]=b
    return cir,bul


def assoc_operator(op,ups):
    return all(op[op[A,B],C]==op[A,op[B,C]] for A,B,C in product(ups,repeat=3))


def assoc_relation(mask,size):
    return all(
        any(holds(mask,y,v,w) and holds(mask,u,y,x) for y in range(size))
        == any(holds(mask,z,w,x) and holds(mask,u,v,z) for z in range(size))
        for u,v,w,x in product(range(size),repeat=4)
    )


def census(size,leq):
    ups=upsets(size,leq)
    categories={};full=[]
    for mask in range(1 << size**3):
        if not admissible(mask,size,leq):
            continue
        cir,bul=operations(mask,size,leq,ups)
        key=(assoc_relation(mask,size),assoc_operator(cir,ups),assoc_operator(bul,ups))
        categories[key]=categories.get(key,0)+1
        full.append((mask,key))
    return categories,full


def main():
    chain=[[True,True],[False,True]]
    stats,rows=census(2,chain)
    expected={(True,True,True):32,(False,True,True):11,(False,True,False):24}
    assert stats==expected, (stats,expected)
    assert len(rows)==67
    # Independent structural grouping by the four-bit upper-coordinate row R(1,-,-).
    by_row={}
    for mask,(rel,cir,bul) in rows:
        row=(mask>>4)&15
        by_row.setdefault(row,[0,0,0])
        if rel and cir and bul: by_row[row][0]+=1
        elif not rel and cir and bul: by_row[row][1]+=1
        elif not rel and cir and not bul: by_row[row][2]+=1
        else: raise AssertionError((mask,rel,cir,bul))
    assert by_row=={
        0:[1,0,0], 8:[10,0,0], 10:[3,1,8],
        12:[3,1,8], 14:[8,0,8], 15:[7,9,0]
    },by_row
    assert [mask for mask,(_r,_c,b) in rows if not b]==[
        160,162,164,166,168,170,172,174,192,194,196,198,
        200,202,204,206,224,226,228,230,232,234,236,238]
    # Distinct two-world Boolean base and the one-world base cannot separate
    # the three associativity conditions.
    discrete,_=census(2,[[True,False],[False,True]])
    assert discrete=={(True,True,True):50,(False,False,False):206},discrete
    singleton,_=census(1,[[True]])
    assert singleton=={(True,True,True):2},singleton
    # Witness I: existential operator associative, universal not associative.
    A,B,C=0,2,0  # empty, top-only, empty
    cir,bul=operations(160,2,chain,upsets(2,chain))
    assert admissible(160,2,chain) and assoc_operator(cir,upsets(2,chain))
    assert bul[bul[A,B],C]==3 and bul[A,bul[B,C]]==0
    # Witness II: both induced operations associative but the ternary relation fails.
    cir,bul=operations(173,2,chain,upsets(2,chain))
    assert admissible(173,2,chain) and not assoc_relation(173,2)
    assert assoc_operator(cir,upsets(2,chain)) and assoc_operator(bul,upsets(2,chain))
    print('VERIFY_OK: chain=67, relational+both=32, both/nonrelational=11, circle-only=24;')
    print('singleton=2, discrete two-world=50/206; masks 160 and 173 reproduced.')

if __name__=='__main__':
    main()
