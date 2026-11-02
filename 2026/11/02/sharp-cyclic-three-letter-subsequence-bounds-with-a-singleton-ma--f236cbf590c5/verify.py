"""Exhaustive finite corroboration of sharp singleton-marker cyclic subsequence bounds.
Run with Python 3: python circular_parikh_checker.py
"""
from itertools import combinations


def literal_triples(s):
    # Count increasing-position subsequences spelling abc.
    a = ab = abc = 0
    for ch in s:
        if ch == 'a':
            a += 1
        elif ch == 'b':
            ab += a
        elif ch == 'c':
            abc += ab
        else:
            raise AssertionError(ch)
    return abc


def orbit_total(s):
    return sum(literal_triples(s[i:] + s[:i]) for i in range(len(s)))


def gap_total(v):
    return sum((i + 1) * v[i + 1:].count('b')
               for i, ch in enumerate(v) if ch == 'a')


def proposed_max(a, b):
    return max(a * (b - t) * (2 * t + a + 1) // 2
               for t in range(b + 1))


def optimal_strings(a, b):
    M = proposed_max(a, b)
    return {'b' * t + 'a' * a + 'b' * (b-t) for t in range(b + 1)
            if a * (b-t) * (2*t + a + 1) == 2*M}


def minimum_positive_words(a,b):
    return {'a' + 'b'*b + 'a'*(a-1),
            'b'*(b-1) + 'a' + 'b' + 'a'*(a-1)}


def main():
    nprofiles = total_necklaces = total_rotations = 0
    for a in range(1,8):
        for b in range(1,8):
            nprofiles += 1
            n=a+b
            spectrum={}
            for zeropos in combinations(range(n),a):
                zz=set(zeropos)
                v=''.join('a' if i in zz else 'b' for i in range(n))
                s='c'+v
                actual=orbit_total(s)
                asserted=gap_total(v)
                assert actual == asserted,(a,b,v,actual,asserted)
                spectrum.setdefault(actual,set()).add(v)
                total_necklaces+=1
                total_rotations+=len(s)
            M=proposed_max(a,b)
            assert max(spectrum)==M,(a,b,'maximum',max(spectrum),M)
            assert spectrum[M]==optimal_strings(a,b),(a,b,'maxima')
            assert spectrum[0]=={'b'*b+'a'*a},(a,b,'zero')
            assert min(x for x in spectrum if x>0)==b,(a,b,'min_positive')
            assert spectrum[b]==minimum_positive_words(a,b),(a,b,'minimizers')
            assert set(range(1,b)).isdisjoint(spectrum),(a,b,'gap')
    print('VERIFY_OK profiles=%d circular_classes=%d literal_rotations=%d maxima_and_all_extremizers=True positive_gap=True' %
          (nprofiles,total_necklaces,total_rotations))

if __name__=='__main__':
    main()
