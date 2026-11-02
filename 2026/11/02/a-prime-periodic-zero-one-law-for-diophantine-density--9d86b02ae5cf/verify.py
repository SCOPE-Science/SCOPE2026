"""Exact finite checks for the prime-periodic Diophantine-density classification.

Only finite sanity checks; the general theorem is proved mathematically.
"""
from itertools import combinations
from math import gcd


def primes_at_most(n):
    return [p for p in range(2,n+1) if all(p%d for d in range(2,int(p**.5)+1))]


def min_numerator(p,q,residues,ell):
    out = []
    for v in range(1,q):
        if v % ell in residues:
            r = (v*p) % q
            out.append(min(r,q-r))
    return min(out) if out else None


def check():
    total_subsets = total_witnesses = total_full = 0
    for ell in primes_at_most(7):
        for mask in range(1<<ell):
            residues = {r for r in range(ell) if mask & (1<<r)}
            total_subsets += 1
            if not residues:
                continue
            if 0 in residues or len(residues)==ell-1:
                for q in range(2*ell+1,62):
                    for p in range(1,q):
                        if gcd(p,q)!=1:
                            continue
                        best = min_numerator(p,q,residues,ell)
                        assert best is not None and best <= ell, (ell,residues,p,q,best)
                        total_full += 1
            else:
                missing = next(t for t in range(1,ell) if t not in residues)
                a = (-pow(missing,-1,ell)) % ell
                assert 1 <= a < ell
                for q in range(2*ell+1,250):
                    if (a*q+1)%ell:
                        continue
                    p = (a*q+1)//ell
                    assert gcd(p,q)==1 and 1<=p<q
                    best = min_numerator(p,q,residues,ell)
                    assert best is not None and ell*best >= q, (ell,residues,p,q,best)
                    total_witnesses += 1
    # An arbitrarily high ordinary-density but zero-Diophantine-density example.
    ell=101
    residues=set(range(1,ell))-{ell-1}
    for q in range(2*ell+1,1000):
        if (q+1)%ell: continue
        p=(q+1)//ell
        best=min_numerator(p,q,residues,ell)
        assert best is not None and ell*best>=q
        total_witnesses+=1
    print('VERIFY_OK')
    print('prime_residue_subsets:',total_subsets)
    print('full_density_coprime_pairs:',total_full)
    print('zero_density_obstructed_pairs:',total_witnesses)
    print('nontrivial near-unit natural density example: 99/101')

if __name__=='__main__': check()
