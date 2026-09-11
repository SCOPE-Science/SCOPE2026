"""Verify the container-count obstruction arithmetic for lane-1052.

Claim: n=4096, cap 0.52*C(n,2) per container => |C| >= exp(n^1.5/10^4).
Proof route: balanced complete bipartite graphs K_{A,A^c} (|A|=2048) are
triangle-free hence B_2(64)-free; each container covers few of them because
its complement is dense (>=0.48*C(n,2) edges) so has few components (r<=1259)
and every covered bipartition is a union of complement components.
Uses only stdlib; all key steps are exact integer arithmetic except the final
log comparison, whose margin (~1930 nats) dwarfs float error (~1e-12).
"""
import math

n = 4096
N = n * (n - 1) // 2          # C(4096,2) = 8386560
assert N == 8386560, N

# Container edge cap: 0.52*N = 4361011.2 -> integer M <= 4361011
M_cap = 4361011
assert M_cap == math.floor(0.52 * N), M_cap
missing = N - M_cap            # >= 4025549
assert missing == 4025549, missing
assert missing > 0.48 * N

# Component bound: complement has >= `missing` edges on r components, so
# (n-r+1)(n-r)/2 >= missing. Refute r >= 1260 with exact integers:
t = n - 1260                  # = 2836; (n-r+1)(n-r) <= 2837*2836 for r>=1260
assert t == 2836
assert 2837 * 2836 == 8045732
assert 2 * missing == 8051098
assert 2837 * 2836 < 2 * missing  # so r <= 1259
r_max = 1259

# Total balanced bicliques (unordered): C(4096,2048)/2 >= 2^4096/(4097*2).
# Each container covers <= 2^(r-1) <= 2^1258 of them.
# Hence |C| >= 2^4096/(4097*2^1259) = 2^2837/4097.
logC_lower = 2837 * math.log(2) - math.log(4097)
target_exp = n ** 1.5 / 1e4
assert abs(target_exp - 26.2144) < 1e-9, target_exp
print(f"N={N} missing={missing} r_max={r_max}")
print(f"ln|C| >= {logC_lower:.4f}  vs  target {target_exp:.4f}")
print(f"margin = {logC_lower - target_exp:.2f} nats")
print(f"|C| >= 2^2837/4097 ~= e^{logC_lower:.1f} ~= 10^{logC_lower / math.log(10):.1f}")
print(f"threshold = e^{target_exp:.4f} ~= {math.exp(target_exp):.3e}")
assert logC_lower > target_exp + 100  # enormous certified margin
print("VERIFY_OK")
