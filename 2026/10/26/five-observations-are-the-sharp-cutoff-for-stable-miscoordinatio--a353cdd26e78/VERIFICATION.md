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

# Verification of the finite-sample threshold

The supporting `check_sampling.py` program uses Python's standard-library `fractions.Fraction`; execute `python check_sampling.py` in a directory containing this file. Its assertions passed in the supplied test execution.

Checked facts: exact binomial tail factorization for all five nontrivial low-size threshold modes; the \(k=5\), cutoff-three tail; the \(\{2,5\}\) mixed drift identity; opposite-sign rational brackets around both interior roots for \(\alpha=503/1000\); strict radical bounds separating that witness from the critical fold; finite-grid checks of the \(k\le4\) drift decomposition. Checking the identities at six distinct rationals is conclusive for polynomials of degree at most five, unlike the separate finite-grid qualitative sanity tests.

The universal nonexistence conclusion is established by the analytical concavity/end-point argument, not by a grid. The existence, uniqueness, fold and basin statements use the exact cubic critical-point/monotonicity argument in `RESULT.md`; finite numerical experiments cannot certify those infinite assertions. No independent audit was conducted.
