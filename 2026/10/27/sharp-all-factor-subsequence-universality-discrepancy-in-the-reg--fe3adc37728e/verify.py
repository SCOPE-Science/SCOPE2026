#!/usr/bin/env python3
"""Finite reductions for a sharp all-factor subsequence-universality theorem.

Every infinite-case implication is proved separately in the theorem text.
"""
from itertools import product

def paper(n):
    assert n >= 0
    odd = (n + 1) // ((n + 1) & -(n + 1))
    return int(odd % 4 == 3)

def scan(word, state=-1):
    """Return (number of completed binary arches, residual -1/0/1)."""
    arches = 0
    for letter in word:
        if state == -1:
            state = letter
        elif state != letter:
            arches += 1
            state = -1
    return arches, state

blocks = {(par, last): (0,0,1,par,0,1,1,last)
          for par, last in product((0,1), repeat=2)}

# An exact four-word check establishes the universal transfer table.
for (par, last), block in blocks.items():
    for initial in (-1,0,1):
        got = scan(block, initial)
        want = (3 - last + int(initial == 1), 1 if last else -1)
        assert got == want, (par,last,initial,got,want)

# All three finite endpoint regimes in the symbolic proof.
limits = {}
lo, hi = 1000, -1000
for block in blocks.values():
    for r in range(8):
        for s in range(r+1,9):
            arches, _ = scan(block[r:s])
            delta = 8*arches - 3*(s-r)
            lo=min(lo,delta);hi=max(hi,delta)
limits['one_block']=(lo,hi)

lo, hi = 1000, -1000
for left in blocks.values():
    for right in blocks.values():
        for r in range(8):
            for s in range(1,9):
                arches,_ = scan(left[r:]+right[:s])
                delta=8*arches-3*(8-r+s)
                lo=min(lo,delta);hi=max(hi,delta)
limits['adjacent_blocks']=(lo,hi)

lo, hi = 1000, -1000
for left in blocks.values():
    for right in blocks.values():
        for middle_last in (0,1):
            for r in range(8):
                left_count,left_state = scan(left[r:])
                for s in range(1,9):
                    right_count,_=scan(right[:s], 1 if middle_last else -1)
                    # If there are k>=1 complete middle blocks, their
                    # contribution is 3k-middle_last+int(left_state==1).
                    delta=8*(left_count + int(left_state==1)
                             -middle_last + right_count)-3*(8-r+s)
                    lo=min(lo,delta);hi=max(hi,delta)
limits['middle_complete_blocks']=(lo,hi)
assert limits == {'one_block':(-10,6),'adjacent_blocks':(-11,7),
                  'middle_complete_blocks':(-11,7)},limits

# Direct finite checks, separate from the proof by arbitrary blocks.
length = 4096
w=[paper(n) for n in range(length)]
for j in range(0,length//8):
    assert tuple(w[8*j:8*j+8]) == blocks[(j%2,paper(j))]
    for q in (-1,0,1):
        assert scan(w[8*j:8*j+8],q) == (3-paper(j)+int(q==1),
                                          1 if paper(j) else -1)
for J in range(1,length//8+1):
    assert scan(w[:8*J])[0] == 3*J-paper(J-1)
for a in range(length):
    state=-1; arches=0
    for b in range(a+1,length+1):
        bit=w[b-1]
        if state == -1: state=bit
        elif state != bit: arches+=1;state=-1
        assert -11 <= 8*arches-3*(b-a) <= 7,(a,b,arches)
assert scan(w[7:24])[0]==5 and 8*5-3*17==-11
assert scan(w[2:13])[0]==5 and 8*5-3*11==7

# An independently specified scattered-subsequence check on short factors.
from itertools import product

def direct_index(t):
    sub={()} # all distinct scattered subsequences
    for letter in t:
        sub |= {x+(letter,) for x in list(sub)}
    k=0
    while all(tuple(x) in sub for x in product((0,1),repeat=k+1)):
        k+=1
    return k

for a in range(32):
    for b in range(a+1,min(a+13,33)):
        assert scan(w[a:b])[0]==direct_index(w[a:b]),(a,b)
print('PAPERFOLDING_SHARP_UNIVERSALITY_PASS',limits,
      'direct_positions',length,'extrema',(-11,7))
