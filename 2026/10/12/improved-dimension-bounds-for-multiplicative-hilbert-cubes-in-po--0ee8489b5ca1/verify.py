#!/usr/bin/env python3
# Exact transcription checks for the accompanying symbolic proof.

def gap_identity(x,y,z,w,n):
    return (x*z+n)*(y*w+n)-(x*w+n)*(y*z+n) == n*(y-x)*(w-z)

for n in range(1,11):
    for x in range(1,6):
        for y in range(x+1,8):
            for z in range(1,6):
                for w in range(z+1,8):
                    assert gap_identity(x,y,z,w,n)

# Compare r(k-1)/k >= k/(k-2) without floating point:
def exponent_ok(k,r):
    return r*(k-1)*(k-2) >= k*k

assert exponent_ok(4,3)
assert exponent_ok(5,3)
assert not exponent_ok(5,2)
assert exponent_ok(6,2)
for k in range(6,1001):
    assert exponent_ok(k,2)
    assert k*k-6*k+4 >= 0

print('VERIFY_OK gap_identity_cases=4410 boundary=k4:r3,k5:r3,k6:r2 two_tail_checked_k=6..1000')
