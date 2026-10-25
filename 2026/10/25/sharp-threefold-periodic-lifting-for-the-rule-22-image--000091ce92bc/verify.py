#!/usr/bin/env python3
"""Complete exact Boolean-semigroup certificate for periodic lifting in ECA 22.

Python 3 standard library only. The breadth-first search halts at its exact
closure under both generators. No length cutoff or numerical extrapolation.
"""
from collections import deque
from itertools import product

RULE = 22
IDENTITY = tuple(1 << i for i in range(4))

def compose(a, b):
    """Boolean composition of binary relations, encoded by four bit rows."""
    return tuple(union(row, b) for row in a)

def union(row, b):
    value = 0
    for j in range(4):
        if row & (1 << j): value |= b[j]
    return value

def labeled_edges(symbol):
    rows = [0]*4
    for x,y,z in product((0,1), repeat=3):
        if (RULE >> (4*x+2*y+z)) & 1 == symbol:
            rows[2*x+y] |= 1 << (2*y+z)
    return tuple(rows)
G = (labeled_edges(0), labeled_edges(1))
assert G == ((1,8,2,12),(2,4,1,0))

def trace(a):
    return any(row & (1 << i) for i, row in enumerate(a))

def least_return_multiplier(a):
    prod = a
    for multiplier in range(1,5):
        if trace(prod):return multiplier
        prod=compose(prod,a)
    return 0

def word_relation(word):
    a=IDENTITY
    for ch in word:
        a=compose(a,G[int(ch)])
    return a

# Exact closure of every Boolean relation represented by a finite word.
q=deque([IDENTITY]);word_for={IDENTITY:''};T={}
while q:
    a=q.popleft()
    children=(compose(a,G[0]),compose(a,G[1]))
    T[a]=children
    for letter,b in enumerate(children):
        if b not in word_for:
            word_for[b]=word_for[a]+str(letter)
            q.append(b)
assert len(T)==2375
assert all(all(b in T for b in T[a]) for a in T)
assert all(compose(a,G[b])==T[a][b] for a in T for b in (0,1))

# Exactly two relations have no period-one or period-two cycle but a
# period-three cycle; no relation first acquires a cycle at period four.
types={a:least_return_multiplier(a) for a in T}
three={a for a in T if types[a]==3}
assert len(three)==2
assert three == {G[1], compose(G[1],G[1])}
assert all(t != 4 for t in types.values())

# Exhaustive prefix automaton remembers whether a zero has occurred.
# This proves no mixed binary word can land in the exceptional relations.
start=(IDENTITY,False)
q=deque([start]);seen={start}
while q:
    a,has_zero=q.popleft()
    if has_zero:assert types[a] != 3
    for b in (0,1):
        new=(T[a][b],has_zero or b==0)
        if new not in seen:seen.add(new);q.append(new)
assert len(seen)==2375
assert all(not flag or types[a] != 3 for a,flag in seen)

# All-one words are exceptional precisely when their length is not
# divisible by three, since the 1-edge relation is a directed 3-cycle.
for n in range(1,100):
    k=least_return_multiplier(word_relation('1'*n))
    assert k==(1 if n%3==0 else 3)

# Independent brute-force periodic images agree for all words on rings
# through length 10, including words requiring multiplier 2 or 3.
for n in range(1,11):
    possible=set()
    for inp in product('01',repeat=n):
        w=''.join(str((RULE >> (4*int(inp[(i-1)%n])+2*int(inp[i])+int(inp[(i+1)%n])))&1) for i in range(n))
        possible.add(w)
    for bits in product('01',repeat=n):
        w=''.join(bits)
        assert (w in possible)==(least_return_multiplier(word_relation(w))==1)

assert least_return_multiplier(word_relation('001'))==2
assert least_return_multiplier(word_relation('1'))==3
assert least_return_multiplier(word_relation('0'))==1
print('VERIFY_OK: 2375 relations exhaustively closed; exactly two triple-only states; no quadruple-only state; no mixed-word triple case; 2046 exact ring tests')
