"""Independent exact-rational verification of matching-fitness Moran stars.

Uses only the Python standard library. Invoke: python3 verify.py
"""
from fractions import Fraction as Q
from math import factorial


def solve(matrix, vector):
    """Exact Gauss-Jordan elimination on a rational linear system."""
    n = len(vector)
    aug = [list(matrix[i]) + [vector[i]] for i in range(n)]
    for col in range(n):
        pivot = next((i for i in range(col, n) if aug[i][col]), None)
        if pivot is None:
            raise ArithmeticError('singular transient system')
        aug[col], aug[pivot] = aug[pivot], aug[col]
        z = aug[col][col]
        aug[col] = [v / z for v in aug[col]]
        for row in range(n):
            if row != col and aug[row][col]:
                coeff = aug[row][col]
                aug[row] = [a - coeff * b for a, b in zip(aug[row], aug[col])]
    return [aug[i][-1] for i in range(n)]


def exact_chain(ell, r):
    """Enumerate all 2**(ell+1) labelled configurations, not symmetry states."""
    n = ell + 1
    all_red = (1 << n) - 1
    transient = [state for state in range(1, all_red)]
    indices = {state: i for i, state in enumerate(transient)}
    m = len(transient)
    mat = [[Q(int(i == j)) for j in range(m)] for i in range(m)]
    direct_fixation = [Q(0) for _ in range(m)]
    num_nonzero_transitions = 0
    for state, i in indices.items():
        typ = [(state >> j) & 1 for j in range(n)]
        env = [1] + [0] * ell
        fitness = [r if typ[j] == env[j] else Q(1) for j in range(n)]
        total = sum(fitness)
        # Original graph is a labelled star, 0 is the hub.
        for parent in range(n):
            neighbors = list(range(1, n)) if parent == 0 else [0]
            for target in neighbors:
                probability = fitness[parent] / (total * len(neighbors))
                next_state = (state | (1 << target)) if typ[parent] else (state & ~(1 << target))
                if next_state == all_red:
                    direct_fixation[i] += probability
                elif next_state in indices:
                    mat[i][indices[next_state]] -= probability
                num_nonzero_transitions += 1
    h = solve(mat, direct_fixation)
    # g(state)=E[duration * 1_{fixation}]; g=h+Qg, so (I-Q)g=h.
    g = solve(mat, h)
    initial = indices[1]
    return h[initial], g[initial] / h[initial], num_nonzero_transitions


def harmonic(n):
    return sum((Q(1, j) for j in range(1, n + 1)), Q(0))


def coefficients(ell):
    l = Q(ell)
    d = l*l + 1
    a = l**4 * (l-1) * (2*l-1) / (6*(l+1)*d)
    b = l/(l+1) * (l + harmonic(ell) + l**3*(l-1)*(l+4)/(3*d))
    c = a + l/(l+1) * (l * harmonic(ell-1) - (l-1))
    return a,b,c


def verify_embedded_chain(ell):
    d = ell * ell + 1
    # Direct balance of visit counts in the jump chain and the Doob transform.
    u = [Q(d - ell*k, d) for k in range(ell)]
    v = [Q(0)] + [Q(ell*(ell-k), d) for k in range(1,ell)] + [Q(0)]
    assert u[0] == 1
    for k in range(1,ell):
        assert u[k] == (u[k-1] + ell*v[k])/Q(ell+1)
    for k in range(1,ell):
        assert v[k] == (ell*u[k] + v[k+1])/Q(ell+1)
    hh_a = [Q(1+ell*k,d) for k in range(ell)]
    hh_b = [Q(ell*k,d) for k in range(1,ell)]
    for k in range(ell):
        left = (hh_a[k+1] if k<ell-1 else Q(1)) + ell*(hh_b[k-1] if k>=1 else Q(0))
        assert hh_a[k] == left/Q(ell+1)
    for k in range(1,ell):
        left = (hh_b[k-2] if k>=2 else Q(0)) + ell*hh_a[k]
        assert hh_b[k-1] == left/Q(ell+1)
    # Independently rebuild A,B,C by summing conditioned-state visits.
    A = B = C = Q(0)
    for k in range(ell):
        U = u[k] * hh_a[k] / hh_a[0]
        B += U * Q(ell,ell+1)*(1+Q(1,ell-k))
        C += U * Q(ell,ell+1) * Q(k,ell-k)
    for k in range(1,ell):
        V = v[k] * hh_b[k-1] / hh_a[0]
        B += V * Q(ell,ell+1)*(1+Q(1,k))
        A += V * Q(ell,ell+1)*Q(ell-k,k)
    assert (A,B,C)==coefficients(ell), (ell, (A,B,C),coefficients(ell))
    assert A>0 and C>A
    return A,B,C


def main():
    assertions = 0
    for ell in range(2,7):
        a,b,c = verify_embedded_chain(ell)
        assertions += 4*ell
        if ell <= 5:
            for r in (Q(1,2), Q(1), Q(6,5), Q(3,2), Q(2), Q(3)):
                actual_p, actual_t, _ = exact_chain(ell,r)
                assert actual_p == Q(1,ell*ell+1), (ell,r,actual_p)
                assert actual_t == a*r + b + c/r, (ell,r,actual_t,a*r+b+c/r)
                assertions += 2
        print('star leaves =',ell,'A,B,C =',a,b,c)
    print('PASS: independent full-configuration chain and embedded-chain formulas;',assertions,'exact assertions')

if __name__=='__main__':
    main()
