#!/usr/bin/env python3
from itertools import combinations, combinations_with_replacement
from functools import lru_cache
from pathlib import Path
import json

VECTORS = tuple(range(1, 8))  # nonzero vectors of F_2^3 as 3-bit integers
T = 5
WITNESS_COUNTS = (0, 1, 1, 2, 2, 2, 2)


def compositions(total, k, prefix=()):
    if k == 1:
        yield prefix + (total,)
        return
    for i in range(total + 1):
        yield from compositions(total - i, k - 1, prefix + (i,))


def expand(counts):
    return tuple(v for v, c in zip(VECTORS, counts) for _ in range(c))


def rank(cols):
    span = {0}
    for x in cols:
        span |= {y ^ x for y in tuple(span)}
    return len(span).bit_length() - 1


def span_contains(vals, target):
    span = {0}
    for x in vals:
        span |= {y ^ x for y in tuple(span)}
    return target in span


def minimal_recovery_masks(cols, target):
    n = len(cols)
    out = []
    # An inclusion-minimal spanning set is linearly independent, so in dimension
    # three it has at most three columns.
    for r in (1, 2, 3):
        for inds in combinations(range(n), r):
            vals = tuple(cols[i] for i in inds)
            if not span_contains(vals, target):
                continue
            minimal = True
            for rr in range(1, r):
                for sub in combinations(inds, rr):
                    if span_contains(tuple(cols[j] for j in sub), target):
                        minimal = False
                        break
                if not minimal:
                    break
            if minimal:
                out.append(sum(1 << i for i in inds))
    return tuple(sorted(set(out)))


def can_pack_same(cols, target, need=T):
    masks = minimal_recovery_masks(cols, target)

    @lru_cache(None)
    def dfs(i, used, left):
        if left == 0:
            return True
        if len(masks) - i < left:
            return False
        for j in range(i, len(masks)):
            m = masks[j]
            if m & used:
                continue
            if dfs(j + 1, used | m, left - 1):
                return True
        return False

    return dfs(0, 0, need)


def is_asp(cols):
    if rank(cols) != 3:
        return False
    return all(can_pack_same(cols, target, T) for target in sorted(set(cols)))


def recovery_assignment(cols, req):
    rec = {target: minimal_recovery_masks(cols, target) for target in set(req)}

    @lru_cache(None)
    def dfs(rem, used):
        if not rem:
            return ()
        best_target = None
        best_options = None
        for target in sorted(set(rem)):
            options = tuple(m for m in rec[target] if not (m & used))
            if best_options is None or len(options) < len(best_options):
                best_target, best_options = target, options
        if not best_options:
            return None
        nxt = list(rem)
        nxt.remove(best_target)
        nxt = tuple(sorted(nxt))
        for mask in best_options:
            tail = dfs(nxt, used | mask)
            if tail is not None:
                return ((best_target, mask),) + tail
        return None

    return dfs(tuple(sorted(req)), 0)


def can_serve_request(cols, req):
    return recovery_assignment(cols, req) is not None


def is_asb(cols):
    if rank(cols) != 3:
        return False
    types = tuple(sorted(set(cols)))
    return all(
        can_serve_request(cols, req)
        for req in combinations_with_replacement(types, T)
    )


def validate_certificate(cols):
    path = Path(__file__).with_name('witness_certificate.json')
    data = json.loads(path.read_text(encoding='utf-8'))
    if data.get('field') != 'F_2' or data.get('dimension') != 3:
        raise AssertionError('bad certificate metadata')
    if tuple(data.get('columns_3bit', ())) != cols:
        raise AssertionError('certificate columns differ from witness')

    types = tuple(sorted(set(cols)))
    expected = list(combinations_with_replacement(types, T))
    rows = data.get('requests', [])
    if data.get('request_count') != len(expected) or len(rows) != len(expected):
        raise AssertionError('wrong certificate request count')

    seen = set()
    for row in rows:
        req = tuple(row['request'])
        if req not in expected or req in seen:
            raise AssertionError(('bad or duplicate request', req))
        seen.add(req)
        recs = row.get('recoveries', [])
        if len(recs) != T:
            raise AssertionError(('wrong recovery count', req))
        if sorted(r['target'] for r in recs) != list(req):
            raise AssertionError(('target multiset mismatch', req))
        used = set()
        for rec in recs:
            inds = tuple(rec['indices'])
            if not inds or len(set(inds)) != len(inds):
                raise AssertionError(('invalid recovery indices', req, inds))
            if any(i < 1 or i > len(cols) for i in inds):
                raise AssertionError(('index outside witness', req, inds))
            if used.intersection(inds):
                raise AssertionError(('recoveries are not disjoint', req))
            used.update(inds)
            vals = tuple(cols[i - 1] for i in inds)
            if not span_contains(vals, rec['target']):
                raise AssertionError(('recovery does not span target', req, rec))
    if seen != set(expected):
        raise AssertionError('certificate misses a request multiset')
    return len(rows)


def main():
    checked_by_n = {}
    for n in range(3, 10):
        checked = 0
        asp = 0
        for counts in compositions(n, 7):
            cols = expand(counts)
            if rank(cols) != 3:
                continue
            checked += 1
            if is_asp(cols):
                asp += 1
        checked_by_n[n] = (checked, asp)
        if asp != 0:
            raise AssertionError((n, asp))

    witness = expand(WITNESS_COUNTS)
    if len(witness) != 10 or rank(witness) != 3:
        raise AssertionError('bad witness dimensions')
    if not is_asp(witness):
        raise AssertionError('witness fails ASP')
    if not is_asb(witness):
        raise AssertionError('witness fails ASB')
    certificate_count = validate_certificate(witness)
    if certificate_count != 252:
        raise AssertionError(certificate_count)

    print('rank-3 multiplicity vectors checked by length:', checked_by_n)
    print('witness columns (3-bit labels):', witness)
    print('witness request multisets checked:', certificate_count)
    print('VERIFY_OK ASP(3,5,2)=ASB(3,5,2)=10')


if __name__ == '__main__':
    main()
