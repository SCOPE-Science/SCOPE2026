#!/usr/bin/env python3
"""Check explicit cycle-cover certificates in Boolean disjointness graphs."""
import math

COVERS = {5: [[1, 14, 17, 12, 19, 4, 26, 5, 10, 21, 8, 22, 9, 18, 13, 2, 25, 6, 24, 7, 16, 11, 20, 3, 28]], 6: [[1, 54, 9, 52, 11, 20, 35, 28, 33, 22, 41, 18, 45, 16, 39, 24, 37, 26, 36, 19, 44, 3, 60], [2, 29, 34, 13, 50, 12, 51, 8, 23, 40, 21, 42, 5, 58, 4, 27, 32, 15, 48, 7, 56, 6, 25, 38, 17, 14, 49, 10, 53]], 7: [[1, 116, 11, 52, 75, 20, 107, 16, 109, 18, 105, 22, 97, 30, 96, 27, 100, 26, 101, 2, 117, 10, 85, 42, 21, 106, 17, 46, 81, 14, 113, 12, 115, 4, 121, 6, 89, 38, 73, 54, 72, 55, 8, 118], [3, 92, 35, 28, 99, 24, 39, 88, 37, 90, 5, 120, 7, 112, 15, 64, 59, 68, 51, 76, 50, 77, 34, 29, 98, 13, 114, 9, 102, 25, 70, 57, 66, 53, 74, 49, 78, 48, 79, 32, 91, 36, 83, 44, 67, 60, 65, 58, 69, 56, 71, 40, 23, 104, 19, 108], [33, 82, 45, 80, 43, 84, 41, 86]]}
SINGLE_25 = [7, 24, 3, 28, 1, 14, 17, 6, 25, 4, 26, 5, 10, 21, 2, 13, 18, 12, 19, 8, 22, 9, 20, 11, 16]

def core_vertices(r):
    return set(s for s in range(1, 1 << r) if 1 <= s.bit_count() <= r-2)

def check_cycles(r, cycles, expected):
    V = core_vertices(r)
    used=set()
    total=0
    for cyc in cycles:
        assert len(cyc)>=3
        assert len(cyc)==len(set(cyc))
        for a,b in zip(cyc,cyc[1:]+cyc[:1]):
            assert a in V and b in V
            assert (a&b)==0
        assert not used.intersection(cyc)
        used.update(cyc)
        total+=len(cyc)
    c=math.comb(r,r//2)
    U=(1<<r)-2-(c+1)//2
    assert total==expected==U
    return len(V),len(cycles)

def verify_layers(r):
    V=core_vertices(r)
    k=r//2
    B={s for s in V if s.bit_count()<k}
    A=V-B
    c=math.comb(r,k)
    if r%2==0:
        assert len(B)==(1<<(r-1))-1-c//2
    else:
        assert len(B)==(1<<(r-1))-1-c
    E_A=0
    edges=0
    for s in sorted(V):
        for t in V:
            if t<=s or s&t: continue
            edges+=1
            if s in A and t in A:
                E_A+=1
                if r%2==0:
                    assert s.bit_count()==t.bit_count()==k
                    assert s|t==(1<<r)-1
                else:
                    sizes=sorted((s.bit_count(),t.bit_count()))
                    assert sizes in ([k,k],[k,k+1])
                    if sizes==[k,k+1]: assert s|t==(1<<r)-1
    if r%2==0: assert E_A==c//2
    else:
        assert E_A>=c  # all complementary middle/upper pairs
    return len(V),edges,E_A

def main():
    expected={5:25,6:52,7:108,8:219,9:447,10:896}
    checks=0
    for r in range(5,11):
        n,e,ea=verify_layers(r)
        c=math.comb(r,r//2)
        u=(1<<r)-2-(c+1)//2
        assert u==expected[r]
        assert n==(1<<r)-r-2
        print('LAYERS_OK r=%d vertices=%d edges=%d upper_edges=%d cap=%d'%(r,n,e,ea,u))
        checks+=1
    for r,cyc in sorted(COVERS.items()):
        n,m=check_cycles(r,cyc,expected[r])
        print('COVER_OK r=%d cycle_count=%d covered=%d'%(r,m,expected[r]))
        checks+=1
    check_cycles(5,[SINGLE_25],25)
    print('SINGLE_CYCLE_OK r=5 length=25')
    checks+=1
    print('VERIFY_OK checks=%d certificates=4'%(checks))
if __name__=='__main__': main()
