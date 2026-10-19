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

The stand-alone checker `check.py` evaluates the exact \(2\times2\) normal-equations projection, multiplies it with the Richardson matrix in both orders, and compares the computed spectral norms to the symbolic closed expressions. It checks the eigenvalues, rank-one power identities, sharp maximizers, and the unique positive cubic threshold. Execution completed successfully: 1,510 matrix/parameter cases plus analytic-extremizer and threshold checks.

The mathematical proof in `RESULT.md` establishes global optimization for every admissible coarse line and condition number. Numerical tests sample only finitely many cases; they do not certify an infinite statement. No independent audit, human expert validation, or formal proof assistant verification has been performed.
