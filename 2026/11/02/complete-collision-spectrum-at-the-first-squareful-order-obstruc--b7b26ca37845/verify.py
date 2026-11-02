#!/usr/bin/env python3
"""Exact integer-mask dynamic program for the mod-10 power-permutation spectrum."""
from collections import defaultdict, Counter
from math import factorial

def main():
    n=10
    dp={(0,0):1}
    for i in range(1,n+1):
        next_dp=defaultdict(int)
        for (used_exponents,used_residues),count in dp.items():
            for exponent in range(1,n+1):
                bit=1<<(exponent-1)
                if used_exponents&bit: continue
                residue=pow(i,exponent,n)
                next_dp[(used_exponents|bit, used_residues|(1<<residue))]+=count
        dp=next_dp
    distribution=Counter()
    for (used_exponents,used_residues),count in dp.items():
        assert used_exponents==(1<<n)-1
        distribution[used_residues.bit_count()]+=count
    expected={5:9792,6:537408,7:1822464,8:1175040,9:84096}
    assert dict(distribution)==expected,(distribution,expected)
    assert sum(distribution.values())==factorial(n)
    print('VERIFY_OK',sorted(distribution.items()))
if __name__=='__main__':main()
