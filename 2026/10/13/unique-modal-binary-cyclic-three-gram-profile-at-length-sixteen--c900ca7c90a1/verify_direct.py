"""Direct exhaustive census independent of Eulerian arborescence formulas.
Requires Python 3 standard library only. Run next to profile_census.csv.
"""
from collections import Counter
from pathlib import Path
import csv


def profile(word, length):
    counts = [0]*8
    for i in range(length):
        a = (word >> i) & 1
        b = (word >> ((i + 1) % length)) & 1
        c = (word >> ((i + 2) % length)) & 1
        counts[4*a + 2*b + c] += 1
    return tuple(counts)


def census(length):
    result = Counter()
    for word in range(1 << length):
        result[profile(word, length)] += 1
    assert sum(result.values()) == 1 << length
    return result


def main():
    by_profile = census(16)
    assert len(by_profile) == 271
    sorted_weights = sorted(by_profile.values(), reverse=True)
    assert sorted_weights[:3] == [1296,1280,1152]
    assert [p for p,v in by_profile.items() if v == 1296] == [(2,)*8]
    assert [p for p,v in by_profile.items() if v == 1280] == [(1,2,3,2,2,3,2,1)]
    path = Path(__file__).with_name('profile_census.csv')
    with path.open(newline='', encoding='utf-8') as fh:
        rows = list(csv.reader(fh))
    assert rows[0] == ['000','001','010','011','100','101','110','111','fiber_size']
    expected = [list(map(str, (*p, by_profile[p]))) for p in sorted(by_profile)]
    assert rows[1:] == expected, 'profile census differs from exhaustive word count'
    early = census(8)
    assert len(early) == 27 and max(early.values()) == 24
    assert early[(1,)*8] == 16
    assert [p for p,v in early.items() if v == 24] == [(0,1,2,1,1,2,1,0)]
    print('DIRECT_OK n=16 words=65536 profiles=271 maximum=1296 unique; second=1280 unique; n=8 maximum=24 uniform=16')

if __name__ == '__main__':
    main()
