#!/usr/bin/env python3
"""Independent modular-free checks of the exact dyadic correlation theorem.
Finite checks supplement, and do not replace, the symbolic row identity.
"""
from collections import Counter

def sign(n):
    return -1 if n.bit_count() & 1 else 1

def direct(k, r):
    m = (1 << k) + 1
    return sum(sign(n) * sign(m*n) for n in range(1 << r))

def step(row, k):
    m = (1 << k) + 1
    nxt = Counter()
    for c, w in row.items():
        for b in (0, 1):
            nxt[(c + m*b)//2] += w * (-1 if c & 1 else 1)
    return {c:w for c,w in nxt.items() if w}

def test(k):
    rows=[{0:1}]
    for _ in range(k+2):
        rows.append(step(rows[-1],k))
    assert rows[k] == {i:1 for i in range(1 << k)}
    target=Counter(rows[k+2])
    for coeff,j in [(-1,k+1),(-1,2),(3,1),(-2,0)]:
        for c,w in rows[j].items():
            target[c] += coeff*w
    assert not any(target.values()), (k, dict(target))
    values=[sum(w*sign(c) for c,w in row.items()) for row in rows]
    assert values == [1]+[0]*(k+1)+[2],(k,values)
    extended=values[:]
    for r in range(1,24):
        extended.append(extended[r+k+1]+extended[r+2]-3*extended[r+1]+2*extended[r])
    for r in range(14):
        observed=direct(k,r)
        assert extended[r]==observed,(k,r,extended[r],observed)
    return len(rows),len(extended)

if __name__=='__main__':
    for k in range(2,10):
        lengths=test(k)
        print(f'PASS k={k} signed_rows={lengths[0]} recurrence_terms={lengths[1]} direct_prefixes=14')
    print('PASS: 8 parameter values, 112 directly enumerated dyadic prefixes, signed row identities and recurrences')
