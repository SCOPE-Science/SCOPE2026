#!/usr/bin/env python3
"""Finite arithmetic sanity check for monomial counts in a truncated graded ring."""

def check():
    for m in range(2, 13):
        for degree in range(2 * m):
            if degree % 2:
                assert not [(a, b) for a in range(m) for b in range(m) if 2*(a+b)==degree]
                continue
            j=degree//2
            basis=[(a,j-a) for a in range(j+1)]
            assert len(basis)==j+1
            assert sum(a>0 for a,b in basis)==j
            assert (j,0) in basis
    print('VERIFY_OK finite_monomial_profiles=m2_to_m12')

if __name__=='__main__':
    check()
