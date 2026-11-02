"""Independent finite checks for a fixed two-agent public-announcement formula.

Run: python3 checker.py. Exhaustive over two equivalence relations and all
p/q-valuations through four worlds, and over exclusive-valuations through five.
"""
from itertools import product
from math import factorial


def partitions(n):
    def visit(i, blocks):
        if i == n:
            yield tuple(tuple(b) for b in blocks)
            return
        for j in range(len(blocks)):
            blocks[j].append(i)
            yield from visit(i + 1, blocks)
            blocks[j].pop()
        blocks.append([i])
        yield from visit(i + 1, blocks)
        blocks.pop()
    yield from visit(0, [])


def equivalence_masks(part, n):
    out = [0] * n
    for block in part:
        mask = sum(1 << v for v in block)
        for v in block:
            out[v] = mask
    return tuple(out)


def update(survivors, a, b, p, q, n):
    kept = 0
    for i in range(n):
        bit = 1 << i
        if not survivors & bit:
            continue
        if (not p & bit or (a[i] & survivors & q)) and (not q & bit or (b[i] & survivors & p)):
            kept |= bit
    return kept


def evolution(n, a, b, p, q):
    survivors = (1 << n) - 1
    trace = [survivors]
    while True:
        nxt = update(survivors, a, b, p, q, n)
        if nxt == survivors:
            break
        trace.append(nxt)
        survivors = nxt
    return trace


def canonical(n, a, b, p, q, trace):
    if len(trace) != n + 1 or trace[-1] != 0:
        return False
    order = []
    for t in range(1, n + 1):
        eliminated = trace[t - 1] ^ trace[t]
        if eliminated.bit_count() != 1:
            return False
        order.append(eliminated.bit_length() - 1)
    if any((bool(p & 1 << w) == bool(q & 1 << w)) for w in order):
        return False
    if any(bool(p & 1 << order[j]) == bool(p & 1 << order[j - 1]) for j in range(1, n)):
        return False
    expected_a = [1 << i for i in range(n)]
    expected_b = [1 << i for i in range(n)]
    for j in range(1, n):
        w, prev = order[j], order[j - 1]
        target = expected_a if p & (1 << w) else expected_b
        target[w] |= 1 << prev
        target[prev] |= 1 << w
    return tuple(expected_a) == a and tuple(expected_b) == b


def graph_walk_survivors(n, a, b, p, q, times):
    # The digraph has a directed loop at every 00 and 11 world.
    edges = [0] * n
    for i in range(n):
        bit = 1 << i
        in_p, in_q = bool(p & bit), bool(q & bit)
        if in_p and not in_q:
            edges[i] = a[i] & q
        elif in_q and not in_p:
            edges[i] = b[i] & p
        else:
            edges[i] = bit
    # A walk of exactly t edges exists from a vertex iff it remains after t steps.
    alive = (1 << n) - 1
    out = [alive]
    for _ in range(times):
        alive = sum(1 << i for i, nbrs in enumerate(edges) if nbrs & alive)
        out.append(alive)
    return out


def check(n, exclusive):
    relations = [equivalence_masks(part, n) for part in partitions(n)]
    all_mask = (1 << n) - 1
    valuations = ([(p, all_mask ^ p) for p in range(1 << n)] if exclusive
                  else [(p, q) for p in range(1 << n) for q in range(1 << n)])
    full_count = 0
    total = 0
    for a in relations:
        for b in relations:
            for p, q in valuations:
                total += 1
                trace = evolution(n, a, b, p, q)
                extremal = len(trace) == n + 1
                if extremal:
                    assert canonical(n, a, b, p, q, trace), (n, a, b, p, q)
                    full_count += 1
                assert trace == graph_walk_survivors(n, a, b, p, q, len(trace) - 1)
    assert full_count == 2 * factorial(n), (n, full_count, 2 * factorial(n))
    return total, full_count


def check_single_agent(n):
    relations = [equivalence_masks(part, n) for part in partitions(n)]
    count = 0
    for a in relations:
        for p in range(1 << n):
            for q in range(1 << n):
                trace = evolution(n, a, a, p, q)
                assert len(trace) <= 2, (n, a, p, q)
                count += 1
    return count


def check_long_zigzags(max_n=100):
    for n in range(1, max_n + 1):
        order = list(range(n))
        for start_p in (False, True):
            p = sum(1 << i for i in range(n) if (i % 2 == 0) == start_p)
            q = ((1 << n) - 1) ^ p
            a = [1 << i for i in range(n)]
            b = [1 << i for i in range(n)]
            for j in range(1, n):
                link = a if p & (1 << j) else b
                link[j] |= 1 << (j - 1)
                link[j - 1] |= 1 << j
            trace = evolution(n, tuple(a), tuple(b), p, q)
            assert len(trace) == n + 1
            assert trace == [((1 << n) - 1) ^ ((1 << i) - 1) for i in range(n + 1)]
            assert canonical(n, tuple(a), tuple(b), p, q, trace)
    return 2 * max_n


if __name__ == '__main__':
    for n in range(1, 5):
        total, extrema = check(n, exclusive=False)
        print('all valuations:', n, total, 'extremal:', extrema)
    n = 5
    total, extrema = check(n, exclusive=True)
    print('exclusive valuations:', n, total, 'extremal:', extrema)
    print('single-agent checked:', check_single_agent(4))
    print('long canonical constructions checked:', check_long_zigzags())
    print('ALL_CHECKS_OK')
