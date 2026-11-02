"""Exact symbolic checks for two-state harmonic-trap covariance camouflage.

Requires SymPy. Execute ``python verify.py``.
The universal inequalities and ODE uniqueness are proved in RESULT.md;
the assertions here reproduce the nontrivial rational identities.
"""
import sympy as sp


def equal(left, right, label):
    if sp.cancel(left - right) != 0:
        raise AssertionError(label)
    return 1


def main():
    k1, k2, alpha, beta, D, rho = sp.symbols(
        'k1 k2 alpha beta D rho', positive=True
    )
    ones = sp.Matrix([[1, 1]])
    Qstar = sp.Matrix([[-alpha, beta], [alpha, -beta]])
    K = sp.diag(k1, k2)
    q = alpha + beta
    pi = sp.Matrix([beta / q, alpha / q])
    w2 = 2 * D * (2 * K - Qstar).inv() * pi
    variance = sp.factor((ones * w2)[0])
    w4 = 12 * D * (4 * K - Qstar).inv() * w2
    fourth = sp.factor((ones * w4)[0])
    cumulant = sp.factor(fourth - 3 * variance**2)
    T = k1 + k2 + q
    Delta = k1 * k2 + k1 * beta + k2 * alpha
    effective_rate = D / variance
    checks = 0
    checks += equal(
        variance,
        D * (q**2 + 2 * alpha * k1 + 2 * beta * k2)
        / (q * (2 * k1 * k2 + alpha * k2 + beta * k1)),
        'stationary variance',
    )
    checks += equal(
        effective_rate**2 - T * effective_rate + Delta,
        alpha * beta * (k2-k1)**2
        * (q**2 + 2*(beta-alpha)*(k2-k1) - 4*k1*k2)
        / (q**2 + 2*alpha*k1 + 2*beta*k2)**2,
        'single-exponential necessary condition',
    )
    ar = (rho - k1) * (rho + k2) / (k2 - k1)
    br = (k2 - rho) * (rho + k1) / (k2 - k1)
    tuned = {alpha: ar, beta: br}
    checks += equal((alpha+beta).subs(tuned, simultaneous=True), 2*rho, 'rate sum')
    checks += equal(variance.subs(tuned, simultaneous=True), D/rho, 'tuned variance')
    checks += equal((effective_rate**2 - T*effective_rate + Delta).subs(
        tuned, simultaneous=True), 0, 'tuned characteristic root')
    checks += equal(
        cumulant.subs(tuned, simultaneous=True),
        9*D**2*(rho-k1)*(k2-rho)
        / (rho**2*(rho**2 + rho*(k1+k2) + 3*k1*k2)),
        'tuned fourth cumulant',
    )
    checks += equal(
        (ones * ((Qstar-K)*w2))[0], -D, 'covariance right derivative'
    )
    # Compare the fourth-moment computation with the Gaussian-mixture variance.
    checks += equal((cumulant/3), fourth/3 - variance**2, 'mixture variance relation')
    from fractions import Fraction
    for v1 in (Fraction(1, 4), Fraction(1, 2), Fraction(1)):
        for r in (Fraction(1), Fraction(2), Fraction(3)):
            for v2 in (Fraction(4), Fraction(5), Fraction(7)):
                for noise in (Fraction(1, 3), Fraction(1), Fraction(2)):
                    if not (v1 < r < v2):
                        continue
                    values = {k1: sp.Rational(v1.numerator,v1.denominator),
                              k2: sp.Rational(v2.numerator,v2.denominator),
                              rho: sp.Rational(r.numerator,r.denominator),
                              D: sp.Rational(noise.numerator,noise.denominator)}
                    a_num = ar.subs(values)
                    b_num = br.subs(values)
                    assert a_num > 0 and b_num > 0
                    actual = {k1:values[k1], k2:values[k2],
                              alpha:a_num,beta:b_num,D:values[D]}
                    assert sp.cancel(variance.subs(actual) - values[D]/values[rho]) == 0
                    checks += 1
                    assert sp.cancel(cumulant.subs(actual) -
                            9*values[D]**2*(values[rho]-values[k1])*(values[k2]-values[rho]) /
                            (values[rho]**2 * (values[rho]**2+values[rho]*(values[k1]+values[k2])+3*values[k1]*values[k2]))) == 0
                    checks += 1
                    assert cumulant.subs(actual) > 0
                    checks += 1
    sample = {k1:sp.Integer(1), k2:sp.Integer(4),
              alpha:sp.Integer(2),beta:sp.Integer(2),D:sp.Integer(1)}
    checks += equal(variance.subs(sample),sp.Rational(1,2),'example variance')
    checks += equal(cumulant.subs(sample),sp.Rational(9,52),'example cumulant')
    checks += equal(fourth.subs(sample),sp.Rational(12,13),'example fourth moment')
    checks += equal((fourth/variance**2).subs(sample),sp.Rational(48,13),'example kurtosis')
    off = {k1:1,k2:4,alpha:1,beta:2,D:1}
    assert (effective_rate**2 - T*effective_rate + Delta).subs(off) != 0
    checks += 1
    print(f'PASS: {checks} exact symbolic and rational identity checks')

if __name__ == '__main__':
    main()
