"""Standard-library check of a sharp three-erasure finite Fourier frame bound.

Recomputes small principal Gram matrices without using the closed-form
largest-eigenvalue expression as an eigenvalue routine. This is supporting
finite testing; the proof for all orders is mathematical, not experimental.
"""
import math
from itertools import combinations


def leading_eigenvalue(a):
    """Largest eigenvalue of a real symmetric 3-by-3 matrix by Jacobi sweeps."""
    a = [list(row) for row in a]
    for _ in range(100):
        p, q = max(((0, 1), (0, 2), (1, 2)), key=lambda ij: abs(a[ij[0]][ij[1]]))
        if abs(a[p][q]) < 2e-14:
            break
        h = a[p][q]
        tau = (a[q][q] - a[p][p]) / (2 * h)
        t = (1 if tau >= 0 else -1) / (abs(tau) + math.sqrt(1 + tau * tau))
        c = 1 / math.sqrt(1 + t * t)
        s = t * c
        app, aqq = a[p][p], a[q][q]
        a[p][p] = app - t * h
        a[q][q] = aqq + t * h
        a[p][q] = a[q][p] = 0.0
        for k in range(3):
            if k != p and k != q:
                akp, akq = a[k][p], a[k][q]
                a[k][p] = a[p][k] = c * akp - s * akq
                a[k][q] = a[q][k] = s * akp + c * akq
    return max(a[0][0], a[1][1], a[2][2])


def dirichlet(n, distance):
    return 1 + 2 * math.cos(2 * math.pi * distance / n)


def predicted(n):
    d1, d2 = dirichlet(n, 1), dirichlet(n, 2)
    return 3 + (d2 + math.sqrt(d2*d2 + 8*d1*d1))/2


def consecutive(n, inds):
    return any(set(inds) == {(b+j) % n for j in range(3)} for b in range(n))


def main():
    orders = range(6, 49)
    triples_checked = 0
    largest_err = 0.0
    smallest_gap = 1.0
    for n in orders:
        goal = predicted(n)
        max_seen = -1.0
        maximizers = 0
        best_nonconsecutive = -1.0
        for inds in combinations(range(n), 3):
            triples_checked += 1
            a,b,c = inds
            matrix = [[3., dirichlet(n, a-b), dirichlet(n, a-c)],
                      [dirichlet(n, a-b), 3., dirichlet(n, b-c)],
                      [dirichlet(n, a-c), dirichlet(n, b-c), 3.]]
            v = leading_eigenvalue(matrix)
            max_seen = max(max_seen, v)
            if abs(v-goal) < 2e-9:
                assert consecutive(n, inds), (n, inds, v, goal)
                maximizers += 1
            else:
                assert v < goal - 1e-9, (n, inds, v, goal)
                best_nonconsecutive = max(best_nonconsecutive, v)
        assert maximizers == n, (n, maximizers)
        assert abs(max_seen - goal) < 2e-9, (n, max_seen, goal)
        largest_err = max(largest_err, abs(max_seen-goal))
        smallest_gap = min(smallest_gap, goal-best_nonconsecutive)
        assert 0 < 1 - goal/n < 1
    print('orders_tested:', len(orders), 'from', min(orders), 'through', max(orders))
    print('erasure_triples_checked:', triples_checked)
    print('exact_maximizer_count_per_order: N cyclic translates')
    print('largest_absolute_eigenvalue_formula_error:', format(largest_err, '.5g'))
    print('smallest_nonmaximizer_eigenvalue_gap:', format(smallest_gap, '.5g'))
    print('status: all finite corroboration checks passed')

if __name__=='__main__':
    main()
