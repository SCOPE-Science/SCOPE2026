"""Independent exhaustive element-level EF types, with no orbit reduction."""
from functools import lru_cache

identifiers = {}
def intern(key):
    if key not in identifiers:
        identifiers[key] = len(identifiers)+1
    return identifiers[key]

@lru_cache(None)
def typ(n, xs, depth):
    atoms = tuple(int((xs[i] & ~xs[j]) == 0) for i in range(len(xs)) for j in range(len(xs)))
    if depth == 0:
        return intern(('atomic', atoms))
    next_types = set(typ(n, xs+(y,), depth-1) for y in range(1<<n))
    return intern((depth, atoms, tuple(sorted(next_types))))

if __name__ == '__main__':
    answers=[typ(n, (), 3) for n in range(1, 8)]
    print('n=1..7 direct rank-3 type identifiers:',answers)
    print('cached tuple instances:',typ.cache_info().currsize)
    assert len(set(answers[:6]))==6, 'small Boolean lattices not pairwise separated'
    assert answers[5]==answers[6], 'six- and seven-atom Boolean lattices differ'
    print('DIRECT_RANK3_FINITE_PASS')
