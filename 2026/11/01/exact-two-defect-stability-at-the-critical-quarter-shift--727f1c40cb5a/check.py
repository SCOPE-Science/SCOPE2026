"""Finite diagnostics for periodic two-defect shifted-sinc bounds.

Run: python check.py
Requires: numpy.
The analytic argument covers all periods; this script is supplementary.
"""
import math
import numpy as np


def eta(period, separation):
    p, l = period, separation
    assert p >= 3 and 1 <= l < p
    g = math.pi / (2 * p)
    beta = math.pi * l / p
    d = 1 / (p * math.sin(g))
    b = 1 / (p * math.sin(beta - g))
    c = 1 / (p * math.sin(beta + g))
    return (math.sqrt(4*d*d + (b+c)**2) - abs(b-c))/2


def lower(period, separation):
    x = eta(period, separation)
    return 1 - math.sqrt(max(0, 1-x*x))


def matrix_lower(period, separation):
    p = period
    r = np.arange(p)[:, None]
    col = np.arange(p)[None, :]
    signs = np.ones(p)
    signs[0] = signs[separation] = -1
    H = np.exp(-2j * np.pi * r * (col + signs / 4)/p)/math.sqrt(p)
    return float(np.linalg.eigvalsh(H.conj().T @ H)[0])


def run():
    n = 0
    for p in range(3, 26):
        observed = []
        for l in range(1, p):
            a = lower(p, l)
            direct = matrix_lower(p, l)
            assert abs(a-direct) < 5e-12, (p,l,a,direct)
            assert a >= lower(p, 1)-2e-13, (p,l,a)
            observed.append(a)
            n += 2
        assert abs(min(observed)-lower(p,1)) < 1e-12
        n += 1
    for p in [30,40,60,80,120]:
        for l in sorted(set([1,2,3,p//4,p//2,p-3,p-2,p-1])):
            x=lower(p,l)
            assert abs(x-matrix_lower(p,l)) < 2e-11
            n += 1
    last=float('inf')
    for p in range(3, 250):
        x=lower(p,1)
        assert x < last + 1e-14
        last=x
        n += 1
    s=2*(math.sqrt(13)-1)/(3*math.pi)
    infimum=1-math.sqrt(1-s*s)
    assert last > infimum and abs(last-infimum)<1e-5
    n+=1
    print('PASS finite assertions:',n)
    print('limiting eta:',format(s,'.15f'))
    print('infimum squared lower bound:',format(infimum,'.15f'))
    print('period 4 exact lower:',format(lower(4,1),'.15f'))

if __name__=='__main__':run()
