#!/usr/bin/env python3
"""Reproduce finite factor and antidictionary checks for Thue--Morse words."""
from collections import Counter

def substitute(w):
    return ''.join('01' if c == '0' else '10' for c in w)

def factors(w):
    return {w[i:j] for i in range(len(w)) for j in range(i+1,len(w)+1)}

def minimal_absent_factors(w):
    fs = factors(w)
    result = set()
    for v in fs:
        for left in '01':
            z = left + v
            if z not in fs and z[:-1] in fs and z[1:] in fs:
                result.add(z)
    for c in '01':
        if c not in fs:
            result.add(c)
    return result

def predicted_spectrum(m):
    counts = Counter({3: 2, 2**(m-2) + 2: 5})
    for j in range(m-3):
        counts[3 * (2**j) + 2] += 4
    return counts

def check():
    w = '0'
    checked = []
    for m in range(10):
        if m >= 3:
            fs = factors(w)
            absent = minimal_absent_factors(w)
            spectrum = Counter(map(len, absent))
            assert spectrum == predicted_spectrum(m), (m, spectrum, predicted_spectrum(m))
            assert len(absent) == 4*m-5
            R = 2**(m-2)
            assert len({w[i:i+R+1] for i in range(len(w)-R)}) == 3*R
            assert len({w[i:i+R+2] for i in range(len(w)-R-1)}) == 3*R-1
            for z in absent:
                assert z not in fs and z[1:] in fs and z[:-1] in fs
            checked.append((m,len(w),len(absent),dict(sorted(spectrum.items()))))
        w = substitute(w)
    # Independently test context assertions for infinite-word approximants.
    w = '0'
    for _ in range(12):
        w = substitute(w)
    def contexts(v):
        return {w[i-1] + w[i+len(v)] for i in range(1,len(w)-len(v)) if w[i:i+len(v)] == v}
    for v in ['01','10','0110','1001','01101001','10010110']:
        assert contexts(v) == {'00','01','10','11'}, (v,contexts(v))
    for j in range(6):
        v='010'; u='101'
        for _ in range(j):
            v=substitute(v);u=substitute(u)
        expected = {'01','10'} if j%2 == 0 else {'00','11'}
        assert contexts(v) == expected and contexts(u) == expected,(j, contexts(v), contexts(u),expected)
    print('VERIFY_OK', checked)
if __name__ == '__main__':
    check()
