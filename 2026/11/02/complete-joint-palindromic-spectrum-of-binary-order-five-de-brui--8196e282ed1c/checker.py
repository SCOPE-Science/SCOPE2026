"""Exhaustive certificate for circular palindromes in binary order-five de Bruijn cycles.

Standard-library-only. Run as: python checker.py
All periods, rotations, and palindromes are computed directly from the definitions.
"""
from collections import Counter
from pathlib import Path

ORDER = 5
N = 1 << ORDER
V = 1 << (ORDER - 1)
MASK = V - 1
EXPECTED_TOTAL = {22: 32, 23: 32, 24: 200, 27: 192, 28: 920, 29: 544, 30: 128}
EXPECTED_LONGEST = {7: 200, 8: 192, 9: 856, 10: 128, 11: 392, 12: 32, 13: 200, 15: 48}
EXPECTED_JOINT = {
 (22,7):32, (23,7):32, (24,7):104, (24,9):96,
 (27,8):96, (27,9):80, (27,11):16,
 (28,7):32, (28,8):96, (28,9):528, (28,10):64,
 (28,11):88, (28,12):32, (28,13):48, (28,15):32,
 (29,9):144, (29,10):64, (29,11):240, (29,13):80, (29,15):16,
 (30,9):8, (30,11):48, (30,13):72,
}


def canonical(word):
    """Start at the unique cyclic 00000 window."""
    assert len(word) == N and set(word) <= set('01')
    twice = word + word
    shifts = [i for i in range(N) if twice[i:i+ORDER] == '0'*ORDER]
    assert len(shifts) == 1
    i = shifts[0]
    return twice[i:i+N]


def rooted_euler_cycles():
    """Enumerate all edge-simple directed closed tours, fixing edge 00000 first."""
    bits = ['0']
    seen = 1
    def visit(v, used):
        if len(bits) == N:
            if v == 0:
                yield canonical(''.join(bits))
            return
        for bit in range(2):
            edge = v*2 + bit
            if (used >> edge) & 1:
                continue
            bits.append(str(bit))
            yield from visit(((v << 1) | bit) & MASK, used | (1 << edge))
            bits.pop()
    yield from visit(0, seen)


def ordered_hierholzer_cycles():
    """Independent enumeration using all 2^16 local outgoing-edge orders."""
    for choices in range(1 << V):
        visited = 0
        reverse_edges = []
        def walk(vertex):
            nonlocal visited
            options = (0,1) if (choices >> vertex) & 1 == 0 else (1,0)
            for bit in options:
                edge = vertex*2 + bit
                if (visited >> edge) & 1:
                    continue
                visited |= 1 << edge
                walk(((vertex << 1) | bit) & MASK)
                reverse_edges.append(str(bit))
        walk(0)
        assert visited == (1 << N) - 1
        yield canonical(''.join(reversed(reverse_edges)))


def palindromes_via_windows(word):
    double = word + word
    return {double[i:i+length] for i in range(N)
            for length in range(1,N+1)
            if double[i:i+length] == double[i:i+length][::-1]}


def palindromes_via_centers(word):
    """Independently enumerate odd/even palindromes by outward expansion."""
    data = word * 3
    result = set()
    for start in range(N):
        center = N + start
        for left, right in ((center, center), (center, center+1)):
            while right - left + 1 <= N and data[left] == data[right]:
                result.add(data[left:right+1])
                left -= 1
                right += 1
    return result


def spectrum(pals):
    hist = Counter(map(len, pals))
    return (len(pals), max(map(len,pals)),
            tuple(hist.get(i,0) for i in range(1,N+1)))


def verify():
    by_paths = list(rooted_euler_cycles())
    assert len(by_paths) == len(set(by_paths)) == 2048
    assert set(by_paths) == set(ordered_hierholzer_cycles())
    joint = Counter(); total = Counter(); longest = Counter(); profiles = Counter()
    rows = []
    for word in sorted(by_paths):
        substrings = { (word+word)[i:i+ORDER] for i in range(N) }
        assert len(substrings) == N == (1 << ORDER)
        assert len({word[i:] + word[:i] for i in range(N)}) == N
        first = palindromes_via_windows(word)
        assert first == palindromes_via_centers(word)
        size, maximum, prof = spectrum(first)
        assert prof[:ORDER] == (2,2,4,4,8)
        total[size] += 1
        longest[maximum] += 1
        joint[size,maximum] += 1
        profiles[prof] += 1
        rows.append((word,size,maximum,prof))
    assert dict(total) == EXPECTED_TOTAL
    assert dict(longest) == EXPECTED_LONGEST
    assert dict(joint) == EXPECTED_JOINT
    assert len(profiles) == 51 and sum(profiles.values()) == 2048
    assert max(maximum for _,_,maximum,_ in rows) == 15
    assert min(size for _,size,_,_ in rows) == 22
    loc = Path(__file__).resolve().parent
    expected_joint = ['total\tlongest\tcycles'] + [f'{s}\t{l}\t{num}' for (s,l),num in sorted(joint.items())]
    assert (loc/'joint_spectrum.tsv').read_text('utf-8').splitlines() == expected_joint
    expected_profiles = ['profile_lengths_1_to_32\tcycles'] + [','.join(map(str,p))+'\t'+str(num) for p,num in sorted(profiles.items())]
    assert (loc/'lengthwise_profiles.tsv').read_text('utf-8').splitlines() == expected_profiles
    expected_full = ['cycle_bits\ttotal_distinct\tlongest\tprofile_lengths_1_to_32'] + [w+'\t'+str(s)+'\t'+str(l)+'\t'+','.join(map(str,p)) for w,s,l,p in rows]
    assert (loc/'full_census.tsv').read_text('utf-8').splitlines() == expected_full
    print('PASS: 2048 primitive de Bruijn cycles; 2 generators agree; 2 palindrome tests agree; 23 joint classes; 51 lengthwise profiles')
    print('totals', sorted(total.items()))
    print('longest', sorted(longest.items()))

if __name__ == '__main__':
    verify()
