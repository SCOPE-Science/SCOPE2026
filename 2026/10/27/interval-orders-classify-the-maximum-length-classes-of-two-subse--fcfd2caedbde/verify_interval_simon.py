"""Standalone reproducibility checker for maximum-length Simon-2 classes.
Python standard library only. Independent BFS and doubled-endpoint enumeration.
"""
from collections import Counter


def transition(state, letter, q):
    one = state & ((1 << q) - 1)
    pair = state >> q
    for a in range(q):
        if (one >> a) & 1:
            pair |= 1 << (q * a + letter)
    return (one | (1 << letter)) | (pair << q)


def bfs(q):
    depth = {0: 0}
    queue = [0]
    for state in queue:
        for a in range(q):
            nxt = transition(state, a, q)
            if nxt not in depth:
                depth[nxt] = depth[state] + 1
                queue.append(nxt)
    return depth


def pair_signature(word, q):
    s = 0
    for i, a in enumerate(word):
        s |= (1 << a)
        for b in word[i+1:]:
            s |= 1 << (q + q*a + b)
    return s


def interval_relation(word, q):
    left = [len(word)]*q
    right = [-1]*q
    for i,a in enumerate(word):
        left[a] = min(left[a],i)
        right[a] = i
    rel = 0
    for a in range(q):
        for b in range(q):
            if a!=b and right[a]<left[b]:
                rel |= (1 << (q*a+b))
    return rel


def all_doubled(q):
    remaining = [2]*q
    w = []
    def go():
        if len(w)==2*q:
            yield tuple(w)
            return
        for a in range(q):
            if remaining[a]:
                remaining[a]-=1; w.append(a)
                yield from go()
                w.pop(); remaining[a]+=1
    yield from go()


def verify(q):
    minima = bfs(q)
    assert max(minima.values()) == 2*q
    top = {state for state, dist in minima.items() if dist==2*q}
    mask = sum(1 << (q+q*a+a) for a in range(q))
    # Depth 2q is equivalent to having at least two of every letter.
    assert all(((state & mask)==mask)==(state in top) for state in minima)
    relation_to_deck = {}
    deck_to_relation = {}
    evaluated = 0
    for w in all_doubled(q):
        evaluated += 1
        sig = pair_signature(w,q)
        rel = interval_relation(w,q)
        if rel in relation_to_deck:
            assert relation_to_deck[rel] == sig
        else:
            relation_to_deck[rel] = sig
        if sig in deck_to_relation:
            assert deck_to_relation[sig] == rel
        else:
            deck_to_relation[sig] = rel
    assert set(relation_to_deck.values()) == top
    assert len(relation_to_deck) == len(deck_to_relation) == len(top)
    known_index=[0,3,16,152,2326,52132]
    known_top=[0,1,3,19,207,3451]
    assert len(minima)==known_index[q]
    assert len(top)==known_top[q]
    return len(minima),len(top),evaluated

if __name__=='__main__':
    for q in range(1,6):
        i,t,e=verify(q)
        print(f'q={q} all_classes={i} deepest_classes={t} doubled_words={e}')
    print('INTERVAL_SIMON2_PASS')
