"""Finite-state arithmetic certificate for Stern modulo-five discrepancy extrema.
Run using Python 3 with no third-party dependencies.
"""
from functools import lru_cache
from pathlib import Path
import csv

MOD = 5
STATES = tuple((a,b) for a in range(MOD) for b in range(MOD) if a or b)
assert len(STATES) == 24

def weight(a):
    return int(a == 1) - int(a == 4)

def left(v):
    a,b=v
    return (a,(a+b)%MOD)

def right(v):
    a,b=v
    return ((a+b)%MOD,b)

def next_layer(prev):
    out = {}
    for v in STATES:
        sl,hl,jl=prev[left(v)]
        sr,hr,jr=prev[right(v)]
        out[v]=(sl+sr,max(hl,sl+hr),min(jl,sl+jr))
    return out

rows=[{v:(weight(v[0]),max(0,weight(v[0])),min(0,weight(v[0]))) for v in STATES}]
for _ in range(40):
    rows.append(next_layer(rows[-1]))

# This identity, verified for all 24 states, propagates to every later
# layer by substituting the same max/min recurrence at both depths.
for v in STATES:
    s,h,j=rows[16][v]
    assert rows[28][v]==(s,h+4,j-4),v

expected_max=(7,7,7,7,8,8,8,8,9,9,9,9)
expected_min=(-1,-1,-2,-2,-2,-2,-4,-4,-4,-4,-5,-5)
for off in range(12):
    r=8+off
    assert rows[r][(0,1)][1:] == (expected_max[off],expected_min[off])
for r in range(8,16):
    a=rows[r][(0,1)]
    b=rows[r+12][(0,1)]
    assert b == (a[0],a[1]+4,a[2]-4)

# Independent method: calculate an arbitrary prefix by binary-block
# decomposition without the max/min dynamic program.
@lru_cache(maxsize=None)
def total_block(v,r):
    if r==0:
        return weight(v[0])
    return total_block(left(v),r-1)+total_block(right(v),r-1)

def prefix(N):
    assert N>=0
    v=(0,1)
    out=0
    for bit in range(N.bit_length()-1,-1,-1):
        if (N>>bit)&1:
            out+=total_block(left(v),bit)
            v=right(v)
        else:
            v=left(v)
    return out

# Independent direct integer Stern recurrence for the first 16384 terms.
limit=16384
stern=[0]*(limit+1)
stern[1]=1
for i in range(2,limit+1):
    if i%2==0: stern[i]=stern[i//2]
    else: stern[i]=stern[i//2]+stern[i//2+1]
running=0
for i in range(limit):
    running+=weight(stern[i]%5)
    assert prefix(i+1)==running,(i,running,prefix(i+1))
assert prefix(2190711)==-5
assert prefix(2190712)==-6
assert prefix(8693111)==11
assert prefix(8693112)==12

# If a certificate file is adjacent to the script, compare its claimed
# exact 24-state rows with the freshly computed transition table.
certificate=Path(__file__).with_name('CERTIFICATE.csv')
if certificate.exists():
    with certificate.open(newline='',encoding='utf-8') as fh:
        data=list(csv.DictReader(fh))
    assert len(data)==len(STATES)
    seen=set()
    for record in data:
        v=(int(record['a']),int(record['b']))
        assert v in STATES and v not in seen
        seen.add(v)
        for depth in (16,28):
            got=tuple(int(record[f'{x}{depth}']) for x in ('sum','max','min'))
            assert got==rows[depth][v],(v,depth,got)
print('VERIFY_OK: 24-state depth-16/28 certificate, twelve bases, 16384 direct Stern prefixes, and two distant witnesses')
