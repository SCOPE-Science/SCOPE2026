"""Exhaustive certificate for four-world max-min transitive q-level fuzzy relations.
Standard Python 3 only. On n labelled worlds, only off-diagonal entries vary.
The enumerated masks range over ALL 2^(n(n-1)) directed graphs.
"""
from math import comb

TARGET = [1,354,8331,63730,235344,488760,604752,444192,179328,30720]

def relation_masks(n):
    edges = [(i,j) for i in range(n) for j in range(n) if i != j]
    reflexive = []
    for mask in range(1 << len(edges)):
        edge = [[i == j for j in range(n)] for i in range(n)]
        for index, (i,j) in enumerate(edges):
            if (mask >> index)&1:
                edge[i][j] = True
        if all(not(edge[i][j] and edge[j][k]) or edge[i][k]
               for i in range(n) for j in range(n) for k in range(n)):
            reflexive.append(mask)
    return edges, reflexive

def strict_chain_counts(masks, h):
    # mask 0 = diagonal-only relation. Each other mask is a distinct preorder.
    states = sorted((m for m in masks if m != 0), key=int.bit_count)
    predecessors = {m:[p for p in states if p != m and (p & m) == p]
                    for m in states}
    ways = {m:1 for m in states}  # chains of length 1 ending at m
    coefficients = [1]
    for length in range(1, h+1):
        coefficients.append(sum(ways.values()))
        ways = {m:sum(ways[p] for p in predecessors[m]) for m in states}
    assert not any(ways.values()), 'Nonzero chain beyond structural bound'
    return coefficients

def binomial_polynomial(q, coefficients):
    return sum(a*comb(q-1,k) for k,a in enumerate(coefficients)
               if q-1 >= k)

def direct_three(q):
    from itertools import product
    n=3; edges=[(i,j) for i in range(n) for j in range(n) if i!=j]
    total=0
    for vals in product(range(q),repeat=len(edges)):
        matrix = [[q-1 if i==j else 0 for j in range(n)] for i in range(n)]
        for (i,j),v in zip(edges,vals):matrix[i][j]=v
        if all(matrix[i][k]>=min(matrix[i][j],matrix[j][k])
               for i in range(n) for j in range(n) for k in range(n)):
            total += 1
    return total

def main():
    edges4, masks4 = relation_masks(4)
    assert len(edges4) == 12 and len(masks4) == 355
    coeffs4 = strict_chain_counts(masks4,9)
    assert coeffs4 == TARGET,coeffs4
    for q, expected in ((1,1),(2,355),(3,9040),(4,89786),(5,541667)):
        assert binomial_polynomial(q,coeffs4)==expected
    # An independent q=3 check: each pair of nested binary cuts is enumerated.
    assert sum(1 for A in masks4 for B in masks4 if (A&B)==B)==9040
    # Symbolic polynomial checks with exact integer arithmetic at 10 arguments;
    # both sides are polynomials of degree at most 9, so 10 points prove identity.
    for q in range(1,11):
        numerator = q*(160*q**8 + 1206*q**7 + 3156*q**6
                        +1134*q**5 -8736*q**4 +4914*q**3
                        +974*q**2 -639*q -279)
        assert numerator%1890 == 0
        assert binomial_polynomial(q,coeffs4)==numerator//1890
    _, masks3=relation_masks(3)
    assert len(masks3)==29
    coeffs3=strict_chain_counts(masks3,5)
    assert coeffs3==[1,28,135,240,180,48]
    for q in range(1,6):
        assert direct_three(q)==binomial_polynomial(q,coeffs3)
    print('FOUR_WORLD_PREORDERS',len(masks4))
    print('STRICT_CHAIN_COEFFICIENTS',coeffs4)
    print('FOUR_WORLD_Q_LEVEL_COUNTS',[binomial_polynomial(q,coeffs4) for q in range(1,6)])
    print('THREE_WORLD_BRUTE_VALIDATED',list(range(1,6)))
    print('ALL_CHECKS_OK')
if __name__=='__main__':main()
