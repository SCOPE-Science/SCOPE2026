"""Independent exact-arithmetic checks for a three-component reshuffling model.

Run: python3 verify.py
This is a finite supplementary verification, not a substitute for the proof.
"""
from fractions import Fraction as F
from itertools import permutations

C = (-1, 0, 1)

def geometry(q):
    assert 0 < q < 1
    r = q**3
    a = (1-q)**2*(1+q)/(1-r)
    digits = sorted({q*q*c[0]+q*c[1]+c[2] for c in permutations(C)})
    offsets = [(1-q)*z for z in digits]
    expected = [(1-q)**2*d for d in (-1-q, -1, -q, q, 1, 1+q)]
    assert offsets == expected
    gaps = [(offsets[i+1]-offsets[i])/(1-q)**2 for i in range(5)]
    assert gaps == [q, 1-q, 2*q, 1-q, q]
    assert a == max(abs(x)/(1-r) for x in offsets)
    T = 2*r*(1+q)/(1-r)
    separated = min(gaps) > T
    full = max(gaps) <= T
    return r, a, T, separated, full

def main():
    cases = [F(1,10),F(1,4),F(1,2),F(51,100),F(3,5),F(2,3),F(3,4),F(9,10)]
    for q in cases:
        r,a,T,sep,full = geometry(q)
        root_sep_poly = 1-q-3*q**3-q**4
        root_full_poly = 1-q*q-2*q**3
        assert sep == (root_sep_poly > 0)
        assert full == (root_full_poly <= 0)
        digit_variance = F(2,3)*(1+q+q*q)
        offsets = [(1-q)**2*d for d in (-1-q,-1,-q,q,1,1+q)]
        assert sum(offsets) == 0
        assert sum(v*v for v in offsets)/6 == (1-q)**4*digit_variance
        stationary_variance = sum(v*v for v in offsets)/6/(1-r*r)
        assert stationary_variance == 2*(1-q)**3/(3*(1+q**3))
        # The exact k-epoch second moment follows a geometric recursion.
        for k in range(1,8):
            s = sum((r*r)**j for j in range(k)) * sum(v*v for v in offsets)/6
            assert s == stationary_variance*(1-r**(2*k))
        print(f'q={q}: separated={sep}, full_interval={full}, variance={stationary_variance}')
    p = lambda q: 1-q-3*q**3-q**4
    h = lambda q: 1-q*q-2*q**3
    assert p(F(516,1000))>0>p(F(517,1000))
    assert h(F(657,1000))>0>h(F(658,1000))
    # Derivatives p'=-1-9q^2-4q^3 and h'=-2q-6q^2 are negative on (0,1).
    assert p(F(1,2))>0>p(F(2,3))
    assert h(F(1,2))>0>h(F(3,4))
    print('PASS: eight rational systems, 48 exact permutations, 56 finite-time moment identities, and root brackets')

if __name__=='__main__':
    main()
