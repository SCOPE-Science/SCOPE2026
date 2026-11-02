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

# Verification

The argument is analytical for all positive fertility parameters and all survival probabilities in the stated ranges. Its central steps are trace and determinant invariance under cyclic matrix products, the exact commutator-determinant identity, and the Perron formula for a strictly positive two-by-two matrix.

Run `python3 artifacts/verify.py` with Python 3. The checker uses `fractions.Fraction` and tests 16,128 exact rational determinant and trace comparisons plus an exact subcritical-to-supercritical expected-growth witness; it does not use simulated trajectories. The comparison for this witness with unity follows from exact squares \(73<81<82\).

The finite checker is only a supplementary consistency test; it does not prove the parameter-wide theorem. No independent external audit was performed. Historical priority, especially possible implication by a general matrix-mixture theorem, has not been conclusively certified. Expected population growth must not be identified with positive almost-sure stochastic growth or ecological persistence.
