"""Exact arithmetic tests for the stated finite binomial gcd formula.
Standard library only. These tests are not the infinite proof.
"""
from math import comb, gcd


def factors(n):
    f = {}
    p = 2
    while p * p <= n:
        if n % p == 0:
            a = 0
            while n % p == 0:
                n //= p
                a += 1
            f[p] = a
        p += 1 if p == 2 else 2
    if n > 1:
        f[n] = 1
    return f


def predicted(n):
    ans = 1
    for p, a in factors(n).items():
        m = n // p**a
        L, power = 0, 1
        while power * p <= m:
            power *= p
            L += 1
        ans *= p**max(0, a - L)
    return ans


def exact_v_binomial(n, k, p):
    v = 0
    d = p
    while d <= n:
        v += n // d - k // d - (n - k) // d
        d *= p
    return v


def observed_v(n, p):
    k = n - 1
    return min(exact_v_binomial(q*k, k, p) for q in range(2, n+1))


def main():
    tested = 0
    for n in range(3, 1201):
        prediction = predicted(n)
        obs = 1
        for p in factors(n):
            obs *= p**observed_v(n,p)
        assert obs == prediction, (n, obs, prediction)
        tested += 1
    # Direct large-binomial gcd, independent of valuation arithmetic.
    direct_cases = 0
    for n in range(3, 81):
        k = n - 1
        g = 0
        for q in range(2, n+1):
            g = gcd(g, comb(q*k,k))
        assert g == predicted(n), (n,g,predicted(n))
        direct_cases += 1
    # Check the special upper-witness identity separately.
    witness_cases = 0
    for n in range(3, 401):
        for p,a in factors(n).items():
            P=p**a
            m=n//P
            if m>=P or m<2:continue
            for t in range(1,m):
                q=1+t*P
                left=exact_v_binomial(q*(n-1),n-1,p)
                right=a-exact_v_binomial(m-1,t,p)
                assert left==right,(n,p,t,left,right)
                witness_cases+=1
    print('CERTIFICATE_OK n_formulas=',tested, 'direct_gcd_cases=',direct_cases,'witness_identity_cases=',witness_cases)

if __name__=='__main__': main()
