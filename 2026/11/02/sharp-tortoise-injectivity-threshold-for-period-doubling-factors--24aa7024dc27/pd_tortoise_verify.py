"""Exact finite core for the period-doubling tortoise classification.

The external mathematical argument proves that all length-10 factors occur
within the first 42 symbols, and that no later collisions are possible once
length-10 image injectivity is established. This program verifies the complete
finite core using integer arithmetic and independently checks substitution.
"""
from collections import defaultdict


def symbol(i):
    k = i + 1
    v = 0
    while k % 2 == 0:
        k //= 2
        v += 1
    return str(v % 2)


def tortoise(word):
    j = word.find('1')
    return word if j < 0 else word[:j] + word[j + 1:] + '1'


def run():
    d = ''.join(symbol(i) for i in range(42))
    s = '0'
    for _ in range(6):
        s = ''.join('01' if c == '0' else '00' for c in s)
    assert d == s[:42]
    assert len(d) == 42
    assert all('0000' not in d[i:i+4] for i in range(39))
    assert len({d[i:i+10] for i in range(33)}) == 16
    count, collisions = [], []
    for n in range(1, 11):
        factors = {d[i:i+n] for i in range(43-n)}
        classes = defaultdict(list)
        for w in sorted(factors):
            classes[tortoise(w)].append(w)
        count.append((len(factors), len(classes)))
        bad = {k: v for k, v in classes.items() if len(v) > 1}
        collisions.append(sum(len(v)-1 for v in classes.values()))
        if n == 9:
            assert bad == {'000010101': ['000101010', '010001010']}
        if n == 10:
            assert not bad
            assert len(classes) == 16
            print('The 16 complete length-10 factor / image pairs:')
            for w in sorted(factors):
                print(w, tortoise(w))
    assert count == [(2,2),(3,2),(5,3),(6,3),(8,5),(10,7),(11,9),(12,10),(14,13),(16,16)]
    print('PASS: all n=1,...,10 (factor count, tortoise count):', count)
    print('PASS: unique n=9 collision: 000101010 / 010001010')
    print('PASS: 16 distinct n=10 tortoise images')
    print('PASS: v2 and substitution prefix independently agree for 42 digits')
    # Farther-prefix tests are nonessential corroboration, not infinite proof.
    long = '0'
    for _ in range(12):
        long = ''.join('01' if a == '0' else '00' for a in long)
    for n in (10,11,12,16,24,32,64):
        ff = {long[i:i+n] for i in range(len(long)-n+1)}
        assert len(ff) == len({tortoise(w) for w in ff})
    print('PASS: auxiliary length checks at n=10,11,12,16,24,32,64')
    print('FINITE CORE CERTIFIED; all-n step is the separately stated prefix lemma.')


if __name__ == '__main__':
    run()
