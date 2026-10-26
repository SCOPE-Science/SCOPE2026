"""Independent exact cycle-class checks for a two-character symmetric-group L4 inequality.
Standard library only; finite computations corroborate the all-degree proof.
"""
from collections import Counter
from fractions import Fraction
from itertools import permutations
from math import factorial, isclose

EXPECTED = {
    4: (4, 2, 2, 0, 3),
    5: (4, 3, 4, 4, 6),
    6: (4, 3, 5, 6, 13),
    7: (4, 3, 5, 7, 15),
    8: (4, 3, 5, 7, 16),
}
ROOTS = {
    4: (1.553224934017562, 7.317018044683561),
    5: (0.8685170918213297, 15.641081748080278),
    6: (0.647806942708833, 22.379326363868724),
    7: (0.597051387082760, 24.713866882268370),
    8: (0.5763678605391691, 25.267327761536930),
}


def partitions(n, upper=None):
    if upper is None:
        upper = n
    if n == 0:
        yield ()
        return
    for k in range(min(n, upper), 0, -1):
        for rest in partitions(n-k, k):
            yield (k,) + rest


def moments_by_conjugacy_classes(n):
    e = [Fraction(0) for _ in range(5)]
    first = second = cross = Fraction(0)
    weight_sum = Fraction(0)
    for part in partitions(n):
        counts = Counter(part)
        denominator = 1
        for cycle_size, multiplicity in counts.items():
            denominator *= cycle_size**multiplicity * factorial(multiplicity)
        w = Fraction(1, denominator)
        x = counts[1]
        y = counts[2]
        a = x - 1
        b = x*(x-3)//2 + y
        weight_sum += w
        first += w*a*a
        second += w*b*b
        cross += w*a*b
        e[0] += w*a**4
        e[1] += w*a**3*b
        e[2] += w*a*a*b*b
        e[3] += w*a*b**3
        e[4] += w*b**4
    assert weight_sum == 1
    assert (first, second, cross) == (1, 1, 0)
    return tuple(e)


def direct_moments(n):
    tally = [0]*5
    for p in permutations(range(n)):
        seen = [False]*n
        c1 = c2 = 0
        for j in range(n):
            if seen[j]:
                continue
            k = j
            length = 0
            while not seen[k]:
                seen[k] = True
                length += 1
                k = p[k]
            c1 += length == 1
            c2 += length == 2
        a = c1 - 1
        b = c1*(c1-3)//2 + c2
        for k, term in enumerate((a**4, a**3*b, a*a*b*b, a*b**3, b**4)):
            tally[k] += term
    return tuple(Fraction(k, factorial(n)) for k in tally)


def h(n, t):
    if n == 4:
        return t*(2*t**3+2*t**2-6*t-3)
    if n == 5:
        return (t+1)**2*(3*t*t+2*t-4)
    if n == 6:
        return 3*t**4+11*t**3+9*t*t-2*t-6
    if n == 7:
        return 3*t**4+11*t**3+12*t*t-7
    return 3*t**4+11*t**3+12*t*t+t-7


def sharp_ratio(n, t):
    m40,m31,m22,m13,m04=EXPECTED[min(8,n)]
    return (m40*t**4+4*m31*t**3+6*m22*t*t+4*m13*t+m04)/(1+t*t)**2


def run():
    tests = 0
    for n in range(4, 15):
        observed = moments_by_conjugacy_classes(n)
        assert observed == EXPECTED[min(n, 8)], (n, observed)
        tests += 1
    for n in range(4, 8):
        assert direct_moments(n) == EXPECTED[n]
        tests += 1
    for n in range(4, 9):
        lo, hi = 0.00000001, 4.
        assert h(n,lo)<0 and h(n,hi)>0
        for i in range(80):
            mid=(lo+hi)/2
            if h(n,mid)<0:
                lo=mid
            else:
                hi=mid
        rt=(lo+hi)/2
        expected_root,expected_const=ROOTS[n]
        assert isclose(rt, expected_root, rel_tol=1e-12,abs_tol=1e-12)
        assert isclose(sharp_ratio(n,rt),expected_const,rel_tol=1e-12,abs_tol=1e-12)
        for t in (0,0.01,0.1,0.3,0.5,1,2,5,20,100):
            assert sharp_ratio(n,t)<=expected_const+1e-10
            tests+=1
        tests += 3
    for n in range(4, 8):
        assert ROOTS[n+1][1]>ROOTS[n][1]
        tests+=1
    print('VERIFY_OK', 'independent_cycle_class_moments_n=4..14',
          'permutation_moments_n=4..7','assertions='+str(tests))

if __name__ == '__main__':
    run()
