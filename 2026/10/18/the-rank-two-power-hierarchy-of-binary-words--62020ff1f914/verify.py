#!/usr/bin/env python3
"""Independent finite transition-closure and direct word/game checks.

No external packages are required. Run: python3 verify.py
All printed assertions are mathematical consistency checks, not claims of external certification.
"""
from collections import Counter, deque, defaultdict
from itertools import product
import json
from pathlib import Path

ALPHABET = (0, 1)

# State = (alphabet mask, left-point-pair mask, right-point-pair mask).
# For either pair mask the bit (4*c + B) records letter c and context alphabet B.
def transition(state, c):
    alphabet, left, right = state
    new_left = left | (1 << (4*c + alphabet))
    new_right = 1 << (4*c)
    for k in range(8):
        if right & (1 << k):
            cc, suffix = divmod(k, 4)
            new_right |= 1 << (4*cc + (suffix | (1 << c)))
    return (alphabet | (1 << c), new_left, new_right)

def reconstruct_square(state):
    alphabet, left, right = state
    ans = set()
    for k in range(8):
        letter, ctx = divmod(k, 4)
        if left & (1 << k): ans.add((letter, ctx, alphabet))
        if right & (1 << k): ans.add((letter, alphabet, ctx))
    return frozenset(ans)

def reconstruct_cube(state):
    alphabet, _, _ = state
    return reconstruct_square(state) | frozenset(
        (c, alphabet, alphabet) for c in ALPHABET if alphabet & (1 << c))

def direct_type(word):
    """Compute all pointed rank-one types from literal positions of a word."""
    return frozenset((c,
        sum(1 << b for b in set(word[:i])),
        sum(1 << b for b in set(word[i+1:])))
        for i,c in enumerate(word))

def explicit_two_round_game(a,b):
    """Two-round EF game over ordered binary words, completely unrolled."""
    def atomic(i,k,j,h):
        return a[i] == b[j] and a[k] == b[h] and (i<k) == (j<h) and (i==k) == (j==h)
    # Pointed 1-round game, Spoiler can choose in either word.
    def one_round(i,j):
        return (all(any(atomic(i,k,j,h) for h in range(len(b))) for k in range(len(a)))
                and all(any(atomic(i,k,j,h) for k in range(len(a))) for h in range(len(b))))
    # First round can be in either word.
    return (all(any(one_round(i,j) for j in range(len(b))) for i in range(len(a)))
        and all(any(one_round(i,j) for i in range(len(a))) for j in range(len(b))))

def closure():
    start = (0,0,0)
    reps = {start: ''}
    queue = deque((start,))
    while queue:
        state = queue.popleft()
        for c in ALPHABET:
            nxt = transition(state,c)
            if nxt not in reps:
                reps[nxt] = reps[state] + str(c)
                queue.append(nxt)
    return reps

