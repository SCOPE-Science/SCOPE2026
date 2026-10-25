#!/usr/bin/env python3
"""Finite checks for shifted regular paperfolding DFAO state enumeration."""

def paperfolding(n):
    assert n>=0
    x=n+1
    x >>= ((x&-x).bit_length()-1)+1
    return x&1

def formula(c):
    return 4 if c==0 else c.bit_length()+5

def literal_kernel(c, extra=3, terms=None):
    if terms is None: terms=max(100,4*c+20)
    # Every state is a residual function n -> f(2^k*n+c+r).
    # Enumerate all prefixes through k = bit_length(c)+extra.
    keys=set()
    for k in range(c.bit_length()+extra+1):
        base=1<<k
        for r in range(base):
            keys.add(bytes(paperfolding(base*n+c+r) for n in range(terms)))
    return len(keys)

def structural_kernel(c):
    # All residuals fall in 4 families: shifted f, two parities, two constants.
    shifts={c>>k for k in range(c.bit_length()+3)}
    parity={((c+(1<<(k-1)))>>k)&1 for k in range(1,c.bit_length()+4)}
    return len(shifts)+len(parity)+2

for c in list(range(96))+[127,128,129,191,192,255]:
    v=literal_kernel(c)
    predicted=formula(c)
    assert v==predicted==structural_kernel(c),(c,v,predicted,structural_kernel(c))
print('PASS: full literal residual enumeration, all c=0..95 and selected c=127,128,129,191,192,255; residuals to depth bit_length(c)+3 with at least max(100,4*c+20) continuation values.')
for c in (256,257,383,511,512,513,1023,1024,16384):
    assert structural_kernel(c)==formula(c),(c,structural_kernel(c),formula(c))
print('PASS: structural enumeration for boundary shifts through c=16384.')
# Independent direct arithmetic rule at arbitrary offset and every k,r,z with bounded parameter grid.
for c in range(40):
    for k in range(1,9):
        b=1<<k
        for r in range(b):
            w=c+r+1
            residue=w%b
            q=w//b
            for z in (0,1,2,7,17,64):
                if residue==0:
                    want=paperfolding(z+q-1)
                elif residue==b//2:
                    want=(z+q)&1
                else:
                    t=(residue & -residue).bit_length()-1
                    want=(residue>>(t+1))&1
                got=paperfolding(b*z+c+r)
                assert got==want,(c,k,r,z,got,want)
print('PASS: all residue-type rules, 40 shifts × 8 levels × every prefix × 6 continuations.')
