"""Self-contained small-field checks for commuting algebra retractions.
Run with Python 3.11+; no third-party dependencies.
"""
from collections import Counter
from itertools import product
from math import prod


def gl(n, q):
    return prod(q**n - q**i for i in range(n))


def expected(n, k, q, all_products=False):
    tags = tuple(range(1 << k))
    counts = Counter()

    def assignments(remaining, t):
        if t == len(tags)-1:
            yield (remaining,)
        else:
            for x in range(remaining+1):
                for tail in assignments(remaining-x,t+1):
                    yield (x,)+tail

    for ns in assignments(n, 0):
        m = [sum(ns[a]*ns[b] for a in tags for b in tags if (a & b)==v)
             for v in tags]
        stabilizer_dim = sum(ns[v]*m[v] for v in tags)
        orbit = gl(n, q)//prod(gl(s,q) for s in ns)
        # The quotient GL_n/prod(GL_{ns}) is an integer.
        coefficient = orbit*q**(n**3-stabilizer_dim)
        ranks = tuple((sum(ns[v] for v in tags if v & (1<<j))) for j in range(k))
        ranks = tuple(s+s*s for s in ranks)
        if all_products:
            assert k == 2
            intersect = ns[3]
            ranks = ranks + (intersect + intersect*intersect,)
        counts[ranks] += coefficient
    return counts


def column_action(columns, x):
    y=0
    for j,c in enumerate(columns):
        if x & (1<<j):
            y ^= c
    return y


def composition(a,b):
    return tuple(column_action(a,x) for x in b)


def rank_binary(columns):
    pivots={}
    for x in columns:
        while x:
            i=x.bit_length()-1
            if i not in pivots:
                pivots[i]=x
                break
            x ^= pivots[i]
    return len(pivots)


def binary_endomorphisms(n):
    assert n in (1,2)
    full = n+n*n
    for a in product(range(1<<n), repeat=n):
        tensor_cols=[]
        for i in range(n):
            for j in range(n):
                out=0
                for u in range(n):
                    if a[i] & (1<<u):
                        for v in range(n):
                            if a[j] & (1<<v):
                                out ^= 1<<(n+u*n+v)
                tensor_cols.append(out)
        for f in product(range(1<<(n*n)), repeat=n):
            columns = tuple(a[i] | (f[i]<<n) for i in range(n))+tuple(tensor_cols)
            assert len(columns)==full
            yield columns


def brute_pair(n, all_products=False):
    idempotents=[]
    for F in binary_endomorphisms(n):
        if composition(F,F)==F:
            idempotents.append((F,rank_binary(F)))
    tally=Counter()
    for F,rf in idempotents:
        for G,rg in idempotents:
            comp = composition(F,G)
            if comp==composition(G,F):
                key = (rf,rg,rank_binary(comp)) if all_products else (rf,rg)
                tally[key] += 1
    return len(idempotents), tally


def main():
    for n in (1,2):
        idem,tally = brute_pair(n)
        e=expected(n,2,2)
        assert tally==e, (n,tally,e)
        full=brute_pair(n, all_products=True)[1]
        assert full==expected(n,2,2,all_products=True), (n,full)
        assert idem == sum(expected(n,1,2).values())
        if n == 2:
            assert full[(2,2,0)]==384 and full[(2,2,2)]==96
    # In each characteristic-independent field, the dimensions of the
    # simultaneous eigenspaces specify nonnegative exponents.
    for n in range(1,5):
        for k in (1,2,3):
            for q in (2,3,4):
                result=expected(n,k,q)
                assert all(v>0 for v in result.values())
                assert sum(result.values())>=1
    print('VERIFY_OK',brute_pair(2)[0],sum(expected(2,2,2).values()))

if __name__=='__main__':
    main()
