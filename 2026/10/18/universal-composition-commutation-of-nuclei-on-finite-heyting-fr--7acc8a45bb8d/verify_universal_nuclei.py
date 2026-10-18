"""Independent finite-instance checks for universal commutation of Heyting nuclei.

Requires Python 3 standard library only. No external data.
"""
from collections import Counter
from itertools import combinations


def labelled_posets(n):
    edges = tuple(combinations(range(n), 2))
    for code in range(3 ** len(edges)):
        relation = [1 << i for i in range(n)]
        value = code
        for a, b in edges:
            state = value % 3
            value //= 3
            if state == 1:
                relation[a] |= 1 << b
            elif state == 2:
                relation[b] |= 1 << a
        for via in range(n):
            for x in range(n):
                if relation[x] & (1 << via):
                    relation[x] |= relation[via]
        if any(
            x != y and relation[x] & (1 << y) and relation[y] & (1 << x)
            for x in range(n) for y in range(n)
        ):
            continue
        yield tuple(relation)


def upsets(rel):
    n = len(rel)
    return tuple(
        u for u in range(1 << n)
        if all(not (u & (1 << x)) or (u & rel[x]) == rel[x] for x in range(n))
    )


def nucleus(rel, subset, u):
    return sum(1 << x for x in range(len(rel)) if not (rel[x] & subset & ~u))


def comps(rel):
    n = len(rel)
    remaining = set(range(n))
    answer = []
    while remaining:
        start = next(iter(remaining))
        stack = [start]
        component = {start}
        remaining.remove(start)
        while stack:
            x = stack.pop()
            for y in tuple(remaining):
                if ((rel[x] >> y) & 1) or ((rel[y] >> x) & 1):
                    remaining.remove(y)
                    component.add(y)
                    stack.append(y)
        answer.append(frozenset(component))
    return answer


def is_component_union(rel, subset):
    return all(all(bool(subset & (1 << x)) == bool(subset & (1 << y))
                   for x in comp for y in comp) for comp in comps(rel))


def verify(n):
    counts = Counter()
    instances = 0
    for rel in labelled_posets(n):
        instances += 1
        us = upsets(rel)
        uset = set(us)
        numb = 1 << n
        funcs = [tuple(nucleus(rel, s, u) for u in us) for s in range(numb)]
        assert len(set(funcs)) == numb, (n, rel, 'not bijective')
        for s in range(numb):
            f = funcs[s]
            assert all((a | f[ia]) == f[ia] for ia, a in enumerate(us)), (n, rel, s, 'extensivity')
            assert all(f[ia] in uset for ia in range(len(us)))
            assert all(nucleus(rel,s,nucleus(rel,s,a)) == nucleus(rel,s,a) for a in us), (n, rel,s,'idempotence')
            assert all(nucleus(rel,s,a&b) == (nucleus(rel,s,a)&nucleus(rel,s,b)) for a in us for b in us), (n, rel,s,'meet')
            bottom_probes = all(nucleus(rel,s,nucleus(rel,1<<p,0)) ==
                                nucleus(rel,1<<p,nucleus(rel,s,0)) for p in range(n))
            universal = all(all(nucleus(rel,s,nucleus(rel,t,u)) ==
                                nucleus(rel,t,nucleus(rel,s,u)) for u in us)
                            for t in range(numb))
            component_test = is_component_union(rel,s)
            assert bottom_probes == universal == component_test, (n, rel, s)
        count = sum(is_component_union(rel,s) for s in range(numb))
        assert count == 2 ** len(comps(rel)), (n, rel, count)
        counts[count] += 1
        for p in range(n):
            for q in range(n):
                expected = p == q or not (rel[p] & (1 << q)) and not (rel[q] & (1 << p))
                actual = all(nucleus(rel,1<<p,nucleus(rel,1<<q,u)) ==
                             nucleus(rel,1<<q,nucleus(rel,1<<p,u)) for u in us)
                assert actual == expected, (n,rel,p,q)
    return instances, counts


def main():
    results = {}
    for n in range(5):
        instances, histogram = verify(n)
        results[n] = (instances, sorted(histogram.items()))
    assert results[4][0] == 543
    print('VERIFY_OK')
    for n, (count, histogram) in results.items():
        print('size', n, 'labelled_posets', count, 'central_count_histogram', histogram)

if __name__ == '__main__':
    main()
