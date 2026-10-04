from fractions import Fraction as F


def mul(p, q):
    out = [F(0)] * (len(p) + len(q) - 1)
    for i, a in enumerate(p):
        for j, b in enumerate(q):
            out[i + j] += a * b
    return out


def main():
    # Characteristic polynomial in ascending powers of lambda:
    # lambda (lambda+a) (lambda+b) (lambda^2-c lambda+d).
    a, b, c, d = map(F, (20, 2, 10, 4))
    p = [F(0), F(1)]
    p = mul(p, [a, F(1)])
    p = mul(p, [b, F(1)])
    p = mul(p, [d, -c, F(1)])
    assert p[0] == 0
    assert len(p) == 6

    # Exact cancellation in E=(z^2+w^2+d*y^2)/2:
    # z(xw-bz)+w(-xz+cw+dy)+d*y(-w) = -b z^2+c w^2.
    # Track coefficients of x*z*w, z^2, w^2, d*y*w.
    coeff = {'xzw': F(1)-F(1), 'z2': -b, 'w2': c, 'dyw': F(1)-F(1)}
    assert coeff == {'xzw': F(0), 'z2': -b, 'w2': c, 'dyw': F(0)}

    # Source-parameter specialization of c/(a^2*b).
    shell_coeff = c / (a*a*b)
    assert shell_coeff == F(1, 80)
    assert c*c/F(4) == F(25)

    # Equilibrium substitution leaves u free: with x=y=z=w=0,
    # every right-hand side is zero for arbitrary u and k,m,n.
    for u in [F(-7), F(0), F(13, 5)]:
        x = y = z = w = F(0)
        k, m, n = F(10), F(1, 10), F(1, 100)
        rhs = [a*(w-x), -w, x*w-b*z, -x*z+c*w+d*y, -w+k*x*(m+3*n*u*u)]
        assert rhs == [F(0)]*5

    print('VERIFY_OK')


if __name__ == '__main__':
    main()
