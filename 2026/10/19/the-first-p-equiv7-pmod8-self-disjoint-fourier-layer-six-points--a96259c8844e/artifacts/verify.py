"""Exact test of the smallest self-disjoint Fourier support on (Z/7Z)^2.

Run with Python 3.10 or later: python verify.py
All calculations use integer arithmetic, never floating point.
"""
from itertools import combinations, permutations
from math import comb

P = 7
POINTS = tuple((a, b) for a in range(P) for b in range(P))
DOT = tuple(tuple((a*c + b*d) % P for c, d in POINTS) for a, b in POINTS)
FIELD_ROOTS = ((29, 7), (43, 4), (71, 20), (113, 16))


def primitive_root_p(q, root):
    return root != 1 and pow(root, P, q) == 1 and all(pow(root, j, q) != 1 for j in range(1, P))


def modular_nonzero(indices, q, powers, inverses):
    n = len(indices)
    a = [[powers[DOT[x][y]] for y in indices] for x in indices]
    for k in range(n):
        pivot = next((i for i in range(k, n) if a[i][k]), None)
        if pivot is None:
            return False
        if pivot != k:
            a[k], a[pivot] = a[pivot], a[k]
        inv = inverses[a[k][k]]
        row_k = a[k]
        for i in range(k+1, n):
            row_i = a[i]
            if row_i[k]:
                factor = row_i[k]*inv % q
                for j in range(k+1, n):
                    row_i[j] = (row_i[j] - factor*row_k[j]) % q
                row_i[k] = 0
    return True


def exact_det_zero(indices, perms):
    """In Z[X]/(X^7-1): a zero 7-coefficient vector proves det=0."""
    rows = [[DOT[x][y] for y in indices] for x in indices]
    c = [0]*P
    for perm, sign in perms:
        exponent = sum(rows[i][perm[i]] for i in range(len(indices))) % P
        c[exponent] += sign
    # A cyclotomic zero occurs iff the seven coefficients are constant.
    # Since the determinant's coefficient sum is zero, constant means all zero.
    assert sum(c) == 0
    return c == [0]*P


def permutation_signs(n):
    out = []
    for p in permutations(range(n)):
        inversions = sum(p[i] > p[j] for i in range(n) for j in range(i+1, n))
        out.append((p, -1 if inversions % 2 else 1))
    return out


def main():
    setups = []
    for q, root in FIELD_ROOTS:
        assert primitive_root_p(q, root), (q, root)
        powers = [pow(root, j, q) for j in range(P)]
        inverses = [0]*q
        for a in range(1, q):
            inverses[a] = pow(a, q-2, q)
        setups.append((q,powers,inverses))
    assert all(setups[0][1][j] != setups[0][1][k] for j in range(P) for k in range(j+1,P))
    total_zero = {}
    survivor_counts = {}
    all_exact_sixes = []
    for n in range(1, 7):
        counts = [0]*len(setups)
        exact_count = 0
        perms = permutation_signs(n) if n == 6 else None
        for tail in combinations(range(1,49),n-1):
            indices=(0,)+tail
            for k,(q,powers,inverses) in enumerate(setups):
                if modular_nonzero(indices,q,powers,inverses):
                    break
                counts[k] += 1
            else:
                # For minimality, the four-modulus filter is a sufficient
                # nonvanishing certificate without further exact checks.
                # At size 6 its survivors are inspected exactly.
                if n < 6:
                    raise AssertionError('Unexpected potentially singular small principal minor: '+str(indices))
                if exact_det_zero(indices,perms):
                    exact_count += 1
                    all_exact_sixes.append(indices)
        if n == 6:
            total_zero[n] = exact_count
        survivor_counts[n] = counts
        print('size=%s translated_index_sets=%s zero_mod_filters=%s exact_singular=%s' %
              (n, comb(48,n-1), counts,
               exact_count if n==6 else 0),flush=True)
    # Exactly 672 six-element sets containing the origin give 5488 total
    # singular principal minors, each with a one-dimensional kernel.
    assert total_zero[6] == 672, total_zero[6]
    assert total_zero[6]*49 % 6 == 0
    assert total_zero[6]*49 // 6 == 5488
    witness = ((0,0),(0,1),(0,2),(2,0),(2,1),(2,6))
    lookup = {point:i for i,point in enumerate(POINTS)}
    witness_ids = tuple(sorted(lookup[z] for z in witness))
    assert witness_ids in set(all_exact_sixes)
    assert exact_det_zero(witness_ids,permutation_signs(6))
    # Classify all minimal supports under translations and dot-product similitudes.
    def translate_to_zero(S):
        return min(tuple(sorted(((x-a)%P,(y-b)%P) for x,y in S)) for a,b in S)

    six_sets = [tuple(POINTS[i] for i in S) for S in all_exact_sixes]
    translated_classes = {translate_to_zero(S) for S in six_sets}
    assert len(translated_classes) == 112
    matrices = []
    for a in range(P):
        for b in range(P):
            if not (a or b):
                continue
            matrices += [((a,-b),(b,a)), ((a,b),(b,-a))]
    assert len(matrices) == 96

    def transform(A,S):
        return tuple(((A[0][0]*x+A[0][1]*y)%P,
                      (A[1][0]*x+A[1][1]*y)%P) for x,y in S)

    unseen = set(translated_classes)
    orbit_records = []
    while unseen:
        rep = min(unseen)
        members = {translate_to_zero(transform(A,rep)) for A in matrices}
        assert members <= translated_classes
        unseen -= members
        orbit_records.append((rep,len(members),P*P*len(members)))
    assert [z[1] for z in orbit_records] == [48,16,48], orbit_records
    assert sum(z[2] for z in orbit_records) == 5488
    for rep, reduced_size, total_size in orbit_records:
        print('orbit:', rep, 'translation_classes:', reduced_size,
              'total_supports:', total_size)
    print('VERIFY_OK: all sizes <=5 nonsingular, 672 translated six-set minors, 5488 total six-set minors, three affine-similitude orbits')

if __name__ == '__main__':
    main()
