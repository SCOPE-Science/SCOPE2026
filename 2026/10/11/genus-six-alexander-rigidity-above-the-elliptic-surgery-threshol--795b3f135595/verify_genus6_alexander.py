from fractions import Fraction
from itertools import product


def trim(p):
    p = list(p)
    while len(p) > 1 and p[-1] == 0:
        p.pop()
    return p


def deriv(p):
    return trim([Fraction(i) * p[i] for i in range(1, len(p))] or [Fraction(0)])


def divmod_poly(a, b):
    a = trim(a)
    b = trim(b)
    if b == [0]:
        raise ZeroDivisionError
    q = [Fraction(0)] * max(1, len(a) - len(b) + 1)
    r = a[:]
    while len(r) >= len(b) and r != [0]:
        k = len(r) - len(b)
        c = r[-1] / b[-1]
        q[k] += c
        for j in range(len(b)):
            r[j+k] -= c * b[j]
        r = trim(r)
    return trim(q), trim(r)


def sturm(p):
    p = trim([Fraction(x) for x in p])
    seq = [p, deriv(p)]
    while seq[-1] != [0]:
        _, r = divmod_poly(seq[-2], seq[-1])
        if r == [0]:
            break
        seq.append(trim([-x for x in r]))
    return seq


def sign(x):
    return 1 if x > 0 else -1 if x < 0 else 0


def eval_poly(p, x):
    y = Fraction(0)
    for c in reversed(p):
        y = y*x + c
    return y


def variations(signs):
    s = [x for x in signs if x]
    return sum(a != b for a,b in zip(s, s[1:]))


def variations_minus_infty(seq):
    signs = []
    for p in seq:
        deg = len(p)-1
        signs.append(sign(p[-1]) * (-1 if deg % 2 else 1))
    return variations(signs)


def roots_below_minus_one(p):
    seq = sturm(p)
    vm = variations_minus_infty(seq)
    v1 = variations([sign(eval_poly(q, Fraction(-1))) for q in seq])
    return vm - v1


def alexander_q(support):
    # Q(t)=t^6 Delta(t); output ascending coefficients degree <=12.
    support = sorted(support, reverse=True)
    coeff = {0: 0}
    # Alternating signs on nonzero exponents, starting + at top exponent 6.
    for idx, e in enumerate(support):
        c = 1 if idx % 2 == 0 else -1
        coeff[e] = c
        coeff[-e] = c
    coeff[0] = -1 if len(support) % 2 else 1
    q = [0]*13
    for e,c in coeff.items():
        q[e+6] = c
    return q


def permitted_by_prop24(support):
    # Degrees 6 and 5 are fixed. Proposition 2.4 forbids a first gap
    # at odd offset 3 or 5 from degree 6.
    for d in range(2, 6):
        if (6-d) not in support:
            return d % 2 == 0
    return True

rows=[]
for bits in product([0,1], repeat=4):
    support=[6,5]+[e for e,b in zip([4,3,2,1],bits) if b]
    q=alexander_q(support)
    allowed=permitted_by_prop24(set(support))
    nroot=roots_below_minus_one(q) if allowed else None
    rows.append((tuple(support),allowed,nroot,q))

allowed=[r for r in rows if r[1]]
with_root=[r for r in allowed if r[2] and r[2] > 0]
assert len(rows)==16
assert len(allowed)==11, len(allowed)
assert len(with_root)==1, [(r[0],r[2]) for r in with_root]
support,_,nroot,q=with_root[0]
assert support == (6,5,3,2,1), support
assert nroot == 1
expected=[1,-1,0,1,-1,1,-1,1,-1,1,0,-1,1]
assert q == expected, (q, expected)
print('VERIFY_OK total=16 admissible=11 unique_negative_root_support=6,5,3,2,1 root_count=1')
