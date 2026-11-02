#!/usr/bin/env python3
"""Reproduce the finite Lucas residue and decomposition checks for the stated theorem."""
L=[2,1]
for _ in range(2,14+24*7+1):
    L.append(L[-1]+L[-2])
assert L[13]==521 and L[24]==103682 and L[25]==167761
assert L[24]%12==2 and L[25]%12==1
for k in range(len(L)-24):
    assert L[k+24]%12==L[k]%12
patterns=((6,3,1),(6,4),(6,4,0),(7,),(7,0))
offsets=(23,25,27,29,31)
counts=(4,3,4,2,3)
for m in range(8):
    j=13+24*m
    assert L[j]%12==5
    for off,small,denom in zip(offsets,patterns,counts):
        inds=(j,)+small
        assert len(inds)==len(set(inds))
        assert all(abs(a-b)!=1 for i,a in enumerate(inds) for b in inds[i+1:])
        assert not (0 in inds and 2 in inds)
        assert L[j]+sum(L[k] for k in small)==L[j]+off
        assert len(inds)==denom
        assert (L[j]+off)%denom==0
print('VERIFY_OK boundary=13,24,25 period_mod12=24 profiles=8 all_exact=yes')
