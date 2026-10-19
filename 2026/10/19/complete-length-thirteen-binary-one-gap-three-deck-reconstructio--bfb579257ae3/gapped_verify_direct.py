"""Literal combinatorial enumeration of one-gap decks; independent of the prefix recurrence."""
from collections import Counter, defaultdict
from itertools import combinations

def pattern_counts(word):
    n = len(word)
    result = []
    for length in (1, 2, 3):
        profile = Counter()
        for positions in combinations(range(n), length):
            if all(b-a>=2 for a,b in zip(positions, positions[1:])):
                pattern = ''.join(word[i] for i in positions)
                profile[pattern] += 1
        for num in range(1<<length):
            key = format(num, f'0{length}b')
            result.append(profile[key])
    return tuple(result)

wanted = sorted([
 ('0001010000100','0010000101000'),
 ('0101111010110','0110101111010'),
 ('1001010000101','1010000101001'),
 ('1101111010111','1110101111011')
])
for n in range(1,14):
    profiles = defaultdict(list)
    for x in range(1<<n):
        w = format(x, f'0{n}b')
        profiles[pattern_counts(w)].append(w)
    doubletons = sorted(tuple(g) for g in profiles.values() if len(g)>1)
    sizes = Counter(map(len, profiles.values()))
    if n == 2: assert sizes == {1:2,2:1}
    if 3 <= n <= 12: assert sizes == {1:1<<n}
    if n == 13:
        assert len(profiles) == 8188
        assert sizes == {1:8184,2:4}
        assert doubletons == wanted
        assert all(a[::-1]==b for a,b in doubletons)
    print(n, len(profiles), dict(sorted(sizes.items())))
print('VERIFY_DIRECT_OK')
