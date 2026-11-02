#!/usr/bin/env python3
"""Independent checks of near-capacity burning-sequence enumerations.

Uses only the standard library; no external datasets or programs.
"""
from itertools import product, permutations
from math import factorial


def distance(u, v, n, cycle):
    d = abs(u-v)
    return min(d, n-d) if cycle else d


def status(seq, n, cycle):
    """Return legal, terminal-redundant using original burning dynamics."""
    burned = set()
    for idx, source in enumerate(seq):
        if source in burned:
            return False, False
        redundant = bool(idx and any(distance(source, v, n, cycle) == 1 for v in burned))
        after_spread = set(burned)
        for v in burned:
            if cycle:
                after_spread.update(((v-1)%n, (v+1)%n))
            else:
                if v > 0:
                    after_spread.add(v-1)
                if v+1 < n:
                    after_spread.add(v+1)
        after_spread.add(source)
        burned = after_spread
    return len(burned) == n, redundant


def expected(k,cycle, deficit):
    n = k*k - deficit
    if cycle:
        return (n*factorial(k-1)*(k if deficit else 1),
                2*n*factorial(k-1) if deficit else 0)
    return ((k-1)*factorial(k-1)*(k+2) if deficit else factorial(k),
            2*(k-1)*factorial(k-1) if deficit else 0)


def constructive(k,cycle,deficit):
    n=k*k-deficit
    lengths=[2*(k-1-i)+1 for i in range(k)]
    if cycle:
        orders=((0,)+tail for tail in permutations(range(1,k)))
        for order in orders:
            for overlap in (range(k) if deficit else [-1]):
                for offset in range(n):
                    cursor=offset
                    centers=[None]*k
                    for j,i in enumerate(order):
                        centers[i]=(cursor+(lengths[i]-1)//2)%n
                        cursor+=lengths[i]
                        if j == overlap and j<k-1:
                            cursor-=1
                    yield tuple(centers)
    else:
        for order in permutations(range(k)):
            if not deficit:
                centers=[None]*k
                cursor=0
                for i in order:
                    centers[i]=cursor+(lengths[i]-1)//2
                    cursor+=lengths[i]
                yield tuple(centers)
            else:
                for side in ('left','right'):
                    if lengths[order[0 if side=='left' else -1]]==1:
                        continue
                    centers=[None]*k
                    cursor=-1 if side=='left' else 0
                    for i in order:
                        centers[i]=cursor+(lengths[i]-1)//2
                        cursor+=lengths[i]
                    yield tuple(centers)
                for joint in range(k-1):
                    centers=[None]*k
                    cursor=0
                    for j,i in enumerate(order):
                        centers[i]=cursor+(lengths[i]-1)//2
                        cursor+=lengths[i]
                        if j==joint:
                            cursor-=1
                    yield tuple(centers)


def direct(k,cycle,deficit):
    n=k*k-deficit
    total=red=0
    for seq in product(range(n), repeat=k):
        legal, terminal_red=status(seq,n,cycle)
        if legal:
            total+=1
            red+=terminal_red
    return total,red


def main():
    for k in range(2,5):
        for cycle in (False,True):
            for d in (0,1):
                seen=set()
                reds=0
                n=k*k-d
                for seq in constructive(k,cycle,d):
                    assert seq not in seen, (k,cycle,d,'duplicate',seq)
                    seen.add(seq)
                    legal,red=status(seq,n,cycle)
                    assert legal, (k,cycle,d,'invalid',seq)
                    reds+=red
                assert (len(seen),reds)==expected(k,cycle,d),(k,cycle,d,len(seen),reds)
                exhaustive=direct(k,cycle,d)
                assert exhaustive==expected(k,cycle,d),(k,cycle,d,exhaustive)
                print('DIRECT_AND_CONSTRUCTIVE_OK', 'C' if cycle else 'P',k,d,exhaustive)
    for k in (5,6):
        for cycle in (False,True):
            for d in (0,1):
                seen=set()
                red=0
                for seq in constructive(k,cycle,d):
                    assert seq not in seen,(k,cycle,d,'duplicate',seq)
                    seen.add(seq)
                    legal,last_red=status(seq,k*k-d,cycle)
                    assert legal,(k,cycle,d,'invalid',seq)
                    red+=last_red
                assert (len(seen),red)==expected(k,cycle,d),(k,cycle,d,len(seen),red)
                print('CONSTRUCTIVE_LARGER_OK','C' if cycle else 'P',k,d,len(seen),red)
    print('VERIFY_OK')


if __name__=='__main__':
    main()
