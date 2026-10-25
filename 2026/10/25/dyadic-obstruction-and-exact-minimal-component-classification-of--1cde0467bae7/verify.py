#!/usr/bin/env python3
"""Finite, exact diagnostics for Thue–Morse cyclic cocycles. No external dependencies."""
from math import gcd

def main():
    MAX=8192
    t=[j.bit_count()%2 for j in range(MAX)]
    s=[0]
    for a in t:s.append(s[-1]+a)
    checks=0
    for n in range(MAX):
        if n%2==0:
            assert s[n]==n//2
        else:
            assert s[n]==n//2+t[n//2]
        checks+=1
    for q in range(2,131):
        k=0; m=q
        while m%2==0:
            k+=1;m//=2
        two=1<<k
        for n in range(MAX):
            if two>1:
                r=n%(2*two)
                u=(r//2+(r%2)*(1-t[n]))%two
                assert s[n]%two==u
                checks+=1
            if m>1:
                d=pow(2,-1,m)
                u=(n%2)*(d-t[n])%m
                assert s[n]%m==(n*d+u)%m
                checks+=1
    # For each odd modulus, show the finite witness criterion for primitivity of
    # the decorated length-two substitution: both digits at each residue.
    for m in [1,3,5,7,9,11,13,15,17,19,21,23,25]:
        seen={(a,r) for a,r in ((t[j],j%m) for j in range(MAX))}
        assert len(seen)==2*m, (m,len(seen))
        for startbit in [0,1]:
            for startphase in range(m):
                symbols={(t[j]^startbit,(startphase*MAX+j)%m) for j in range(MAX)}
                assert len(symbols)==2*m,(m,startbit,startphase)
                checks+=1
    # Check each short factor has occurrences in every odd congruence class.
    for width in range(1,7):
        allwords={tuple(t[j:j+width]) for j in range(MAX-width+1)}
        for m in [1,3,5,7,9,11,13]:
            seen={tuple(t[j:j+width]):set() for j in range(MAX-width+1)}
            for j in range(MAX-width+1):seen[tuple(t[j:j+width])].add(j%m)
            assert all(len(rs)==m for rs in seen.values()),(width,m)
            assert set(seen)==allwords
            checks+=len(allwords)
    print('VERIFICATION_OK',checks)
if __name__=='__main__':main()
