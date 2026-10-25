#!/usr/bin/env python3
"""Standalone elementary checks for the Boolean-lattice type transform."""
from itertools import combinations
from math import comb

def downsets(n):
    size=1 << n
    # Generate order ideals from all antichains in rank-filtered fashion.
    # An ideal is coded as an integer bitset over the vertices (subsets) of B_n.
    ideals = [0]
    for vertex in range(size):
        # choose whether the new vertex belongs to the ideal, only when
        # all its strict lower subsets already occur in the ideal.
        below = sum(1 << sub for sub in range(size) if sub != vertex and (sub & vertex) == sub)
        ideals = ideals + [I | (1 << vertex) for I in ideals if (I & below) == below]
    return ideals

def exhaustive(n):
    ideals = downsets(n)
    N = 1 << n
    full = (1 << N) - 1
    # Complement of an upset is a downset.
    upsets = [full ^ I for I in ideals]
    count = 0
    for lower in ideals:
        for upper in upsets:
            if lower & upper:
                continue
            # strict comparability is required for every relation p<x<q.
            if all((s & t) == s and s != t for s in range(N) if (lower >> s) & 1 for t in range(N) if (upper >> t) & 1):
                count += 1
    return len(ideals), count

def predicted(n, D):
    a = [sum((-1)**(s-i)*comb(s,i)*D[i] for i in range(s+1)) for s in range(n+1)]
    return sum(comb(n,s)*a[s]*D[n-s] for s in range(n+1))-2**n

def main():
    D=[]
    actual=[]
    for n in range(5):
        ded, typ=exhaustive(n)
        D.append(ded); actual.append(typ)
        pred=predicted(n,D)
        assert typ==pred,(n,typ,pred)
        print('n=%d M(n)=%d types=%d predicted=%d' % (n,ded,typ,pred))
    assert D==[2,3,6,20,168]
    assert actual==[3,6,18,86,808]
    big=[2,3,6,20,168,7581,7828354,2414682040998,56130437228687557907788]
    for n in range(5,9):
        print('n=%d M(n)=%d predicted_types=%d' % (n,big[n],predicted(n,big)))
    print('ALL_TESTS_PASS')
if __name__=='__main__':main()
