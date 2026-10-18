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

Verification uses the standard-library `verify.py` beside this document. The program constructs weighted Laplacian matrices independently of the spectral formulas, computes exact rational inverses, verifies stochasticity and nonnegative off-diagonals, checks the rational critical boundary and verifies the predicted asymptotic orders numerically. One completed local execution printed `VERIFY_OK 1290 assertion groups; exact rational matrices and singular-limit probes`.

These are finite checks. They do not certify an infinite-family mathematical theorem. The argument for every integer \(r,s\ge2\) and every positive \(a,b\) is in `RESULT.md`. No independent audit has been performed.
