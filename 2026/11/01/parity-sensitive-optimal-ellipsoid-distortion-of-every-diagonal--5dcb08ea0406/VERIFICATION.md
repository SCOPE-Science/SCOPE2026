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

# Reproduction and boundaries

Run `python3 verify.py` in the extracted folder with Python 3, NumPy and SciPy. The verifier independently enumerates vertex orbits with exact rational arithmetic, compares exact centroid and covariance identities, checks John contact distances and simplex plateau and central parity values, and cross-validates random linear-function maxima via an independent linear-programming solver.

The verifier completed successfully with `VERIFY_OK 9960 exact and independent numerical checks`. These checks are not infinite-domain proofs. The universal claim relies on the exact normal projection, the contact criteria, the linear-programming vertex description, the analytic derivative on every interval between integers, and the Taylor coefficients, all shown in RESULT.md. Unrestricted extremality is justified by the stated positive contact measures; uniqueness excludes any hidden rotated or translated competitor.

Scientific limits: real parameters strictly between the two degenerate endpoints; dimensions three or above; diagonal hyperplane directions only; no stability claim for noisy body measurements. Historical novelty is provisionally assessed and is not independently validated.
