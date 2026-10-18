#!/usr/bin/env python3
"""Independent finite verification of cyclic rotation-wise subsequence coverage."""
from itertools import product

def subseq(v,w):
    j=0
    for a in w:
        if a==v[j]:
            j+=1
            if j==len(v):return True
    return False

def covered(v,w):
    if not v:return True
    return any(subseq(v,w[i:]+w[:i]) for i in range(len(w)))

def formula(a,b,r):
    return min(r*a,r*b,2*r+1)

def test():
    tests=0;patterns=0;boundchecks=0
    for a in range(1,7):
      for b in range(1,7):
       for r in range(1,5):
        w='0'*a+'1'*b
        w=w*r
        k=formula(a,b,r)
        if k>9:continue
        for bits in product('01',repeat=k):
            assert covered(''.join(bits),w),(a,b,r,k,''.join(bits))
            patterns+=1
        tests+=1
        missing= next((''.join(x) for x in product('01',repeat=k+1) if not covered(''.join(x),w)),None)
        assert missing is not None,(a,b,r,k)
        boundchecks+=1
    print(f'PASS: {tests} parameter triples, {patterns} universal-pattern checks, {boundchecks} sharpness checks')
    # Confirm separation of quantifiers in a concrete example.
    w='000111'
    assert all(covered(''.join(p),w) for p in product('01',repeat=3))
    assert not any(all(subseq(''.join(p),w[i:]+w[:i]) for p in product('01',repeat=3)) for i in range(len(w)))
    print('PASS: 000111 has rotation-wise 3-universality but no individually 3-universal conjugate')

if __name__=='__main__':test()
