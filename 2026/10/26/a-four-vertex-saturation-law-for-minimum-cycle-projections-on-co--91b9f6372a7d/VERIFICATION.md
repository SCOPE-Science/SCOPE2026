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

# Reproducible verification and limits

Run `python3 verify_split.py` using Python 3's standard library. It constructs grounded graph Laplacians, solves their exact-rational incidence equations, forms each proposed cycle-projection column, and checks zero divergence, the exact operator-norm formula, and the projection identity on small cases. The observed output was: 56 parameter pairs; 1932 edge columns; 1754 full idempotence entries, all passed.

The checker uses no downloaded tables, sampled eigenvalues, or floating-point rounding. Numerical or finite checks do not prove the theorem for infinitely many parameters. The general proof is the signed-permutation averaging, representation decomposition and global piecewise-linear minimization in RESULT.md. The optimality statement concerns real edge-\(\ell_1\) projections only; no independently audited claim is made.
