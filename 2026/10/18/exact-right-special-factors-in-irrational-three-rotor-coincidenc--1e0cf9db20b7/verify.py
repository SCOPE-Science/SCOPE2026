#!/usr/bin/env python3
"""Finite arithmetic cross-checks of a rotor cutting-word theorem.

The universal statement is proved analytically in RESULT.md; bounded
checks here serve only to detect indexing, coding, or enumeration mistakes.
Uses Python's integer square root, no floating-point arithmetic.
"""
from math import isqrt


def floor_alpha(j, d):
    """floor(j / (1 + sqrt(d))) for nonsquare positive integer d>1."""
    assert j >= 0 and d > 1 and isqrt(d)**2 != d
    return (isqrt(d*j*j) - j) // (d-1)


def algebraic_cutting_word(d, count):
    a = [floor_alpha(j, d) for j in range(count+2)]
    return ''.join('3' if a[j+2]-a[j+1] else '1' for j in range(count))


def geometry_cutting_word(d, count):
    """Independently merge horizontal and vertical crossings of y=sqrt(d)x."""
    h = 1  # next horizontal y=h, at time x=h/sqrt(d)
    v = 1  # next vertical x=v, at time x=v
    word = []
    for _ in range(count):
        if h*h < d*v*v:
            word.append('1')
            h += 1
        else:
            word.append('3')
            v += 1
    return ''.join(word)


def exact_factor_right_extensions(word, length):
    rights = {}
    for k in range(len(word)-length):
        key = word[k:k+length]
        if key not in rights:
            rights[key] = set()
        rights[key].add(word[k+length])
    return rights


def run():
    checks = 0
    for d in (2,3,5,6,7,10,11):
        b = algebraic_cutting_word(d, 12000)
        assert b[:3200] == geometry_cutting_word(d, 3200)
        checks += 3200
        rotor = '0' + ''.join('2' + z for z in b)
        for n in range(1,81):
            ext = exact_factor_right_extensions(rotor,n)
            expected = rotor[1:n+1][::-1]
            special = {w: e for w, e in ext.items() if len(e)>1}
            assert special == {expected: {'1','3'}}, (d,n,special,expected)
            assert len(ext) == n+3, (d,n,len(ext))
            assert all(len(e)==1 for w,e in ext.items() if w!=expected)
            checks += 3
    print('VERIFY_OK: 7 exact quadratic slopes; independent crossing merger;'
          ' all right-special factors and complexities through n=80;'
          ' %d checks' % checks)


if __name__ == '__main__':
    run()
