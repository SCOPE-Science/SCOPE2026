#!/usr/bin/env python3
"""Exact, finite-state certificate for four-term Thue--Morse arithmetic factors.

Only the Python standard library is required. Every state and transition is
constructed from elementary binary addition; no precomputed automaton is used.
"""
from collections import Counter, deque

STATES = [(c1,c2,c3,p) for c1 in range(2) for c2 in range(3)
          for c3 in range(4) for p in range(8)]
INDEX = {s:i for i,s in enumerate(STATES)}
assert len(STATES)==192 and len(INDEX)==192
START = INDEX[(0,0,0,0)]
TRANS = [[[0]*2 for _ in range(2)] for _ in STATES]
REVERSE_ZERO = [[] for _ in STATES]
for i,(c1,c2,c3,p) in enumerate(STATES):
    for db in (0,1):
        for nb in (0,1):
            vals = [nb + j*db + c for j,c in zip((1,2,3),(c1,c2,c3))]
            outp = p
            for j,x in enumerate(vals):
                outp ^= ((x&1)^nb)<<j
            nxt = INDEX[(vals[0]//2,vals[1]//2,vals[2]//2,outp)]
            TRANS[i][db][nb] = nxt
            if db==0:
                REVERSE_ZERO[nxt].append((i,nb))

# A state after processing all digits of d is terminal for parity r precisely
# when a finite string of additional high bits of n (and zero bits of d)
# carries the state to the zero-carry state with parity r.
TERMINAL_MASKS=[]
TAIL_NEXT=[]
for r in range(8):
    target=INDEX[(0,0,0,r)]
    visited={target}
    queue=deque([target]); nxtstep={}
    while queue:
        v=queue.popleft()
        for u,nb in REVERSE_ZERO[v]:
            if u not in visited:
                visited.add(u)
                nxtstep[u]=(v,nb)
                queue.append(u)
    TERMINAL_MASKS.append(sum(1<<i for i in visited))
    TAIL_NEXT.append(nxtstep)
assert [sum(bool(x&(1<<START)) for x in TERMINAL_MASKS)] == [1]

BIT_STEPS = [[(1<<TRANS[s][bit][0]) | (1<<TRANS[s][bit][1])
              for s in range(len(STATES))] for bit in (0,1)]
def apply(mask, bit):
    ans=0
    while mask:
        lb = mask & -mask
        ans |= BIT_STEPS[bit][lb.bit_length()-1]
        mask ^= lb
    return ans

def spectrum(mask):
    return sum((1<<r) for r,a in enumerate(TERMINAL_MASKS) if a&mask)

# All possible odd differences start with a least significant bit equal to 1.
FIRST = apply(1<<START,1)
QUEUE=deque([FIRST]); REACH={FIRST}; EDGES={}
while QUEUE:
    v=QUEUE.popleft()
    vnext=(apply(v,0),apply(v,1))
    EDGES[v]=vnext
    for w in vnext:
        if w not in REACH:
            REACH.add(w);QUEUE.append(w)
assert len(REACH)==195, len(REACH)
CLASSES={0x6e:set(),0xf7:set(),0xff:set()}
for s in REACH:
    code=spectrum(s)
    assert code in CLASSES, hex(code)
    CLASSES[code].add(s)
assert tuple(len(CLASSES[k]) for k in (0x6e,0xf7,0xff))==(5,6,184)

# Exact closure certificate. The exceptional classes are precisely the
# binary suffix families 1(0)* and 11(0)*, read least-significant-bit first;
# all remaining prefixes lie in the absorbing 0xff class.
A,B,C = CLASSES[0x6e],CLASSES[0xf7],CLASSES[0xff]
assert FIRST in A
assert EDGES[FIRST][1] in B
assert all(EDGES[s][0] in A for s in A)
assert all(EDGES[s][0] in B and EDGES[s][1] in C for s in B)
assert all(EDGES[s][0] in C and EDGES[s][1] in C for s in C)
assert all(EDGES[s][1] in C for s in A if s != FIRST)
assert EDGES[FIRST][0] != FIRST
assert FIRST not in {EDGES[s][0] for s in A}
# Follow zero edges and verify the two exceptional classes are all obtained.
def zero_orbit(s):
    out=set()
    while s not in out:
        out.add(s)
        s=EDGES[s][0]
    return out
assert zero_orbit(FIRST)==A
assert zero_orbit(EDGES[FIRST][1])==B

def relative_mask(d):
    assert d>0
    state=1<<START
    while d:
        state=apply(state,d&1)
        d >>=1
    return spectrum(state)

def expected_mask(d):
    while d%2==0:d//=2
    return 0x6e if d==1 else 0xf7 if d==3 else 0xff

def witness(d,r):
    bits=[int(c) for c in bin(d)[2:][::-1]]
    # Explicitly retain the high bits chosen for n along each nondeterministic
    # carry path; no search over candidate n is involved.
    curr={START:0}
    for k,db in enumerate(bits):
        nex={}
        for st,n in curr.items():
            for nb in (0,1):
                nxt=TRANS[st][db][nb]
                if nxt not in nex:
                    nex[nxt]=n | (nb<<k)
        curr=nex
    good = TERMINAL_MASKS[r]
    state=next((s for s in curr if good & (1<<s)),None)
    if state is None:return None
    n=curr[state]
    k=len(bits)
    target=INDEX[(0,0,0,r)]
    while state!=target:
        state,nb=TAIL_NEXT[r][state]
        n |= nb<<k
        k+=1
    return n

def tm(n):
    return n.bit_count()&1

num_witnesses=0
for d in range(1,512):
    mask=relative_mask(d)
    assert mask==expected_mask(d), (d,hex(mask))
    for r in range(8):
        n=witness(d,r)
        assert (n is not None)==bool(mask & (1<<r)), (d,r,n)
        if n is not None:
            bits=tuple(tm(n+j*d) for j in range(4))
            code=sum((bits[j]^bits[0])<<(j-1) for j in (1,2,3))
            assert code==r,(d,r,n,bits)
            # Independent bit-complement symmetry, without automaton data.
            k=(n+3*d).bit_length()+1
            comp=tuple(tm(n+(1<<k)+j*d) for j in range(4))
            assert comp==tuple(1-x for x in bits)
            num_witnesses+=1

# Direct finite-word cross-check, independent of the carry machine.
N=80000
seq=bytearray(N)
for i in range(1,N):seq[i]=seq[i>>1]^(i&1)
for d in range(1,129):
    words={tuple(seq[i+j*d] for j in range(4)) for i in range(N-3*d)}
    pred=10 if expected_mask(d)==0x6e else 14 if expected_mask(d)==0xf7 else 16
    assert len(words)==pred,(d,len(words),pred)
    if pred==14:
        assert (0,1,1,0) not in words and (1,0,0,1) not in words
    if pred==10:
        assert (0,0,0,0) not in words and (1,1,1,1) not in words

print('VERIFY_OK base_states=192 determinized_states=195 classes=5,6,184 '
      'relative_spectra=0x6e,0xf7,0xff '
      'exact_witness_d=1..511 '+f'witnesses={num_witnesses} '
      'direct_prefix=80000 d=1..128 '
      'theorem_lengths=10,14,16')
