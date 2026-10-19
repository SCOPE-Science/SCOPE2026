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

# Analytical and computational verification

The proof proceeds by the exact four-interval cycle, explicit transition of its three omitted endpoints, and a two-hole inverse-branch contraction. Every new claim is reproduced mathematically in `RESULT.md`. These arguments cover all real \(r>1\) and \(L>0\) and do not rely on floating-point extrapolation.

Run `python3 verification/check.py` from the root of this embedded package. The checker requires only Python's standard library `fractions`. It establishes finite exact-rational consistency for seven parameter values, all major transition boundaries, the unique repelling two-cycle, entry to the periodic core, and the first ten geometric survivor measures. In its recorded run, all 26,271 checks passed.

The numerical grid is not exhaustive for the uncountable parameter family, and the finite survivor calculations do not certify the asymptotic tail. Those conclusions are proved by the explicit piecewise-affine inverse-branch construction. The full originating 2021 article and related 2022 comparison were not independently readable, so remaining scientific-priority uncertainty is disclosed, not silently assumed resolved.
