"""Verify standalone roots and witness partitions for a length-20 extremizer."""
from pathlib import Path


def test(path='witnesses_n10.tsv'):
    lines = Path(path).read_text(encoding='utf8').splitlines()
    assert len(lines) == 171
    assert lines[0] == 'root\tselected_position_mask'
    word = '01010101101010101010'
    roots = set()
    for line in lines[1:]:
        root, mask = line.split('\t')
        assert len(root) == 10 and set(root) <= set('01')
        assert len(mask) == 20 and mask.count('1') == 10
        left = ''.join(word[i] for i, bit in enumerate(mask) if bit == '1')
        right = ''.join(word[i] for i, bit in enumerate(mask) if bit == '0')
        assert root == left and root == right[::-1]
        assert root not in roots
        roots.add(root)
    print('170 DISTINCT ROOT WITNESSES VERIFIED')


if __name__ == '__main__':
    test()
