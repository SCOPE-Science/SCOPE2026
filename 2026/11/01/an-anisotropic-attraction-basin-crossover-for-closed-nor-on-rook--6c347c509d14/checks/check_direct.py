#!/usr/bin/env python3
"""Exhaustive, direct synchronous self-inclusive NOR on labelled rook boards."""
from collections import defaultdict
from itertools import product
from math import comb

def bitupdate(bits, a, b):
    ans = 0
    for i in range(a):
        for j in range(b):
            ok = True
            for k in range(a):
                if bits & (1 << (k*b+j)):
                    ok = False
                    break
            if ok:
                for l in range(b):
                    if bits & (1 << (i*b+l)):
                        ok = False
                        break
            if ok:
                ans |= 1 << (i*b+j)
    return ans

def h(r,c):
    return sum((-1)**(i+j)*comb(r,i)*comb(c,j)*2**((r-i)*(c-j))
               for i in range(r+1) for j in range(c+1))

def expected(a,b):
    n_cyc = 1 + (2**a-2)*(2**b-2)//2
    allrow = (2**b-1)**a
    allcol = (2**a-1)**b
    B = 1+allrow+allcol-h(a,b)
    return n_cyc, B

def calc(a,b):
    N = a*b
    full=(1<<N)-1
    basin=defaultdict(int)
    periodic_states=set()
    for bits in range(1<<N):
        nxt=bitupdate(bits,a,b)
        nxt2=bitupdate(nxt,a,b)
        nxt3=bitupdate(nxt2,a,b)
        assert nxt3==nxt,(a,b,bits,nxt,nxt2,nxt3)
        key=tuple(sorted((nxt,nxt2)))
        basin[key]+=1
        assert nxt!=nxt2
        if bits==nxt2 or bits==nxt:
            periodic_states.add(bits)
    predicted_cycles,predicted_main=expected(a,b)
    assert len(basin)==predicted_cycles,(a,b,len(basin),predicted_cycles)
    assert basin[(0,full)]==predicted_main,(a,b,basin[(0,full)],predicted_main)
    for key,num in basin.items():
        if key==(0,full):continue
        x,y=key
        def dims(z):
            rr={i for i in range(a) for j in range(b) if z&(1<<(i*b+j))}
            cc={j for i in range(a) for j in range(b) if z&(1<<(i*b+j))}
            return len(rr),len(cc)
        r,c=dims(x)
        assert num==h(r,c)+h(a-r,b-c),(a,b,r,c,num)
    expected_p=2+(2**a-2)*(2**b-2)
    assert len(periodic_states)==expected_p
    assert sum(basin.values())==(1<<N)
    assert predicted_main>(1<<N)//2
    return f'{a}x{b}: {1<<N} states; {len(basin)} cycles; central basin {predicted_main}; periodic {expected_p}'

if __name__=='__main__':
    cases=[(2,2),(2,3),(2,4),(2,5),(2,8),(3,3),(3,4),(3,5),(4,4)]
    total=0
    for a,b in cases:
        print(calc(a,b))
        total+=1<<(a*b)
    print('DIRECT_OK total_states',total)
