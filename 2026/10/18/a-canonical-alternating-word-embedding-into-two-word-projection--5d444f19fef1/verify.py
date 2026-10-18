"""Finite reproducibility checks for canonical two-word projection encodings.

The mathematical inclusion for arbitrary lengths is established by a direct proof;
these finite checks are diagnostic, not an infinite verification.
"""
from collections import Counter
from itertools import combinations, permutations


def multiset_words(n, k):
    counts = [k] * n
    acc = []
    def rec():
        if len(acc) == n * k:
            yield tuple(acc)
            return
        for i in range(n):
            if counts[i]:
                counts[i] -= 1
                acc.append(i)
                yield from rec()
                acc.pop()
                counts[i] += 1
    yield from rec()


def pair_projection(word, a, b):
    return tuple(t for t in word if t == a or t == b)


def alternates(seq):
    return all(seq[i] != seq[i+1] for i in range(len(seq)-1))


def canonical(word):
    return tuple(dict.fromkeys(word)) * (len(word) // len(set(word)))


def check_word(word):
    pair = canonical(word)
    for a, b in combinations(sorted(set(word)), 2):
        u = pair_projection(word, a, b)
        v = pair_projection(pair, a, b)
        assert (u == v) == alternates(u), (word, a, b, u, v)


checks = 0
for n, k in ((2,1),(2,2),(2,3),(3,1),(3,2),(3,3),(4,1),(4,2)):
    num = 0
    for word in multiset_words(n,k):
        check_word(word)
        num += 1
    checks += num
    print(f'exhaustive n={n} k={k}: {num} uniform words verified')

# Verify sample within the much larger four-letter triple-occurrence space.
import random
rng = random.Random(20260526)
for trial in range(2000):
    word = list(range(4))*3
    rng.shuffle(word)
    check_word(word)
print('sample n=4 k=3: 2000 seeded permutations verified')

# Find a concrete 2-uniform representation of the induced 5-cycle.
C5 = {frozenset((i,(i+1)%5)) for i in range(5)}
witness = None
tried = 0
for word in multiset_words(5,2):
    tried += 1
    graph = {frozenset((a,b)) for a,b in combinations(range(5),2)
             if alternates(pair_projection(word,a,b))}
    if graph == C5:
        witness = word
        break
assert witness is not None
check_word(witness)
print('C5 witness classical word:', ''.join(str(c) for c in witness))
print('C5 second canonical word:', ''.join(str(c) for c in canonical(witness)))
print('C5 witness search candidates:', tried)
print('total exhaustive uniform words:', checks)
print('ALL CHECKS PASS')
