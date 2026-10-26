"""Finite independent checks for three-marker unbordered-rotation classification."""
from math import comb
from collections import Counter

def is_unbordered(word):
    return not any(word[:j] == word[-j:] for j in range(1, len(word)))

def circular_word(a, b, c):
    return '1' + '0'*a + '1' + '0'*b + '1' + '0'*c

def brute_cyclic_count(w):
    rotations = {w[i:] + w[:i] for i in range(len(w))}
    return sum(map(is_unbordered, rotations))

def theoretical(a, b, c):
    return int(a != b) + int(b != c) + int(c != a)

def necklace_counts(m):
    delta = int(m % 3 == 0)
    p = m//2 + 1
    B = comb(m+2, 2)
    return {0: delta, 2: p-delta, 3: (B - 3*p + 2*delta)//3}

def test():
    checked = 0
    for m in range(0, 31):
        for a in range(m+1):
            for b in range(m-a+1):
                c = m-a-b
                w = circular_word(a,b,c)
                assert brute_cyclic_count(w) == theoretical(a,b,c), (a,b,c)
                # Crucial nonstandard local lemmas checked as unbordered predicates.
                u = '1'+'0'*a+'1'+'0'*b+'1'+'0'*c
                v = '0'*a+'1'+'0'*b+'1'+'0'*c+'1'
                assert is_unbordered(u) == (c>a), (a,b,c,'first')
                if a>0:
                    assert is_unbordered(v) == (a>c), (a,b,c,'second')
                checked += 1
        # Independently enumerate necklaces by canonical rotation.
        if m <= 16:
            observed = Counter()
            for ones in __import__('itertools').combinations(range(m+3),3):
                s = ''.join('1' if j in ones else '0' for j in range(m+3))
                canonical = min(s[j:]+s[:j] for j in range(m+3))
                observed[canonical] = brute_cyclic_count(s)
            hist = Counter(observed.values())
            assert dict(hist) == {k:v for k,v in necklace_counts(m).items() if v}, (m,hist,necklace_counts(m))
        assert sum(necklace_counts(m).values()) == (comb(m+2,2)+2*int(m%3==0))//3
        # Independent labeled-word count from orbit-stabilizer and orbit sizes.
        z = necklace_counts(m)
        assert (m+3)*z[2]+(m+3)*z[3]+((m+3)//3)*z[0] == comb(m+3,3) if m%3==0 else (m+3)*(z[2]+z[3])==comb(m+3,3)
    # The adjacent-gap criterion cannot naively extend to four ones.
    four='1100110'
    assert not is_unbordered(four) and four[0]=='1'
    print('PASS: triple-gap and boundary predicates in', checked, 'gap triples (m<=30)')
    print('PASS: independent cyclic-necklace histograms for m<=16')
    print('PASS: orbit counts and sharp four-marker limitation')
if __name__ == '__main__': test()
