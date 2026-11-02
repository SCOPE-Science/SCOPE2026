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

- Run `python verify.py` with dependencies in `requirements.txt`.
- Completed checks: exact \(P_c\) discriminant, substitution at the Cauchy bound, fixed-point multiplier identity, the four response-square identities at \(c=1/6\), strict positivity of the witness, and the exact primitive-cycle multiplier \(43/243\).
- General parameter claims are verified by the analytic proof, not by a finite scan. In particular, Coppel's interval-iteration theorem is used to turn the absence of any primitive period-two point into convergence of all iterates on a compact interval.
- The lower-cost player's initial effort must be strictly between zero and one; positive-interior dynamics never use the discontinuous zero-opponent convention. The symbolic script is a consistency check, not independent validation or exhaustive parameter certification.
