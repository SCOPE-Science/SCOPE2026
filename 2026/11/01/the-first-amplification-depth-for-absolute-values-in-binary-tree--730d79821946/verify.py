#!/usr/bin/env python3
"""Exact finite certificate for binary tree BMO absolute-value folding.

Usage: python3 bmo_depth3_verify.py bmo_depth3_certificate.json
Requires only Python's standard library; no optimization libraries.
"""
import itertools
import json
import sys
from fractions import Fraction as Q


def node_sets():
    return ([tuple(range(8)), tuple(range(4)), tuple(range(4, 8))]
            + [tuple(range(i, i + 2)) for i in range(0, 8, 2)])


def constraint_rows():
    result = []
    for js in node_sets():
        n = len(js)
        for eps in itertools.product((-1, 1), repeat=n):
            mean_eps = Q(sum(eps), n)
            row = [Q(0)] * 8
            for p, j in enumerate(js):
                row[j] = (Q(eps[p]) - mean_eps) / n
            if any(row) and row not in result:
                result.append(tuple(row))
    return result


def tree_automorphisms():
    identity = tuple(range(8))
    generators = []
    for length in (2, 4, 8):
        for start in range(0, 8, length):
            generators.append(tuple(
                start + (i-start+length//2) % length
                if start <= i < start+length else i for i in range(8)))
    group = {identity}
    frontier = [identity]
    while frontier:
        p = frontier.pop()
        for g in generators:
            q = tuple(p[g[i]] for i in range(8))
            if q not in group:
                group.add(q)
                frontier.append(q)
    assert len(group) == 128
    return sorted(group)


def canonical_cases(perms):
    def canon_sign(s):
        return min(tuple(s[p[i]] for i in range(8)) for p in perms)
    signs = set()
    for s in itertools.product((-1, 1), repeat=8):
        signs.add(min(canon_sign(s), canon_sign(tuple(-v for v in s))))
    assert len(signs) == 13
    for s in sorted(signs):
        if len(set(s)) == 1:
            continue
        stabilizer = [p for p in perms if tuple(s[p[i]] for i in range(8)) == s]
        subsets = set()
        for t in itertools.product((0, 1), repeat=8):
            if sum(t) in (0, 8):
                continue
            subsets.add(min(tuple(t[p[i]] for i in range(8)) for p in stabilizer))
        for t in sorted(subsets):
            yield (''.join('1' if v == 1 else '0' for v in s), ''.join(map(str, t)))


def oscillation(x, start, stop):
    z = x[start:stop]
    average = sum(z, Q(0)) / len(z)
    return sum((abs(v-average) for v in z), Q(0))/len(z)


def tree_bmo(x):
    return max(oscillation(x, j, j+n)
               for n in (len(x), len(x)//2, len(x)//4, len(x)//8)
               for j in range(0, len(x), n))


def main(path):
    with open(path, encoding='utf-8') as stream:
        data = json.load(stream)
    rows = constraint_rows()
    assert len(rows) == 290
    cases = data['certificates']
    assert data['schema_version'] == 1
    assert len(cases) == data['case_count'] == 910
    expected = set(canonical_cases(tree_automorphisms()))
    observed = set()
    total_weights = 0
    max_objective = Q(0)
    for case in cases:
        s_word, t_word = case['s'], case['t']
        key = (s_word, t_word)
        assert key in expected and key not in observed
        observed.add(key)
        assert len(s_word) == len(t_word) == 8
        s = [1 if z == '1' else -1 for z in s_word]
        t = [int(z) for z in t_word]
        k = sum(t)
        objective = [Q(si) * (Q(ti) - Q(k, 8)) / 4 for si, ti in zip(s, t)]
        lhs = [Q(0)] * 8
        bound = Q(0)
        used = set()
        for idx, num, den in case['w']:
            assert isinstance(idx, int) and isinstance(num, int) and isinstance(den, int)
            assert idx not in used and 0 <= idx < len(rows)+8
            used.add(idx)
            lam = Q(num, den)
            assert lam > 0
            if idx < len(rows):
                bound += lam
                lhs = [v + lam * a for v, a in zip(lhs, rows[idx])]
            else:
                lhs[idx - len(rows)] -= lam * s[idx-len(rows)]
            total_weights += 1
        assert lhs == objective, key
        assert bound <= 1, (key, bound)
        max_objective = max(max_objective, bound)
    assert observed == expected
    # Independent check of the explicit published depth-four witness.
    witness = [Q(v) for v in (0,-8,-12,-12,0,0,0,0,6,1,1,1,1,10,14,14)]
    assert tree_bmo(witness) == Q(5)
    assert tree_bmo([abs(v) for v in witness]) == Q(41, 8)
    # At depth three, all proper-node output oscillations contract by
    # the elementary two- and four-atom mean-absolute-deviation inequality.
    # The 910 dual identities establish root contraction on all sign cells.
    print('EXACT_CERTIFICATE_OK cases=910 constraints=290 '
          'automorphisms=128 dual_terms=%s max_bound=%s '
          'depth4_ratio=%s' % (total_weights, max_objective, Q(41, 40)))


if __name__ == '__main__':
    if len(sys.argv) != 2:
        raise SystemExit('Usage: python3 bmo_depth3_verify.py bmo_depth3_certificate.json')
    main(sys.argv[1])
