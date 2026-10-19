"""Exact finite tests of minimal tight Fourier masks and translation orbits.

All frequency-mask tests use integer residue-class counts; no floating point.
"""
from itertools import product

def tight(B,p,k,J):
    for j in J:
        stride=p**j
        buckets={}
        for b in B:
            prefix=b%stride
            digit=(b//stride)%p
            if prefix not in buckets:
                buckets[prefix]=[0]*p
            buckets[prefix][digit]+=1
        if any(len(set(c))!=1 for c in buckets.values()):
            return False
    return True

def enumerate_case(p,k):
    N=p**k
    subsets=[frozenset(i for i in range(N) if mask>>i&1)
             for mask in range(1,1<<N)]
    for level_bits in range(1<<k):
        J={j for j in range(k) if level_bits>>j&1}
        r=len(J)
        e=sum(p**sum(h<j for h in J) for j in range(k) if j not in J)
        missing=set(range(k))-J
        s=1+max(missing) if missing else 0
        assert e>=s
        optimal=[B for B in subsets if len(B)==p**r and tight(B,p,k,J)]
        assert len(optimal)==p**e,(p,k,J,len(optimal),p**e)
        for B in optimal:
            assert {(b+p**s)%N for b in B}==B
            if s>0:
                assert {(b+p**(s-1))%N for b in B}!=B
            # Check every occupied prefix has the desired number of child digits.
            for j in range(k):
                prefixes={b%(p**j) for b in B}
                for prefix in prefixes:
                    children={(b//(p**j))%p for b in B if b%(p**j)==prefix}
                    assert len(children)==(p if j in J else 1)
        # Translation orbits from canonical sorted representatives.
        orbits={min(tuple(sorted((b+t)%N for b in B)) for t in range(N))
                for B in optimal}
        assert len(orbits)==p**(e-s),(p,k,J,len(orbits),p**(e-s))
    print(f'PASS p={p} k={k} N={N} J_profiles={1<<k}',flush=True)

if __name__=='__main__':
    for p,k in ((2,1),(2,2),(2,3),(3,1),(3,2),(5,1)):
        enumerate_case(p,k)
    print('VERIFY_OK all requested profiles; integer-only and finite',flush=True)
