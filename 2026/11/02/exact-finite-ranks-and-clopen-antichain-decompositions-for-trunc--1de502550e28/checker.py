#!/usr/bin/env python3
"""Independent finite checks for the ordinary-order truncated eventual-domination ranks."""
from itertools import product


def potential(xs, m, k):
    assert m >= 1 and k >= 1
    inds = [i for i in range(m) if xs[i] < k - 1]
    if not inds:
        return 1
    j = max(inds)
    return 1 + j * (k - 1) + (k - 1 - xs[j])


def edge(x, y, m, k):
    # Coordinates past m are fixed in each check; compute genuine eventual onset.
    bad = [i for i in range(len(x)) if not x[i] < y[i]]
    if bad:
        n = max(bad) + 1
    else:
        n = 0
    if n >= m:
        return False
    return x[n] < k and y[n] < k


def sharp_chain(m, k):
    cur = [0] * (m + 3)
    out = [tuple(cur)]
    for j in reversed(range(m)):
        for _ in range(k - 1):
            for i in range(j, len(cur)):
                cur[i] += 1
            out.append(tuple(cur))
    return out


def check():
    pairs = 0
    for m in range(1, 5):
        for k in range(1, 5):
            chain = sharp_chain(m, k)
            assert len(chain) == m * (k - 1) + 1
            assert [potential(v, m, k) for v in chain] == list(range(len(chain), 0, -1))
            for a, b in zip(chain, chain[1:]):
                assert edge(a, b, m, k), (m, k, a, b)
            # Exhaust every pair of length m+1 tuples over a bounded alphabet,
            # modeling longer tails with 0 then 1 repeatedly after the checked prefix.
            if m <= 3:
                pref = list(product(range(k + 1), repeat=m))
                for a in pref:
                    for b in pref:
                        x = a + (0,)
                        y = b + (1,)
                        # To force the monotone tail after coordinate m, repeat the
                        # known final suffix 0 < 1 forever. Then n from finite check
                        # agrees with the genuine least eventual-onset index.
                        if edge(x, y, m, k):
                            pairs += 1
                            assert potential(x, m, k) > potential(y, m, k), (m, k, x, y)
    print(f'ALL_CHECKS_OK sharp_instances=16 checked_edges={pairs}')

if __name__ == '__main__':
    check()
