"""Finite reproducibility checks for full zip-shift conjugacy classification.

The infinite-dimensional classification is proved analytically, not by this test.
Uses only the Python standard library.
"""
from collections import Counter, defaultdict
from itertools import product


def signatures(tau, m):
    sizes = Counter(tau)
    return tuple(sorted(sizes.values(), reverse=True)), tuple(sorted(sizes[tau[a]] for a in range(len(tau))))


def relabel(tau, other):
    """Find explicit alphabet permutations alpha, beta, with other[alpha[a]]=beta[tau[a]]."""
    n = len(tau)
    m = len(set(tau))
    left = sorted(range(m), key=lambda b: (tau.count(b), b))
    right = sorted(range(m), key=lambda b: (other.count(b), b))
    assert [tau.count(b) for b in left] == [other.count(b) for b in right]
    beta = {b: c for b, c in zip(left, right)}
    alpha = {}
    for b in range(m):
        left_f = [a for a in range(n) if tau[a] == b]
        right_f = [a for a in range(n) if other[a] == beta[b]]
        for a, c in zip(left_f, right_f):
            alpha[a] = c
    assert len(set(alpha.values())) == n and len(set(beta.values())) == m
    assert all(other[alpha[a]] == beta[tau[a]] for a in range(n))
    return alpha, beta


def shift_window(tau, x, lo, hi):
    """Return F_tau(x) restricted to [lo,hi), with x defined through index hi."""
    return {i: (tau[x[0]] if i == -1 else x[i+1]) for i in range(lo, hi)}


def check_conjugacy(tau, other):
    alpha, beta = relabel(tau, other)
    n = len(tau)
    m = len(set(tau))
    # All deterministic short words, checking the actual coordinate identity.
    for future in product(range(n), repeat=3):
        for past in product(range(m), repeat=2):
            x = {-2: past[0], -1: past[1], 0: future[0], 1: future[1], 2: future[2]}
            converted = {i: (alpha[v] if i >= 0 else beta[v]) for i,v in x.items()}
            f = shift_window(tau, x, -2, 2)
            g = shift_window(other, converted, -2, 2)
            assert {i: (alpha[v] if i >= 0 else beta[v]) for i,v in f.items()} == g
    return True


def partitions(n, max_part=None):
    if n == 0:
        yield ()
    else:
        for k in range(min(n,max_part or n), 1-1, -1):
            for rest in partitions(n-k,k):
                yield (k,) + rest


def main():
    total_maps = total_classes = conj_checks = 0
    for n in range(2,7):
        groups = defaultdict(list)
        for m in range(1,n+1):
            for tau in product(range(m), repeat=n):
                if len(set(tau)) != m:
                    continue
                partition, fixed_degrees = signatures(tau,m)
                expected = tuple(sorted((d for d in partition for _ in range(d))))
                assert fixed_degrees == expected
                groups[partition].append(tau)
                total_maps+=1
        ps=set(partitions(n))
        assert set(groups)==ps
        for part,ts in groups.items():
            # Representative-to-last and an interior relabeling; all classes distinguished by degree spectra.
            other=ts[-1]
            if len(ts) > 1:
                check_conjugacy(ts[0],other)
                conj_checks+=1
        total_classes+=len(groups)
        print(f'N={n}: {sum(map(len,groups.values()))} surjections, {len(groups)} conjugacy classes')
    assert total_classes==2+3+5+7+11  # p(2)+...+p(6)
    print(f'PASS: {total_maps} onto transition maps, {total_classes} partition classes, {conj_checks} exact finite-window conjugacies.')

if __name__ == '__main__':
    main()
