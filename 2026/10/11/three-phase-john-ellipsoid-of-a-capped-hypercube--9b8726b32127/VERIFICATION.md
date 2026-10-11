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

The accompanying `verify.py` uses only the Python standard library. Execute `python3 verify.py` in this directory.

The exact-rational checks cover 5,520 parameter instances with \(2\le n\le21\), checking positive eigenvalues, coordinate support inequalities, rank support inequalities, and equality patterns at all three parameter regimes. An independently parameterized grid tests the determinant against the proposed optimum for 248 additional parameter cases. Both checks passed.

The verifier does not exhaust all real parameters, prove uniqueness under arbitrary nonsymmetric perturbations, or establish literature originality. All-dimensional correctness instead uses the permutation-invariance theorem for the unique John ellipsoid, exact support-function evaluation, and one-variable determinant optimization reproduced in RESULT.md. No independent audit is claimed.
