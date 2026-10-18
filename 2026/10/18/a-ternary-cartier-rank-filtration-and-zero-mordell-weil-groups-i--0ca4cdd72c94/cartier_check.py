#!/usr/bin/env python3
"""Exact verification for the characteristic-three hyperelliptic Cartier rank formula.

No third-party modules are required. The theorem for all exponents follows from
the digit-shift proof, not from this finite sample.
"""

def expected(s, k):
    if k <= s:
        return (2 ** k) * (3 ** (s-k))
    if k <= 2 * s:
        return 2 ** (2*s-k)
    return 0

def coefficient_map(s):
    q = 3 ** s
    deg = 2*q+2
    rows = {}
    cols = set()
    for i in range(1,q+1):
        nonzeros = []
        for j in range(1,q+1):
            exp = 3*i-j
            if exp == deg:
                nonzeros.append((j,1))
            if exp == 1:
                nonzeros.append((j,2))
        assert len(nonzeros) <= 1
        if nonzeros:
            j,scalar = nonzeros[0]
            assert j not in cols
            cols.add(j)
            rows[i] = j
        else:
            rows[i] = 0
    return rows

def verify_one(s):
    q=3**s
    rows=coefficient_map(s)
    # Successive nonzero entries of the powers of the matrix; because rows
    # and columns are unique, their number equals the matrix rank.
    power={i:i for i in range(1,q+1)}
    for k in range(2*s+3):
        rank=sum(v!=0 for v in power.values())
        assert rank == expected(s,k), (s,k,rank,expected(s,k))
        if k == 2*s:
            assert rank == 1
        power={i:(rows[v] if v else 0) for i,v in power.items()}
    # digit-model comparison on every index
    for i in range(1,q+1):
        word=[]
        t=i-1
        for j in range(s):
            word.append((t//(3**(s-1-j)))%3)
        if word[0] == 0:
            dest=word[1:]+[1]
        elif word[0] == 2:
            dest=word[1:]+[0]
        else:
            dest=None
        if dest is None:
            assert rows[i]==0
        else:
            target=1+sum(digit*(3**(s-1-j)) for j,digit in enumerate(dest))
            assert target==rows[i], (s,i,target,rows[i])
    return [expected(s,k) for k in range(2*s+2)]

if __name__=='__main__':
    for s in range(1,7):
        seq=verify_one(s)
        print(f's={s} genus={3**s} ranks={seq}')
    print('VERIFY_OK digit_shift_and_exact_rank_profiles s=1..6')
