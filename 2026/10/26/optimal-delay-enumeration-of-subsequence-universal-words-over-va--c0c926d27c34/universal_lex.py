"""Lexicographic O(n)-delay enumeration of q-ary k-subsequence universal words.
Uses the greedy-arch prefix slack and an ordered linked list of unobserved letters.
Requires no third-party packages; streaming with O(n) working memory.
"""
from itertools import product, islice

class Missing:
    __slots__ = ('q', 'prev', 'nxt', 'used', 'count')
    def __init__(self, q):
        self.q = q
        self.prev = [i-1 for i in range(q+1)]
        self.nxt = [i+1 for i in range(q+1)]
        self.prev[0] = q
        self.nxt[q] = 0
        self.nxt[0] = 1
        self.used = [False] * (q+1)
        self.count = 0
    def take(self, x):
        l, r = self.prev[x], self.nxt[x]
        self.nxt[l] = r
        self.prev[r] = l
        self.used[x] = True
        self.count += 1
        return l, r
    def restore(self, x, l, r):
        self.nxt[l] = x
        self.prev[r] = x
        self.prev[x] = l
        self.nxt[x] = r
        self.used[x] = False
        self.count -= 1

class Frame:
    __slots__ = ('pos', 'arches', 'slack', 'missing', 'cursor', 'undo')
    def __init__(self, pos, arches, slack, missing, q, k, undo=None):
        self.pos = pos
        self.arches = arches
        self.slack = slack
        self.missing = missing
        self.cursor = 1 if arches >= k or slack > 0 else missing.nxt[0]
        self.undo = undo

def universal_words(n, k, q):
    """Yield all words in lexicographic order as q-ary tuples.

    For n,k>=0, q>=1. O(n+q) initialization and worst-case O(n)
    delay between consecutive complete outputs on a unit-cost RAM,
    with O(n) working space in every nonempty instance (k>=1).
    """
    if n < 0 or k < 0 or q < 1:
        raise ValueError('Require n,k>=0 and q>=1')
    if k and n < k*q:
        return
    word = [0] * n
    first = Missing(q) if k else None
    stack = [Frame(0, 0, n-k*q, first, q, k)]
    while stack:
        f = stack[-1]
        if f.pos == n:
            yield tuple(word)
            stack.pop()
            if f.undo is not None:
                f.undo[0].restore(*f.undo[1:])
            continue
        x = f.cursor
        if (f.arches >= k or f.slack > 0):
            if x > q:
                stack.pop()
                if f.undo is not None:
                    f.undo[0].restore(*f.undo[1:])
                continue
            f.cursor = x+1
        else:
            if x == 0:
                stack.pop()
                if f.undo is not None:
                    f.undo[0].restore(*f.undo[1:])
                continue
            f.cursor = f.missing.nxt[x]
        word[f.pos] = x
        if f.arches >= k:
            child = Frame(f.pos+1, f.arches, f.slack, None, q, k)
        elif f.missing.used[x]:
            assert f.slack > 0
            child = Frame(f.pos+1, f.arches, f.slack-1, f.missing, q, k)
        else:
            left, right = f.missing.take(x)
            undo = (f.missing,x,left,right)
            if f.missing.count == q:
                arches = f.arches + 1
                missing = Missing(q) if arches < k else None
                child = Frame(f.pos+1, arches, f.slack, missing, q, k, undo)
            else:
                child = Frame(f.pos+1, f.arches, f.slack, f.missing, q, k, undo)
        stack.append(child)

def universality_index(word, q):
    seen = set()
    arches = 0
    for x in word:
        seen.add(x)
        if len(seen) == q:
            arches += 1
            seen.clear()
    return arches

def check():
    cases = emitted = 0
    for q in range(1,5):
        for n in range(8):
            for k in range(4):
                actual = list(universal_words(n,k,q))
                expected = [w for w in product(range(1,q+1),repeat=n)
                            if universality_index(w,q) >= k]
                assert actual == expected, (q,n,k,len(actual),len(expected))
                cases += 1
                emitted += len(actual)
    for q,k,n in ((21,1,21),(200,1,200),(53,2,106),(3,1,1500)):
        first = list(islice(universal_words(n,k,q),3))
        assert len(first)==3 and all(universality_index(w,q)>=k for w in first)
    print(f'UNIVERSAL_LEX_LINEAR_DELAY_PASS cases={cases} emitted_words={emitted} high_alphabet_and_long_word_tests=4')
if __name__ == '__main__':
    check()
