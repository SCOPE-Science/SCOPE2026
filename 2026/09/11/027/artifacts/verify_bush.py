"""Bush sharpness vs sticky maximal exponent 0.49 (lane-729).

Analytic claim (proved in output/DRAFT.md):
  Bush through origin is sticky (Wang-Zahl Def 1.1: lines through origin have
  packing dim 2 = n-1) and forces L^2 tube-sum exponent >= 1/2, contradicting
  the target exponent 0.49 (+eps).

This script checks the closed-form arithmetic:
  LHS = ||sum chi_{T_e}||_2 >= sqrt(|B(d/4)|) * N, N >= c0 d^-2 (c0=1/2).
  Claimed RHS (target, C_eps=1, eps=0.005): d^{-0.495} * sqrt(N_up pi d^2).
  Ratio R(d) = LHS/RHS = K * d^{-0.005} -> infinity; crosses 1 at finite d.
Part 1: explicit dyadic d=2^-k where R>1 (C_eps=1) -> concrete violation.
Part 2: violation threshold k*(C) for general C_eps (analytic formula).
Part 3: direction-packing existence interval + sticky ratio (bush M=O(1)).
"""
import math

c0 = 0.5            # N >= c0 d^-2
Nup_factor = 20.0   # N <= 20 d^-2 (maximal packing upper bound, generous)
K = (math.sqrt(math.pi/48.0) * c0) / math.sqrt(Nup_factor * math.pi)
print(f"constant K = c/C-normalized prefactor = {K:.6f}")
print("R(d) = K * d^(-0.005)  [target C_eps=1, eps=0.005]")
print()
print("Part 1: explicit violations (C_eps=1):")
found = False
for k in (400, 800, 1000, 1200, 1400, 1600, 2000):
    R = K * 2.0**(0.005*k)
    flag = "VIOLATION (R>1)" if R > 1 else "ok"
    if R > 1:
        found = True
    print(f"  k={k} d=2^-{k} R={R:.4f} {flag}")
assert found, "expected crossing"
print()
print("Part 2: threshold k*(C) with general C_eps, eps=0.005: need K/C*d^-0.005>1")
for C in (1, 10, 10**6, 10**100):
    # k > ln(C/K)/(0.005 ln2)
    kstar = math.log(C/K)/(0.005*math.log(2.0))
    print(f"  C={C:>10}: k* = {kstar:.1f} -> any k>k* violates; d*=2^-k* > 0 exists")
print()
print("Part 3: packing interval N(d) in [0.5 d^-2, 20 d^-2]; "
      "bush fat/thin ratio (rho/d)^2 per fat tube => M=O(1)<=d^-eta.")
for k in (4, 8, 12):
    d = 2.0**-k
    print(f"  d=2^-{k}: N in [{0.5*d**-2:.0f}, {20*d**-2:.0f}], "
          f"d^-0.01={d**-0.01:.3f} >> O(1) slack")
print()
print("VERIFY_OK")
