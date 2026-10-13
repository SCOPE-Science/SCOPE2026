#!/usr/bin/env python3
"""Exhaustive finite certificate for six-bit two-adjacent-deletion codebooks."""
from itertools import product

WORDS = [''.join(bits) for bits in product('01', repeat=6)]
RECEIVED = [''.join(bits) for bits in product('01', repeat=4)]
D = {x: {x[:i] + x[i+2:] for i in range(5)} for x in WORDS}
T = tuple(y for y in RECEIVED if y[1] == y[3])
assert len(T) == 8
# Every word yields a member of T: delete one of its three disjoint pairs.
for x in WORDS:
    assert any(x[:i] + x[i+2:] in T for i in (0, 2, 4))

bucket = {y: tuple(x for x in WORDS if D[x].intersection(T) == {y}) for y in T}
assert [len(bucket[y]) for y in T] == [5, 4, 5, 4, 4, 5, 4, 5]
visited = [0]*9
solutions = []
def search(depth, chosen, used):
    visited[depth] += 1
    if depth == len(T):
        solutions.append(tuple(sorted(chosen)))
        return
    for x in bucket[T[depth]]:
        if D[x].isdisjoint(used):
            search(depth+1, chosen+(x,), used | D[x])
search(0, tuple(), set())
assert visited == [1, 5, 13, 28, 17, 8, 11, 2, 2], visited
EXPECTED = [
    ('000000','001011','010101','011110','100001','101010','110100','111111'),
    ('000000','000111','010010','010101','101010','101101','111000','111111'),
]
assert sorted(solutions) == sorted(EXPECTED), (solutions, EXPECTED)
for C in solutions:
    assert len(C) == 8
    assert not any(D[x] & D[y] for i,x in enumerate(C) for y in C[i+1:])
    assert all(''.join(str(int(a)^int(b)) for a,b in zip(x,y)) in C for x in C for y in C)
    assert tuple(sorted(x[::-1] for x in C)) == C
    assert tuple(sorted(''.join('1' if c=='0' else '0' for c in x) for x in C)) == C
print('BUCKETS_VERIFY_OK max=8 exact_labeled_optima=2 all_optima_linear=True')
print('partial_nodes=',visited)
for C in sorted(solutions): print(' '.join(C))
