"""Finite-field exhaustive checks of square-zero remainder idempotent fibers.

Usage: python3 verify.py (Python standard library only).
"""
from itertools import product


def fadd(x, y, q):
    return x ^ y if q == 4 else (x + y) % q


def fmul(x, y, q):
    if q != 4:
        return x * y % q
    a = 0
    for k in range(2):
        if (y >> k) & 1:
            a ^= x << k
    if a & 8:
        a ^= 0b1110
    if a & 4:
        a ^= 0b111
    return a


def fneg(x, q):
    return x if q == 4 else (-x) % q


def fsub(x, y, q):
    return fadd(x, fneg(y, q), q)


def predicted(d, p, s, q):
    r = len(p)
    lo, *middles, hi = d
    if lo != hi:
        coefficients = [s[i] if middles[i] == hi else p[i] for i in range(r)]
        return q ** (r + 1) if all(x == 0 for x in coefficients) else q ** r
    active = [i for i in range(r) if middles[i] != lo]
    t = len(active)
    c = 0
    for i in range(r):
        if i not in active:
            c = fadd(c, fmul(p[i], s[i], q), q)
    if t == 0:
        return int(c == 0)
    return q ** (2*t-1) + q**t - q**(t-1) if c == 0 else q**(2*t-1) - q**(t-1)


def check(r, q):
    n = r + 2
    edgepairs = [(0, j) for j in range(1, n - 1)] + [(j, n - 1) for j in range(1, n - 1)] + [(0, n - 1)]
    allpairs = [(i, i) for i in range(n)] + edgepairs
    possible_idempotents = {}
    # Enumerate the idempotents with their prescribed diagonal by literal
    # convolution, not by the classification being tested.
    for d in product((0, 1), repeat=n):
        ids = []
        for coeff in product(range(q), repeat=len(edgepairs)):
            e = dict(zip(allpairs, d + coeff))
            for i, j in allpairs:
                prod = 0
                for k in range(i, j + 1):
                    prod = fadd(prod, fmul(e.get((i,k),0),e.get((k,j),0),q),q)
                if prod != e[(i,j)]:
                    break
            else:
                ids.append(e)
        possible_idempotents[d] = ids

    checks = 0
    for d in product((0, 1), repeat=n):
        for arm in product(range(q), repeat=2*r):
            p, s = arm[:r], arm[r:]
            observed = 0
            for e in possible_idempotents[d]:
                squared = 0
                for j in range(r):
                    x = fsub(p[j],e[(0,j+1)],q)
                    y = fsub(s[j],e[(j+1,n-1)],q)
                    squared = fadd(squared,fmul(x,y,q),q)
                if squared == 0:
                    observed += 1
            want = predicted(d,p,s,q)
            assert observed == want, (r,q,d,p,s,observed,want)
            checks += 1
    best = max(predicted(d,p,s,q) for d in product((0,1),repeat=n)
               for p in product(range(q), repeat=r)
               for s in product(range(q), repeat=r))
    formula = q**(2*r-1) + q**r - q**(r-1)
    assert best == formula if r >= 2 else best >= 1
    return checks


def main():
    cases = [(1,2),(1,3),(2,2),(2,3),(2,4),(3,2)]
    total = sum(check(r,q) for r,q in cases)
    print('DIAMOND_SQZERO_NILCLEAN_OK',len(cases),'families',total,'fibers')


if __name__ == '__main__':
    main()
