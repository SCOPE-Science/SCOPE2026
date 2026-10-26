"""Independent exhaustive verification of the minimal-fort theorem for comb trees.

Python 3 standard library only. Spine vertices are 0,...,n-1;
private leaves are n,...,2*n-1. The exhaustive routine evaluates the
original neighborhood definition for every vertex subset, and uses a
subset dynamic program to recognize inclusion-minimal forts.
"""
from collections import Counter


def original_minimal_forts(n):
    size = 2*n
    neighbors = [0]*size
    for i in range(n):
        j=n+i
        neighbors[i] |= 1<<j
        neighbors[j] |= 1<<i
        if i+1<n:
            neighbors[i] |= 1<<(i+1)
            neighbors[i+1] |= 1<<i
    any_fort = bytearray(1<<size)
    minimal = set()
    fort_count = 0
    for mask in range(1,1<<size):
        proper_contains_fort = False
        bits=mask
        while bits:
            lsb=bits&-bits
            if any_fort[mask^lsb]:
                proper_contains_fort=True
                break
            bits-=lsb
        fort = True
        for v in range(size):
            if not mask>>v&1 and (neighbors[v]&mask).bit_count()==1:
                fort=False
                break
        if fort:
            fort_count += 1
            if not proper_contains_fort:
                minimal.add(mask)
        any_fort[mask] = fort or proper_contains_fort
    return minimal, fort_count


def claimed_minimal_forts(n):
    output=set()
    for a in range(n):
        for b in range(a,n,2):
            chosen=set(range(a,b+1,2))
            mask=0
            for i in chosen:
                mask |= (1<<i) | (1<<(n+i))
            for i in (a-1,b+1):
                if 0<=i<n:
                    mask |= (1<<(n+i))
            output.add(mask)
    return output


def predicted_profile(n):
    counts=Counter()
    for k in range(1,n//2+1):
        counts[2*k+1] += 2
        counts[2*k+2] += n-2*k
    if n%2:
        counts[n+1] += 1
    return +counts


def main():
    total_tested=0
    total_forts=0
    total_minimal=0
    for n in range(1,10):
        brute, fort_count = original_minimal_forts(n)
        predicted=claimed_minimal_forts(n)
        assert brute == predicted, (n, brute^predicted)
        actual_profile = Counter(mask.bit_count() for mask in brute)
        assert actual_profile == predicted_profile(n), (n,actual_profile,predicted_profile(n))
        assert len(brute)==((n+1)**2)//4
        total_tested += 2**(2*n)
        total_forts += fort_count
        total_minimal += len(brute)
        print('n=%d subsets=%d forts=%d minimal=%d profile=%s' %
              (n,4**n,fort_count,len(brute),dict(sorted(actual_profile.items()))))
    print('VERIFICATION_OK cases=9 subsets=%d forts=%d minimal=%d' %
          (total_tested,total_forts,total_minimal))


if __name__=='__main__':
    main()
