"""Exact, self-contained checks for binary one-gap three-deck collision classification.

Run: python3 CHECK.py
No third-party modules are needed.
"""
from itertools import combinations, product
from collections import defaultdict, Counter

K = 3
PAIRS = (
    ('0010000101000', '0001010000100'),
    ('0110101111010', '0101111010110'),
    ('1010000101001', '1001010000101'),
    ('1110101111011', '1101111010111'),
)

def direct(word, k=K):
    n = len(word)
    out = [0] * sum(2 ** j for j in range(1, k + 1))
    for j in range(1, k + 1):
        for chosen in combinations(range(n), j):
            if any(b - a < 2 for a,b in zip(chosen, chosen[1:])):
                continue
            code = 0
            for t in chosen:
                code = (code << 1) | int(word[t])
            out[(2**j - 2) + code] += 1
    return tuple(out)

def recurrence(word, k=K):
    # ending_counts[i][length][pattern] for selections ending at i.
    # A new final letter can be appended only to selections ending at most i-2.
    total_by_length = [[0]*(1<<j) for j in range(k+1)]
    ending_counts = []
    for i, symbol in enumerate(word):
        b = int(symbol)
        end = [[0]*(1<<j) for j in range(k+1)]
        end[1][b] = 1
        for j in range(2,k+1):
            if i >= 2:
                for code,num in enumerate(sum_ends(ending_counts[:i-1],j-1)):
                    end[j][(code<<1)|b] += num
        ending_counts.append(end)
        for j in range(1,k+1):
            for code,num in enumerate(end[j]):
                total_by_length[j][code] += num
    return tuple(x for j in range(1,k+1) for x in total_by_length[j])

def sum_ends(states,j):
    counts=[0]*(1<<j)
    for end in states:
        for code,n in enumerate(end[j]):
            counts[code]+=n
    return counts

def flip(s):return ''.join('1' if c=='0' else '0' for c in s)

def reps(n):return (format(m,'0%db'%n) for m in range(1<<n))

def test():
    assert all(len(a)==len(b)==13 and a!=b for a,b in PAIRS)
    for n in range(1,14):
        deck_classes=defaultdict(list)
        for w in reps(n):
            sig = recurrence(w)
            deck_classes[sig].append(w)
            if n in (1,2,3,8,12,13):
                assert sig == direct(w), (n,w)
        nontrivial=sorted(tuple(group) for group in deck_classes.values() if len(group)>1)
        if 5 <= n < 13:
            assert len(nontrivial)==0, (n,nontrivial[:4])
        if n == 13:
            assert nontrivial == sorted(tuple(sorted(p)) for p in PAIRS), nontrivial
            assert len(deck_classes)==8188
            assert Counter(map(len,deck_classes.values()))=={1:8184,2:4}
        print('length',n,'classes',len(deck_classes),'nontrivial',len(nontrivial),flush=True)
    # Strong puncture tests plus explicit finding that stronger three-deck
    # hypotheses on punctures do NOT hold.
    for a,b in PAIRS:
        assert a[::-1]==b
        assert direct(a,3)==direct(b,3)
        for puncture in (lambda s:s[1:],lambda s:s[:-1],lambda s:s[1:-1]):
            assert direct(puncture(a),2)==direct(puncture(b),2)
            assert direct(puncture(a),3)!=direct(puncture(b),3)
    # Test a cross-section of arbitrary two-sided contexts; general proof is combinatorial.
    contexts=('','0','1','00','11','01','10','001','1010','001101')
    for a,b in PAIRS:
        for left,right in product(contexts,repeat=2):
            assert recurrence(left+a+right) == recurrence(left+b+right)
    # Concatenation in an unrestricted context produces exponentially many
    # distinct words with the same complete gapped deck.
    base_a,base_b=PAIRS[3]
    for m in (1,2,3):
        words=[''.join(blocks) for blocks in product((base_a,base_b), repeat=m)]
        assert len(set(words)) == 2**m
        assert len({recurrence(w) for w in words}) == 1
    # Codebooks contain all singleton deck classes, plus one from each doubleton.
    # Under reversal and complement, each 4-choice maximum codebook maps to another.
    singleton = set(reps(13)) - {w for pair in PAIRS for w in pair}
    assert len(singleton)==8184
    sym = [lambda s:s, lambda s:s[::-1], flip, lambda s:flip(s[::-1])]
    assert all({f(w) for w in singleton}==singleton for f in sym)
    lookup={w:(i,j) for i,pair in enumerate(PAIRS) for j,w in enumerate(pair)}
    def transform_mask(mask,f):
        result=0
        for i,pair in enumerate(PAIRS):
            source=pair[(mask>>i)&1]
            ni,nj=lookup[f(source)]
            result|=(nj<<ni)
        return result
    all_masks=set(range(16))
    orbits=set()
    while all_masks:
        m=min(all_masks)
        orbit=frozenset(transform_mask(m,f) for f in sym)
        orbits.add(orbit)
        all_masks-=orbit
    fixed=[sum(transform_mask(mask,f)==mask for mask in range(16)) for f in sym]
    assert fixed == [16,0,4,4], fixed
    assert len(orbits)==6
    print('GAPPED_THREE_DECK_PASS words=8192 classes=8188 doubletons=4 codebooks=16 orbits=6',flush=True)

if __name__=='__main__':test()
