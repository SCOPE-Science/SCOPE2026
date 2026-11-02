"""Direct finite-field verification for affine-quandle algebra idempotents.
Run: python3 check_modular_affine.py. Uses Python standard library only.
"""
from itertools import product
from math import comb


def circ_mul(f, g, p):
    out = [0] * p
    for i, x in enumerate(f):
        if x:
            for j, y in enumerate(g):
                if y:
                    out[(i + j) % p] += x * y
    return [x % p for x in out]


def star(f, g, p, lam):
    aa = (1 - lam) % p
    out = [0] * p
    for i, x in enumerate(f):
        if x:
            for j, y in enumerate(g):
                if y:
                    out[(aa * i + lam * j) % p] += x * y
    return [x % p for x in out]


def resonance(p, lam):
    aa = (1 - lam) % p
    return [j for j in range(1, p) if (pow(aa, j, p) + pow(lam, j, p)) % p == 1]


def logarithmic_basis(p):
    one = [1] + [0] * (p - 1)
    z = [-1 % p, 1] + [0] * (p - 2)
    v = [0] * p
    term = one
    for j in range(1, p):
        term = circ_mul(term, z, p)
        scale = (1 if j % 2 else -1) * pow(j, -1, p)
        v = [(v[i] + scale * term[i]) % p for i in range(p)]
    vpowers = [one]
    for j in range(1, p):
        vpowers.append(circ_mul(vpowers[-1], v, p))
    return vpowers


def exp_cyc(h, p):
    one = [1] + [0] * (p - 1)
    out = one[:]
    term = one[:]
    fact = 1
    for j in range(1, p):
        term = circ_mul(term, h, p)
        fact = fact * j % p
        out = [(out[i] + term[i] * pow(fact, -1, p)) % p for i in range(p)]
    return out


def parametric_set(p, lam):
    J = resonance(p, lam)
    v = logarithmic_basis(p)
    result = set()
    for co in product(range(p), repeat=len(J)):
        h = [0] * p
        for c, j in zip(co, J):
            for k in range(p):
                h[k] = (h[k] + c * v[j][k]) % p
        e = tuple(exp_cyc(h, p))
        assert star(e, e, p, lam) == list(e), (p, lam, J, co)
        result.add(e)
    assert len(result) == p ** len(J)
    return result


def brute_count(p, lam):
    # Directly enumerate all p^p coefficient vectors, independently of log/exp.
    aa = (1 - lam) % p
    eq = [(aa * i + lam * j) % p for i in range(p) for j in range(p)]
    count = 0
    for vec in product(range(p), repeat=p):
        aug = sum(vec) % p
        if aug not in (0, 1):
            continue
        out = [0] * p
        for i, x in enumerate(vec):
            if x:
                start = p * i
                for j, y in enumerate(vec):
                    if y:
                        out[eq[start + j]] += x * y
        if all((out[k] - vec[k]) % p == 0 for k in range(p)):
            count += 1
    return count


def main():
    cases = [(3, 2), (5, 2), (5, 3), (7, 2), (7, 3), (7, 4)]
    for p, lam in cases:
        J = resonance(p, lam)
        expected = p ** len(J) + 1
        ps = parametric_set(p, lam)
        actual = brute_count(p, lam)
        assert actual == expected, (p, lam, J, expected, actual)
        assert len(ps) + 1 == actual
        print('EXHAUSTIVE',p,lam,'resonance',J,'idempotents',actual)
    # Parameter-level checks at higher primes without claiming exhaustive counts.
    for p, lam in [(11, 3), (13, 4), (17, 2), (19, 8), (31, 16)]:
        J = resonance(p, lam)
        basis = logarithmic_basis(p)
        for j in J:
            e = tuple(exp_cyc(basis[j], p))
            assert star(e, e, p, lam) == list(e)
        print('BASIS-CHECK',p,lam,'resonance',J,'predicted',p ** len(J) + 1)
    print('MODULAR_AFFINE_QUANDLE_IDEMPOTENTS_OK 6 5')

if __name__ == '__main__':
    main()
