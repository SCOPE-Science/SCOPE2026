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
# Mathematical verification and limits

Run `python verify.py` with Python 3 and `mpmath`. The standalone program builds the two-image plume formula directly, computes log-concentration divided differences, recovers the physical source parameters, and tests the fourth-order asymptotic coefficient and finite-sample strict monotonicity. These checks are reproducible finite corroboration only.

The actual complete proof of global uniqueness is the strict concavity and divided-difference argument in `RESULT.md`; it holds for all three distinct nonnegative heights and all \(A,\sigma>0\), \(H\ge0\). The sharp \(1/4\) inverse exponent is proved analytically using a curve of models that holds two observations fixed.

No numerical simulation is used as a substitute for the proof, and no noisy-field accuracy or historical independent validation is asserted. Scientific limitations and historical-priority risks are documented in `RESULT.md` and `REVIEW.md`.
