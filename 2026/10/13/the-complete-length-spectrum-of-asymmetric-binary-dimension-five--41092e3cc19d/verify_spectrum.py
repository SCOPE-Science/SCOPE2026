"""Independent exhaustive permutation-of-basis check for rigid binary point-set witnesses."""
from itertools import permutations
CORE=(1,2,4,8,16,3,5,6,9,14,18,25,17,22,24,26)

def image(v, q):
    y=0
    for i in range(5):
        if v&(1<<i): y ^= q[i]
    return y

def independent(p):
    piv=[0]*5
    for x in p:
        while x:
            h=x.bit_length()-1
            if piv[h]: x ^= piv[h]
            else:
                piv[h]=x
                break
        else: return False
    return True

for length in (12,13,14,15):
    S=CORE[:length]
    assert len(set(S))==length
    Sset=set(S)
    automorphisms=0
    for q in permutations(S,5):
        if independent(q) and all(image(v,q) in Sset for v in S):
            automorphisms+=1
            assert q==(1,2,4,8,16)
    assert automorphisms==1
    # The complement in the 31 nonzero vectors has the same linear stabilizer.
    print('length',length,'witness',','.join(map(str,S)),'stabilizer',automorphisms,'complement_length',31-length)
print('VERIFY_OK')
