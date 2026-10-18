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
The companion `verify.py` requires Python 3 and only the standard library. Run `python verify.py` from the extracted directory. The program checks the quadratic cross-section surplus as an exact factorization over rational numbers, checks both transformed boundary latitudes, checks the equality Gram entries and the exact upper-bound/constructive-volume identity for integer dimensions from \(2\) through \(16\). It also performs finite random checks for arbitrary-position simplices in dimensions \(2\) through \(5\).

Observed execution from the complete package source material: `VERIFY_OK exact_rational_surplus_checks=3675 stochastic_simplex_tests=8000 dimensions=2..16`.

These checks do not prove a universal quantification. The proof in `RESULT.md` establishes the theorem for every integer \(n\ge2\) and every real \(0<h\le2\), with strict boundary and equality conditions analyzed analytically. No independent audit, outside mathematical review, or external certification has been performed.
