"""Independent finite tests for half-threshold progressive activation on trees.

Run: python check_cascades.py
Requires Python >=3.10 and networkx >=2.8.
This is a finite cross-check, not a proof for unbounded order.
"""
import networkx as nx


def simulate(T, initial):
    n = T.number_of_nodes()
    active = {initial}
    while True:
        added = {v for v in T if v not in active
                 and 2 * sum(u in active for u in T.neighbors(v)) >= T.degree(v)}
        if not added:
            return len(active)
        active.update(added)


def structural_sum(T):
    hubs = {v for v in T if T.degree(v) >= 3}
    n = len(T)
    if not hubs:
        return n * n
    low = set(T) - hubs
    seen = set()
    s = len(hubs)
    for v in low:
        if v in seen:
            continue
        component = {v}
        work = [v]
        seen.add(v)
        while work:
            a = work.pop()
            for b in T.neighbors(a):
                if b in low and b not in seen:
                    seen.add(b)
                    component.add(b)
                    work.append(b)
        m = len(component)
        boundary = sum(b in hubs for a in component for b in T.neighbors(a))
        s += m*m + boundary*m
    return s


if __name__ == '__main__':
    all_trees = 0
    all_seed_checks = 0
    for n in range(4, 13):
        minimum = 10**12
        optimizer_count = 0
        candidate_minimizers = []
        count = 0
        for T in nx.nonisomorphic_trees(n):
            count += 1
            empirical_sum = sum(simulate(T, v) for v in T)
            all_seed_checks += n
            formula_sum = structural_sum(T)
            assert empirical_sum == formula_sum, (n, empirical_sum, formula_sum)
            hubs = sum(T.degree(v) >= 3 for v in T)
            expected_optimizer = (hubs == (n-2)//2 and all(T.degree(v) != 2 for v in T))
            if empirical_sum < minimum:
                minimum = empirical_sum
                optimizer_count = 0
                candidate_minimizers = []
            if empirical_sum == minimum:
                optimizer_count += 1
                candidate_minimizers.append((expected_optimizer, sorted(T.degree(v) for v in T)))
            assert empirical_sum >= 2*n - (n-2)//2
        predicted = 2*n - (n-2)//2
        assert minimum == predicted, (n, minimum, predicted)
        for is_expected, ds in candidate_minimizers:
            assert is_expected, (n, ds)
            hubs = (n-2)//2
            expected_degrees = ([1]*(n-hubs)+([3]*hubs if n % 2 == 0 else [3]*(hubs-1)+[4]))
            assert ds == sorted(expected_degrees), (n, ds, expected_degrees)
        print(f'n={n}, nonisomorphic_trees={count}, minimum_sum={minimum}, optimizers={optimizer_count}')
        all_trees += count
    print(f'PASS: {all_trees} tree topologies, {all_seed_checks} seeded cascades, structural identity and all-minimizer checks')
