#!/usr/bin/env python3
"""Finite-state certificate for universal ternary 0-1 quotient representations of 289.
No third-party packages required. Uses arbitrary-precision integer arithmetic.
"""
from collections import deque

M = 289
R = (1, 0, -1, -1, 1, 1)   # R(x)=1-x^2-x^3+x^4+x^5, R(3)=289
W = (96, 32, 11, 4, 1)
# For each live carry, mask of (q_{i-1},...,q_{i-5}), least recent in low bit.
LIVE = {
    0:0, 1:16, 4:8, 11:4, 12:20, 32:2, 33:18, 37:26,
    44:22, 48:30, 96:1, 100:9, 107:5, 111:13,
    112:29, 132:11, 133:27, 140:23, 143:15, 144:31,
}
TRAP = {5,14,15,16,43,46,98,101,128,129,130,139}

def edges(c):
    """Each edge is (new_carry, denominator_digit, numerator_digit)."""
    assert 0 <= c <= M // 2
    if c % 3 == 0:
        yield c // 3, 0, 0
        yield (c + M - 1) // 3, 1, 1
    elif c % 3 == 1:
        yield (c - 1) // 3, 0, 1
    else:
        yield (c + M) // 3, 1, 0

def polynomial_coefficient(q, history):
    return q - ((history >> 1)&1) - ((history >> 2)&1) + ((history >> 3)&1) + ((history >> 4)&1)

def weighted_history(h):
    return sum(w * ((h >> j)&1) for j,w in enumerate(W))

def convolution(a,b):
    z=[0] * (len(a)+len(b)-1)
    for i,x in enumerate(a):
        for j,y in enumerate(b): z[i+j]+=x*y
    return z

def evaluate(coeffs,base):
    return sum(c*base**i for i,c in enumerate(coeffs))

def verify():
    assert evaluate(R,3)==M
    assert len(LIVE)==20 and len(TRAP)==12 and not (set(LIVE)&TRAP)
    assert set(LIVE)|TRAP <= set(range(M//2+1))
    assert LIVE[96]==1 and LIVE[0]==0
    for c,h in LIVE.items():
        assert weighted_history(h)==c,(c,h)
        for d,q,p in edges(c):
            if d in LIVE:
                assert (((h<<1)|q)&31)==LIVE[d], (c,h,d,q,p)
                assert polynomial_coefficient(q,h)==p,(c,h,d,q,p)
            else:
                assert d in TRAP, (c,d)
    for c in TRAP:
        for d,q,p in edges(c):
            assert d in TRAP,(c,d)
    assert sorted((c,d,q,p) for c in LIVE for d,q,p in edges(c) if d in TRAP)==[(48,16,0,0),(96,128,1,1)]
    todo=deque([96]);reached={96}
    while todo:
        c=todo.popleft()
        for d,q,p in edges(c):
            if d not in reached:reached.add(d);todo.append(d)
    assert reached==set(LIVE)|TRAP
    # Explicit nontrivial Newman-polynomial example.
    Q=[1,0,1,1,0,1]
    P=[1,0,0,0,0,0,0,1,0,1,1]
    assert convolution(R,Q)==P
    assert evaluate(P,3)==M*evaluate(Q,3)==80920
    # Non-exhaustive independent check by bounded walks; infinite proof above.
    frontier=[(96,[1],[1])]
    compared=0
    for depth in range(1,25):
        nxt=[]
        for carry,qdigits,pdigits in frontier:
            for d,qq,pp in edges(carry):
                q2=qdigits+[qq];p2=pdigits+[pp]
                if d==0:
                    assert convolution(R,q2)==p2+[0]*5, (q2,p2)
                    compared+=1
                if d in LIVE and depth<24:
                    nxt.append((d,q2,p2))
        frontier=nxt
    print('VERIFY_OK', 'live_states',len(LIVE),'traps',len(TRAP),'reachable',len(reached),'walks_checked',compared)

if __name__=='__main__':verify()
