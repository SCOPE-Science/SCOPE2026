from math import comb

def D(n,m):
    return comb(m+2*n-3,m) + 2*n - 2

def G(n,d,m):
    return comb(d+2*n-3,2*n-2) - comb(d-m+2*n-3,2*n-2)

def A(n,d,m):
    return comb(d+2*n-2,2*n-2) - comb(d-m+2*n-2,2*n-2)

checks = 0

for n in range(4, 51):
    # m=2, d>=4 boundary identity and monotonicity sample.
    closed = 2*(n-1)*(n+1)*(2*n-3)//3
    assert G(n,4,2) - D(n,2) == closed
    assert closed > 0
    prev = G(n,4,2)
    for d in range(5, 81):
        cur = G(n,d,2)
        assert cur > prev
        assert cur > D(n,2)
        prev = cur
        checks += 1

    # m>=3 boundary identity and sampled monotonicity.
    for m in range(3, 21):
        rhs = comb(m+2*n-3,m-1) - (2*n-1)
        assert G(n,m+1,m) - D(n,m) == rhs
        assert rhs > 0
        prev = G(n,m+1,m)
        for d in range(m+2, m+16):
            cur = G(n,d,m)
            assert cur > prev
            assert cur > D(n,m)
            prev = cur
            checks += 1

    # Cubic-quadric two-cone arithmetic.
    d2 = D(n,2)
    assert d2 == (n-1)*(2*n+1)
    h0 = comb(2*n,3) - 4*n + 4
    h2 = comb(2*n,3) - 2*n + 2
    a = A(n,3,2)
    assert a - h0 == d2 + 2*n - 2
    assert a - h2 == d2
    assert 2*n - 1 < d2
    assert 4*n - 4 < d2
    assert 2*n - 4 >= 4
    checks += 7

print(f"finite_identity_and_inequality_checks={checks}")
print("m_ge_3_boundary_identity=ok")
print("m_eq_2_d_eq_4_closed_form=ok")
print("cubic_quadric_codimensions=ok")
print("cubic_quadric_stratum_inequalities=ok")
print("VERIFY_OK")
