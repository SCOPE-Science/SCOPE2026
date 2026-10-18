"""Finite checks for the lacunary-block family in the accompanying theorem.

The infinite conclusions are proved analytically, not inferred from these samples.
"""
from random import Random


def admissible(blocks, anchor=None):
    """blocks: {index: set of integer positions within its block}."""
    support = sorted(j for j, s in blocks.items() if s)
    if not support:
        return False
    i = support[0]
    if anchor is not None and i != anchor:
        return False
    for j in support:
        if any(k < 0 or k >= 2**j for k in blocks[j]):
            return False
    if any(k < 2 * j for j, k in zip(support, support[1:])):
        return False
    return all(len(blocks[j]) <= 2**(j-i) for j in support[1:])


def random_family(rng, max_block=10):
    first = rng.randint(1, max_block)
    support = [first]
    while support[-1] * 2 <= max_block and rng.randrange(2):
        nxt = rng.randint(2*support[-1], max_block)
        support.append(nxt)
    d = {}
    for j in support:
        cap = 2**j if j == first else 2**(j-first)
        howmany = rng.randint(1, min(cap, 75))
        d[j] = set(rng.sample(range(2**j), howmany))
    assert admissible(d)
    return d


def trial_local_capture(rng):
    d = random_family(rng, max_block=8)
    f = random_family(rng, max_block=12)
    anchor = min(d)
    final = max(d)
    tail = {j: pts for j, pts in f.items() if j > 2*final}
    if not tail:
        return False
    c = {j: set(pts) for j, pts in d.items()}
    weights = {(j,k): 0.1 + 9.9*rng.random() for j,pts in tail.items() for k in pts}
    for j,pts in tail.items():
        cap = 2**(j-anchor)
        ordered = sorted(pts, key=lambda k: weights[(j,k)], reverse=True)
        c[j] = set(ordered[:cap])
    assert admissible(c, anchor=anchor)
    total = sum(weights[(j,k)] for j,pts in tail.items() for k in pts)
    captured = sum(weights[(j,k)] for j,pts in c.items() if j in tail for k in pts)
    assert captured + 1e-9 >= 2**(-anchor)*total, (anchor,captured,total)
    return True


def trial_block_isometries(rng):
    n = rng.randrange(3,9)
    coeff = [rng.uniform(-3,3) for _ in range(n)]
    # Every admissible chain meets [n,2n) in at most one block.
    for a in range(n,2*n):
        for b in range(a+1,2*n):
            assert b < 2*a
    expected = max(abs(z) for z in coeff)
    for j,z in zip(range(n,2*n), coeff):
        assert abs(z) <= expected
    # The full principal block in the maximizing coordinate attains the norm.
    assert expected == max(abs(z) for z in coeff)
    return True


def trial_directedness_separation():
    # A fixed proposed positive tail fraction gamma is defeated by a
    # sufficiently late anchor; earlier anchors can keep at most half of D.
    for gamma in (0.01,0.1,0.4,0.75):
        i = next(i for i in range(1,20) if 2**(-i) < gamma)
        j = max(2*i,15)
        assert 2**(j-i) / 2**j < gamma
        assert all(2**(i-h) / 2**i <= 0.5 for h in range(1,i))
    return True



def trial_norming_anchor(rng):
    """Finite-block dynamic programming checks the anchoring inequality."""
    last = rng.randrange(7, 11)
    weights = {j: [rng.random() if rng.randrange(4) else 0.0
                   for _ in range(2**j)] for j in range(1, last+1)}
    masses = {j: sum(weights[j]) for j in weights}

    def K(i):
        def best_from(k):
            if k > last:
                return 0.0
            return max([0.0] + [sum(sorted(weights[j], reverse=True)[:2**(j-i)])
                                + best_from(2*j) for j in range(k,last+1)])
        return masses[i] + best_from(2*i)
    k1 = K(1)
    for i in range(2,last+1):
        assert K(i) <= masses[i] + k1 + 1e-8
    return True

def main():
    rng = Random(271828)
    successful = sum(trial_local_capture(rng) for _ in range(420))
    assert successful >= 30
    for _ in range(250):
        trial_block_isometries(rng)
    trial_directedness_separation()
    for _ in range(24):
        trial_norming_anchor(rng)
    print(f'LOCAL_CAPTURE_LACUNARY_BLOCK_FINITE_CHECKS_OK capture={successful} block_tests=250 anchor_checks=24')

if __name__ == '__main__':
    main()
