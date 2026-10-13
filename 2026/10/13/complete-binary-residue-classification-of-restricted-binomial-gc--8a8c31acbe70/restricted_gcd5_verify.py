#!/usr/bin/env python3
"""Independent checks of the 2-adic formula for restricted binomial gcds at modulus 5."""
from itertools import combinations, combinations_with_replacement

def predicted(n):
    assert n > 5 and n % 5 == 0
    exps = [i for i in range(n.bit_length()) if n >> i & 1]
    r = tuple((pow(2, i, 5) for i in exps))
    minimal = not any(sum(sub) % 5 == 0
                      for j in range(1, len(r))
                      for sub in combinations(r, j))
    if not minimal:
        return 0
    if len(r) == 2:
        return 3 if n % 2 else 2
    if len(r) == 3 and n % 2 and tuple(sorted(r)) == (1, 2, 2):
        return 2
    return 1

def dp_exact(n):
    """Optimize binary digit weights of k and n-k under 5 | k, 0 < k < n.
    Independent from the zero-sum/splitting proof."""
    d = {(0, 0, False, False): 0}
    for pos in range(n.bit_length() + 1):
        nd = {}
        target = (n >> pos) & 1
        for (carry, remainder, seen_k, seen_l), w in d.items():
            for x in (0, 1):
                for y in (0, 1):
                    z = x + y + carry - target
                    if z not in (0, 2):
                        continue
                    state = (z // 2, (remainder + x * pow(2, pos, 5)) % 5,
                             seen_k or bool(x), seen_l or bool(y))
                    nw = w + x + y
                    if nw < nd.get(state, 10 ** 6):
                        nd[state] = nw
        d = nd
    w = d.get((0, 0, True, True))
    if w is None:
        raise AssertionError('No admissible interior lower index')
    return w - n.bit_count()

def brute_exact(n):
    return min((k.bit_count() + (n-k).bit_count()-n.bit_count())
               for k in range(5, n, 5))

def zero_sum_types_and_splits():
    types = []
    for w in range(2, 6):
        for ms in combinations_with_replacement(range(1, 5), w):
            if sum(ms) % 5:
                continue
            if any(sum(sub) % 5 == 0 for j in range(1, w)
                   for sub in combinations(ms, j)):
                continue
            types.append(ms)
    assert [sum(len(t) == w for t in types) for w in (2, 3, 4, 5)] == [2, 4, 4, 4]
    for ms in types:
        if len(ms) == 2 or ms == (1, 2, 2):
            continue
        witness = False
        for r in set(ms):
            remaining = list(ms)
            remaining.remove(r)
            new = (3 * r) % 5
            if new in remaining:
                continue
            tokens = remaining + [new, new]
            if any(sum(sub) % 5 == 0 for j in range(1, len(tokens))
                   for sub in combinations(tokens, j)):
                witness = True
                break
        assert witness, ms
    return len(types)

def main():
    minimal_types = zero_sum_types_and_splits()
    tests = 0
    for n in range(10, 20001, 5):
        p = predicted(n)
        d = dp_exact(n)
        assert p == d, ('DP', n, p, d)
        if n <= 1000:
            b = brute_exact(n)
            assert p == b, ('brute', n, p, b)
        tests += 1
    extremes = []
    for n in range(10, 20001, 5):
        if predicted(n) == 3:
            extremes.append(n)
    assert extremes[:4] == [65, 1025, 16385][:len(extremes[:4])]
    print('VERIFY_OK minimal_zero_sum_types='+str(minimal_types)+' entries='+str(tests)+' brute_entries='+str(len(range(10, 1001, 5))) +
          ' level_three='+str(len(extremes))+' first_level_three='+str(extremes[:5]))
if __name__ == '__main__':
    main()
