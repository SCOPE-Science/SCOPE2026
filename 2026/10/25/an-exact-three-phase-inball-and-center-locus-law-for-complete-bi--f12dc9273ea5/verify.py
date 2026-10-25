"""Exact-arithmetic checks of cut-distance and center-contact classification."""
from fractions import Fraction
from itertools import combinations


def rank(vectors):
    if not vectors:
        return 0
    mat = [[Fraction(a) for a in v] for v in vectors]
    rows, cols = len(mat), len(mat[0])
    r = 0
    for c in range(cols):
        pivot = next((i for i in range(r, rows) if mat[i][c] != 0), None)
        if pivot is None:
            continue
        mat[r], mat[pivot] = mat[pivot], mat[r]
        val = mat[r][c]
        mat[r] = [z/val for z in mat[r]]
        for k in range(rows):
            if k != r and mat[k][c]:
                factor = mat[k][c]
                mat[k] = [mat[k][j]-factor*mat[r][j] for j in range(cols)]
        r += 1
        if r == rows:
            break
    return r


def verify():
    orbit_checks = 0
    for p in range(2, 22):
        for q in range(p, 71):
            n = p + q
            rho2 = min(n, (p+1)**2)
            for a in range(p+1):
                for b in range(q+1):
                    t = a+b
                    if t == 0 or (a == 0 and b > 1) or (b == 0 and a > 1):
                        # Only connected vertex subsets determine facets.
                        continue
                    delta = a*(q-b)+b*(p-a)
                    v = t+delta
                    assert v*v >= rho2*t
                    equal = v*v == rho2*t
                    predicted = ((t == n and n <= (p+1)**2)
                                 or (a == 0 and b == 1 and n >= (p+1)**2))
                    assert equal == predicted, (p,q,a,b,equal,predicted)
                    orbit_checks += 1
    subset_checks = 0
    rank_checks = 0
    for p in range(2, 6):
        for q in range(p, 10):
            n = p+q
            rho2 = min(n, (p+1)**2)
            contact_normals=[]
            for subset in range(1, 1 << n):
                a=(subset & ((1 << p)-1)).bit_count()
                b=(subset >> p).bit_count()
                t=a+b
                if (a == 0 and b > 1) or (b == 0 and a > 1):
                    continue
                delta=a*(q-b)+b*(p-a)
                v=t+delta
                assert v*v >= rho2*t
                if v*v == rho2*t:
                    contact_normals.append([(subset >> j)&1 for j in range(n)])
                subset_checks+=1
            expected_dim=(n-1 if n < (p+1)**2 else p-1 if n == (p+1)**2 else p)
            actual_dim=n-rank(contact_normals)
            assert actual_dim==expected_dim,(p,q,actual_dim,expected_dim)
            rank_checks+=1
    print('EXACT_OK orbit_cut_tests=',orbit_checks,
          'explicit_connected_subset_tests=',subset_checks,
          'contact_normal_rank_cases=',rank_checks)

if __name__=='__main__':
    verify()
