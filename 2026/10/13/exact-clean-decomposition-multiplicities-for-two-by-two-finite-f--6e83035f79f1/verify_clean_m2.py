from itertools import product


def det2(a, q):
    return (a[0] * a[3] - a[1] * a[2]) % q


def mul(a, b, q):
    x, y, z, w = a
    r, s, t, u = b
    return ((x*r+y*t) % q, (x*s+y*u) % q,
            (z*r+w*t) % q, (z*s+w*u) % q)


def sub(a, b, q):
    return tuple((x-y) % q for x, y in zip(a, b))


def idempotents(q):
    return [e for e in product(range(q), repeat=4) if mul(e, e, q) == e]


def eigenline_count(a, q):
    reps = [(1, t) for t in range(q)] + [(0, 1)]
    out = 0
    for x, y in reps:
        ax = (a[0]*x + a[1]*y) % q
        ay = (a[2]*x + a[3]*y) % q
        if x == 1:
            if ay == (ax*y) % q:
                out += 1
        elif ax == 0:
            out += 1
    return out


def predicted(a, q):
    I = (1, 0, 0, 1)
    scalar = a[1] % q == 0 and a[2] % q == 0 and a[0] % q == a[3] % q
    if scalar:
        lam = a[0] % q
        return 1 if lam in (0, 1) else q*q + q + 2
    e = eigenline_count(a, q)
    d0 = det2(a, q)
    d1 = det2(sub(a, I, q), q)
    epsilon = int(d0 == 0 or d1 == 0)
    return q*q - 1 + e - q*epsilon + int(d0 != 0) + int(d1 != 0)


def actual(a, q, idem):
    return sum(det2(sub(a, e, q), q) != 0 for e in idem)


for q in (2, 3, 5, 7):
    idem = idempotents(q)
    assert len(idem) == q*(q+1) + 2
    distribution = {}
    for a in product(range(q), repeat=4):
        got = actual(a, q, idem)
        want = predicted(a, q)
        assert got == want, (q, a, got, want)
        distribution[got] = distribution.get(got, 0) + 1
    print(q, sorted(distribution.items()))
print('VERIFY_OK')
