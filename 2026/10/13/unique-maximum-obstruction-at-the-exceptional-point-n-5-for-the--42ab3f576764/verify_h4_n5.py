from itertools import combinations


def pair_sums(B):
    return {B[i] + B[j] for i in range(4) for j in range(i + 1, 4)}


def has_witness(A):
    # If every pair sum is in A subset [1,10], then the two largest
    # elements have sum at most 10, so all candidates lie in [1,9].
    for B in combinations(range(1, 10), 4):
        if pair_sums(B) <= A:
            return True, B
    return False, None

U = set(range(1, 11))
obstructions = []
for missing in range(1, 11):
    A = U - {missing}
    ok, B = has_witness(A)
    if not ok:
        obstructions.append(missing)
assert obstructions == [5], obstructions

# Independent exhaustive small-n check of the threshold values.
def h4_small(n):
    U = tuple(range(1, 2*n + 1))
    # Candidates only need elements below 2n; if all sums are in U,
    # then each summand is at most 2n-1.
    candidates = list(combinations(range(1, 2*n), 4))
    def has(A):
        A=set(A)
        return any(pair_sums(B) <= A for B in candidates)
    for h in range(0, n + 2):
        k=n+h
        if k > 2*n:
            return h
        if all(has(A) for A in combinations(U, k)):
            return h
    raise AssertionError('threshold not found')

small = [h4_small(n) for n in range(1, 6)]
assert small == [2, 3, 4, 4, 5], small

explicit = {
    1:(1,2,3,4), 2:(1,2,3,4), 3:(1,3,4,5), 4:(1,2,4,5),
    6:(1,2,3,6), 7:(1,2,3,7), 8:(1,2,3,4), 9:(1,2,3,4), 10:(1,2,3,4)
}
for missing,B in explicit.items():
    assert pair_sums(B) <= U-{missing}

print('VERIFY_OK complements=10 unique_obstruction_missing=5 small_h4=2,3,4,4,5')
