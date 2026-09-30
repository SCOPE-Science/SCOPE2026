from math import gcd


def rgs_partitions(m):
    if m == 0:
        yield ()
        return
    a = [0] * m
    def rec(i, mx):
        if i == m:
            yield tuple(a)
            return
        for v in range(mx + 2):
            a[i] = v
            yield from rec(i + 1, max(mx, v))
    a[0] = 0
    yield from rec(1, 0)


def is_congruence(part):
    m = len(part)
    signatures = {}
    for x in range(m):
        nbrs = [x]
        if x > 0:
            nbrs.append(x - 1)
        if x + 1 < m:
            nbrs.append(x + 1)
        sig = frozenset(part[y] for y in nbrs)
        b = part[x]
        if b in signatures and signatures[b] != sig:
            return False
        signatures[b] = sig
    return True


def refines(p, q):
    image = {}
    for i, b in enumerate(p):
        if b in image and image[b] != q[i]:
            return False
        image[b] = q[i]
    return True


def frequency(part):
    n = len(part) - 1
    blocks = len(set(part))
    if blocks == 1:
        return None
    if blocks == n + 1:
        return 1
    step = blocks - 1
    rests = sum(part[i] == part[i + 1] for i in range(n))
    assert (n - rests) % step == 0
    return (n - rests) // step


def notation(part):
    n = len(part) - 1
    blocks = len(set(part))
    if blocks == 1:
        return 'top'
    if blocks == n + 1:
        return 'Id'
    step = blocks - 1
    rests = [i for i in range(n) if part[i] == part[i + 1]]
    return f'<{step};{",".join(map(str, rests))}>' if rests else f'<{step}>'

all_cons = {}
for n in range(0, 6):
    cons = [p for p in rgs_partitions(n + 1) if is_congruence(p)]
    all_cons[n] = cons
    print('L', n, 'count', len(cons))
    for p in cons:
        f = frequency(p)
        if f is None:
            continue
        image = sorted({frequency(t) for t in cons if frequency(t) is not None and refines(t, p)})
        divisors = sorted(d for d in range(1, f + 1) if f % d == 0)
        print(' ', notation(p), 'f=', f, 'image=', image, 'divisors=', divisors)

# Minimality through L_4.
for n in range(0, 5):
    for rho in all_cons[n]:
        f = frequency(rho)
        if f is None:
            continue
        image = {frequency(t) for t in all_cons[n] if frequency(t) is not None and refines(t, rho)}
        divisors = {d for d in range(1, f + 1) if f % d == 0}
        assert image == divisors, (n, notation(rho), f, image, divisors)

# Exact defect classification on L_5.
defects = []
for rho in all_cons[5]:
    f = frequency(rho)
    if f is None:
        continue
    image = {frequency(t) for t in all_cons[5] if frequency(t) is not None and refines(t, rho)}
    divisors = {d for d in range(1, f + 1) if f % d == 0}
    if image != divisors:
        defects.append((notation(rho), rho, f, sorted(image), sorted(divisors - image)))
expected = [
    ('<1;1>', (0,1,1,0,1,0), 4, [1,4], [2]),
    ('<1;3>', (0,1,0,1,1,0), 4, [1,4], [2]),
]
assert sorted(defects) == sorted(expected), defects

# The frequency-2 congruence exists but is incomparable with each defective rho.
f2 = [p for p in all_cons[5] if frequency(p) == 2]
assert len(f2) == 1 and notation(f2[0]) == '<2;2>'
for _, rho, _, _, _ in defects:
    assert not refines(f2[0], rho)

print('DEFECTS', defects)
print('VERIFY_OK')
