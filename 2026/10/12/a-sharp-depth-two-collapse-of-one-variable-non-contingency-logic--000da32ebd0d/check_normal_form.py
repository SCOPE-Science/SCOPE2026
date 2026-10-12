#!/usr/bin/env python3
"""Exact finite semantics checks for unary non-contingency on complete irreflexive frames."""
from itertools import product

def check(n):
    assert n >= 1
    # Each state is (valuation mask, pointed world).
    states=[(m,w) for m in range(1<<n) for w in range(n)]
    si={s:i for i,s in enumerate(states)}
    U=(1<<len(states))-1
    P=sum(1<<j for j,(m,w) in enumerate(states) if m>>w & 1)
    def d(X):
        v=0
        for j,(m,w) in enumerate(states):
            vals={bool(X>>si[(m,v)] & 1) for v in range(n) if v!=w}
            if len(vals)<=1: v|=1<<j
        return v
    # Independent modal-depth partition refinement: all Boolean functions of
    # current types are permitted, then one further Delta is applied.
    depth_atoms=[P,U^P]
    spectra=[4]
    for depth in range(1,4):
        base=set()
        for bits in range(1<<len(depth_atoms)):
            mask=0
            for j,X in enumerate(depth_atoms):
                if (bits>>j)&1:mask|=X
            base.add(mask)
        douts=[d(X) for X in base]
        sigs={}
        for i in range(len(states)):
            sig=tuple((X>>i)&1 for X in depth_atoms + douts)
            sigs.setdefault(sig,0)
            sigs[sig]|=1<<i
        depth_atoms=list(sigs.values())
        spectra.append(2**len(depth_atoms))
    expected_spectra=([4,4,4,4] if n<=2 else [4,16,16,16] if n==3 else [4,16,64,64])
    assert spectra==expected_spectra,(n,spectra,expected_spectra)
    dp=d(P)
    a0= U^d(P & dp)
    a1= U^d((U^P) & dp)
    codes={}
    for j,s in enumerate(states):
        k=tuple((x>>j)&1 for x in (P,dp,a0,a1))
        codes.setdefault(k,0)
        codes[k]|=1<<j
    partition=list(codes.values())
    assert sum(partition)==U, (n,'overlap') # disjoint bit masks; sum==OR
    expected=2 if n<=2 else (4 if n==3 else 6)
    assert len(partition)==expected,(n,len(partition),expected)
    # Closure of every union of atoms under the actual semantic modality.
    atoms=partition
    combinations=set()
    for mask in range(1<<len(atoms)):
        x=0
        for j,a in enumerate(atoms):
            if mask>>j&1:x|=a
        combinations.add(x)
    assert len(combinations)==(1<<expected)
    for X in combinations:
        Y=d(X)
        assert Y in combinations,(n, 'closure failed')
    # Verify the alleged class description using only the input counts.
    predicted={}
    for m,w in states:
        p=(m>>w)&1
        b= ((m.bit_count())-p)
        if n<=2: cls=(p,'ALL')
        elif b in (0,n-1):cls=(p,'E')
        elif p==0 and b==1:cls=(p,'S')
        elif p==1 and b==n-2:cls=(p,'S')
        else:cls=(p,'M')
        j=si[(m,w)]
        predicted.setdefault(cls,0)
        predicted[cls]|=1<<j
    assert set(predicted.values())==set(atoms),(n,'signature mismatch')
    # Test the modal box separation for 1,2,... n.
    box=0
    for j,(m,w) in enumerate(states):
        if all(m>>v&1 for v in range(n) if v!=w):box|=1<<j
    if n>=2:
        assert box not in combinations,(n,'box expressible unexpectedly')
    else:
        assert box ==U
    print(f'n={n} states={len(states)} pointed_types={len(atoms)} unary_formula_classes={len(combinations)} depth_spectrum={spectra} modal_closure=PASS box_not_definable={n>=2}')

if __name__=='__main__':
    for n in range(1,10):check(n)
    print('VERIFY_OK')
