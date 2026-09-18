from fractions import Fraction


def qbin(n, k, q):
    if k < 0 or k > n:
        return 0
    num = den = 1
    for i in range(k):
        num *= q ** (n - i) - 1
        den *= q ** (k - i) - 1
    return num // den


def isotropic(m, r, q):
    if r < 0 or r > m:
        return 0
    ans = qbin(m, r, q)
    for i in range(r):
        ans *= q ** (m - i) + 1
    return ans


def disjoint_isotropic(M, a, k, q):
    ans = 0
    for j in range(min(a, k) + 1):
        ans += ((-1) ** j * q ** (j * (j - 1) // 2)
                * qbin(a, j, q) * isotropic(M - j, k - j, q))
    return ans


def counts(m, q):
    n = sum(qbin(2 * m, d, q) for d in range(2 * m + 1))
    n += sum(q ** r * isotropic(m, r, q) for r in range(m + 1))
    e = 0
    for r in range(m + 1):
        for s in range(m + 1):
            for t in range(min(r, s) + 1):
                total = disjoint_isotropic(m - t, r - t, s - t, q)
                orth = q ** ((r - t) * (s - t)) * isotropic(m - r, s - t, q)
                e += (isotropic(m, r, q) * qbin(r, t, q)
                      * (total - orth) * q ** (r + s - t))
    return n, n * n - e, e


def span_f2(gens):
    space = {0}
    for g in gens:
        space |= {x ^ g for x in tuple(space)}
    return frozenset(space)


def bracket_h2_f2(a, b):
    c = (((a >> 0) & 1) * ((b >> 1) & 1)
         ^ ((a >> 1) & 1) * ((b >> 0) & 1)
         ^ ((a >> 2) & 1) * ((b >> 3) & 1)
         ^ ((a >> 3) & 1) * ((b >> 2) & 1))
    return c << 4


def exhaustive_h2_f2():
    subspaces = {frozenset({0})}
    changed = True
    while changed:
        changed = False
        for U in tuple(subspaces):
            for v in range(32):
                if v not in U:
                    W = span_f2(tuple(U) + (v,))
                    if W not in subspaces:
                        subspaces.add(W)
                        changed = True
    subalgebras = [
        U for U in subspaces
        if all(bracket_h2_f2(a, b) in U for a in U for b in U)
    ]
    permuting = 0
    for A in subalgebras:
        for B in subalgebras:
            AplusB = {a ^ b for a in A for b in B}
            if all(bracket_h2_f2(a, b) in AplusB for a in A for b in B):
                permuting += 1
    return len(subspaces), len(subalgebras), permuting


if __name__ == "__main__":
    for m in (1, 2, 3):
        for q in (2, 3, 5):
            n, p, e = counts(m, q)
            print("formula", m, q, n, p, e, Fraction(p, n * n))
    total_subspaces, nsub, nperm = exhaustive_h2_f2()
    print("H2(F2)", total_subspaces, nsub, nperm, nsub * nsub - nperm)
    assert (total_subspaces, nsub, nperm) == (374, 158, 18964)
    assert counts(2, 2) == (158, 18964, 6000)
