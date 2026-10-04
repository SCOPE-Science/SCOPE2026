from itertools import product
from fractions import Fraction


def add(a, b, mods):
    return tuple((x + y) % m for x, y, m in zip(a, b, mods))


def neg(a, mods):
    return tuple((-x) % m for x, m in zip(a, mods))


def zero(mods):
    return tuple(0 for _ in mods)


def elements_A(mods):
    return list(product(*[range(m) for m in mods]))


def mul_dic(x, z, mods, y):
    a, e = x
    b, f = z
    term = b if e == 0 else neg(b, mods)
    c = add(a, term, mods)
    if e and f:
        c = add(c, y, mods)
    return (c, e ^ f)


def inverse(g, elements, mul, identity):
    for h in elements:
        if mul(g, h) == identity and mul(h, g) == identity:
            return h
    raise AssertionError('no inverse')


def generated_subgroup(gens, elements, mul, identity):
    invs = [inverse(g, elements, mul, identity) for g in gens]
    steps = list(gens) + invs
    H = {identity}
    changed = True
    while changed:
        changed = False
        for h in list(H):
            for g in steps:
                for u in (mul(h, g), mul(g, h)):
                    if u not in H:
                        H.add(u)
                        changed = True
    return frozenset(H)


def all_subgroups(elements, mul, identity):
    trivial = frozenset([identity])
    found = {trivial}
    queue = [trivial]
    while queue:
        H = queue.pop()
        for g in elements:
            if g not in H:
                K = generated_subgroup(list(H) + [g], elements, mul, identity)
                if K not in found:
                    found.add(K)
                    queue.append(K)
    return list(found)


def cyclic_subgroups(elements, mul, identity):
    return list({generated_subgroup([g], elements, mul, identity) for g in elements})


def permute(H, K, mul):
    HK = {mul(h, k) for h in H for k in K}
    KH = {mul(k, h) for h in H for k in K}
    return HK == KH


def abelian_data(mods, y):
    A = elements_A(mods)
    identity = zero(mods)
    amul = lambda a, b: add(a, b, mods)
    LA = all_subgroups(A, amul, identity)
    CA = cyclic_subgroups(A, amul, identity)
    Y = {identity, y}
    containing = [B for B in LA if Y.issubset(B)]
    m = len(A)

    omega = sum(m // len(B) for B in containing)
    xi = 0
    for B in containing:
        for C in containing:
            inter = B & C
            D = {add(b, c, mods) for b in B for c in C}
            # |(A/D)[2]| = #{x in A : 2x in D} / |D|.
            t2 = sum(1 for x in A if add(x, x, mods) in D) // len(D)
            xi += (m // len(inter)) * t2

    ell = len(LA)
    c = len(CA)
    q = m // 2
    q2 = sum(1 for x in A if add(x, x, mods) in Y) // 2
    sd = Fraction(ell * ell + 2 * ell * omega + xi, (ell + omega) ** 2)
    csd = Fraction(c * c + 2 * c * q + q * q2, (c + q) ** 2)
    return sd, csd


def brute(mods, y):
    A = elements_A(mods)
    elements = [(a, e) for a in A for e in (0, 1)]
    identity = (zero(mods), 0)
    mul = lambda x, z: mul_dic(x, z, mods, y)
    L = all_subgroups(elements, mul, identity)
    C = cyclic_subgroups(elements, mul, identity)
    sd = Fraction(sum(permute(H, K, mul) for H in L for K in L), len(L) ** 2)
    csd = Fraction(sum(permute(H, K, mul) for H in C for K in C), len(C) ** 2)
    return sd, csd


tests = [
    ((4,), (2,)),
    ((6,), (3,)),
    ((8,), (4,)),
    ((2, 2), (1, 0)),
    ((2, 2), (1, 1)),
    ((2, 4), (1, 0)),
    ((2, 4), (0, 2)),
    ((2, 4), (1, 2)),
    ((2, 6), (1, 0)),
    ((2, 6), (0, 3)),
]

for mods, y in tests:
    direct = brute(mods, y)
    formula = abelian_data(mods, y)
    assert direct == formula, (mods, y, direct, formula)

assert abelian_data((6,), (3,)) == (Fraction(29, 32), Fraction(43, 49))
assert abelian_data((8,), (4,)) == (Fraction(113, 121), Fraction(7, 8))
assert abelian_data((2, 6), (1, 0))[0] == Fraction(215, 242)
assert abelian_data((2, 6), (0, 3))[0] == Fraction(215, 242)
assert abelian_data((2, 8), (0, 4)) == (Fraction(333, 361), Fraction(7, 8))

print('VERIFY_OK')
