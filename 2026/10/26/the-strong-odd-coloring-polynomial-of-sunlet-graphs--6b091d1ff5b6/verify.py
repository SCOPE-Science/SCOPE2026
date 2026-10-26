"""Standalone exact verification for strong-odd colorings of cycle coronas.

Run: python3 verify.py
All arithmetic is integer and all enumerations are exhaustive over stated ranges.
"""
from itertools import product


def formula(n, q):
    assert n >= 3 and q >= 0
    t = q - 3
    r = 4 - q
    a = 1 + t * (q - 2)
    u0, u1 = 2, -t
    for _ in range(n):
        u0, u1 = u1, -t * u1 + r * a * u0
    return (a ** n + (q - 1) * u0
            + q * (q - 3) // 2 * r ** n
            + (q - 1) * (q - 2) // 2 * (-r) ** n)


def original_definition_count(n, q):
    """Enumerate all assignments on 2n vertices; test the original rules."""
    result = 0
    examined = 0
    for rim in product(range(q), repeat=n):
        if any(rim[i] == rim[(i + 1) % n] for i in range(n)):
            continue
        for leaves in product(range(q), repeat=n):
            examined += 1
            if any(leaves[i] == rim[i] for i in range(n)):
                continue
            # All leaf neighborhoods have a single vertex, hence are automatic.
            good = True
            for i in range(n):
                around = (rim[(i - 1) % n], rim[(i + 1) % n], leaves[i])
                counts = {c: around.count(c) for c in around}
                if any(count % 2 == 0 for count in counts.values()):
                    good = False
                    break
            if good:
                result += 1
    return result, examined


def transfer_trace(n, q):
    """Independent q(q-1)-state transfer construction and exact trace."""
    states = [(a, b) for a in range(q) for b in range(q) if a != b]
    where = {state: i for i, state in enumerate(states)}
    outgoing = [[] for _ in states]
    for i, (a, b) in enumerate(states):
        for c in range(q):
            if c != b:
                outgoing[i].append((where[(b, c)], 1 if c == a else q - 3))
    ans = 0
    for start in range(len(states)):
        cur = {start: 1}
        for _ in range(n):
            nxt = {}
            for i, count in cur.items():
                for j, weight in outgoing[i]:
                    nxt[j] = nxt.get(j, 0) + count * weight
            cur = nxt
        ans += cur.get(start, 0)
    return ans


def main():
    cases = [(n, q) for n in range(3, 6) for q in range(2, 5)]
    cases += [(4, 5), (6, 3)]
    total = 0
    for n, q in cases:
        actual, examined = original_definition_count(n, q)
        total += examined
        asserted = formula(n, q)
        assert actual == asserted, (n, q, actual, asserted)
    print('ORIGINAL_DEFINITION_OK cases={} examined_proper_rim_leaf_assignments={}'.format(
        len(cases), total))

    runs = 0
    for q in range(2, 9):
        for n in range(3, 15):
            a, b = formula(n, q), transfer_trace(n, q)
            assert a == b, (n, q, a, b)
            runs += 1
    print('TRANSFER_TRACE_OK cases={}'.format(runs))
    for n in range(3, 15):
        assert formula(n, 2) == (2 if n % 2 == 0 else 0)
        assert formula(n, 3) == (6 if n % 2 == 0 else 0)
        assert formula(n, 4) == 3 ** n + 3 * (-1) ** n
        assert formula(n, 0) == formula(n, 1) == 0
    print('SPECIALIZATIONS_OK n=3..14 palettes=0,1,2,3,4')
    print('REFERENCE_VALUES n=3..7 q=4:', [formula(n, 4) for n in range(3, 8)])
    print('REFERENCE_VALUES n=3..7 q=5:', [formula(n, 5) for n in range(3, 8)])
    print('VERIFICATION_OK')


if __name__ == '__main__':
    main()
