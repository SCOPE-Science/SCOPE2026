from math import gcd, isqrt


def direct_age_status(r, a, b):
    def chart(m, c):
        canonical = True
        terminal = True
        for j in range(1, m):
            num = r*j + (j*c) % m
            canonical &= num >= m
            terminal &= num > m
        return canonical, terminal
    ca, ta = chart(a, b)
    cb, tb = chart(b, a)
    return ca and cb, ta and tb


def direct_pairs(r):
    # The Gorenstein conditions imply canonicality and hence b-a<=r, a<=r+b-a,
    # so b<=3r. This is a proven finite box, not a heuristic cutoff.
    out = set()
    for a in range(1, 2*r + 1):
        for b in range(a, 3*r + 1):
            h = r + a + b
            if h % a == 0 and h % b == 0:
                out.add((a, b))
    return out


def core_pairs(r):
    out = set()
    for k in range(1, r + 1):
        if r % k:
            continue
        for g in range(1, k + 3):
            n = g*k + 1
            for B in range(1, isqrt(n) + 1):
                if n % B:
                    continue
                A = n // B
                if A < B:
                    continue
                if (A + 1) % g or (B + 1) % g:
                    continue
                u, v = (A + 1)//g, (B + 1)//g
                if gcd(u, v) != 1:
                    continue
                kk = g*u*v - u - v
                assert kk == k
                a = (r//k)*v
                b = (r//k)*u
                out.add((a, b))
    return out


def divisor_count(n):
    return sum(n % d == 0 for d in range(1, n + 1))

for r in range(2, 101):
    direct = direct_pairs(r)
    core = core_pairs(r)
    assert direct == core, (r, direct ^ core)

    expected_nonterminal = {(2*r//t, r + 2*r//t) for t in range(1, 2*r + 1) if 2*r % t == 0}
    expected_nonterminal.add((r, r))

    observed_nonterminal = set()
    for a, b in direct:
        h = r + a + b
        x, y = h//a, h//b
        canonical, terminal = direct_age_status(r, a, b)
        assert canonical
        assert terminal == (y > 2 and x > 3), (r, a, b, x, y)
        if not terminal:
            observed_nonterminal.add((a, b))

    assert observed_nonterminal == expected_nonterminal, (r, observed_nonterminal, expected_nonterminal)
    assert len(observed_nonterminal) == divisor_count(2*r) + 1

print('VERIFY_OK r=2..100; finite divisor-core parameterization, canonicality, terminal criterion, boundary family and count all agree with direct Gorenstein divisibility and chart ages')
