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

# Reproduction and scope

Execute `python verify.py` with Python 3, NumPy, SciPy and mpmath. The script checks 275 independent numerical conditions: symmetry-derived row sums, direct distance-matrix linear solves, signs and normalizations, convex hull exposure, small-scale zeta-matrix approximations, high precision threshold calculations and asymptotic trends. Output includes `PASS: 275 independent row, direct linear solve, sign, threshold, and asymptotic checks.` and `n=4 critical radius: 0.834207951426`.

The proof in `RESULT.md` is analytic for every integer \(n\ge4\) and every real \(0<r\le1\). The numerical tests are finite, and do not certify infinite quantifiers, historical originality, or independent mathematical validation. Historical-priority risk for the unavailable full text of the main motivating preprint is described in `REVIEW.md`.
