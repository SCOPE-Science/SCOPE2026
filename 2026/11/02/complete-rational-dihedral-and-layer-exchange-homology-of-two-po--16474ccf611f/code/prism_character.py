"""Exact signed-cell, character and quotient checks for finite prism parameters."""
from prism_core import char

def test(n):
    def u(a,b):
        return sum(((-i if b else i)+a) % n == i for i in range(n)) - 1
    mult = 0
    for a in range(n):
        for b in (0,1):
            v = u(a,b)
            v2 = n-1 if b else u((2*a) % n, 0)
            mult += ((v*v - v2)//2) * (-1 if b else 1)
            for c in (0,1):
                t = char(n,a,b,c)
                expected_h1 = (-1)**(b+c) * (t[3]+t[4])
                expected_h2 = (v*v - v2)//2 - (-1)**b + (-1)**c
                assert t[-2] == expected_h1
                assert t[-1] == expected_h2
    assert mult == 2*n*((n-1)//2)
    d = [char(n,a,b,0) for a in range(n) for b in (0,1)]
    full = [char(n,a,b,c) for a in range(n) for b in (0,1) for c in (0,1)]
    cyc = [char(n,a,0,0) for a in range(n)]
    assert sum(t[-2] for t in d) == 0
    assert sum(t[-1] for t in d) == 2*n
    assert sum(t[-2] for t in full) == 0
    assert sum(t[-1] for t in full) == 0
    assert sum(t[-2] for t in cyc) == 3*n
    assert sum(t[-1] for t in cyc) == n*((n-1)//2)

if __name__ == '__main__':
    for n in range(5,19):
        test(n)
    print('PRISM_FULL_GROUP_CHARACTERS_OK_5_TO_18')
