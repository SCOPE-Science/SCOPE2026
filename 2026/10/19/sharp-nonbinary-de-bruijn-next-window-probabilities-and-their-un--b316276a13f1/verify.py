#!/usr/bin/env python3
"""Exact checks for sharp nonbinary next-window marginal extremes.
No third-party packages required. Run: python3 verify.py
"""
from collections import Counter
from fractions import Fraction
from itertools import permutations, product
from math import factorial


def formula(q, word):
    n = len(word) - 1
    assert q >= 2 and n >= 2 and all(0 <= a < q for a in word)
    if len(set(word)) == 1:
        return Fraction(0)
    m = n - 1
    a, b, c = tuple(word[:m]), tuple(word[1:m+1]), tuple(word[2:])
    def walks(x, y, k):
        return int(x[k:] == y[:m-k])
    return (1 + sum((Fraction(walks(b,a,k)-walks(b,b,k)-walks(c,a,k)+walks(c,b,k), q**(k+1)) for k in range(m)), Fraction(0))) / (q-1)


def all_cycles(q, n):
    """Independent exhaustive local-transition permutation enumeration."""
    m = n - 1
    vertices = list(product(range(q), repeat=m))
    vid = {v:i for i,v in enumerate(vertices)}
    N = len(vertices)
    next_data = []
    for v in vertices:
        for z in range(q):
            dst = v[1:] + (z,)
            next_data.append((vid[dst],v[0]))
    good = 0
    counts = Counter()
    for maps in product(permutations(range(q)), repeat=N):
        edge = 0
        seen = 0
        for _ in range(N*q):
            bit = 1 << edge
            if seen & bit:
                break
            seen |= bit
            dst, incoming = next_data[edge]
            edge = dst*q + maps[dst][incoming]
        if edge != 0 or seen.bit_count() != N*q:
            continue
        good += 1
        for b in vertices:
            v = vid[b]
            for a in range(q):
                counts[(a,) + b + (maps[v][a],)] += 1
    return good, counts


def bareiss(a):
    """Exact integer determinant using fraction-free elimination."""
    n = len(a)
    a = [row[:] for row in a]
    if not n: return 1
    sign = 1
    denom = 1
    for k in range(n-1):
        if a[k][k] == 0:
            s = next((i for i in range(k+1,n) if a[i][k]),None)
            if s is None:
                return 0
            a[k],a[s] = a[s],a[k]
            sign *= -1
        p = a[k][k]
        for i in range(k+1,n):
            for j in range(k+1,n):
                x = a[i][j]*p-a[i][k]*a[k][j]
                assert x % denom == 0
                a[i][j] = x // denom
        for i in range(k+1,n):
            a[i][k] = 0
        denom = p
    return sign * a[-1][-1]


def arborescences(q,n,word=None):
    """Independent whole-matrix Matrix-Tree computation after arc contraction."""
    m=n-1
    vv=list(product(range(q),repeat=m))
    ind={v:i for i,v in enumerate(vv)}
    N=len(vv)
    arcs=[(ind[v],ind[v[1:]+(c,)]) for v in vv for c in range(q)]
    if word is not None:
        a,b,c=(tuple(word[:m]),tuple(word[1:m+1]),tuple(word[2:]))
        assert len(set(word))>1
        # Remove one unique occurrence of each prescribed edge and insert a macro edge.
        e=(ind[a],ind[b]); f=(ind[b],ind[c]);
        assert e!=f
        arcs.remove(e)
        arcs.remove(f)
        arcs.append((ind[a],ind[c]))
    mat=[[0]*N for _ in range(N)]
    for x,y in arcs:
        mat[x][x]+=1
        mat[x][y]-=1
    return bareiss([row[1:] for row in mat[1:]])


def check():
    count_words=0
    for q,n in [(2,2),(2,3),(2,4),(2,5),(3,2),(4,2)]:
        total,counts=all_cycles(q,n)
        theory=factorial(q)**(q**(n-1))//(q**n)
        assert total==theory,(q,n,total,theory)
        for w in product(range(q),repeat=n+1):
            expected=formula(q,w)
            assert Fraction(counts[w],total)==expected,(q,n,w,counts[w],total,expected)
            count_words+=1
        print('TRANSITIONS',q,n,'cycles',total,'candidate_words',q**(n+1),'OK')
    for q,n in [(2,2),(2,3),(2,4),(2,5),(3,2),(3,3),(4,2),(4,3)]:
        tau=arborescences(q,n)
        assert tau==q**(q**(n-1)-n),(q,n,tau)
        num=0
        for w in product(range(q),repeat=n+1):
            p=formula(q,w)
            assert 0<=p<=1,(q,n,w,p)
            num+=p
            if len(set(w))>1:
                tau_after=arborescences(q,n,w)
                assert Fraction(tau_after,(q-1)*tau)==p,(q,n,w,p,tau_after,tau)
        assert num==q**n,(q,n,num)
        print('MATRIX_TREE',q,n,'rooted_arborescences',tau,'candidate_words',q**(n+1),'OK')
    # Explicit order-two class laws, including the binary obstruction.
    for q in range(2,13):
        assert formula(q,(0,0,0))==0
        assert formula(q,(0,0,1))==Fraction(1,q-1)
        assert formula(q,(1,0,0))==Fraction(1,q-1)
        assert formula(q,(0,1,0))==Fraction(q-2,q*(q-1))
        if q>=3: assert formula(q,(0,1,2))==Fraction(1,q)
    # Global extremum, equality-case, and sharpness check over finite orders.
    for q, upper_n in [(3, 8), (4, 6), (5, 5), (6, 4), (7, 3)]:
        for n in range(2, upper_n + 1):
            lowest = Fraction(q-2, q*(q-1))
            highest = Fraction(1, q-1)
            actual_min = None
            actual_max = Fraction(0)
            low_words = set()
            high_words = set()
            for w in product(range(q), repeat=n+1):
                if len(set(w)) == 1:
                    assert formula(q,w) == 0
                    continue
                p = formula(q,w)
                assert lowest <= p <= highest, (q,n,w,p)
                if actual_min is None or p < actual_min:
                    actual_min, low_words = p, {w}
                elif p == actual_min:
                    low_words.add(w)
                if p > actual_max:
                    actual_max, high_words = p, {w}
                elif p == actual_max:
                    high_words.add(w)
            forced = {((a,)*n+(b,)) for a in range(q) for b in range(q) if a != b}
            forced |= {((b,)+(a,)*n) for a in range(q) for b in range(q) if a != b}
            assert high_words == forced and actual_max == highest, (q,n)
            if n == 2:
                alt = {(a,b,a) for a in range(q) for b in range(q) if a != b}
                assert low_words == alt and actual_min == lowest, (q,n)
            else:
                assert actual_min > lowest, (q,n)
            print('SHARP_BOUND',q,n,'min',str(actual_min),'max',str(actual_max),
                  'maximizers',len(high_words),'minimizers',len(low_words),'OK')
    print('ALL EXACT CHECKS PASSED')

if __name__=='__main__':check()
