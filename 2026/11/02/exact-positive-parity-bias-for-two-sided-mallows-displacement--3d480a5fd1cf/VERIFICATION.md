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

# Reproduction and verification

Run `python3 verify_mallows_parity.py` using Python 3; it uses only the standard library. The executable checks the signed distribution identity in two mathematically distinct finite forms: an integer-coefficient expansion of Gnedin–Olshanski's joint inversion-count series, and the product \(\prod_{k\ge1}[(1-t^k)/(1+t^k)]^2\). All 19 coefficients through degree 18 agree exactly. Six direct numerical conditional-mixture sums agree with independently evaluated products for \(t\in\{0.1,0.25,0.35,0.5,0.6,0.8\}\), and seven sampled parameters exhibit strict product ordering. The checker prints `CHECKS_PASSED` on successful completion.

These are finite deterministic checks, not certificates of an identity on an infinite interval. The infinite result is proved in RESULT.md via the source's exact probability-generating function, the classical \(q\)-binomial theorem for \(|t|<1\), and convergence/monotonicity arguments. The precise model is the stationary balanced two-sided Mallows permutation with \(0<t<1\); finite Mallows permutations at \(Q>1\) enter only through the previously proved interpretation of their limiting fixed-point constants. No external independent validation was performed.
