"""Finite checks for canonical observable neighbourhood signatures.

Reproduces the modal operations directly from their set-theoretic semantics.
Requires Python 3 standard library only.
"""
from itertools import combinations, product


def upsets(leq):
    n = len(leq)
    return tuple(mask for mask in range(1 << n) if all(
        not (mask & (1 << i)) or (mask & (1 << j))
        for i in range(n) for j in range(n) if leq[i][j]))


def masks_minmax(leq):
    n = len(leq)
    maximal = sum(1 << i for i in range(n) if all(not leq[i][j] or i == j for j in range(n)))
    width = max(sum(1 for i in range(n) if mask & (1 << i))
                for mask in range(1 << n) if all(not (mask & (1 << i)) or
                not (mask & (1 << j)) or i == j or (not leq[i][j] and not leq[j][i])
                for i in range(n) for j in range(n)))
    return maximal, width


def box_signature(family, maxima):
    ans = []
    for u in family:
        tr = u & maxima
        if not any(v != u and (v & tr) == tr and (v & u) == v for v in family):
            ans.append(u)
    return tuple(sorted(ans))


def diamond_signature(family, maxima):
    return tuple(sorted(u for u in family if not any(
        v != u and (u & v) == u and (v & maxima) == (u & maxima) for v in family)))


def box(family, inst, scope):
    return any((u & scope) == u and all(u & a for a in inst) for u in family)


def diamond(family, inst, scope):
    return all(any((u & a) == u for a in inst) or bool(u & scope) for u in family)


def all_families(up):
    return [tuple(up[i] for i in range(len(up)) if bits & (1 << i))
            for bits in range(1 << len(up))]


def verify_frame(name, leq):
    up = upsets(leq)
    maxima, width = masks_minmax(leq)
    for typ, fn, sig in [('box', box, lambda fam: box_signature(fam,maxima)),
                         ('diamond', diamond, lambda fam: diamond_signature(fam,maxima))]:
        signature_to_table = {}
        table_to_signature = {}
        count = 0
        for fam in all_families(up):
            normal = sig(fam)
            # All combinations of upset arguments at arity at most width.
            table = tuple(fn(fam, inst, scope) for k in range(width + 1)
                          for inst in product(up, repeat=k) for scope in up)
            if normal in signature_to_table:
                assert signature_to_table[normal] == table, (name,typ,'forward',fam)
            else:
                signature_to_table[normal] = table
            if table in table_to_signature:
                assert table_to_signature[table] == normal, (name,typ,'reverse',fam)
            else:
                table_to_signature[table] = normal
            count += 1
        assert len(signature_to_table) == len(table_to_signature)
        print(f'{name}: {typ} families={count} observable_signatures={len(signature_to_table)} cutoff={width}')


def order_from_pairs(n, pairs):
    return [[i == j or (i,j) in pairs for j in range(n)] for i in range(n)]


def run():
    samples = [
        ('singleton', order_from_pairs(1, [])),
        ('two_antichain', order_from_pairs(2, [])),
        ('two_chain', order_from_pairs(2, [(0,1)])),
        ('three_antichain', order_from_pairs(3, [])),
        ('three_chain', order_from_pairs(3, [(0,1),(1,2),(0,2)])),
        ('three_V', order_from_pairs(3, [(0,2),(1,2)])),
        ('three_Lambda', order_from_pairs(3, [(0,1),(0,2)])),
        ('four_chain', order_from_pairs(4, [(i,j) for i in range(4) for j in range(i+1,4)])),
        ('two_plus_two', order_from_pairs(4, [(0,1),(2,3)])),
        ('five_chain', order_from_pairs(5, [(i,j) for i in range(5) for j in range(i+1,5)])),
        ('six_chain', order_from_pairs(6, [(i,j) for i in range(6) for j in range(i+1,6)])),
    ]
    for name, leq in samples:
        verify_frame(name,leq)
    # A sharp two-world loss on box data despite all arities.
    lc=order_from_pairs(2, [(0,1)])
    ups=upsets(lc)
    nb1=(2,)
    nb2=(2,3)
    for arity in range(5):
        for inst in product(ups,repeat=arity):
            for scope in ups:
                assert box(nb1,inst,scope) == box(nb2,inst,scope)
    # Diamond also loses a smaller, same-trace neighbourhood on the two-world chain.
    for arity in range(5):
        for inst in product(ups, repeat=arity):
            for scope in ups:
                assert diamond((3,), inst, scope) == diamond((2,3), inst, scope)
    # Unlike a box witness, the empty diamond neighbourhood is observable at arity zero.
    for scope in (0,1):
        assert diamond((), (), scope) != diamond((0,), (), scope)
    print('Two-world box and diamond equivalences, and one-world diamond emptiness detection: passed')

if __name__ == '__main__':
    run()
