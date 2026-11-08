---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "evidence": null,
    "status": "not_performed"
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Reproducibility checks

Run `python3 verify.py` with Python 3.8 or later. The program is standalone and uses only standard-library `decimal` and `math.isqrt`. It constructs the Fibonacci fixed point independently of an exact-integer Beatty formula, constructs the Lucas word by two definitions (a Lucas-style concatenation recurrence and an inflation of the Fibonacci word), and checks all corresponding symbols in the first 50,000 positions. The Beatty construction uses exactly
\[
 \lfloor k(3+\sqrt5)/2\rfloor
 =\left\lfloor(3k+\lfloor\sqrt{5k^2}\rfloor)/2\right\rfloor
\]
and the analogous \(5+\sqrt5\) expression, so it involves no floating-point rounding.

It compares the simultaneous circle coding with the constructed symbols at 90-decimal-digit arithmetic precision, and checks observed pair counts against the proved densities for prefix sizes \(100,1000,10000,50000\). Observed output:
```
PREFIX 100 pair_counts [31, 31, 14, 24] max_absolute_error 1.5572809000084122
PREFIX 1000 pair_counts [297, 321, 151, 231] max_absolute_error 2.60679774997897
PREFIX 10000 pair_counts [2946, 3234, 1526, 2294] max_absolute_error 2.203932499369089
PREFIX 50000 pair_counts [14724, 16178, 7637, 11461] max_absolute_error 2.640450004206072
VERIFY_OK N=50000 morphism_and_Lucas_recursion=yes exact_Beatty=yes joint_rotation_coding=yes four_densities=yes
```

The density order is \(00,01,10,11\). Verification of finitely many indices is **not** a proof that the coding and discrepancy bounds hold for all indices; that proof is in RESULT.md. The exact-integer statements are checked without floating arithmetic; the separate rotation-threshold comparisons use finite high-precision decimals and should be treated as corroboration, not proof. Independent mathematical audit: not performed.
