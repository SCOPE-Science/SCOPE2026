#!/usr/bin/env python3
"""Exact finite tests for randomly generated finite S5 modal algebras."""
from itertools import product
from math import comb, factorial


def partitions(n):
    if n == 0:
        yield ()
        return
    def rec(i, blocks):
        if i == n:
            yield tuple(tuple(b) for b in blocks)
            return
        for j in range(len(blocks)):
            blocks[j].append(i)
            yield from rec(i+1, blocks)
            blocks[j].pop()
        blocks.append([i])
        yield from rec(i+1, blocks)
        blocks.pop()
    yield from rec(0, [])


def direct_good(blks, colors):
    signatures = []
    for b in blks:
        s = frozenset(colors[i] for i in b)
        if len(s) != len(b):
            return False
        signatures.append(s)
    return len(set(signatures)) == len(signatures)


def exact_coefficient(n,q):
    coefficients=[1]+[0]*n
    for s in range(1,min(n,q)+1):
        for _ in range(comb(q,s)):
            for j in range(n,s-1,-1):
                coefficients[j]+=coefficients[j-s]
    return factorial(n)*coefficients[n]


def test():
    checks=0
    for n in range(1,6):
        bs=list(partitions(n))
        for q in range(2,5):
            br=0
            for blks in bs:
                for colors in product(range(q),repeat=n):
                    direct=direct_good(blks,colors)
                    br+=direct
                    if n<=4 or (n==5 and q==2):
                        # Definable color atoms generate the same Boolean algebra as binary predicate bits.
                        seed={0,(1<<n)-1}
                        for c in range(q):
                            seed.add(sum(1<<i for i in range(n) if colors[i]==c))
                        cur=seed
                        full=(1<<n)-1
                        while True:
                            nxt=set(cur)
                            for a in cur:
                                nxt.add(full^a)
                                for b in cur:
                                    nxt.add(a&b)
                                out=0
                                for block in blks:
                                    mask=sum(1<<i for i in block)
                                    if a&mask==mask:out|=mask
                                nxt.add(out)
                            if len(nxt)==len(cur):break
                            cur=nxt
                        assert (len(cur)==1<<n)==direct,(n,q,blks,colors)
                        checks+=1
            rhs=exact_coefficient(n,q)
            assert br==rhs,(n,q,br,rhs)
            print('exact',n,q,br,'/',len(bs)*q**n)
            checks+=1
    print('S5_RANDOM_GENERATION_EXACT_OK',checks)

if __name__=='__main__':test()
