#!/usr/bin/env python3
"""Exact self-contained checks for short binary two-burst deletion codes."""
from itertools import product, combinations


def ball(w):
    n = len(w)
    assert n >= 4
    return frozenset(w[:i] + w[i + 2:j] + w[j + 2:]
                     for i in range(n - 3) for j in range(i + 2, n - 1))


def binary_words(n):
    return [''.join(z) for z in product('01', repeat=n)]


def hit(n):
    if n == 7:
        return frozenset(w for w in binary_words(3) if w[0] == w[2])
    if n == 8:
        return frozenset(w for w in binary_words(4) if w[0] == w[2] and w[1] == w[3])
    if n == 9:
        return frozenset(w for w in binary_words(5) if w[0] == w[2] == w[4])
    return frozenset(binary_words(n - 4))


def periodic(n):
    return {''.join(z[i % 2] for i in range(n)) for z in product('01',repeat=2)}


def check_code(c,n):
    assert len(c) == len(set(c))
    assert all(len(w) == n and set(w) <= {'0','1'} for w in c)
    balls = [ball(w) for w in c]
    for i,j in combinations(range(len(c)),2):
        assert not balls[i] & balls[j], (n, c[i], c[j], balls[i]&balls[j])


def c9():
    gs = ('100000111', '010101010', '001010010')
    return {''.join(str((sum(int(gs[j][i])*((mask>>j)&1) for j in range(3)))%2)
                    for i in range(9)) for mask in range(8)}


def main():
    # Exhaustive cover certificates: these prove the upper bounds because
    # deletion balls of a correcting code must be pairwise disjoint.
    for n in range(5,10):
        H = hit(n)
        expected = {5:2, 6:4, 7:4, 8:4, 9:8}[n]
        assert len(H) == expected
        assert all(ball(x)&H for x in binary_words(n)), n

    check_code({'00000','11111'},5)
    for n in (6,7,8):
        c = periodic(n)
        assert len(c)==4
        check_code(c,n)
        assert all(len(ball(w))>=1 for w in c)
    code = c9()
    assert len(code)==8
    check_code(code,9)
    balls9 = [ball(w) for w in sorted(code)]
    assert frozenset().union(*balls9) == frozenset(binary_words(5))
    assert sorted(map(len,balls9)) == [1,1,1,1,7,7,7,7]
    assert code == {
        '000000000', '100000111', '010101010', '110101101',
        '001010010', '101010101', '011111000', '111111111'
    }

    # Exhaustive verification of the six length-eight symmetry representatives.
    table = [
        ('00011011',4,7,'0000'), ('00011110',4,6,'0000'),
        ('00101101',2,4,'0101'), ('00110110',2,7,'0101'),
        ('00111001',1,6,'1111'), ('01001110',4,7,'0101'),
    ]
    universe=set(binary_words(8))
    cases={''.join(blocks) for blocks in __import__('itertools').permutations(('00','01','10','11'))}
    covered=set()
    for w,i,j,y in table:
        assert w in cases
        assert j>=i+2
        output=w[:i-1]+w[i+1:j-1]+w[j+1:]
        assert output==y,(w,i,j,output,y)
        for q in (w, w[::-1]):
            for z in (q, ''.join('1' if c=='0' else '0' for c in q)):
                covered.add(z)
    assert covered == cases, (len(covered),len(cases), cases-covered)
    for n in range(5,10):
        print('n=%d upper=%d achieved=%d' % (n,len(hit(n)), (2 if n==5 else (8 if n==9 else 4))))
    print('n9 linear code: ' + ' '.join(sorted(code)))
    print('VERIFY_OK')

if __name__=='__main__': main()
