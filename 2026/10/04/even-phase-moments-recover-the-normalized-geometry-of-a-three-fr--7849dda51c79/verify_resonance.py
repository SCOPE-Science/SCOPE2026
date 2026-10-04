from math import factorial, gcd, comb

def multinom(r, m):
    ans = factorial(r)
    for x in m:
        ans //= factorial(x)
    return ans

def direct_coefficients(r, A, B):
    terms = []
    for m0 in range(r + 1):
        for m1 in range(r - m0 + 1):
            m2 = r - m0 - m1
            m = (m0, m1, m2)
            terms.append((m, A*m1 + B*m2, multinom(r, m)))
    out = {}
    for m, f, cm in terms:
        for mp, fp, cp in terms:
            if f == fp:
                d = tuple(m[j] - mp[j] for j in range(3))
                out[d] = out.get(d, 0) + cm*cp
    return out

def predicted_coefficient(r, A, B, t):
    rem = r - t*B
    ans = 0
    for u0 in range(rem + 1):
        for u1 in range(rem - u0 + 1):
            u2 = rem - u0 - u1
            m = (u0, u1 + t*B, u2)
            mp = (u0 + t*(B-A), u1, u2 + t*A)
            ans += multinom(r, m)*multinom(r, mp)
    return ans

checks = 0
for r in range(1, 11):
    for B in range(2, 26):
        for A in range(1, B):
            if gcd(A, B) != 1:
                continue
            got = direct_coefficients(r, A, B)
            expected_keys = {(0,0,0)}
            for t in range(1, r//B + 1):
                v = (-(B-A)*t, B*t, -A*t)
                expected_keys.add(v)
                expected_keys.add(tuple(-x for x in v))
                assert got[v] == predicted_coefficient(r, A, B, t)
            assert set(got) == expected_keys
            if r < B:
                assert len(got) == 1
            if r == B:
                v = (-(B-A), B, -A)
                assert got[v] == comb(B, A)
            checks += 1
print(f"VERIFY_OK cases={checks} r_max=10 B_max=25 exact_integer_collision_check")
