"""Reproduce exact finite-alphabet cyclic sliding-sum one-erasure counts.

Only the elementary channel definition is used in the exhaustive test.
Usage: python verify_erased_weight_reads.py
"""
from itertools import product
from math import gcd


def read_vector(word, width):
    n = len(word)
    s = sum(word[:width])
    out = [s]
    for i in range(1,n):
        s += word[(i+width-1)%n] - word[i-1]
        out.append(s)
    return tuple(out)


def predicted(q, n, width):
    g = gcd(n, width)
    if g != 1:
        return None
    r = pow(n, -1, width)
    m = (n * r - 1) // width
    assert 1 <= r < width and 1 <= m < n
    edge_count = max(q-r, 0)**(n-m)*max(q-(width-r), 0)**m
    max_list = 1 + (q - 1) // max(r, width-r)
    return q**n - edge_count, max_list, edge_count


def exact_census(q, n, width):
    full, erased = {}, {}
    for w in product(range(q), repeat=n):
        v = read_vector(w, width)
        full[v] = full.get(v, 0) + 1
        t = v[1:]
        erased[t] = erased.get(t, 0) + 1
    return full, erased


def check_kernel(n, width):
    if gcd(n, width) != 1: return
    r = pow(n, -1, width)
    m = (n*r-1)//width
    negative = {(j*width)%n for j in range(1,m+1)}
    v = [r-width if j in negative else r for j in range(n)]
    sums = read_vector(v, width)
    assert sums == (width,) + (0,)*(n-1), (n,width,v,sums)
    assert sum(v) == 1 and gcd(r, width) == 1
    assert v.count(r-width) == m and v.count(r) == n-m


def verify():
    total_words = 0
    cases = 0
    for n in range(3, 251):
        for width in range(2,n):
            check_kernel(n,width)
    print('Integer one-hole kernel checked in all coprime cases for 3 <= n <= 250')
    for q, nmax in ((2, 15),(3, 10),(4, 8),(5, 7)):
        for n in range(3, nmax+1):
            for width in range(2, n):
                full, erased = exact_census(q,n,width)
                p = predicted(q,n,width)
                if p is None:
                    # Check exact preservation of the entire fiber partition.
                    assert len(full) == len(erased), (q,n,width,'redundancy')
                    assert sorted(full.values()) == sorted(erased.values()),(q,n,width,'fibers')
                else:
                    got = len(erased), max(erased.values())
                    assert got == p[:2], (q,n,width,got,p)
                    edges = q**n - len(erased)
                    assert edges == p[2]
                total_words += q**n
                cases += 1
        print(f'q={q} exhaustive up to length {nmax}: PASS')
    print(f'PASS: {cases} exact parameter cases, {total_words} source instances')


if __name__ == '__main__':
    verify()
