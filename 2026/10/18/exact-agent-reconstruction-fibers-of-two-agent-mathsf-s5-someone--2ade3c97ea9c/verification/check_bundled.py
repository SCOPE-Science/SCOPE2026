"""Reproducible finite checks for a two-agent S5 bundled-box reconstruction theorem.

Run: python check_bundled.py
No third-party dependencies.
"""
from collections import defaultdict
from itertools import combinations

def partitions(n):
    if n == 0:
        yield ()
        return
    for rest in partitions(n - 1):
        for i in range(len(rest)):
            p = list(rest)
            p[i] |= 1 << (n - 1)
            yield tuple(sorted(p))
        yield tuple(sorted(rest + (1 << (n - 1),)))

def blocks_of(p, n):
    return tuple(next(b for b in p if b & (1 << w)) for w in range(n))

def operator_signature(ep, fp, n):
    # The signature is the entire Boolean operation on the powerset carrier.
    return tuple(sum(1 << w for w in range(n)
                     if ((ep[w] & s) == ep[w] or (fp[w] & s) == fp[w]))
                 for s in range(1 << n))

def transverse(ep, fp):
    return all((ep[w] & ~fp[w]) and (fp[w] & ~ep[w]) for w in range(len(ep)))

def components(ep, fp, n):
    unseen = set(range(n))
    count = 0
    while unseen:
        count += 1
        seen = {unseen.pop()}
        while True:
            more = {v for v in unseen if any(((ep[u] | fp[u]) >> v) & 1 for u in seen)}
            if not more:
                break
            seen |= more
            unseen -= more
    return count

def check(n):
    ps = list(dict.fromkeys(partitions(n)))
    for p in ps:
        assert sum(p) == (1 << n) - 1
        assert sum(x.bit_count() for x in p) == n
    bps = [(p, blocks_of(p, n)) for p in ps]
    all_signatures = defaultdict(list)
    transversal_pairs = 0
    fibre_sizes = defaultdict(int)
    for p, ep in bps:
        for q, fp in bps:
            sig = operator_signature(ep, fp, n)
            is_trans = transverse(ep, fp)
            if is_trans:
                transversal_pairs += 1
            all_signatures[sig].append((p, q, ep, fp, is_trans))
    for sig, members in all_signatures.items():
        trans_members = [v for v in members if v[4]]
        if trans_members:
            assert len(trans_members) == len(members), ('nontransverse same signature', n)
            p, q, ep, fp, _ = trans_members[0]
            c = components(ep, fp, n)
            assert len(members) == 2 ** c, ('fibre wrong size', n, p, q, c, len(members))
            assert all(components(a,b,n) == c for _,_,a,b,_ in members)
            fibre_sizes[len(members)] += 1
    print(f'n={n}: Bell={len(ps)}, ordered_pairs={len(ps)**2}, trans_pairs={transversal_pairs}, transverse_fibres={sum(fibre_sizes.values())}, fibre_histogram={dict(sorted(fibre_sizes.items()))}')

if __name__ == '__main__':
    for n in range(1, 7):
        check(n)

# The following tests are independent of an enumeration of all partitions:
# reconstruct the endpoint sets from the truth table and exhibit the sharp
# eight-world ambiguity by explicitly exchanging agents in one component.

def minimal_true_sets(signature, w, n):
    true_sets = [u for u in range(1 << n) if signature[u] & (1 << w)]
    return frozenset(u for u in true_sets
                     if not any(v != u and (v & u) == v for v in true_sets))

def rectangular_components(n):
    assert n >= 4
    c = n // 4
    points = []
    for i in range(c):
        for a in range(2):
            for b in range(2):
                points.append((i, a, b))
    # Extra points are duplicates of the first incidence cell.
    points.extend([(0, 0, 0)] * (n - 4 * c))
    assert len(points) == n
    def relations(flipped):
        ep, fp = [], []
        for w, (i, a, b) in enumerate(points):
            x, y = (b, a) if i in flipped else (a, b)
            ep.append(sum(1 << v for v, (j,aa,bb) in enumerate(points)
                          if j == i and ((bb if j in flipped else aa) == x)))
            fp.append(sum(1 << v for v, (j,aa,bb) in enumerate(points)
                          if j == i and ((aa if j in flipped else bb) == y)))
        return tuple(ep), tuple(fp)
    baseline = relations(frozenset())
    expected = operator_signature(*baseline, n)
    distinct = set()
    for mask in range(1 << c):
        selected = frozenset(i for i in range(c) if mask & (1 << i))
        ep,fp = relations(selected)
        assert transverse(ep, fp)
        assert operator_signature(ep,fp,n) == expected
        assert all(len(minimal_true_sets(expected,w,n)) == 2 for w in range(n))
        distinct.add((ep,fp))
    assert len(distinct) == (1 << c)
    if n >= 8:
        e0, f0 = baseline
        e1, f1 = relations(frozenset((0,)))
        assert (e1,f1) != (e0,f0)
        assert (e1,f1) != (f0,e0)
    print(f'rectangular sharpness n={n} components={c} distinct_agent_assignments={len(distinct)}')

if __name__ == '__main__':
    for n in range(4, 13):
        rectangular_components(n)
