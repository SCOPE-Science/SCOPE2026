from math import comb, cos, pi, isclose


def filtered_binomial(q, h):
    return sum(comb(2*h, m) for m in range(2*h+1) if (m-h) % q == 0)


def double_expansion(q, h):
    # Coefficient sum from (1+z)^h(1+z^{-1})^h after q-root averaging.
    return sum(comb(h, k)*comb(h, ell)
               for k in range(h+1) for ell in range(h+1)
               if (k-ell) % q == 0)


def direct_moment(q, h, a, b):
    return sum(abs(a + b*complex(cos(2*pi*j/q), __import__('math').sin(2*pi*j/q)))**(2*h)
               for j in range(q)) / q

exact_cases = 0
for q in range(2, 19):
    for h in range(2, 15):
        B = filtered_binomial(q, h)
        D = double_expansion(q, h)
        assert B == D, (q, h, B, D)
        central = comb(2*h, h)
        assert (B == central) == (q > h), (q, h, B, central)
        # Nonzero surviving phase frequencies among |r-2k| <= r <= h.
        freqs = {abs(r-2*k) for r in range(h+1) for k in range(r+1)
                 if (r-2*k) != 0 and (r-2*k) % q == 0}
        assert (len(freqs) == 0) == (q > h), (q, h, freqs)
        if q <= h:
            assert q in freqs
        # The t^2 coefficient includes C(h,2) C(2,1) > 0.
        assert comb(h, 2) * comb(2, 1) > 0
        exact_cases += 1

# Deterministic numerical stress checks of the sharp inequality.
checks = 0
for q in (2, 3, 4, 5, 7, 11):
    for h in (2, 3, 4, 5, 7, 10):
        Kpow = filtered_binomial(q, h) / (2**h)
        for ra in (0.1, 0.4, 1.0, 2.5):
            for rb in (0.2, 0.7, 1.0, 3.0):
                for ph in (0.0, 0.17, 0.63, 1.1):
                    a = ra
                    b = rb * complex(cos(ph), __import__('math').sin(ph))
                    lhs = direct_moment(q, h, a, b)
                    rhs = Kpow * (abs(a)**2 + abs(b)**2)**h
                    assert lhs <= rhs * (1 + 2e-11) + 2e-11, (q, h, ra, rb, ph, lhs, rhs)
                    checks += 1
        # Aligned equal magnitudes are always extremal.
        lhs = direct_moment(q, h, 1.0, 1.0)
        rhs = Kpow * (2.0**h)
        assert isclose(lhs, rhs, rel_tol=2e-11, abs_tol=2e-11)
        # Above threshold the phase is free; below threshold a q-th-root phase is extremal.
        if q > h:
            b = complex(cos(0.371), __import__('math').sin(0.371))
        else:
            b = complex(cos(2*pi/q), __import__('math').sin(2*pi/q))
        lhs = direct_moment(q, h, 1.0, b)
        assert isclose(lhs, rhs, rel_tol=2e-11, abs_tol=2e-11)

print(f"VERIFY_OK exact_cases={exact_cases} numerical_checks={checks} threshold=exact equality=checked")
