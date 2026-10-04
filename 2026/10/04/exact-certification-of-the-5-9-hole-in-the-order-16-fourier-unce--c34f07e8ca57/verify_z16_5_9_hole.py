#!/usr/bin/env python3
"""Exact certificate for the absence of the support pair (5,9) on Z/16Z.

The Fourier matrix is F[r,c] = zeta^(r*c), where zeta is a primitive
16th root of unity.  Arithmetic is exact because Phi_16(X)=X^8+1:
every determinant is reduced to its eight integer coefficients in the
basis 1,zeta,...,zeta^7.
"""
import collections
import itertools

N = 16
ALL = (1 << N) - 1


def rotate_mask(mask, shift):
    if shift == 0:
        return mask
    return ((mask << shift) | (mask >> (N - shift))) & ALL


def translation_representatives(size):
    reps = []
    for comb in itertools.combinations(range(N), size):
        mask = sum(1 << x for x in comb)
        if mask == min(rotate_mask(mask, t) for t in range(N)):
            reps.append(comb)
    return reps


PERMS = {}
for k in range(1, 6):
    data = []
    for p in itertools.permutations(range(k)):
        inversions = sum(p[i] > p[j] for i in range(k) for j in range(i + 1, k))
        data.append((p, -1 if inversions & 1 else 1))
    PERMS[k] = data


def determinant_nonzero(rows, cols):
    """Return whether the square Fourier minor is nonzero, exactly."""
    k = len(rows)
    coeff = [0] * 8
    for p, sign in PERMS[k]:
        exponent = sum(rows[i] * cols[p[i]] for i in range(k)) & 15
        if exponent >= 8:
            coeff[exponent - 8] -= sign
        else:
            coeff[exponent] += sign
    return any(coeff)


def exact_rank(rows, cols, upper=None):
    """Rank over Q(zeta_16), by exact minor tests."""
    top = min(len(rows), len(cols))
    if upper is not None:
        top = min(top, upper)
    for k in range(top, 0, -1):
        for rr in itertools.combinations(rows, k):
            for cc in itertools.combinations(cols, k):
                if determinant_nonzero(rr, cc):
                    return k
    return 0


def main():
    # Time translation preserves the zero-frequency set up to phases;
    # modulation translates that zero set.  Since gcd(16,5)=gcd(16,7)=1,
    # all translation orbits of 5-sets and 7-sets have length 16.
    supports = translation_representatives(5)
    zero_sets = translation_representatives(7)
    assert len(supports) == 273
    assert len(zero_sets) == 715
    assert len(supports) * len(zero_sets) == 195195

    full_rank = 0
    deficient = 0
    rank_hist = collections.Counter()
    deletion_ok = collections.Counter()
    extension_fail = collections.Counter()
    admissible = []

    for A in supports:
        for B in zero_sets:
            # First detect rank 5 quickly.
            if any(determinant_nonzero(rr, A) for rr in itertools.combinations(B, 5)):
                full_rank += 1
                continue

            deficient += 1
            r = exact_rank(B, A, upper=4)
            rank_hist[r] += 1

            # Kernel contains a vector nonzero in every coordinate iff it is
            # not contained in any coordinate hyperplane.  This is equivalent
            # to deleting any one support column leaving the rank unchanged.
            if any(exact_rank(B, A[:j] + A[j + 1 :], upper=min(r, 4)) != r for j in range(5)):
                continue
            deletion_ok[r] += 1

            # To have exactly B as the Fourier zero set, the kernel must not be
            # contained in the kernel of any additional Fourier row.  This is
            # equivalent to every one-row extension raising rank by one.
            bad_y = None
            for y in range(N):
                if y in B:
                    continue
                rows = tuple(sorted(B + (y,)))
                if exact_rank(rows, A, upper=min(r + 1, 5)) != r + 1:
                    bad_y = y
                    break
            if bad_y is None:
                admissible.append((A, B, r))
            else:
                extension_fail[r] += 1

    assert full_rank == 193416
    assert deficient == 1779
    assert rank_hist == collections.Counter({4: 1752, 3: 27})
    assert deletion_ok == collections.Counter({4: 136})
    assert extension_fail == collections.Counter({4: 136})
    assert admissible == []

    print("support_representatives=273")
    print("zero_set_representatives=715")
    print("orbit_pairs=195195")
    print("full_rank=193416")
    print("rank_deficient=1779")
    print("rank_histogram={3:27,4:1752}")
    print("deletion_conditions_pass=136")
    print("extension_conditions_fail=136")
    print("admissible_exact_support_pairs=0")
    print("VERIFY_OK")


if __name__ == "__main__":
    main()
