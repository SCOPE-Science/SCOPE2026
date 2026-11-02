#!/usr/bin/env python3
"""Independent finite checks of ternary ordered-bigram profile enumeration.

Run: python3 verify_ternary_profiles.py
No third-party packages are required.
"""
from itertools import product
from math import comb

# Coefficients of Q(x)F(x)=N(x), where F(x) counts nonempty
# ternary ordered-bigram multispectra by their total number of bigrams.
# This derives a coefficient table from the closed rational expression.
P = [9, -12, 5, 19, -4, -10, -14, 14, 6, -9, 3]

def multiply(a, b):
    out = [0]*(len(a)+len(b)-1)
    for i, ai in enumerate(a):
        for j, bj in enumerate(b):
            out[i+j] += ai*bj
    return out

def power(a, n):
    out = [1]
    for _ in range(n):
        out = multiply(out, a)
    return out

Q = multiply(multiply(power([1,-1],7),power([1,1],2)),[1,1,1])
N = [0] + P

def predicted(m_max):
    c = [0]*(m_max+1)
    for m in range(m_max+1):
        c[m] = (N[m] if m<len(N) else 0)-sum(Q[j]*c[m-j] for j in range(1, min(len(Q),m+1)))
    return c

def signature(word):
    out = [0]*9
    for a,b in zip(word, word[1:]):
        out[3*a+b] += 1
    return tuple(out)

def compositions(total, cells):
    if cells==1:
        yield (total,)
        return
    for x in range(total+1):
        for suffix in compositions(total-x, cells-1):
            yield (x,)+suffix

def eulerian_matrix(matrix):
    # Direct multigraph realization criterion. Isolated vertices are ignored.
    out = [sum(matrix[3*i:3*i+3]) for i in range(3)]
    inc = [sum(matrix[3*j+i] for j in range(3)) for i in range(3)]
    active = [i for i in range(3) if out[i]+inc[i]>0]
    if not active:
        return False
    imbalance = sorted(out[i]-inc[i] for i in range(3))
    if imbalance not in ([0,0,0],[-1,0,1]):
        return False
    reached = {active[0]}
    frontier = [active[0]]
    while frontier:
        v=frontier.pop()
        for u in active:
            if u not in reached and (matrix[3*v+u] or matrix[3*u+v]):
                reached.add(u)
                frontier.append(u)
    return len(reached)==len(active)

def main():
    expected=predicted(20)
    words_tested = 0
    profiles_tested = 0
    for m in range(1,11):
        words = set()
        for w in product(range(3),repeat=m+1):
            words.add(signature(w))
            words_tested += 1
        assert len(words)==expected[m], (m,len(words),expected[m])
        legal=set()
        for matrix in compositions(m,9):
            if eulerian_matrix(matrix):
                legal.add(matrix)
        assert legal == words, (m,len(legal),len(words),len(legal^words))
        profiles_tested += len(words)
    assert expected[1:12] == [9,24,65,156,342,683,1272,2226,3708,5919,9120]
    # Distinct one-letter hosts all produce the same empty ordered-bigram profile.
    assert len({signature((i,)) for i in range(3)}) == 1
    print('VERIFY_OK word_lengths=2..11 literal_words='+str(words_tested)+
          ' sum_distinct_profiles='+str(profiles_tested)+
          ' matrix_degrees=1..10 rational_coefficients=1..20 Euler_criterion_vs_literal=TRUE')

if __name__=='__main__':
    main()
