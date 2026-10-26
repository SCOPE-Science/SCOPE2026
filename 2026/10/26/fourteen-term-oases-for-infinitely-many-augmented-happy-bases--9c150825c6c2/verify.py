#!/usr/bin/env python3
"""Independent integer checks for augmented-happy 14-oases.
Run with Python 3, no third-party dependencies.
The infinite argument is given in RESULT.md, not inferred from finite scans.
"""

from math import isqrt


def digit_defect(b, h, j, k):
    assert 0 <= h < b and 0 <= j < b and 0 <= k < b
    return h * (b * b - h) + j * (b - j) + k * (1 - k)


def finite_maximum(b):
    # Exhaustive over every three-digit or shorter positive integer 1<=r<b^3.
    # All higher-digit oasis runs are bounded by this mirage spectrum:
    # see Swart et al. (2019), Theorem 10.
    values = set()
    for r in range(1, b ** 3):
        q, k = divmod(r, b)
        h, j = divmod(q, b)
        values.add(r - h * h - j * j - k * k)
    vmax = sorted(values)
    longest, last, first, starts = 0, None, None, []
    for z in vmax:
        if last is None or z != last + 1:
            first = z
            runlen = 0
        runlen = z - first + 1
        if runlen > longest:
            longest, starts = runlen, [first]
        elif runlen == longest:
            starts.append(first)
        last = z
    assert longest >= 1
    pos = [z for z in starts if z >= 0]
    # A positive (or nonnegative) extremal run is a true oasis. The paper
    # bounds any longer oasis by the longest mirage.
    assert pos
    return longest, min(pos)


def pell_q(u, t):
    return 2*t*t - (10*u + 5)*t - 2*u*u - 28*u + 22


def step(u, t):
    return (13741001*u + 71351280*t + 179115300,
            71351280*u + 370497401*t + 930070960)


def fourteen_witnesses(u, t):
    assert u >= 1 and u % 2 == 1 and t >= 8 and t % 4 == 0
    assert pell_q(u, t) == 0
    m_num = 5*t + 2*u + 14
    assert m_num % 4 == 0
    m = m_num // 4
    b = 2*m
    x = 11
    C = digit_defect(b, x, m, 0)
    assert C == x*b*b - x*x + m*m
    assert C >= 13 and b >= 28
    # q = s*s + z*(z-1) for 0<=s<=3 and z in {0,2,3,4}.
    found = {}
    for s in range(4):
        for z in (0, 2, 3, 4):
            q = s*s + z*(z-1)
            if 0 <= q <= 13:
                found[q] = (x, m-s, z)
    assert set(found) == set(range(14)) - {5, 8}
    found[5] = (x+1, m-t, b-u)
    found[8] = (x+1, m-t-5, b-u-2)
    for q, (h, j, k) in sorted(found.items()):
        assert 0 < h < b and 0 <= j < b and 0 <= k < b
        assert digit_defect(b, h, j, k) == C-q, (u,t,q)
    return b, C, found


def main():
    expected = {2:2,4:6,6:5,8:8,10:8,12:8,14:8,16:8,18:8,
                20:9,22:11,24:9,26:11,28:14}
    observed = {b:finite_maximum(b) for b in expected}
    assert {b:v[0] for b,v in observed.items()} == expected
    assert observed[28] == (14, 8686), observed[28]
    u,t = 1,8
    for n in range(4):
        b,C,w = fourteen_witnesses(u,t)
        print('Pell index',n,'base',b,'oasis start',C-13,
              'oasis length',len(w))
        U,V = 58*u+81, 4*t-10*u-5
        assert U*U - 29*V*V == 10940
        un,tn = step(u,t)
        Un,Vn = 58*un+81, 4*tn-10*un-5
        a,k = 192119201,35675640
        assert a*a-29*k*k == 1
        assert (Un,Vn) == (a*U + 29*k*V, k*U+a*V)
        assert un > u and tn > t
        u,t=un,tn
    print('finite exact oasis maxima:',{b:v[0] for b,v in observed.items()})
    print('VERIFIED: 14-oasis witnesses, Pell recurrence and all three-digit spectra for bases 2..28')


if __name__ == '__main__':
    main()
