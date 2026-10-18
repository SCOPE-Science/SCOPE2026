#!/usr/bin/env python3
"""Independent exhaustive checks for a two-dependence-atom team-size enumerator."""
from math import comb


def polynomial(r, s):
    # Coefficients of the claimed rectangular cross-cover enumerator.
    v = [r*s*comb(r+s-1, k) for k in range(r+s)]
    v[0] -= r*s-1
    v[1] -= r*s*(r+s-2)
    for k in range(2, s+1):
        v[k] -= r*(s-1)*comb(s,k)
    for k in range(2, r+1):
        v[k] -= s*(r-1)*comb(r,k)
    if min(r,s) >= 2:
        v[2] -= 2*comb(r,2)*comb(s,2)
    return v


def independent_bruteforce(r, s):
    # Independently construct each row-column cross as a bit mask.
    hist = [0]*(r*s+1)
    crosses = []
    for i in range(r):
        for j in range(s):
            cross = 0
            for a in range(r):
                for b in range(s):
                    if a == i or b == j:
                        cross |= (1 << (a*s+b))
            crosses.append(cross)
    for subset in range(1 << (r*s)):
        if any(subset & ~cross == 0 for cross in crosses):
            hist[subset.bit_count()] += 1
    return hist


def direct_lax_semantics(q, bits):
    assignments = [(x,y,z) for x in range(q) for y in range(q) for z in range(q)]
    team = [a for h,a in enumerate(assignments) if bits >> h & 1]
    for coloring in range(1 << len(team)):
        left = [a for k,a in enumerate(team) if coloring >> k & 1]
        right = [a for k,a in enumerate(team) if not(coloring >> k & 1)]
        if all(u[1] == v[1] for u in left for v in left if u[0] == v[0]) and \
           all(u[2] == v[2] for u in right for v in right if u[0] == v[0]):
            return True
    return False


def direct_cross_criterion(q, bits):
    for x in range(q):
        slice_ = [(y,z) for y in range(q) for z in range(q)
                  if bits >> (x*q*q + y*q + z) & 1]
        if not any(all(y == a or z == b for y,z in slice_)
                   for a in range(q) for b in range(q)):
            return False
    return True


def main():
    for r in range(1,5):
        for s in range(1,5):
            actual = independent_bruteforce(r,s)
            predicted = polynomial(r,s)
            assert actual[:len(predicted)] == predicted, (r,s,actual,predicted)
            assert not any(actual[len(predicted):]), (r,s,actual)
            assert all(v >= 0 for v in predicted)
            if r == s:
                print('square fibers:',r,'coefficients:',predicted,'total:',sum(predicted))
    print('ALL_16_RECTANGULAR_FIBER_CENSUSES_OK')
    for bits in range(1<<8):
        assert direct_lax_semantics(2,bits) == direct_cross_criterion(2,bits)
    assert sum(direct_lax_semantics(2,b) for b in range(256)) == 225
    print('BINARY_256_FULL_TEAMS_OK')
    print('DEPENDENCE_RECTANGULAR_SIZE_ENUMERATOR_OK')

if __name__ == '__main__':
    main()
