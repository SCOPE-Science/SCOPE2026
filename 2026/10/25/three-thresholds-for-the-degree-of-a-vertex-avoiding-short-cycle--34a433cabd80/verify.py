"""Exact finite checks for a distinguished vertex free of triangles and four-cycles."""
from fractions import Fraction
from math import comb, lgamma, log, exp
from collections import defaultdict


def direct_coefficients(n):
    edges = [(i, j) for i in range(n) for j in range(i+1, n)]
    by_degrees = defaultdict(lambda: defaultdict(int))
    for mask in range(1 << len(edges)):
        adj = [0] * n
        k = mask.bit_count()
        for idx, (a, b) in enumerate(edges):
            if mask >> idx & 1:
                adj[a] |= 1 << b
                adj[b] |= 1 << a
        d = adj[0].bit_count()
        neigh = adj[0]
        valid = True
        for i in range(1, n):
            if neigh >> i & 1:
                if adj[i] & neigh:
                    valid = False
                    break
            elif (adj[i] & neigh).bit_count() >= 2:
                valid = False
                break
        if valid:
            by_degrees[d][k] += 1
    return by_degrees


def expected_coefficients(n):
    m = n - 1
    by_degrees = defaultdict(lambda: defaultdict(int))
    # Choice of the root neighborhood, edges to root, edges among neighbors,
    # and allowable choices for edges from each outside vertex to neighbors.
    # Edges among outside vertices are unrestricted.
    for d in range(m + 1):
        o = m - d
        pref = comb(m, d)
        for j in range(o + 1):
            # Of the o outsiders, j choose one of d possible neighbor links.
            # Edges among outsiders form an arbitrary graph.
            for z in range(comb(o, 2) + 1):
                if d == 0 and j:
                    continue
                mult = pref * comb(o, j) * d**j * comb(comb(o, 2), z)
                if mult:
                    by_degrees[d][d + j + z] += mult
    return by_degrees


def weight(n, d, p):
    m=n-1
    q=1-p
    b= q**d + d*p*q**(d-1) if d else Fraction(1)
    return comb(m,d)*p**d*q**(m-d+comb(d,2))*b**(m-d)


def ratio(n, d, p):
    m=n-1
    return Fraction(m-d,d+1)*p/(1+(d-1)*p)*(1 - d*p*p/(1+(d-1)*p))**(m-d-1)


def main():
    checks=0
    for n in range(2, 7):
        a=direct_coefficients(n)
        b=expected_coefficients(n)
        for d in range(n):
            for k in range(comb(n,2)+1):
                assert a[d].get(k,0)==b[d].get(k,0),(n,d,k)
                checks += 1
        for p in [Fraction(1,3),Fraction(2,5),Fraction(1,2)]:
            for d in range(n):
                numerator=sum(v*p**k*(1-p)**(comb(n,2)-k) for k,v in a[d].items())
                assert numerator == weight(n,d,p),(n,d,p)
                checks+=1
            for d in range(1,n-1):
                assert ratio(n,d,p)==weight(n,d+1,p)/weight(n,d,p),(n,d,p)
                checks+=1
    print(f'PASS {checks} exact assertions, exhaustive graph enumeration through six vertices')

if __name__=='__main__':
    main()
