"""Reproducible finite checks for dyadic prefixes of the powers-of-two characteristic word.
This program proves no infinite statement: the all-order upper bound uses a published
word-attractor theorem and the all-order lower bound uses the direct interval proof.
"""
from __future__ import annotations


def word(m: int) -> bytes:
    n = 1 << m
    return bytes(49 if i & (i-1) == 0 else 48 for i in range(1, n+1))


def witness(m: int) -> list[int]:
    if m % 2 == 0:
        k = m // 2
        return [2*4**j for j in range(k)] + [3*4**(k-1)]
    k = (m-1)//2
    return [4**j for j in range(k+1)] + [6*4**(k-1)]


def forced_intervals(m: int) -> list[tuple[int, int, bytes]]:
    w = word(m)
    blocks = [(1,2,b'11')]
    for j in range(2, m-1, 2):
        blocks.append((1<<j,1<<(j+1),b'1'+b'0'*((1<<j)-1)+b'1'))
    if m % 2:
        l = (1<<(m-1))-(1<<(m-3))
        r = (1<<(m-1))+1
        blocks.append((l,r,b'0'*(1<<(m-3))+b'10'))
    l = (1<<m)-(1<<(m-2))
    blocks.append((l, 1<<m, b'0'*(1<<(m-2))+b'1'))
    for l,r,pattern in blocks:
        assert w[l-1:r] == pattern, (m,l,r,'pattern mismatch')
        assert w.count(pattern)==1, (m,l,r,'not unique')
    assert all(a[1]<b[0] for a,b in zip(blocks,blocks[1:])), (m,'overlap',[(l,r)for l,r,_ in blocks])
    assert len(blocks)==(m+1)//2+1, (m,'wrong forced count')
    return blocks


def all_factors_covered(m: int) -> tuple[int,int]:
    w=word(m)
    s=[p-1 for p in witness(m)]
    # Store unique factors and mark them covered by any occurrence crossing S.
    facs: dict[bytes, bool] = {}
    count=0
    for start in range(len(w)):
        mark=False
        for end in range(start+1,len(w)+1):
            if end-1 in s: mark=True
            fac=w[start:end]
            if fac not in facs:
                facs[fac]=mark
            elif mark:
                facs[fac]=True
            count+=1
    assert all(facs.values()),(m,'attractor misses',next(f.hex() for f,v in facs.items() if not v))
    return len(facs),count


def main() -> None:
    for m in range(2,15):
        blocks=forced_intervals(m)
        s=witness(m)
        assert len(s)==len(blocks)
        assert len(set(s))==len(s) and all(1<=p<=1<<m for p in s)
        check = all_factors_covered(m) if m<=9 else None
        if check is not None:
            distinct,occurrences=check
            print(f'm={m} length={1<<m} optimum={len(blocks)} forced={len(blocks)} witness={s} distinct_factors={distinct} occurrences={occurrences} coverage=PASS')
        else:
            print(f'm={m} length={1<<m} forced={len(blocks)} witness_size={len(s)} lower_certificate=PASS coverage=not_exhaustively_checked')
    print('FINITE_CHECKS_PASS')

if __name__=='__main__': main()
