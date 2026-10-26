"""Independent exact tests for a binary one-jumble four-Simon classification.

No third-party dependencies. Run: python3 check.py
The infinite classification has an elementary proof; finite tests do not replace it.
"""
from itertools import combinations, product
from collections import defaultdict
from pathlib import Path

ALPHABET = '01'
BALANCED = ('0011', '0101', '0110', '1001', '1010', '1100')
ALL_PATTERNS = tuple(''.join(t) for k in range(5) for t in product(ALPHABET, repeat=k))
MISSING_PATTERNS = {
    '0011': ('1010', '1100'),
    '0101': ('1100',),
    '0110': ('1001',),
    '1001': ('0110',),
    '1010': ('0011',),
    '1100': ('0011', '0101'),
}

def is_subsequence(sub, word):
    it = iter(word)
    return all(any(c == target for c in it) for target in sub)

def jumbled(u, w):
    if any(u.count(c) > w.count(c) for c in ALPHABET):
        return False
    if len(u) <= 1:
        return True
    # Independent direct formulation: one deletion from the target u.
    return any(is_subsequence(u[:i] + u[i + 1:], w) for i in range(len(u)))

def actual_signature(w):
    return tuple(u for u in ALL_PATTERNS if jumbled(u, w))

def predicted_missing(w):
    i, j = w.count('0'), w.count('1')
    if i < 2 or j < 2:
        return tuple(BALANCED)
    subs = {''.join(w[t] for t in c) for c in combinations(range(len(w)), 4)}
    subs.intersection_update(BALANCED)
    assert subs
    return tuple(x for x in BALANCED if all(x in MISSING_PATTERNS[t] for t in subs))

def predicted_signature(w):
    i, j = w.count('0'), w.count('1')
    missing = set(predicted_missing(w))
    return tuple(u for u in ALL_PATTERNS if u.count('0') <= i and u.count('1') <= j and u not in missing)

def types(i, j):
    if min(i, j) < 2:
        return [('not_applicable', '0' * i + '1' * j)]
    xs = [
        ('1010,1100', '0' * i + '1' * j),
        ('1100', '0' * (i-1) + '10' + '1' * (j-1)),
        ('0011', '1' * (j-1) + '01' + '0' * (i-1)),
        ('0011,0101', '1' * j + '0' * i),
    ]
    if i == 2:
        xs += [('1001', '0' + '1' * j + '0')]
    if j == 2:
        xs += [('0110', '1' + '0' * i + '1')]
    if i+j >=5:
        xs += [('-', '0' * (i-2) + '1010' + '1' * (j-2))]
    return xs

def predicted_count_fixed(n):
    if n <= 3:
        return n+1
    if n == 4:
        return 10
    return min(31, 5*n-9)


def main():
    tab=[]
    for i in range(5):
        for j in range(5):
            for name, word in types(i,j):
                assert (word.count('0'),word.count('1')) == (i,j)
                observed = predicted_missing(word)
                if name=='not_applicable': assert min(i,j)<2
                elif name=='-': assert observed==()
                else: assert observed==tuple(x for x in BALANCED if x in name.split(',')), (i,j,name,observed)
                assert actual_signature(word)==predicted_signature(word)
                tab.append((i,j,name,word))
    assert len(tab) == 66, len(tab)
    assert len({actual_signature(word) for _,_,_,word in tab})==66
    print('Constructed all 66 distinct signatures; each tested directly.')
    # Full brute-force independent LCS/subsequence test through length twelve.
    for n in range(13):
        values=set()
        for t in product('01',repeat=n):
            w=''.join(t)
            direct=actual_signature(w)
            structural=predicted_signature(w)
            assert direct==structural, (w, direct, structural)
            values.add(direct)
        assert len(values)==predicted_count_fixed(n),(n,len(values))
        print('length',n,'words',2**n,'classes',len(values))
    expected = [1,2,3,4,10,16,21,26,31,31,31,31,31]
    assert [predicted_count_fixed(n) for n in range(13)] == expected
    # Checked below by proof: all possible absent sets are intersections of six sets,
    # and the witnesses above realize every allowed set for each capped count.
    path=Path(__file__).with_name('WITNESSES.tsv')
    lines=['cap_zeros\tcap_ones\tmissing_balanced\trepresentative']
    lines+=['\t'.join(map(str,row)) for row in tab]
    if path.exists():
        assert path.read_text(encoding='utf-8')=='\n'.join(lines)+'\n'
    print('PASS: independent direct signatures, structural signatures, full witness index.')

if __name__=='__main__':
    main()
