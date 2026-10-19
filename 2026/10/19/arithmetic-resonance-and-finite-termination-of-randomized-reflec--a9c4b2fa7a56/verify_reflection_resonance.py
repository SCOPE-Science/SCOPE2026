"""Exact checks for the two-line randomized reflection-bundle theorem.

Usage: python verify_reflection_resonance.py
Dependency: sympy==1.14.0 (Python 3.10+).
The infinite claims follow from the proof, not from these finite checks.
"""
from itertools import product
from math import comb
from fractions import Fraction
import sympy as sp


def inverse_rational_matrix(a):
    """Exact Gauss-Jordan inversion using Fraction, for small rational matrices."""
    n = len(a)
    t = [[Fraction(a[i][j]) for j in range(n)] +
         [Fraction(int(i == j)) for j in range(n)] for i in range(n)]
    for i in range(n):
        k = next(k for k in range(i, n) if t[k][i])
        t[i], t[k] = t[k], t[i]
        v = t[i][i]
        t[i] = [u / v for u in t[i]]
        for j in range(n):
            if j != i:
                v = t[j][i]
                t[j] = [t[j][l] - v*t[i][l] for l in range(2*n)]
    return [row[n:] for row in t]


def expectation_orthogonal_pair(r, numerator, denominator):
    """Expected index of first orthogonal consecutive sampled lines, odd r."""
    assert r % 2 == 1 and 0 < 2*numerator < denominator
    q = r // 2
    ss = list(range(-q, q+2))
    probabilities = [Fraction(comb(r, q+s), 2**r) for s in ss]
    killed = lambda a,b: (2*numerator*(a-b)) % (2*denominator) == denominator
    # Check: (a-b)*theta = (2j+1)*pi/2, theta=(numerator/denominator)*pi.
    Q = [[Fraction(0) if killed(a,b) else probabilities[j]
          for j,b in enumerate(ss)] for a in ss]
    inv = inverse_rational_matrix([[Fraction(int(i == j)) - Q[i][j]
                                    for j in range(len(ss))] for i in range(len(ss))])
    h = [sum(row) for row in inv]
    E = Fraction(1) + sum(p*hh for p,hh in zip(probabilities,h))
    return ss, probabilities, h, E


def direct_matrix_checks(r, theta):
    """Compare every word with exact reflection-rotation identities."""
    R0 = sp.diag(1,-1)
    R1 = sp.Matrix([[sp.cos(2*theta),sp.sin(2*theta)],
                    [sp.sin(2*theta),-sp.cos(2*theta)]])
    R = [R0,R1]
    I = sp.eye(2)
    q = r//2
    counts = {s:0 for s in (range(-q,q+2) if r%2 else range(-q,q+1))}
    zero_words = 0
    for word in product((0,1),repeat=r):
        S = sum((1 if (r-1-j)%2==0 else -1)*digit
                for j,digit in enumerate(word))
        counts[S]+=1
        M=I
        for digit in word:
            M=R[digit]*M
        if r%2:
            target=sp.Matrix([[sp.cos(2*S*theta),sp.sin(2*S*theta)],
                              [sp.sin(2*S*theta),-sp.cos(2*S*theta)]])
        else:
            target=sp.Matrix([[sp.cos(2*S*theta),-sp.sin(2*S*theta)],
                              [sp.sin(2*S*theta),sp.cos(2*S*theta)]])
        assert all(sp.simplify(x)==0 for x in M-target)
        T=(I+M)/2
        if all(sp.simplify(x)==0 for x in T):
            zero_words+=1
        if r%2:
            assert sp.simplify(T.det())==0
            assert sp.simplify(T.trace()-1)==0
    for s,c in counts.items():
        assert c==comb(r,q+s)
    return len(tuple(product((0,1),repeat=r))),zero_words


def main():
    tested=0
    for theta in (sp.pi/4,sp.pi/6):
        for r in range(1,8):
            n,k=direct_matrix_checks(r,theta)
            tested+=n
            print(f'theta={theta}, r={r}, words={n}, one-block-zero={k}')
    states,p,h,E=expectation_orthogonal_pair(3,1,4)
    assert states==[-1,0,1,2]
    assert p==[Fraction(1,8),Fraction(3,8),Fraction(3,8),Fraction(1,8)]
    assert h==[Fraction(40,9),Fraction(56,9),Fraction(56,9),Fraction(40,9)]
    assert E==Fraction(61,9)
    print('pi/4, r=3: first perpendicular pair expected index =', E)
    _,_,h,E=expectation_orthogonal_pair(3,1,6)
    assert h==[Fraction(32),Fraction(36),Fraction(36),Fraction(32)]
    assert E==36
    print('pi/6, r=3: first perpendicular pair expected index =',E)
    # Even r=4, theta=pi/4: only S=+/-2 kills; probability 2/16.
    assert Fraction(comb(4,0)+comb(4,4),16)==Fraction(1,8)
    print('pi/4, r=4: geometric one-block success = 1/8, mean = 8')
    print('PASS: exact word/matrix comparisons =',tested)

if __name__=='__main__':
    main()
