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

The standalone `verify_cesaro.py` computes the generalized Cesàro images and the mixed endpoint norm using exact `fractions.Fraction` arithmetic. It compares the proposed maximum with all binary supports in dimensions 2–9 for four geometric parameters and four mixing parameters: 128 cases and 16,192 support vectors. It also verifies the exact harmonic expression, strict positive threshold ordering, and 3,885 adjacent-comparison sign identities in dimensions 4–40.

Reproduce using `python verify_cesaro.py`; the script prints a PASS summary or raises `AssertionError`. The universal proof uses indicator reduction, monotonicity of the geometric column sums, and algebraic harmonic comparisons; finite diagnostics do not establish quantification beyond the tested cases.

No independent audit has been performed.
