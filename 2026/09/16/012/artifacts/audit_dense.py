"""Independent edge-branching exhaustive check. Python standard library only.

Builds link domains by matching, without the structural link classification.
Unlike dense_stars.py, does not remove complete five-vertex components.
"""
from itertools import combinations
from small_stars import matching_rank, is_saturated
import json
import sys


def check(n, deficit, cap):
    triples = list(combinations(range(n), 3))
    index = {e: i for i, e in enumerate(triples)}
    pairs = list(combinations(range(n - 1), 2))
    patterns = []
    for k in range(cap + 1):
        for selected in combinations(range(len(pairs)), k):
            if matching_rank([pairs[i] for i in selected]) <= 4:
                patterns.append(selected)
    domains = []
    incident = []
    for v in range(n):
        others = [x for x in range(n) if x != v]
        bits = [1 << index[tuple(sorted((v, others[a], others[b])))]
                for a, b in pairs]
        incident.append(sum(bits))
        domains.append([sum(bits[i] for i in p) for p in patterns])
    present = sum(1 << index[(0, a, b)] for a, b in combinations(range(1, 5), 2)
                  if cap == 6 or (a, b) != (3, 4))
    absent = incident[0] ^ present
    target = 2 * n - deficit
    allbits = (1 << len(triples)) - 1
    nodes = leaves = witnesses = 0

    def visit(yes, no, options):
        nonlocal nodes, leaves, witnesses
        nodes += 1
        while True:
            if yes & no or yes.bit_count() > target or (allbits ^ no).bit_count() < target:
                return
            next_options = []
            forced_yes, forced_no = yes, no
            lo = hi = 0
            for v in range(n):
                required = yes & incident[v]
                allowed = [p for p in options[v] if p & no == 0 and p & required == required]
                if not allowed:
                    return
                common, possible = incident[v], 0
                low, high = cap, 0
                for p in allowed:
                    common &= p
                    possible |= p
                    low = min(low, p.bit_count())
                    high = max(high, p.bit_count())
                lo += low
                hi += high
                forced_yes |= common
                forced_no |= incident[v] ^ possible
                next_options.append(allowed)
            if lo > 3 * target or hi < 3 * target:
                return
            options = next_options
            if (forced_yes, forced_no) == (yes, no):
                break
            yes, no = forced_yes, forced_no
        unknown = allbits ^ (yes | no)
        if not unknown:
            leaves += 1
            if yes.bit_count() == target:
                edges = [e for i, e in enumerate(triples) if yes >> i & 1]
                if is_saturated(n, edges):
                    witnesses += 1
            return
        v = min((v for v in range(n) if incident[v] & unknown),
                key=lambda v: len(options[v]))
        candidates = incident[v] & unknown
        bit = candidates & -candidates
        visit(yes | bit, no, options)
        visit(yes, no | bit, options)

    visit(present, absent, domains)
    return dict(n=n, deficit=deficit, cap=cap, patterns=len(patterns),
                nodes=nodes, leaves=leaves, witnesses=witnesses)


if __name__ == '__main__':
    cases = [(6, 3), (7, 3), (8, 3), (9, 3), (8, 4), (6, 4), (9, 5)]
    if len(sys.argv) > 1:
        cases = [tuple(map(int, sys.argv[1:3]))]
    for n, d in cases:
        for cap in (5, 6):
            result = check(n, d, cap)
            if (n, d) in [(6, 3), (7, 3), (8, 3), (9, 3), (8, 4)]:
                assert result['witnesses'] == 0
            if (n, d) == (6, 4):
                assert result['witnesses'] == 3
            if (n, d) == (9, 5):
                assert result['witnesses'] == (6 if cap == 5 else 0)
            print(json.dumps(result), flush=True)
