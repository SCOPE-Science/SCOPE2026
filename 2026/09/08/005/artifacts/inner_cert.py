"""Inner-disc Rouché certificate (FULLY RIGOROUS, exact rational arithmetic).

For n in 10..14, r = 3n/10: prove tail T(r,n) = sum_{k>n} r^k/k!  <  e^{-r} <= min_{|z|=r} |e^z|.
Then Rouche: s_n and e^z have same zero count (0) in |z|<r.
Uses only fractions.Fraction (exact). Prints certificate + machine-checkable inequalities.
"""
from fractions import Fraction
import math

def exp_upper(x, M):
    """Rigorous upper bound on e^x (x>0 rational) via Taylor to M + geometric remainder."""
    assert x > 0
    S = sum((x**k) / Fraction(math.factorial(k)) for k in range(M + 1))
    b = (x**(M + 1)) / Fraction(math.factorial(M + 1))
    q = x / Fraction(M + 2)   # ratio bound for subsequent terms
    assert q < 1
    R = b / (1 - q)
    return S + R

def tail_upper(r, n):
    """Rigorous upper bound on sum_{k>n} r^k/k! via geometric majorant."""
    a = (r**(n + 1)) / Fraction(math.factorial(n + 1))
    q = r / Fraction(n + 2)
    assert q < 1
    return a / (1 - q)

print("n, r, T_upper, exp(r)_upper, T*exp_upper<1 ?, ratio_float")
ok_all = True
for n in range(10, 15):
    r = Fraction(3 * n, 10)
    T = tail_upper(r, n)
    U = exp_upper(r, 30)
    prod = T * U
    ok = prod < 1
    ok_all &= ok
    print(f"n={n} r={r} T<={float(T):.8e} e^r<={float(U):.8e} T*e^r={float(prod):.8f} (<1: {ok})")
    # exact inequality witness: numerator/denominator bit sizes
    print(f"   exact: T*U = {prod.numerator}/{prod.denominator} < 1 : {ok}")
print("INNER CERTIFICATE:", "PASS (all n)" if ok_all else "FAIL")
