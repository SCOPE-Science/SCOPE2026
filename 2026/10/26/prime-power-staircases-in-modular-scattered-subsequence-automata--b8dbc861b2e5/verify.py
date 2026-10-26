"""Independent finite checks for a prime-modular scattered-subsequence DFA.
Only the mathematical construction and reproducibility are encoded here.
"""
from itertools import product
from math import comb

def period(p, r):
    q = 1
    while q <= r:
        q *= p
    return q

def factored_count(word, r, p):
    # Directly accumulate the number of subsequence occurrences.
    zeros, count = 0, 0
    for letter in word:
        if letter == '0':
            zeros += 1
        else:
            count = (count + comb(zeros, r)) % p
    return count

def model(word, r, p):
    q = period(p, r)
    a, t = 0, 0
    for letter in word:
        if letter == '0':
            a = (a + 1) % q
        else:
            t = (t + comb(a, r)) % p
    return a, t

def quotient_count(p, r, residue):
    q = period(p, r)
    states = list(product(range(q), range(p)))
    # Independent partition refinement (not a stipulated formula for the result).
    def action(st, letter):
        a, t = st
        return ((a + 1) % q, t) if letter == 0 else (a, (t + comb(a, r)) % p)
    classes = [{s for s in states if s[1] == residue},
               {s for s in states if s[1] != residue}]
    classes = [c for c in classes if c]
    while True:
        cl = {st: index for index, block in enumerate(classes) for st in block}
        new = []
        for block in classes:
            buckets = {}
            for st in block:
                signature = (cl[action(st, 0)], cl[action(st, 1)])
                buckets.setdefault(signature, set()).add(st)
            new.extend(buckets.values())
        if len(new) == len(classes):
            return len(new)
        classes = new

def run():
    checked = 0
    tested_words = 0
    for p, rs in ((2, range(2, 19)), (3, range(2, 13)),
                  (5, range(2, 11)), (7, range(2, 9))):
        for r in rs:
            q = period(p, r)
            for residue in range(p):
                got = quotient_count(p, r, residue)
                assert got == p * q, (p, r, residue, got, p*q)
            checked += 1
            # Compare the DFA to a direct scattered-embedding count, not to
            # another minimization implementation.
            if r <= 8 and p <= 5:
                for n in range(0, 12):
                    for bits in product('01', repeat=n):
                        w = ''.join(bits)
                        a, t = model(w, r, p)
                        assert a == w.count('0') % q
                        assert t == factored_count(w, r, p), (p, r, w)
                        tested_words += 1
    # Critical Lucas-support obstruction for all tested parameters.
    for p, rs in ((2, range(2, 36)), (3, range(2, 24)),
                  (5, range(2, 16)), (7, range(2, 15))):
        for r in rs:
            q = period(p, r)
            seq = [comb(n, r) % p for n in range(q)]
            assert seq[r] == 1
            assert seq[r - q//p] == 0
            assert all(any((seq[j] != 0) != (seq[(j+d) % q] != 0)
                           for j in range(q)) for d in range(1,q))
    print('VERIFY_OK', 'minimal_automata', checked, 'direct_words', tested_words)
if __name__ == '__main__':
    run()
