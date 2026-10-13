#!/usr/bin/env python3
"""Exact finite tests for the forbidden-target sum/product extremum.
Pure Python; does not infer infinite truth from finite tests.
"""

def primes_upto(n):
    out = []
    for p in range(2, n + 1):
        if all(p % q for q in range(2, int(p**0.5) + 1)):
            out.append(p)
    return out


def projective_order(p, a):
    # Iterate the nonfixed projective point infinity under x -> a-a/x.
    x = None
    for k in range(1, p + 2):
        if x is None:
            x = a
        elif x == 0:
            x = None
        else:
            x = a * (x - 1) * pow(x, -1, p) % p
        if x is None:
            return k
    raise AssertionError('period exceeds projective line cardinality')


def graph(p, target):
    g = [set() for _ in range(p)]
    loop = set()
    for x in range(p):
        y = (target-x)%p
        if x == y:
            loop.add(x)
        else:
            g[x].add(y)
            g[y].add(x)
        if x:
            y = target * pow(x, -1, p) % p
            if x == y:
                loop.add(x)
            else:
                g[x].add(y)
                g[y].add(x)
    return g, loop


def components(g):
    done = set()
    for x in range(len(g)):
        if x not in done:
            seen = {x}
            stack = [x]
            while stack:
                v = stack.pop()
                for w in g[v]:
                    if w not in seen:
                        seen.add(w)
                        stack.append(w)
            done |= seen
            yield seen


def maximum_independent(g, loops):
    # Independent set DP for paths and cycles; no reliance on the proposed formula.
    total = 0
    for vertex_set in components(g):
        if len(vertex_set) == 1:
            total += int(next(iter(vertex_set)) not in loops)
            continue
        endpoint = next((v for v in vertex_set if len(g[v]) < 2), None)
        start = endpoint if endpoint is not None else min(vertex_set)
        order = [start]
        previous = None
        here = start
        while True:
            choices = g[here] - ({previous} if previous is not None else set())
            if not choices:
                break
            next_vertex = min(choices)
            if next_vertex == start:
                break
            assert next_vertex not in order
            order.append(next_vertex)
            previous, here = here, next_vertex
        assert len(order) == len(vertex_set), (order, vertex_set)
        is_cycle = endpoint is None

        def path_best(seq):
            exclude, include = 0, -10**9
            for v in seq:
                exclude, include = max(exclude, include), exclude + (1 if v not in loops else -10**9)
            return max(exclude, include)

        if not is_cycle:
            total += path_best(order)
        else:
            choices = [path_best(order[1:])]
            if order[0] not in loops:
                choices.append(1 + path_best(order[2:-1]))
            total += max(choices)
    return total


def direct_brute(p, t):
    # Exhaust all subsets, and test pairwise sums and products directly.
    best = 0
    for mask in range(1 << p):
        size = mask.bit_count()
        if size <= best:
            continue
        elements = [x for x in range(p) if mask & (1<<x)]
        valid = True
        for x in elements:
            for y in elements:
                if (x+y)%p == t or (x*y)%p == t:
                    valid = False
                    break
            if not valid:
                break
        if valid:
            best = size
    return best


def main():
    count = 0
    exceptional = 0
    for p in primes_upto(199):
        if p < 5:
            continue
        for t in range(1, p):
            m = projective_order(p, t)
            square = (pow(t, (p-1)//2, p) == 1)
            defect = int(square and m % 2 == 0)
            predicted = (p-1)//2 - defect
            g, loops = graph(p, t)
            observed = maximum_independent(g, loops)
            assert observed == predicted, (p, t, predicted, observed, m)
            assert all(len(x) <= 2 for x in g)
            if p <= 13:
                assert direct_brute(p, t) == predicted, (p, t)
            count += 1
            exceptional += defect
    assert maximum_independent(*graph(7, 1)) == 3
    assert maximum_independent(*graph(7, 2)) == 2
    assert maximum_independent(*graph(11, 3)) == 4
    print(f'VERIFY_OK prime_target_pairs={count} exact_defect_one={exceptional} tested_primes=5..199')
    print('All component-DP optima agree; all subsets exhausted for primes <=13.')
    print('Examples: (p,target,max)=(7,1,3),(7,2,2),(11,3,4).')

if __name__=='__main__':
    main()
