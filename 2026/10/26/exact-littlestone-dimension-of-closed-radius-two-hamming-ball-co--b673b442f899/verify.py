"""Standalone checks for Hamming-radius-two online shattering witnesses.

Run in the directory containing witnesses.json: python3 verify.py
The all-dimensional upper bound is mathematical and is proved in RESULT.md.
"""
import json
from functools import lru_cache
from pathlib import Path

raw = json.loads(Path(__file__).with_name('witnesses.json').read_text(encoding='utf-8'))

def label(center, query):
    return int((center ^ query).bit_count() <= 2)

for case in raw['witnesses']:
    d, k = case['dimension'], case['depth']
    n = 1 << d
    leaves = []
    def visit(tree, sequence):
        remaining = k-len(sequence)
        if remaining == 0:
            assert set(tree) == {'center'}
            center = tree['center']
            assert type(center) is int and 0 <= center < n
            assert all(label(center, query) == bit for query,bit in sequence)
            leaves.append(center)
            return
        assert set(tree) == {'query', 'zero', 'one'}
        query = tree['query']
        assert type(query) is int and 0 <= query < n
        visit(tree['zero'], sequence+[(query,0)])
        visit(tree['one'], sequence+[(query,1)])
    visit(case['tree'], [])
    assert len(leaves) == 1 << k and len(set(leaves)) == len(leaves)
    print('TREE_OK dimension=%d depth=%d verified_paths=%d' % (d,k,len(leaves)))

# Independent minimax calculation on the whole concept family for all small sizes.
for d, expected in ((1,0),(2,0),(3,1),(4,3),(5,4),(6,5)):
    n = 1<<d
    masks = [sum(1<<c for c in range(n) if label(c,q)) for q in range(n)]
    @lru_cache(None)
    def can_shatter(versions, remaining):
        if remaining == 0: return True
        if versions.bit_count() < 1 << remaining: return False
        for positive_mask in masks:
            yes = versions & positive_mask
            no = versions ^ yes
            if (yes.bit_count() >= 1 << (remaining-1)
                and no.bit_count() >= 1 << (remaining-1)
                and can_shatter(yes,remaining-1)
                and can_shatter(no,remaining-1)):
                return True
        return False
    all_hypotheses = (1<<n)-1
    assert can_shatter(all_hypotheses, expected)
    assert not can_shatter(all_hypotheses, expected+1)
    print('EXACT_SMALL_OK dimension=%d littlestone=%d states=%d' % (d,expected,can_shatter.cache_info().currsize))

# Direct finite corroboration of the universal upper-bound proof's
# double-ball intersection structural cases. This is not an infinite proof.
for d in (5,6,7,8):
    n=1<<d
    ball0={c for c in range(n) if c.bit_count()<=2}
    for wt in (1,2):
        y=(1<<wt)-1
        neighborhood={c for c in ball0 if label(c,y)}
        for z in range(n):
            one={c for c in neighborhood if label(c,z)}
            zero=neighborhood-one
            if len(one) in (0,len(neighborhood)):
                continue
            # By the two explicit case decompositions in the proof, one
            # branch either has at most 5 hypotheses, or is a translated
            # one-star (possibly with its center).
            def is_small_or_star(group):
                if len(group) <=5: return True
                for t in range(n):
                    if all((c^t).bit_count()<=1 for c in group):
                        return True
                return False
            assert is_small_or_star(one) or is_small_or_star(zero), (d,wt,z)
    print('DOUBLE_BALL_BRANCH_CHECK_OK dimension=%d' % d)
print('ALL_CERTIFICATES_OK')
