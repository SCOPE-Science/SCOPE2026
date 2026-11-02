"""Exact wheel Padé positivity algebra checks (requires SymPy)."""
import sympy as S

T = S.symbols('t')


def wheel_laplacian(m):
    L = S.zeros(m + 1)
    for i in range(m):
        for j in ((i + 1) % m, m):
            L[i, i] += 1
            L[j, j] += 1
            L[i, j] -= 1
            L[j, i] -= 1
    return L


def pade_matrix(L):
    I = S.eye(L.rows)
    Q = I + T * L / 2 + T**2 * L**2 / 12
    N = I - T * L / 2 + T**2 * L**2 / 12
    return Q.inv() * N


def check(a, b):
    assert S.cancel(a - b) == 0, (S.factor(a), S.factor(b))


def finite_identity_checks():
    done = 0
    D5 = (3*T**2+3*T+1)*(121*T**4+462*T**3+720*T**2+504*T+144)
    D6 = ((T**2+3*T+3)*(4*T**2+6*T+3)
          *(25*T**2+30*T+12)*(49*T**2+42*T+12))
    F = 230*T**6-1440*T**5-6921*T**4-10440*T**3-7668*T**2-2808*T-432
    expected = {
        3: {1: 3*T/(4*T**2+6*T+3), 3: 3*T/(4*T**2+6*T+3)},
        4: {1: 12*T/(25*T**2+30*T+12),
            2: 24*T**2*(4*T+3)/((3*T**2+6*T+4)*(25*T**2+30*T+12)),
            4: 12*T/(25*T**2+30*T+12)},
        5: {1: T*(55*T**4+462*T**3+876*T**2+576*T+144)/D5,
            2: T**2*(451*T**3+858*T**2+576*T+144)/D5,
            5: T/(3*T**2+3*T+1)},
        6: {1: -3*T*F/D6,
            2: 3*T**2*(1730*T**5+6060*T**4+9039*T**3+6876*T**2+2664*T+432)/D6,
            3: 18*T**2*(370*T**5+1080*T**4+1257*T**3+768*T**2+252*T+36)/D6,
            6: 12*T/(49*T**2+42*T+12)},
    }
    for m, classes in expected.items():
        L = wheel_laplacian(m)
        M = pade_matrix(L)
        for d, want in classes.items():
            check(M[0, d], want)
            done += 1
        for i in range(m):
            for j in range(m):
                if i == j:
                    continue
                d = min((i-j) % m, (j-i) % m)
                check(M[i,j], classes[d])
        for i in range(m):
            check(M[i,m], classes[m])
        assert all(S.cancel(sum(M.row(i)) - 1) == 0 for i in range(m+1))
    print('finite_rational_offdiag_classes', done)
    return F


def pseudoinverse_checks():
    for m in range(3, 13):
        L = wheel_laplacian(m)
        N = m + 1
        J = S.ones(N)
        Lplus = (L + J/N).inv() - J/N
        B = S.Matrix(L[:m,:m])
        target = B.inv() - S.Rational(m+2, (m+1)**2)*S.ones(m)
        assert Lplus[:m,:m] == target
        assert S.simplify(Lplus[0,1] - Lplus[1,0]) == 0
    print('pseudoinverse_wheel_sizes', 10)


def root_and_asymptotic_checks(F):
    assert S.Poly(F, T).all_coeffs()[0] > 0
    assert all(v < 0 for v in S.Poly(F, T).all_coeffs()[1:])
    assert F.subs(T, S.Rational(491,50)) < 0
    assert F.subs(T, S.Rational(246,25)) > 0
    rho = (3-S.sqrt(5))/2
    bound = S.simplify(rho/S.sqrt(5)-S.Rational(8,49))
    assert S.simplify(bound-(147*S.sqrt(5)-325)/490) == 0
    assert bound.evalf() > 0
    for m in (6,7,9,15,32):
        L = wheel_laplacian(m)
        # Numerical reciprocal-polynomial matrix evaluation, not infinite certification.
        import numpy as np
        arr = np.asarray(L, dtype=float)
        eig, U = np.linalg.eigh(arr)
        t = 10**5
        z = t*eig
        rr = (1-z/2+z*z/12)/(1+z/2+z*z/12)
        p01 = float((U[0,:]*rr)@U[1,:])
        assert p01 < -1e-8, (m,p01)
    print('first_failing_wheel_root_bracket_and_large_step_samples', 5)


def main():
    F = finite_identity_checks()
    pseudoinverse_checks()
    root_and_asymptotic_checks(F)
    print('VERIFY_OK')

if __name__ == '__main__':
    main()
