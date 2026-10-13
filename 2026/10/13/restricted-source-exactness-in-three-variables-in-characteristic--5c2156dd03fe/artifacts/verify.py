#!/usr/bin/env python3
"""Exact finite residue-pattern verifier for the characteristic 2 and 3 theorem."""
from collections import Counter
from itertools import product


def invmod(a, p):
    return pow(a % p, -1, p)


def rank_mod(cols, p, nrows=3):
    """Rank of a matrix given by column vectors over F_p."""
    if not cols:
        return 0
    A = [[cols[j][i] % p for j in range(len(cols))] for i in range(nrows)]
    r = 0
    for c in range(len(cols)):
        pivot = next((i for i in range(r, nrows) if A[i][c] % p), None)
        if pivot is None:
            continue
        A[r], A[pivot] = A[pivot], A[r]
        z = invmod(A[r][c], p)
        A[r] = [(z*x) % p for x in A[r]]
        for i in range(nrows):
            if i != r and A[i][c] % p:
                t = A[i][c] % p
                A[i] = [(A[i][j] - t*A[r][j]) % p for j in range(len(cols))]
        r += 1
        if r == nrows:
            break
    return r


def kernel_basis(row, p):
    """A basis of ker(row) in F_p^3, by exhaustive vectors."""
    vecs = []
    for v in product(range(p), repeat=3):
        if v == (0, 0, 0):
            continue
        if sum(row[i]*v[i] for i in range(3)) % p == 0:
            if rank_mod(vecs + [v], p) > rank_mod(vecs, p):
                vecs.append(v)
    return vecs


def exact_target_basis(w, p, boundary=None):
    lam = tuple((w[i] + 1) % p for i in range(3))
    if boundary is None:
        return kernel_basis(lam, p) if any(lam) else []
    # On a boundary weight w_s=-1, the raw coefficient line is k e_s;
    # it is exact precisely when lambda is nonzero.
    if any(lam):
        e = [0, 0, 0]
        e[boundary] = 1
        return [tuple(e)]
    return []


def predecessor_basis(w, r, p, boundary=None):
    lam = tuple((w[i] + 1) % p for i in range(3))
    lam_prev = tuple((lam[i] - (1 if i == r else 0)) % p for i in range(3))
    if boundary is None:
        if w[r] == 0:
            # predecessor has boundary coordinate -1 at r
            if any(lam_prev):
                e = [0, 0, 0]
                e[r] = 1
                return [tuple(e)]
            return []
        return kernel_basis(lam_prev, p) if any(lam_prev) else []
    # target already has boundary s. A valid predecessor uses r != s and w_r>0,
    # retaining the same boundary coefficient line k e_s.
    if r == boundary or w[r] <= 0:
        return []
    if any(lam_prev):
        e = [0, 0, 0]
        e[boundary] = 1
        return [tuple(e)]
    return []


def bracket_image_columns(w, p, boundary=None):
    lam = tuple((w[i] + 1) % p for i in range(3))
    out = []
    for r in range(3):
        if boundary is None:
            # target interior: every anchor is valid; w_r=0 means boundary predecessor
            pass
        elif r == boundary or w[r] <= 0:
            continue
        # Quadratic anchor coefficient space K_r=ker(mu_r), mu_r=sigma+epsilon_r.
        mu = tuple((1 + (1 if i == r else 0)) % p for i in range(3))
        K = kernel_basis(mu, p)
        B = predecessor_basis(w, r, p, boundary)
        for a in K:
            la = sum(lam[i]*a[i] for i in range(3)) % p
            for b in B:
                lb = sum(lam[i]*b[i] for i in range(3)) % p
                c = tuple((la*b[i] - lb*a[i]) % p for i in range(3))
                if c != (0, 0, 0):
                    out.append(c)
    return out


def canonical_values(p):
    # 0 is an actual zero coordinate. 1,...,p-1 represent positive residues;
    # p represents a positive integer congruent to 0 mod p.
    return list(range(p + 1))


def verify_prime(p):
    vals = canonical_values(p)
    counts = Counter()
    failures = []
    total = 0

    # Interior signatures. Exclude (0,0,0): its sum is 0, hence it cannot occur
    # for an actual target weight of degree d>=3, where sum w_i=d-1>=2.
    for w in product(vals, repeat=3):
        if w == (0, 0, 0):
            continue
        E = exact_target_basis(w, p)
        cols = bracket_image_columns(w, p)
        td = rank_mod(E, p)
        ir = rank_mod(cols, p)
        counts[("interior", td, ir)] += 1
        total += 1
        if td != ir:
            failures.append(("interior", w, td, ir))

    # Boundary signatures: one coordinate is -1. Exclude the case in which both
    # other coordinates are 0, whose weight sum is -1 and is impossible for d>=3.
    for s in range(3):
        others = [i for i in range(3) if i != s]
        for a, b in product(vals, repeat=2):
            if a == 0 and b == 0:
                continue
            w = [0, 0, 0]
            w[s] = -1
            w[others[0]] = a
            w[others[1]] = b
            w = tuple(w)
            E = exact_target_basis(w, p, s)
            cols = bracket_image_columns(w, p, s)
            td = rank_mod(E, p)
            ir = rank_mod(cols, p)
            counts[("boundary", td, ir)] += 1
            total += 1
            if td != ir:
                failures.append(("boundary", w, td, ir))

    expected_total = {2: 50, 3: 108}[p]
    expected_counts = {
        2: Counter({
            ("interior", 2, 2): 25,
            ("boundary", 1, 1): 21,
            ("boundary", 0, 0): 3,
            ("interior", 0, 0): 1,
        }),
        3: Counter({
            ("interior", 2, 2): 62,
            ("boundary", 1, 1): 42,
            ("boundary", 0, 0): 3,
            ("interior", 0, 0): 1,
        }),
    }[p]
    assert total == expected_total, (p, total)
    assert counts == expected_counts, (p, counts)
    assert not failures, failures
    print(f"p={p}: signatures={total}; breakdown={dict(sorted(counts.items()))}; failures=0")


def main():
    verify_prime(2)
    verify_prime(3)
    print("CHECK_OK")


if __name__ == "__main__":
    main()
