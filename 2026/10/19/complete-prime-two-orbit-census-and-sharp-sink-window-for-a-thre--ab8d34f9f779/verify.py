"""Exact checks of the asymmetric two-step characteristic polynomial."""

from sympy import Matrix, eye, expand, simplify, sqrt, symbols


def main():
    X, Y, Z, B, lam = symbols("X Y Z B lambda", real=True)
    U = symbols("U", real=True, nonzero=True)
    V = -1 / U
    F = Matrix([Y**2, Y * Z, X - B])
    J = F.jacobian((X, Y, Z))

    def point(s, t, parameter):
        return Matrix([t**2, s, s**2 - parameter])

    def evaluate(expr, p, parameter):
        return expr.subs({X: p[0], Y: p[1], Z: p[2], B: parameter},
                         simultaneous=True).applyfunc(simplify)

    parameter = U**2 + V**2
    p, q = point(U, V, parameter), point(V, U, parameter)
    assert evaluate(F, p, parameter) == q.applyfunc(simplify)
    assert evaluate(F, q, parameter) == p.applyfunc(simplify)
    return_jacobian = evaluate(J, q, parameter) * evaluate(J, p, parameter)
    expected = lam**3 - lam**2 + 2 * (parameter**2 - 2) * lam - 4
    assert simplify(expand((lam * eye(3) - return_jacobian).det() - expected)) == 0

    for sign in (-1, 1):
        s, t = (sign + sqrt(5)) / 2, (sign - sqrt(5)) / 2
        p, q = point(s, t, 3), point(t, s, 3)
        assert evaluate(F, p, 3) == q.applyfunc(simplify)
        assert evaluate(F, q, 3) == p.applyfunc(simplify)
        return_jacobian = evaluate(J, q, 3) * evaluate(J, p, 3)
        expected = lam**3 - lam**2 + 14 * lam - 4
        assert simplify(expand((lam * eye(3) - return_jacobian).det() - expected)) == 0

    print("ASYMMETRIC_FLOQUET_CHECK_OK")


if __name__ == "__main__":
    main()
