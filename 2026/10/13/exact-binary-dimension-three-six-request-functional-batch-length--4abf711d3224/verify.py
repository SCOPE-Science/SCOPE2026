"""Replay the exact 924-row recovery certificate for a binary [11,3,6] code."""
from itertools import combinations_with_replacement
from pathlib import Path

COLUMNS = (1, 2, 3, 4, 5, 6, 7, 1, 2, 4, 7)

def span(values):
    space = {0}
    for vec in values:
        space = space | {x ^ vec for x in space}
    return space

def verify():
    assert len(COLUMNS) == 11 and span(COLUMNS) == set(range(8))
    cert = Path(__file__).resolve().with_name('certificates.tsv')
    requests_seen = set()
    sizes = {}
    with cert.open('r', encoding='utf-8') as stream:
        for lineno, raw in enumerate(stream, 1):
            raw = raw.rstrip('\n')
            if not raw or raw.startswith('#'):
                continue
            cells = raw.split('\t')
            assert len(cells) == 2, ('columns',lineno)
            word, blocks = cells
            assert len(word) == 6 and all(c in '1234567' for c in word), lineno
            assert word == ''.join(sorted(word)) and word not in requests_seen, lineno
            requests_seen.add(word)
            groups = blocks.split('|')
            assert len(groups) == 6, lineno
            used = set()
            for target, group in zip(word, groups):
                names = [int(i) for i in group.split(',')]
                assert len(names) > 0 and len(names) == len(set(names)), lineno
                assert all(1 <= i <= 11 for i in names), lineno
                assert not used.intersection(names), lineno
                used.update(names)
                assert int(target) in span(COLUMNS[i-1] for i in names), lineno
                sizes[len(names)] = sizes.get(len(names),0)+1
    expected = {''.join(map(str,x)) for x in combinations_with_replacement(range(1,8),6)}
    assert requests_seen == expected and len(expected) == 924
    # Confirm binary minimum distance six, independently of any precomputed logs.
    weights = [sum((u & col).bit_count()%2 for col in COLUMNS) for u in range(1,8)]
    assert min(weights) == 6, weights
    print('VERIFY_OK 924/924 recovery lists; rank=3; minimum distance=6; sizes=',dict(sorted(sizes.items())))
if __name__ == '__main__':
    verify()
