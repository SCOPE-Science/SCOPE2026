"""Independent finite exact-arithmetic checks of squarefree polynomial product energy."""
from collections import Counter
from itertools import product

def mul(a, b, p):
    c = [0] * (len(a) + len(b) - 1)
    for i, x in enumerate(a):
        for j, y in enumerate(b):
            c[i + j] = (c[i + j] + x * y) % p
    return tuple(c)

def rem(a, b, p):
    a = list(a)
    while a and len(a) >= len(b):
        f = a[-1] * pow(b[-1], -1, p) % p
        shift = len(a) - len(b)
        for j, y in enumerate(b):
            a[shift + j] = (a[shift + j] - f * y) % p
        while a and a[-1] == 0:
            a.pop()
    return tuple(a)

def gcd(a, b, p):
    while b:
        a, b = b, rem(a, b, p)
    if not a:
        return ()
    c = pow(a[-1], -1, p)
    return tuple((x * c) % p for x in a)

def squarefree(f, p):
    deriv = [(i * f[i]) % p for i in range(1, len(f))]
    while deriv and deriv[-1] == 0:
        deriv.pop()
    return len(gcd(f, tuple(deriv), p)) == 1

def monics(d, p):
    return [(*coeffs, 1) for coeffs in product(range(p), repeat=d)]

def direct_energy(d, p):
    ff = [f for f in monics(d, p) if squarefree(f, p)]
    multiplicities = Counter(mul(f, g, p) for f in ff for g in ff)
    return sum(v * v for v in multiplicities.values())

def parametrized_energy(d, p):
    total = 0
    for b in range(d + 1):
        a = d - b
        ff_a = [f for f in monics(a, p) if squarefree(f, p)]
        ff_b = [f for f in monics(b, p) if squarefree(f, p)]
        for v in ff_b:
            for w in ff_b:
                if len(gcd(v, w, p)) != 1:
                    continue
                for u in ff_a:
                    if len(gcd(u, v, p)) != 1 or len(gcd(u, w, p)) != 1:
                        continue
                    for x in ff_a:
                        if len(gcd(x, v, p)) == 1 and len(gcd(x, w, p)) == 1:
                            total += 1
    return total

def run():
    tested = 0
    for d in (1, 2, 3):
        for p in (2, 3, 5, 7):
            if p ** d > 400:
                continue
            observed = direct_energy(d, p)
            expected = parametrized_energy(d, p)
            assert observed == expected, (d, p, observed, expected)
            if d == 1:
                assert observed == 2 * p**2 - p
            if d == 2:
                assert observed == 3*p**4-10*p**3+12*p**2-5*p
            print(f"PASS d={d} q={p}: energy={observed}")
            tested += 1
    print(f"PASS: {tested} exact field-degree tests")
if __name__ == '__main__':
    run()