def main():
    reps = closure()
    assert len(reps) == 37, len(reps)
    assert Counter(s[0] for s in reps) == Counter({0:1, 1:2, 2:2, 3:32})
    # Every successor is accounted for, and the empty state was included:
    # an exact induction over word length proves that ALL words reach these states.
    assert all(transition(s,c) in reps for s in reps for c in ALPHABET)
    square = defaultdict(list)
    cube = defaultdict(list)
    for s, root in reps.items():
        if s[0] != 3: continue
        x = tuple(sorted(reconstruct_square(s)))
        y = tuple(sorted(reconstruct_cube(s)))
        square[x].append(root)
        cube[y].append(root)
        w = tuple(map(int,root))
        assert direct_type(w*2) == reconstruct_square(s), root
        assert direct_type(w*3) == reconstruct_cube(s), root
        for k in range(4,8):
            assert direct_type(w*k) == reconstruct_cube(s), (root,k)
    assert len(square) == 30 and len(cube) == 16
    square_min = {s: min(map(len,roots)) for s,roots in square.items()}
    cube_min = {s: min(map(len,roots)) for s,roots in cube.items()}
    assert Counter(square_min.values()) == Counter({2:2,3:6,4:10,5:10,6:2})
    assert Counter(cube_min.values()) == Counter({2:2,3:6,4:6,5:2})
    assert {roots[0] for typ,roots in square.items() if square_min[typ]==6} == {'001100','110011'}
    assert {roots[0] for typ,roots in cube.items() if cube_min[typ]==5} == {'00100','11011'}
    assert all(direct_type(tuple(int(c) for c in w)*2) == frozenset(t) for t,roots in square.items() for w in roots)
    # Independent direct enumeration does not use the transition state.
    for power, classes, maxroot in ((2,square,6),(3,cube,5)):
        encountered = {}
        for n in range(1,maxroot+1):
            for w in product(ALPHABET, repeat=n):
                if set(w) != set(ALPHABET): continue
                typ = tuple(sorted(direct_type(w*power)))
                encountered.setdefault(typ,n)
        assert set(encountered) == set(classes),power
        assert {s:encountered[s] for s in classes} == (square_min if power==2 else cube_min)
    # Check all representative pairs with a generic two-round game rather than using the transition relation.
    sq_words = {s:tuple(int(c) for c in min(roots,key=lambda z:(len(z),z)))*2 for s,roots in square.items()}
    cu_words = {s:tuple(int(c) for c in min(roots,key=lambda z:(len(z),z)))*3 for s,roots in cube.items()}
    for words in (sq_words,cu_words):
        representatives = list(words.values())
        for i in range(len(representatives)):
            for j in range(i+1,len(representatives)):
                assert not explicit_two_round_game(representatives[i],representatives[j]), (i,j)
    # Distinguished witness: 0101 and 010101 have different rank-two types.
    assert not explicit_two_round_game((0,1,0,1),(0,1,0,1,0,1))
    assert len(set(cube)) == 16 and len(set(square))==30
    # Full word-theory universe: 90 mixed rank-two theories (background count).
    seen = {(0,frozenset()):''}; q=deque(seen)
    while q:
        alpha,typ=q.popleft()
        for c in ALPHABET:
            nxt = (alpha | (1<<c), frozenset({(a,l,r | (1<<c)) for a,l,r in typ} | {(c,alpha,0)}))
            if nxt not in seen:
                seen[nxt]=seen[(alpha,typ)]+str(c);q.append(nxt)
    assert len(seen)==97 and sum(alpha==3 for alpha,_ in seen)==90
    assert max(len(w) for s,w in seen.items() if s[0]==3) == 8
    assert {s for s in cube}.issubset(set(square))

    # Fully auditable finite-state certificate, sorted by shortest root then lexical root.
    states = sorted(reps, key=lambda s:(len(reps[s]),reps[s]))
    idx={s:i for i,s in enumerate(states)}
    certificate = {
      'description': 'Complete prefix-closed state graph for nonempty binary-word powers at first-order quantifier rank two',
      'state_count':len(states),'mixed_root_states':32,
      'rank_two_mixed_word_types':90,
      'square_type_count':len(square),'cube_type_count':len(cube),
      'square_shortest_root_histogram':dict(sorted(Counter(square_min.values()).items())),
      'cube_shortest_root_histogram':dict(sorted(Counter(cube_min.values()).items())),
      'square_maximal_minimum_roots':['001100','110011'],
      'cube_maximal_minimum_roots':['00100','11011'],
      'states':[{ 'id':idx[s], 'shortest_root':reps[s],
                  'state':list(s), 'append_0':idx[transition(s,0)],'append_1':idx[transition(s,1)],
                  'square_type': [list(z) for z in sorted(reconstruct_square(s))] if s[0]==3 else None,
                  'cube_type': [list(z) for z in sorted(reconstruct_cube(s))] if s[0]==3 else None}
                for s in states]
    }
    path=Path(__file__).with_name('certificate.json')
    canonical=json.dumps(certificate,sort_keys=True,indent=2,ensure_ascii=False)+'\n'
    if path.exists():
        assert path.read_text(encoding='utf-8') == canonical, 'certificate changed'
    else:
        path.write_text(canonical,encoding='utf-8')
    print('VERIFY_OK states=37 mixed=32 word_types=90 square_types=30 cube_types=16')
    print('SQUARE_MIN_ROOT_HIST={2:2,3:6,4:10,5:10,6:2}')
    print('CUBE_MIN_ROOT_HIST={2:2,3:6,4:6,5:2}')
    print('POWER_STABILIZATION=3 SHARP_WITNESS=01')

if __name__=='__main__':main()
