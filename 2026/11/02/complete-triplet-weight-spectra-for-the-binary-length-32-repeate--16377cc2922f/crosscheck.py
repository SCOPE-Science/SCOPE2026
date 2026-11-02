"""Independent smaller-instance/selected-row checks of the 32-site triplet spectra.
Uses a separate Python encoding and cyclic-window loops, not the C recurrence.
"""
import csv
from collections import Counter

with open('SPECTRUM.csv', newline='', encoding='utf-8') as f:
    rows = list(csv.DictReader(f))
assert len(rows) == 33

# Direct generator-message enumeration for selected codes, crossing the
# syndrome-versus-generator method boundary at i=11,12.
def generator(i):
    # Binomial coefficients mod 2 from Pascal recurrence, independent of
    # the C verifier's binary-submask implementation.
    row = [1]
    for _ in range(i):
        row = [1] + [row[k-1] ^ row[k] for k in range(1,len(row))] + [1]
    return sum(bit << k for k,bit in enumerate(row))

def rot_right(x,r):
    return (x >> r) | ((x << (32-r)) & ((1<<32)-1))

def triplet_weight(x):
    return (x | rot_right(x,1) | rot_right(x,2)).bit_count()

for i in (11,12,16,20,28,29,30,31,32):
    g = generator(i)
    hist = Counter()
    # Gray walk over all 2^(32-i) distinct messages, toggling one basis column
    word = 0
    oldgray = 0
    for j in range(1 << (32-i)):
        gray = j ^ (j>>1)
        if j:
            changed = gray ^ oldgray
            word ^= g << (changed.bit_length()-1)
        oldgray = gray
        hist[triplet_weight(word)] += 1
    for w in range(33):
        assert hist[w] == int(rows[i]['A_'+str(w)]), (i,w)

# Independently count full-triplet weight in all binary words by transfer
# matrix: a cyclic 32-word has w3=32 precisely when it avoids cyclic 000.
n=4
M=[[0]*n for _ in range(n)]
for pair in range(n):
    a,b=pair>>1,pair&1
    for c in (0,1):
        if a or b or c:
            M[pair][(b<<1)|c]+=1

def mul(A,B):
    return [[sum(A[i][k]*B[k][j] for k in range(n)) for j in range(n)] for i in range(n)]
P=[[int(i==j) for j in range(n)] for i in range(n)]
for _ in range(32):P=mul(P,M)
assert sum(P[j][j] for j in range(n))==int(rows[0]['A_32'])==294294531

# Exact conservation, nesting and zero/nonzero boundary.
for i,r in enumerate(rows):
    assert sum(int(r['A_'+str(w)]) for w in range(33))==1<<(32-i)
    assert int(r['A_0'])==1
    if i<32:
        for w in range(33):
            assert int(rows[i+1]['A_'+str(w)])<=int(r['A_'+str(w)])
print('CROSSCHECK_OK')
