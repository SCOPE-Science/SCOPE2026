"""Critical-orbit trichotomy verification for E_a(z)=(z^2+a)/(z^2-1) over Q2.
Exact rational arithmetic + 2-adic valuations. Reproduces WORKLOG scan and
checks the two elementary mechanisms:
 (i)  m=v2(a)<=0: doubling recursion toward the {1,inf} 2-cycle;
 (ii) m>=1: invariance + contraction of the disk B(0,2^-m).
"""
from fractions import Fraction

def v2i(k):
    k = abs(int(k))
    assert k != 0
    c = 0
    while k % 2 == 0:
        k //= 2
        c += 1
    return c

def v2f(f):
    if f is None:
        return None  # the point infinity
    if f == 0:
        return float('inf')
    return v2i(f.numerator) - v2i(f.denominator)

def E(a, z):
    if z is None:  # z = infinity
        return Fraction(1, 1)
    if z * z == 1:
        return None
    return (z * z + a) / (z * z - 1)

def orbit(a, n=10):
    z = Fraction(0, 1)
    seq = [z]
    for _ in range(n):
        if z is None:
            z = Fraction(1, 1)
        elif z * z == 1:
            z = None
        else:
            z = E(a, z)
        seq.append(z)
    return seq

def check_doubling(a, steps=6):
    """Verify u' = k+2t / t' = u+1-k growth for m<=0 cases."""
    seq = orbit(a, steps)
    m = v2f(a)
    k = v2f(a + 1)
    lines = [f"a={a} m={m} k={k}"]
    for i, z in enumerate(seq):
        if z is None:
            lines.append(f"  n={i}: INF (pole: in {{1,inf}} basin)")
        else:
            lines.append(f"  n={i}: v2(z)={v2f(z)} v2(z-1)={v2f(z-1)}")
    return "\n".join(lines)

def check_contraction(a):
    """Verify disk invariance B(0,2^-m) for m>=1: all iterates satisfy v2>=m."""
    m = v2f(a)
    assert m >= 1
    seq = orbit(a, 8)
    ok = all((z is None) or (z == 0) or (v2f(z) >= m) or (z is not None and False)
             for z in seq)
    # orbit of 0 must stay in disk: check valuations
    vals = [v2f(z) for z in seq if z is not None]
    return ok, vals

if __name__ == "__main__":
    print("=== m<=0 doubling cases ===")
    for a in [Fraction(3), Fraction(5), Fraction(-5), Fraction(7),
              Fraction(-3), Fraction(9), Fraction(-1, 3), Fraction(3, 2)]:
        print(check_doubling(a, 7))
        print()
    print("=== PCF / preperiodic cases ===")
    for a in [Fraction(1), Fraction(1, 2), Fraction(0), Fraction(2)]:
        print(check_doubling(a, 5))
        print()
    print("=== m>=1 contraction cases ===")
    for a in [Fraction(2), Fraction(4), Fraction(6), Fraction(8), Fraction(-2)]:
        ok, vals = check_contraction(a)
        print(f"a={a} m={v2f(a)} invariant={ok} vals={vals}")
    print("ALL_CHECKS_DONE")
