"""Exact finite checks for the density-seven prefix-normal enumeration identity.
Run with Python 3 (standard library only)."""
from itertools import combinations

NUM = (1,3,9,17,35,48,76,85,108,103,108,85,76,48,35,17,9,3,1)


def trim(p):
    p = list(p)
    while len(p) > 1 and p[-1] == 0:
        p.pop()
    return p


def add(p, q):
    z = [0] * max(len(p), len(q))
    for i, a in enumerate(p):
        z[i] += a
    for i, a in enumerate(q):
        z[i] += a
    return trim(z)


def mul(p, q):
    z = [0] * (len(p) + len(q) - 1)
    for i, a in enumerate(p):
        if a:
            for j, b in enumerate(q):
                if b:
                    z[i+j] += a*b
    return trim(z)


def power(p, k):
    z = [1]
    for _ in range(k):
        z = mul(z, p)
    return z


def shift(p, k, coefficient=1):
    return [0]*k + [coefficient*a for a in p]


FACTORS = {s: [1] + [0]*(length-1) + [-1]
           for s, length in [('a',1),('b',2),('c',3),('d',4),('e',6)]}
COMMON = dict(a=1,b=3,c=2,d=3,e=2)


def numerator_over_common(terms):
    out = [0]
    for coef, degree, den in terms:
        part = [coef]
        for symbol in COMMON:
            exponent = COMMON[symbol] - den.get(symbol, 0)
            assert exponent >= 0
            part = mul(part, power(FACTORS[symbol], exponent))
        out = add(out, shift(part, degree))
    return out


K_TERMS = [
    (1,0,dict(a=1,c=1,d=1)),
    (1,2,dict(a=1,b=1,d=1)),
    (1,2,dict(b=2,d=1)),
    (1,6,dict(c=1,d=1,e=1)),
    (1,4,dict(b=1,d=2)),
    (1,10,dict(d=2,e=1)),
]
L_TERMS = [
    (1,0,dict(a=1,c=1,d=2)),(1,3,dict(a=1,c=2,d=1)),
    (1,2,dict(a=1,b=1,d=2)),
    (1,2,dict(b=2,d=2)),(1,2,dict(b=3,d=1)),
    (2,6,dict(c=1,d=1,e=2)),(-1,12,dict(c=1,d=1,e=2)),
    (1,10,dict(c=1,d=2,e=1)),(1,9,dict(c=2,d=1,e=1)),
    (2,4,dict(b=1,d=3)),(1,6,dict(b=2,d=2)),
    (2,10,dict(d=3,e=1)),(1,10,dict(d=2,e=2)),
]


def polynomial_identity():
    k = numerator_over_common(K_TERMS)
    ell = numerator_over_common(L_TERMS)
    common = [1]
    for f, exponent in COMMON.items():
        common = mul(common, power(FACTORS[f], exponent))
    # F7/x^7 = (a*L + x*K)/(a^3*e)
    left_base = add(mul(FACTORS['a'], ell), shift(k, 1))
    target_den = mul(mul(FACTORS['a'], FACTORS['c']),
                     mul(power(FACTORS['d'], 2), power(FACTORS['e'], 3)))
    left = mul(left_base, target_den)
    right = mul(list(NUM), mul(common,
                        mul(power(FACTORS['a'], 3), FACTORS['e'])))
    assert trim(left) == trim(right), 'formal rational-function identity failed'
    return target_den


def coefficients(denominator, horizon):
    numer = [0]*7 + list(NUM)
    out = []
    for n in range(horizon + 1):
        out.append((numer[n] if n < len(numer) else 0) - sum(
            denominator[j]*out[n-j]
            for j in range(1, min(n, len(denominator)-1)+1)))
    return out


def direct_prefix_normal(positions, n):
    counts = [0]*(n+1)
    ones = set(positions)
    for i in range(n):
        counts[i+1] = counts[i] + (i in ones)
    for length in range(1,n+1):
        for start in range(1,n-length+1):
            if counts[start+length]-counts[start] > counts[length]:
                return False
    return True


def gap_prefix_normal(positions):
    distances = [positions[j+1]-positions[j] for j in range(6)]
    for m in range(1,6):
        left = sum(distances[:m])
        for j in range(1,7-m):
            if left > sum(distances[j:j+m]):
                return False
    return True


def main():
    den = polynomial_identity()
    values = coefficients(den, 35)
    for n in range(7, 26):
        count = 0
        for rest in combinations(range(1, n), 6):
            positions = (0,) + rest
            first = direct_prefix_normal(positions, n)
            second = gap_prefix_normal(positions)
            assert first == second, ('criterion mismatch', n, positions)
            count += first
        assert count == values[n], ('coefficient mismatch', n, count, values[n])
    print('COUNTS_7_TO_25:', [values[n] for n in range(7,26)])
    print('FORMAL_IDENTITY_PASS')
    print('ALL_CHECKS_PASS')

if __name__ == '__main__':
    main()
