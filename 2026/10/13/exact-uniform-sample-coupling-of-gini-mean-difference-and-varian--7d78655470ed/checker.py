from fractions import Fraction

def poly_add(a, b):
    n = max(len(a), len(b))
    out = [Fraction(0) for _ in range(n)]
    for i, v in enumerate(a):
        out[i] += v
    for i, v in enumerate(b):
        out[i] += v
    return out

def poly_scale(a, c):
    return [c*v for v in a]

def poly_mul(a, b):
    out = [Fraction(0) for _ in range(len(a)+len(b)-1)]
    for i, x in enumerate(a):
        for j, y in enumerate(b):
            out[i+j] += x*y
    return out

def integrate_01(a):
    return sum((c/Fraction(i+1) for i, c in enumerate(a)), Fraction(0))

def absdiff_moment(p):
    # 2 * integral_{0<y<x<1} (x-y)^p dy dx
    return Fraction(2, (p+1)*(p+2))

def run(max_n=10000):
    # Conditional means of h=|X-Y| and g=(X-Y)^2/2.
    a = [Fraction(1,2), Fraction(-1), Fraction(1)]
    b = [Fraction(1,6), Fraction(-1,2), Fraction(1,2)]

    Eh = absdiff_moment(1)
    Eg = absdiff_moment(2) / 2
    assert Eh == Fraction(1,3)
    assert Eg == Fraction(1,12)

    Eh2 = absdiff_moment(2)
    Eg2 = absdiff_moment(4) / 4
    Ehg = absdiff_moment(3) / 2

    same_h = Eh2 - Eh*Eh
    same_g = Eg2 - Eg*Eg
    same_hg = Ehg - Eh*Eg
    assert same_h == Fraction(1,18)
    assert same_g == Fraction(7,720)
    assert same_hg == Fraction(1,45)

    Ea2 = integrate_01(poly_mul(a,a))
    Eb2 = integrate_01(poly_mul(b,b))
    Eab = integrate_01(poly_mul(a,b))

    overlap_h = Ea2 - Eh*Eh
    overlap_g = Eb2 - Eg*Eg
    overlap_hg = Eab - Eh*Eg
    assert overlap_h == Fraction(1,180)
    assert overlap_g == Fraction(1,720)
    assert overlap_hg == Fraction(1,360)

    centered_a = poly_add(a, [Fraction(-1,3)])
    centered_b = poly_add(b, [Fraction(-1,12)])
    assert centered_a == poly_scale(centered_b, Fraction(2))

    # q = |X-Y| - (X-Y)^2 has mean 1/6.
    Eq = absdiff_moment(1) - absdiff_moment(2)
    Eq2 = (
        absdiff_moment(2)
        - 2*absdiff_moment(3)
        + absdiff_moment(4)
    )
    varq = Eq2 - Eq*Eq
    assert Eq == Fraction(1,6)
    assert varq == Fraction(1,180)

    formula_checks = 0
    monotonic_checks = 0
    prev_corr2 = None
    for n in range(2, max_n+1):
        M = Fraction(n*(n-1), 2)

        varG = (same_h + 2*(n-2)*overlap_h) / M
        varS = (same_g + 2*(n-2)*overlap_g) / M
        cov = (same_hg + 2*(n-2)*overlap_hg) / M

        assert varG == Fraction(n+3, 45*n*(n-1))
        formula_checks += 1
        assert varS == Fraction(2*n+3, 360*n*(n-1))
        formula_checks += 1
        assert cov == Fraction(n+2, 90*n*(n-1))
        formula_checks += 1

        corr2 = cov*cov/(varG*varS)
        target_corr2 = Fraction(2*(n+2)*(n+2), (n+3)*(2*n+3))
        assert corr2 == target_corr2
        formula_checks += 1
        assert 1-corr2 == Fraction(n+1, (n+3)*(2*n+3))
        formula_checks += 1

        contrast_var = varq / M
        assert contrast_var == Fraction(1, 90*n*(n-1))
        formula_checks += 1

        if prev_corr2 is not None:
            assert corr2 > prev_corr2
            monotonic_checks += 1
        prev_corr2 = corr2

    print("VERIFY_OK")
    print(f"max_n={max_n}")
    print(f"formula_checks={formula_checks}")
    print(f"monotonicity_checks={monotonic_checks}")
    print("exact_kernel_moment_checks=12")

if __name__ == "__main__":
    run()
