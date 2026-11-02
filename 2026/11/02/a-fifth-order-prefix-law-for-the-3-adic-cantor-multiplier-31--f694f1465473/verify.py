#!/usr/bin/env python3
"""Exact finite-state certificate for 3-adic Cantor multiplier 31."""
from collections import deque
M=31
states={0};queue=deque([0]);edges={}
while queue:
    carry=queue.popleft();options=[]
    for digit in (0,1):
        total=M*digit+carry
        if total%3 in (0,1):
            following=total//3
            options.append((digit,following))
            if following not in states:
                states.add(following);queue.append(following)
    edges[carry]=options
EXPECTED={
    0:[(0,0),(1,10)],1:[(0,0)],3:[(0,1),(1,11)],
    4:[(0,1)],5:[(1,12)],10:[(0,3)],11:[(1,14)],
    12:[(0,4),(1,14)],14:[(1,15)],15:[(0,5),(1,15)],
}
assert edges==EXPECTED
assert len(states)==10
# A acts on column vectors indexed by carry states.
def act(v):
    return {c:sum(v[d] for a,d in edges[c]) for c in states}
column={c:1 for c in states};columns=[column]
for _ in range(5):
    column=act(column);columns.append(column)
assert {c:columns[5][c]-columns[4][c]-columns[1][c]-columns[0][c] for c in states}=={c:0 for c in states}
seq=[columns[n][0] for n in range(5)]
for n in range(5,40):seq.append(seq[n-1]+seq[n-4]+seq[n-5])
assert seq[:16]==[1,2,3,5,7,10,15,23,35,52,77,115,173,260,389,581]
# Independent direct 3-adic residue test to 12 places, no automaton.
for n in range(13):
    modulus=3**n
    count=0
    for bits in range(1<<n):
        x=sum(3**i for i in range(n) if (bits>>i)&1)
        y=(31*x)%modulus
        ok=True
        for _ in range(n):
            if y%3==2:ok=False;break
            y//=3
        if ok:count+=1
    assert count==seq[n],(n,count,seq[n])
print('VERIFY_OK states=10 edges=14 statewise_identity=A^5-A^4-A-I; direct_prefix_levels=0..12')
print('PREFIX_COUNTS',seq[:16])
print('DENOMINATOR 1-z-z^4-z^5; NUMERATOR 1+z+z^2+2z^3+z^4')
