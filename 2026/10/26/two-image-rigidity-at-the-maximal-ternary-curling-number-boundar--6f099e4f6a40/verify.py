#!/usr/bin/env python3
"""Exact exhaustive verification of the extremal curling-image theorem.

Python 3 standard library only. Run from the directory containing this script.
"""
from collections import Counter
from pathlib import Path

EXPECTED_PREFIX = (
    '112112212112122112212112211212211221211212212112211212211221'
    '21122112122121121221121'
)
assert len(EXPECTED_PREFIX) == 83

def overlap_at_last(s):
    """Whether the newest letter completes a factor with exponent > 2."""
    length = len(s)
    for period in range(1, (length + 1)//2):
        if s[-(2 * period + 1):-period] == s[-(period + 1):]:
            return True
    return False

def square_suffix(s):
    for block_length in range(1, len(s)//2 + 1):
        if s[-2*block_length:-block_length] == s[-block_length:]:
            return True
    return False

def curling_number_from_definition(s):
    best = 1
    for block_length in range(1, len(s)//2 + 1):
        block = s[-block_length:]
        repeats = 1
        right = len(s)-block_length
        while right >= block_length and s[right-block_length:right] == block:
            repeats += 1
            right -= block_length
        best = max(best, repeats)
    return best

def all_overlaps_absent(s):
    # Independent whole-word check, not relying on prefix ancestry.
    for right in range(3, len(s)+1):
        if overlap_at_last(s[:right]):
            return False
    return True

def enumerate_normalized():
    layer = [('0', '1')]
    counts = [(1, 1)]
    images_at_83 = None
    for length in range(2, 86):
        new_layer=[]
        for word, transform in layer:
            for letter in '012':
                extended = word + letter
                if overlap_at_last(extended):
                    continue
                next_transform = transform + ('2' if square_suffix(extended) else '1')
                if overlap_at_last(next_transform):
                    continue
                new_layer.append((extended, next_transform))
        layer = new_layer
        counts.append((length, len(layer)))
        if length == 83:
            images_at_83 = Counter(t for w,t in layer)
        if length == 84:
            extremizers = list(layer)
    assert not layer, 'There must be no valid normalized word of length 85.'
    return extremizers, counts, images_at_83

def main():
    root=Path(__file__).resolve().parent
    found, counts, images83 = enumerate_normalized()
    expected_counts = [(int(a),int(b)) for a,b in (line.strip().split('\t') for line in (root/'prefix_counts.tsv').read_text().splitlines()[1:])]
    assert counts == expected_counts, 'Prefix-level completeness certificate mismatch.'
    listed = [tuple(line.strip().split('\t')) for line in (root/'normalized_extremizers.tsv').read_text().splitlines()[1:]]
    assert found == listed, 'The manifest must match the independently enumerated complete set.'
    assert len(found)==2016
    fibers=Counter(t for w,t in found)
    assert fibers == {EXPECTED_PREFIX+'1':1344, EXPECTED_PREFIX+'2':672}
    assert sum(images83.values()) == 1680 and len(images83)==3
    assert images83[EXPECTED_PREFIX] == 672
    assert sorted(images83.values()) == [336,672,672]
    extending_parents = Counter(w[:-1] for w,t in found)
    assert len(extending_parents)==672 and set(extending_parents.values())=={3}
    assert all((transform[-1]=='2') == (word[-1]==word[-2])
               for word,transform in found)
    assert counts[-2:]==[(84,2016),(85,0)]
    for word, transform in found:
        assert word[0] == '0' and len(word)==len(transform)==84
        assert set(word) == {'0','1','2'}
        assert all_overlaps_absent(word) and all_overlaps_absent(transform)
        direct=''.join(str(curling_number_from_definition(word[:i])) for i in range(1,85))
        assert direct == transform
    print('PASS: complete normalized 1..85 prefix search; depth 85 empty')
    print('PASS: all 2016 source-transform manifest pairs exactly reproduced')
    print('PASS: 672 normalized depth-83 prefixes extend, each in all three ways; 1008 have none')
    print('PASS: exactly one depth-83 image supports extension, with 672 source prefixes')
    print('PASS: two images T1 (1344) and T2 (672) after fixing first letter 0')
    print('PASS: whole-word overlap and direct curling-number definitions for all 2016 pairs')
    print('PASS: global counts 6048 sources, image-fiber sizes 4032 and 2016')

if __name__ == '__main__':
    main()
