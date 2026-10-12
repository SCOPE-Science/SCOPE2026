"""Finite corroboration for tree fidelity topology bounds. Not a universal proof."""
from fractions import Fraction
from itertools import product


def fidelity(degrees, q):
    result = Fraction(1, 1 << len(degrees))
    for d in degrees:
        result *= 1 + q**d
    return result


def star_degrees(n):
    return [n-1] + [1]*(n-1)


def path_degrees(n):
    return [1,1] + [2]*(n-2)


def from_prufer(n, word):
    ds = [1]*n
    for x in word:
        ds[x] += 1
    return ds

rates = [Fraction(3, 4), Fraction(1, 2), Fraction(0, 1), Fraction(-1, 5), Fraction(-1, 3)]
count = 0
for n in range(4,8):
    lower = path_degrees(n)
    upper = star_degrees(n)
    values = {q: (fidelity(lower,q),fidelity(upper,q)) for q in rates}
    for word in product(range(n), repeat=n-2):
        deg = from_prufer(n,word)
        count += 1
        for q in rates:
            val = fidelity(deg,q)
            fp,fs = values[q]
            if q > 0:
                assert fp <= val <= fs
                assert (val == fs) == (sorted(deg)==sorted(upper))
                assert (val == fp) == (sorted(deg)==sorted(lower))
            elif q < 0:
                assert fs <= val <= fp
                assert (val == fs) == (sorted(deg)==sorted(upper))
                assert (val == fp) == (sorted(deg)==sorted(lower))
            else:
                assert val == Fraction(1, 2**n)
            if max(deg)<=3:
                k = deg.count(3)
                assert deg.count(1) == k+2
                assert deg.count(2) == n-2-2*k
                sub = Fraction(1,2**n)*(1+q)**(k+2)*(1+q*q)**(n-2-2*k)*(1+q**3)**k
                assert val == sub

# Exact rational verification of the high-noise comparison inequality and
# the subcubic branching multiplier, for representative parameter values.
for r in [Fraction(1,3),Fraction(1,5),Fraction(1,20)]:
    assert (1-r)*(1+r+r*r)**2 > 1+r*r
for q in rates:
    lhs = (1+q)*(1+q**3)-(1+q*q)**2
    assert lhs == q*(1-q)**2
print(f'VERIFY_OK {count} labelled tree sequences')
