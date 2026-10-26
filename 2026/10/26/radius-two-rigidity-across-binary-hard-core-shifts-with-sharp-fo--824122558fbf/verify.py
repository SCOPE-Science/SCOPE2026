#!/usr/bin/env python3
"""Reproduce the radius-two hard-core shift endomorphism classification.

Uses exact bitmasks and exhaustive finite-language checks; no external modules.
The infinite-language implications are explained in RESULT.md.
"""
import csv
import io
from collections import Counter, deque
from itertools import product
from pathlib import Path


def legal(word, k):
    last = None
    for i, bit in enumerate(word):
        if bit:
            if last is not None and i - last <= k:
                return False
            last = i
    return True


def words(length, k):
    return [tuple(w) for w in product((0, 1), repeat=length) if legal(w, k)]


def analyze(k):
    local = words(5, k)
    indexing = {w: i for i, w in enumerate(local)}
    four = words(4, k)
    vertex = {w: i for i, w in enumerate(four)}
    edges = [(vertex[w[:4]], vertex[w[1:]], indexing[w]) for w in local]
    checks = [[indexing[w[i:i + 5]] for i in range(k + 1)]
              for w in words(k + 5, k)]
    catalog = []
    max_reachable = 0
    for rule in range(1 << len(local)):
        output = [int(bool(rule & (1 << i))) for i in range(len(local))]
        if any(not legal([output[j] for j in line], k) for line in checks):
            continue
        # Relation on all extendible length-four input contexts.
        transition = [[0, 0] for _ in four]
        for src, dst, label in edges:
            transition[src][output[label]] |= 1 << dst

        def advance(subset, label):
            nxt = 0
            while subset:
                lowest = subset & -subset
                src = lowest.bit_length() - 1
                subset -= lowest
                nxt |= transition[src][label]
            return nxt

        # Legal output words tracked by elapsed zeros (k means sufficient).
        initial = ((1 << len(four)) - 1, k)
        pending = deque([(initial, '')])
        seen = {initial}
        witness = None
        while pending and witness is None:
            (subset, zero_run), prefix = pending.popleft()
            for label in (0, 1):
                if label == 1 and zero_run < k:
                    continue
                new_zeros = 0 if label else min(k, zero_run + 1)
                nxt = advance(subset, label)
                if nxt == 0:
                    witness = prefix + str(label)
                    break
                pair = nxt, new_zeros
                if pair not in seen:
                    seen.add(pair)
                    pending.append((pair, prefix + str(label)))
        max_reachable = max(max_reachable, len(seen))
        catalog.append((k, rule, len(witness) if witness else None,
                        witness or '', len(seen)))
    return local, catalog, max_reachable


def brute_first_missing(k, rule, local, upto):
    index = {w: i for i, w in enumerate(local)}
    for n in range(1, upto + 1):
        image = set()
        for input_word in words(n + 4, k):
            output = ''.join(str((rule >> index[input_word[j:j + 5]]) & 1)
                             for j in range(n))
            image.add(output)
        absent = {''.join(map(str, w)) for w in words(n, k)} - image
        if absent:
            return n, absent
    return None, set()


def run():
    catalogs = {}
    local_sizes = {}
    closure = {}
    for k in (2, 3, 4):
        local, catalog, max_reachable = analyze(k)
        catalogs[k] = catalog
        local_sizes[k] = len(local)
        closure[k] = max_reachable
    assert local_sizes == {2: 9, 3: 7, 4: 6}, local_sizes
    assert [len(catalogs[i]) for i in (2, 3, 4)] == [23, 9, 6]
    assert [sum(row[2] is None for row in catalogs[k]) for k in (2, 3, 4)] == [5, 5, 5]
    assert Counter(row[2] for row in catalogs[2]) == {
        None: 5, 1: 1, 4: 7, 5: 4, 6: 2, 8: 2, 9: 2}
    assert Counter(row[2] for row in catalogs[3]) == {None: 5, 1: 1, 5: 2, 6: 1}
    assert Counter(row[2] for row in catalogs[4]) == {None: 5, 1: 1}
    assert {row[1] for row in catalogs[2] if row[2] == 9} == {96, 258}
    assert {row[1] for row in catalogs[3] if row[2] == 6} == {64}
    assert {row[3] for row in catalogs[2] if row[2] == 9} == {
        '100100001', '100001001'}
    assert {row[3] for row in catalogs[3] if row[2] == 6} == {'100001'}
    # Independent direct input enumeration checks every shorter length and
    # one minimal witness for every nonsurjective map, for k=2,3.
    for k in (2, 3):
        local = words(5, k)
        for _, rule, first, witness, _ in catalogs[k]:
            upper = first if first is not None else (9 if k == 2 else 6)
            got, missing = brute_first_missing(k, rule, local, upper)
            assert got == first, (k, rule, got, first)
            if first is not None:
                assert witness in missing, (k, rule, witness, missing)
    # The k>=4 claim is proved algebraically in RESULT.md, not by extrapolating
    # these finite k tests. This k=4 enumeration checks its boundary instance.
    buffer = io.StringIO()
    writer = csv.writer(buffer, lineterminator='\n')
    writer.writerow(['exclusion_range', 'local_rule_mask', 'first_missing_length',
                     'shortest_missing_word', 'reachable_dfa_pairs'])
    for k in (2, 3, 4):
        for _, mask, length, witness, reached in catalogs[k]:
            writer.writerow([k, mask, '' if length is None else length,
                             witness, reached])
    payload = buffer.getvalue()
    catalog_file = Path(__file__).with_name('classification.csv')
    if catalog_file.exists():
        assert catalog_file.read_text(encoding='utf-8') == payload
    else:
        catalog_file.write_text(payload, encoding='utf-8')
    print('VERIFY_OK: k=2,3,4 preserving maps 23/9/6; onto maps 5/5/5;')
    print('sharp first-missing thresholds k=2:9 (masks 96,258), k=3:6 (mask 64);')
    print('all k=2,3 first missing lengths independently checked by full input enumeration;')
    print(f'largest reachable predecessor-constraint pair sets: {closure};')
    print('for k>=4 algebraically only zero and five shift maps.')


if __name__ == '__main__':
    run()
