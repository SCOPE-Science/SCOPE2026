"""Exact reproducibility checks for Rule 110 one-step spatial image."""
from itertools import product
from collections import deque
from fractions import Fraction

RULE = 110
LABELS = (0, 1)
EDGES = {k: [] for k in LABELS}
for a, b, c in product(LABELS, repeat=3):
    lab = (RULE >> (4 * a + 2 * b + c)) & 1
    EDGES[lab].append((2 * a + b, 2 * b + c))

def next_set(s, symbol):
    return frozenset(v for u, v in EDGES[symbol] if u in s)

start = frozenset(range(4))
queue = deque([start]); reachable = {start}
while queue:
    s = queue.popleft()
    for symbol in LABELS:
        t = next_set(s, symbol)
        if t not in reachable:
            reachable.add(t); queue.append(t)
assert len(reachable) == 8

A = frozenset([frozenset(range(4)), frozenset([1,2,3])])
B = frozenset([frozenset([0,3]), frozenset([2,3])])
C = frozenset([frozenset([1,2])])
D = frozenset([frozenset([0])])
E = frozenset([frozenset([1])])
classes = [A,B,C,D,E]
assert set().union(*(set(cl) for cl in classes)) == reachable - {frozenset()}
transition = [[1,0],[1,2],[3,0],[3,4],[-1,1]]
for i, cl in enumerate(classes):
    for sym in LABELS:
        target = -1 if next_set(next(iter(cl)), sym) == frozenset() else next(j for j, pair in enumerate(classes) if next_set(next(iter(cl)), sym) in pair)
        assert target == transition[i][sym]
        assert all((-1 if next_set(s,sym) == frozenset() else next(j for j,pair in enumerate(classes) if next_set(s,sym) in pair))==target for s in cl)

def accepted(w):
    q=0
    for ch in w:
        q=transition[q][int(ch)] if q>=0 else -1
    return q>=0

def direct_words(n):
    output=set()
    for tup in product(LABELS, repeat=n+2):
        w=''.join(str((RULE >> (4*tup[i]+2*tup[i+1]+tup[i+2])) & 1) for i in range(n))
        output.add(w)
    return output

v=[1]*5
counts=[1]
for n in range(1,21):
    v=[sum(v[q] for q in transition[i] if q>=0) for i in range(5)]
    counts.append(v[0])
assert counts[:13] == [1,2,4,8,16,31,59,112,213,405,769,1459,2768]
for n in range(0,11):
    actual=direct_words(n)
    assert len(actual)==counts[n]
    assert all(accepted(w) for w in actual)
    assert all((w in actual)==accepted(w) for w in map(''.join, product('01', repeat=n)))
# Characteristic polynomial Q(z)=1-3z+3z^2-2z^3+z^5.
# The rational function is P(z)/Q(z), P(z)=1-z+z^2.
Q=[1,-3,3,-2,0,1]; P=[1,-1,1]
for n in range(0,21):
    lhs=sum(Q[k]*counts[n-k] for k in range(min(5,n)+1))
    assert lhs==(P[n] if n<len(P) else 0)
for m in range(1,150):
    w='01'+'0'*m+'10'
    assert not accepted(w)
    assert accepted(w[:-1]) and accepted(w[1:])
# Show states inequivalent by a short distinguishing suffix, including the dead state.
for i in range(-1,5):
    for j in range(i+1,5):
        witness_found=False
        for k in range(0,9):
            for suffix in product('01',repeat=k):
                def accepts_from(q):
                    for ch in suffix:
                        q=transition[q][int(ch)] if q>=0 else -1
                    return q>=0
                if accepts_from(i) != accepts_from(j):
                    witness_found=True; break
            if witness_found:break
        assert witness_found, (i,j)
print('VERIFY_OK: 8 exact subset states, 5 inequivalent live classes, 11 exhaustive word-length checks, 21 recurrence terms, 149 minimal forbidden witnesses')
