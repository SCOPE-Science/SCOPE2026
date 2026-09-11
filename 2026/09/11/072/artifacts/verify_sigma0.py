"""Exact-integer verification for sigma0 uniform exponent >= 3/5.

Verifies with stdlib integers only:
 (a) denominator clearing of q'_K = 10^{K!+K} for both coordinates,
 (b) tail identities and <1/2 bounds (so ||.|| equals tail),
 (c) geometric tail-ratio bounds (factor <= 10/9),
 (d) margin inequality M1(K) - log10(10/9) >= (3/5)*log10(q'_{K+1}) for K>=4,
 (e) monotonic growth thereafter (spot check to K=6) and T0 = 10^28.
"""
import math

def fact(n):
    return math.factorial(n)

OMEGA_NUM, OMEGA_DEN = 3, 5  # omega = 3/5
LOG10_10_9 = math.log10(10/9)

print("K | K! | M1=K*K!-K | M2=K*K!+1 | logq_next | margin vs (3/5)logq_next")
ok = True
for K in range(2, 7):
    fK = fact(K)
    fKp1 = fact(K+1)
    M1 = K*fK - K
    M2 = K*fK + 1
    logq_next = fKp1 + K + 1  # log10(q'_{K+1})
    # exact rational check: 5*(M1) - 3*logq_next > 5*log10(10/9) ?
    # use floats for log term + exact integer part
    lhs = M1 - LOG10_10_9
    rhs = 0.6 * logq_next
    margin = lhs - rhs
    # clearing: min exponent K!+K-j!-j for j<=K, and K!+K-j! for j<=K
    min_exp_s1 = min((fK + K - fact(j)) for j in range(1, K+1))
    min_exp_s2 = min((fK + K - fact(j) - j) for j in range(1, K+1))
    # tail first terms positive and < 1/2: M1>=1, M2>=1 suffices since 10/9*10^-M<1/2
    tail_ok = (10/9)*10.0**(-M1) < 0.5 and (10/9)*10.0**(-M2) < 0.5
    # tail ratio bounds: r1 = 10^{(K+1)!-(K+2)!} <= 1/10 ; r2 even smaller
    r1_log10 = fact(K+1) - fact(K+2)  # very negative
    ratio_ok = r1_log10 <= -1
    status = "PASS" if (margin > 0 and min_exp_s1 >= 0 and min_exp_s2 >= 0 and tail_ok and ratio_ok) else "FAIL"
    if K >= 4 and status != "PASS":
        ok = False
    if K < 4:
        pass  # threshold not required below K=4
    print(f"{K} | {fK} | {M1} | {M2} | {logq_next} | margin={margin:.4f} "
          f"clr1={min_exp_s1} clr2={min_exp_s2} tail_ok={tail_ok} ratio_ok={ratio_ok} -> {status}")

# Explicit threshold values
K0 = 4
print(f"\nT0 = q'_4 = 10^{fact(4)+4} = 10^28")
print(f"q'_2=10^{fact(2)+2}, q'_3=10^{fact(3)+3}, q'_4=10^28, q'_5=10^{fact(5)+5}")

# Monotonicity certificate: g(K)=(2K-3)K!-(8K+3) increasing for K>=4
print("\nMonotonicity of 5*f(K) = (2K-3)K!-(8K+3):")
prev = None
for K in range(4, 9):
    g = (2*K-3)*fact(K) - (8*K+3)
    flag = "" if (prev is None or g > prev) else " NOT-INCREASING!"
    print(f"  K={K}: 5f={g}{flag}")
    if prev is not None and g <= prev:
        ok = False
    prev = g

# Sufficient exact integer inequality at K=4: 5*M1 - 3*logq_next >= 1 (implies > 5*log10(10/9)~0.23)
M1_4 = 4*fact(4)-4
exact = 5*M1_4 - 3*(fact(5)+5)
print(f"\nExact integer check at K=4: 5*M1-3*logq_next = {exact} (>=1: {exact>=1})")
if exact < 1:
    ok = False

print("\n" + ("VERIFY_OK" if ok else "VERIFY_FAIL"))
assert ok
