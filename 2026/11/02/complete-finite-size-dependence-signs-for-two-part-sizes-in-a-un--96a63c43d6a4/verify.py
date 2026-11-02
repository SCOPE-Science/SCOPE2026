#!/usr/bin/env python3
"""Exact finite certificate for the two-size presence-covariance classification.

The infinite reduction uses DeSalvo--Pak's independently published theorem
p(m)^2 > p(m-1)p(m+1) for every integer m >= 26.
This verifier establishes all finite inequalities required by that reduction.
"""
from fractions import Fraction

POS_EXCEPTIONS = {
    (5,2,3), (6,2,4), (7,2,5), (8,3,5),
    (6,1,3), (8,1,3), (10,1,3), (12,1,3),
    (12,1,5), (14,1,3), (16,1,3)
}
ZEROS = {(8,2,6), (9,2,7), (7,3,4), (10,1,5), (9,1,2)}

def partition_numbers(maximum):
    p=[0]*(maximum+1)
    p[0]=1
    for part in range(1,maximum+1):
        for m in range(part,maximum+1):
            p[m]+=p[m-part]
    return p

def defect(p,a,r,s):
    return p[a+r]*p[a+s]-p[a]*p[a+r+s]

def predicted(n,r,s):
    assert 1<=r<s<=n
    if (n,r,s) in ZEROS:
        return 0
    if (r==1 and s==n-1 and n>=3) or (n,r,s) in POS_EXCEPTIONS:
        return 1
    return -1

def sign(x): return (x>0)-(x<0)

p=partition_numbers(150)
assert p[:11] == [1,1,2,3,5,7,11,15,22,30,42]

# The entire bounded rectangle necessary for the infinite proof.
counts={-1:0,0:0,1:0};diagonal_negative=[]
for a in range(26):
    R=26-a
    assert defect(p,a,R,R)>0
    for r in range(1,R+1):
        for s in range(r,R+1):
            F=defect(p,a,r,s)
            if r==s:
                if F<0: diagonal_negative.append((a,r))
                continue
            n=a+r+s
            observed=-sign(F) # covariance is minus this defect
            assert observed==predicted(n,r,s),(n,r,s,observed)
            counts[observed]+=1
    # Along the saturation boundary there is only the persistent exception.
    for r in range(1,R):
        v=defect(p,a,r,R)
        assert (v<0)==(a==0 and r==1)
        assert v!=0
assert counts == {-1:2884, 0:5, 1:36},counts
assert len(diagonal_negative)==15

# Independent complete rational covariance checks for n up to 150,
# including all complementary and forbidden-size cases.
num_covariance_checks=0
for n in range(2,151):
    for r in range(1,n):
        for s in range(r+1,n+1):
            num = (p[n]*p[n-r-s] if r+s<=n else 0)-p[n-r]*p[n-s]
            assert sign(num)==predicted(n,r,s),(n,r,s,num)
            num_covariance_checks+=1

# A separate partition generator checks the probability identity from
# its combinatorial meaning, without using p(n-r-s) in counting.
def partitions(n, upper=None):
    if n==0:
        yield ()
        return
    if upper is None: upper=n
    for m in range(min(n,upper),0,-1):
        for tail in partitions(n-m,m):
            yield (m,)+tail
num_enumerated=0
for n in range(2,15):
    examples=list(partitions(n))
    assert len(examples)==p[n]
    num_enumerated+=len(examples)
    for r in range(1,n):
        for s in range(r+1,n+1):
            x=sum(r in e for e in examples)
            y=sum(s in e for e in examples)
            xy=sum(r in e and s in e for e in examples)
            direct = xy*len(examples)-x*y
            expected = (p[n]*p[n-r-s] if r+s<=n else 0)-p[n-r]*p[n-s]
            assert direct==expected,(n,r,s,direct,expected)

print('PASS: 2925 distinct-size bounded comparisons; 15 diagonal exceptions classified')
print('PASS: 26 positive diagonal caps and 325 boundary comparisons')
print(f'PASS: {num_covariance_checks} independent exact sign checks to n=150')
print(f'PASS: direct integer-partition enumeration, {num_enumerated} partition objects, n=2..14')
print('Finite certificate does not independently prove the published infinite log-concavity theorem.')
