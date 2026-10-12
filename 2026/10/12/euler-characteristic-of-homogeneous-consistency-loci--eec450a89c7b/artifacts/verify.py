from itertools import product
from math import comb, factorial

def monomials(n, d):
    out = []
    def rec(pos, left, cur):
        if pos == n - 1:
            out.append(tuple(cur + [left]))
            return
        for a in range(left + 1):
            rec(pos + 1, left - a, cur + [a])
    rec(0, d, [])
    return out

def pure_label(exp):
    nz = [i for i,a in enumerate(exp) if a]
    if len(nz) == 1:
        return nz[0]
    return None

def formula(n, degrees):
    Ns = [comb(n+d-1, n-1) for d in degrees]
    return sum(((-1)**t) * comb(n,t) *
               prod([N-t for N in Ns]) for t in range(n+1))

def prod(xs):
    z = 1
    for x in xs:
        z *= x
    return z

def stirling2(m,n):
    return sum(((-1)**t) * comb(n,t) * (n-t)**m for t in range(n+1)) // factorial(n)

checked_cases = 0
tuples_checked = 0

cases = []
for n in (2,3):
    for m in range(1,5):
        for degrees in product((1,2), repeat=m):
            Ns = [comb(n+d-1,n-1) for d in degrees]
            if prod(Ns) <= 20000:
                cases.append((n,degrees))
cases += [
    (4,(1,1,1)),
    (4,(1,1,1,1)),
    (4,(1,1,1,1,1)),
    (4,(2,2,2,2)),
]

for n,degrees in cases:
    mons = [monomials(n,d) for d in degrees]
    brute = 0
    for tup in product(*mons):
        tuples_checked += 1
        labels = {pure_label(e) for e in tup}
        labels.discard(None)
        cover = len(labels) == n

        # Independent coordinate-support test:
        # a common zero exists on a coordinate support S iff every selected
        # monomial uses at least one variable outside S.
        no_common_on_coordinate_strata = True
        for mask in range(1, 1 << n):
            some_nonzero = False
            for e in tup:
                supp = {j for j,a in enumerate(e) if a}
                if all(mask & (1 << j) for j in supp):
                    some_nonzero = True
                    break
            if not some_nonzero:
                no_common_on_coordinate_strata = False
                break
        assert cover == no_common_on_coordinate_strata
        if cover:
            brute += 1

    f = formula(n,degrees)
    assert brute == f, (n,degrees,brute,f)
    checked_cases += 1

for n in range(2,9):
    # below threshold
    for m in range(1,n):
        degrees = tuple(1 + (i % 3) for i in range(m))
        assert formula(n,degrees) == 0
    # square threshold
    degrees = tuple(1 + (i % 3) for i in range(n))
    assert formula(n,degrees) == factorial(n)
    # linear overdetermined
    for m in range(n, n+5):
        got = formula(n,(1,)*m)
        assert got == factorial(n) * stirling2(m,n)

assert checked_cases > 30
assert tuples_checked > 10000
print("VERIFY_OK", checked_cases, tuples_checked)
