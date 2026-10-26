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

The `verify.py` program uses Python 3 standard libraries. Run `python3 verify.py` to reproduce seeded random positive-mixture tests, scalar bisection of the fitted exponent, exact-equality checks, normalized-contrast asymptotic checks, two-region directional monotonicity, and the entropy envelope. No third-party datasets or software are required.

The analytical proof, not a finite numerical search, establishes the global exponent inequality, exact equality condition, second-order coefficient, sharp climate-balance bound and global two-basin monotonicity. The computational test samples finite parameter ranges; it does not certify universal mathematical statements or historical priority. The exact two-basin radical example can be verified independently from the formula in `RESULT.md`.
