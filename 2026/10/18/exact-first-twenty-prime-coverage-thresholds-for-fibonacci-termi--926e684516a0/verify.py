"""Exact finite coverage census of Fibonacci terminal block classes."""
from math import isqrt
M = 20
EXPECTED = [0, 2,17,19,43,103,179,277,1009,1033,5573,5573,11777,31907,45979,86837,165887,386329,797287,1115701,1803947]
LAST = ['','S','D','DS','DSS','DSSS','DSSSS','SDSDS','DSSSSD','DDDSD','SDDSDSS','SDDSDSSS','DSSSSDDD','DSSSSSSDSSS','DSSSSDDDD','SDSSSDSSSDD','SSDDSSSDSSDS','DDSSDSSSDSSSS','DDSSSSDSSSDSSS','SSSDDDSSDSDSSS','DSSDSSSSDSDSSSSS']
P_MAX=EXPECTED[-1]
F=[0,1,1]
while F[-1] <= P_MAX:
    F.append(F[-1]+F[-2])
num_words=[0]*(M+1)
num_words[0]=num_words[1]=1
for m in range(2,M+1):
    num_words[m]=num_words[m-1]+num_words[m-2]
seen=[dict() for _ in range(M+1)]
sieve=bytearray(b'\x01')*(P_MAX+1)
sieve[:2]=b'\0\0'
for p in range(2,isqrt(P_MAX)+1):
    if sieve[p]:
        sieve[p*p::p] = b'\0'*((P_MAX-p*p)//p+1)
prime_count=0
for prime in range(2,P_MAX+1):
    if not sieve[prime]:
        continue
    prime_count += 1
    digits=[0]*(len(F)-1)
    remainder=prime
    for k in range(len(F)-1,1,-1):
        if F[k]<=remainder:
            digits[k-1]=1
            remainder -= F[k]
    assert remainder==0
    assert not any(digits[k] and digits[k+1] for k in range(len(digits)-1))
    pos=0
    blocks=''
    while pos < M:
        if digits[pos]==0 and digits[pos+1]==1:
            blocks += 'D'
            pos += 2
        else:
            assert digits[pos]==0
            blocks += 'S'
            pos += 1
        if pos<=M:
            seen[pos].setdefault(blocks,prime)
assert prime_count==135340,(prime_count,135340)
for m in range(1,M+1):
    d=seen[m]
    assert len(d)==num_words[m],(m,len(d),num_words[m])
    maximal=max(d.values())
    assert maximal==EXPECTED[m],(m,maximal,EXPECTED[m])
    assert d[LAST[m]]==maximal,(m,LAST[m])
    for blocks,smallest_prime in d.items():
        assert sum(1 if char=='S' else 2 for char in blocks)==m
        assert sieve[smallest_prime]
print('VERIFY_OK', 'prime_count=',prime_count, 'total_length_20_words=',num_words[20], 'sharp_threshold=',P_MAX)
