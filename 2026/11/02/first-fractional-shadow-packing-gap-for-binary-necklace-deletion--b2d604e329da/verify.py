"""Exact verifier for binary cyclic-word single-deletion packing certificates.

Run from a directory containing certificates.json using Python 3.
No optimization package or external service is required.
"""
import json
from fractions import Fraction
from itertools import product
from pathlib import Path


def canonical(word):
    if not word:
        return ''
    return min(word[i:] + word[:i] for i in range(len(word)))


def necklaces(n):
    return sorted({canonical(''.join(t)) for t in product('01', repeat=n)})


def shadow(word):
    return {canonical(word[:i] + word[i + 1:]) for i in range(len(word))}


def verify():
    cert = json.loads(Path(__file__).with_name('certificates.json').read_text(encoding='utf-8'))
    rows = cert['rows']
    assert [r['n'] for r in rows] == list(range(1, 10))
    sizes = []
    for r in rows:
        n = r['n']
        words = necklaces(n)
        outputs = necklaces(n - 1)
        shadows = {w: shadow(w) for w in words}
        chosen = r['code']
        assert len(chosen) == len(set(chosen))
        assert set(chosen) <= set(words)
        assert all(shadows[a].isdisjoint(shadows[b]) for j, a in enumerate(chosen) for b in chosen[j+1:])
        sizes.append(len(chosen))
        # A valid weighted deletion-shadow cover dominates all integral codes.
        dual = {k: Fraction(v) for k, v in r['fractional_dual'].items()}
        assert set(dual) <= set(outputs)
        assert all(v >= 0 for v in dual.values())
        assert all(sum((dual.get(y, Fraction(0)) for y in shadows[w]), Fraction(0)) >= 1 for w in words)
        dual_sum = sum(dual.values(), Fraction(0))
        if n < 9:
            # Integral lower bound matches fractional upper bound exactly.
            assert dual_sum == len(chosen)
        else:
            assert len(words) == 60 and len(outputs) == 36
            assert len(chosen) == 9 and dual_sum == Fraction(41, 4)
            # Fractional packing weights obey EVERY output-shadow capacity.
            primal = {w: Fraction(v) for w, v in r['fractional_primal'].items()}
            assert set(primal) <= set(words)
            assert all(v >= 0 for v in primal.values())
            assert all(sum((primal.get(w, Fraction(0)) for w in words if y in shadows[w]), Fraction(0)) <= 1 for y in outputs)
            assert sum(primal.values(), Fraction(0)) == dual_sum
            # A fractional cover by genuine pairwise-conflicting cliques
            # bounds the integral code size strictly below ten.
            cover = r['conflict_clique_cover']
            for c in cover:
                C = c['words']; weight = Fraction(c['weight'])
                assert C and weight > 0 and len(C) == len(set(C)) and set(C) <= set(words)
                assert all(not shadows[a].isdisjoint(shadows[b]) for j, a in enumerate(C) for b in C[j + 1:])
            assert all(sum((Fraction(c['weight']) for c in cover if w in c['words']), Fraction(0)) >= 1 for w in words)
            assert sum((Fraction(c['weight']) for c in cover), Fraction(0)) == Fraction(59, 6)
            assert Fraction(59, 6) < 10
    assert sizes == [1, 2, 2, 3, 3, 5, 6, 8, 9]
    print('VERIFY_OK; integral profile=' + ','.join(map(str, sizes)) + '; F(9)=41/4; clique_bound=59/6')


if __name__ == '__main__':
    verify()
