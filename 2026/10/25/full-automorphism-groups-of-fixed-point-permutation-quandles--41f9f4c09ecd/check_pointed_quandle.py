"""Finite checks for pointed-permutation quandles and their automorphisms.

Permutations are functions on 0,...,n-1, represented by their value tuples.
Composition compose(a,b) means a after b.
"""
from itertools import permutations, combinations
from collections import Counter
from math import factorial


def compose(a, b):
    return tuple(a[b[i]] for i in range(len(a)))


def inverse(p):
    out = [None] * len(p)
    for i, j in enumerate(p):
        out[j] = i
    return tuple(out)


def cycle_type(p):
    seen = set()
    lengths = []
    for i in range(len(p)):
        if i not in seen:
            j, count = i, 0
            while j not in seen:
                seen.add(j)
                count += 1
                j = p[j]
            lengths.append(count)
    return tuple(sorted(lengths))


def build(n):
    perms = list(permutations(range(n)))
    P = [(i, p) for p in perms for i in range(n) if p[i] == i]
    ix = {v:k for k,v in enumerate(P)}
    assert len(P)==factorial(n)
    inv = {p:inverse(p) for p in perms}
    table = [[None] * len(P) for _ in P]
    for k, (i,p) in enumerate(P):
        for l, (j,q) in enumerate(P):
            c = compose(compose(q,p),inv[q])
            table[k][l] = ix[(q[i],c)]
    return perms,P,ix,table


def morphism(n, P, ix, f, switched_types):
    fi = inverse(f)
    mapping = []
    for i,p in P:
        if cycle_type(p) in switched_types:
            fixed=[j for j in range(n) if p[j]==j]
            assert len(fixed)==2
            i = fixed[0] if i == fixed[1] else fixed[1]
        c = compose(compose(f,p),fi)
        mapping.append(ix[(f[i],c)])
    return tuple(mapping)


def verify_homomorphism(mapping, table):
    assert len(set(mapping)) == len(mapping)
    for i,row in enumerate(table):
        for j,val in enumerate(row):
            assert mapping[val]==table[mapping[i]][mapping[j]]


def run(n):
    perms,P,ix,table = build(n)
    fixed_two = {cycle_type(p) for p in perms if sum(p[i] == i for i in range(n)) == 2}
    print('n',n,'size',len(P),'two-fixed types',sorted(fixed_two))
    if n<=4:
        # Direct quandle axioms: idempotence, bijectivity, right self-distributivity.
        for i in range(len(P)):
            assert table[i][i] == i
        for j in range(len(P)):
            assert len({table[i][j] for i in range(len(P))})==len(P)
        for i in range(len(P)):
            for j in range(len(P)):
                for k in range(len(P)):
                    assert table[table[i][j]][k]==table[table[i][k]][table[j][k]]
    total=0
    examples=set()
    # The entire predicted group is checked for sizes up to 5.
    for f in perms:
        for mask in range(1<<len(fixed_two)):
            switched={x for t,x in enumerate(sorted(fixed_two)) if (mask >> t)&1}
            mapping=morphism(n,P,ix,f,switched)
            assert mapping not in examples
            examples.add(mapping)
            if n<=5:
                verify_homomorphism(mapping,table)
            total+=1
    assert total == factorial(n)*2**len(fixed_two)
    print('candidate automorphisms checked',total)
    if n==3:
        # Independent exhaustive search of every permutation of the six elements.
        exhaustive=0
        for candidate in permutations(range(len(P))):
            try:
                verify_homomorphism(candidate,table)
                exhaustive+=1
            except AssertionError:
                pass
        assert exhaustive==total==6
        print('exhaustive full Aut count',exhaustive)
    return total

if __name__=='__main__':
    assert [run(n) for n in (3,4,5)] == [6,48,240]
    print('VERIFY_OK')
