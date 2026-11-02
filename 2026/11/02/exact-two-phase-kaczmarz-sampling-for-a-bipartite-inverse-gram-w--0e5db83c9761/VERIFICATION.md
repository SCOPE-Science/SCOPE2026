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

The proof's critical finite identities can be replayed with `python verify.py`. On the packaged source, 450 rational parameter configurations passed exact primal-dual complementarity and objective equalities and numerical semidefinite eigenvalue checks. Twenty additional models were compared with random and perturbed probability vectors; three normalized-row systems were also checked. Exact correctness for all positive real parameters follows from the two positive-semidefinite sum-of-squares decompositions and the correlation-matrix lower bound in RESULT.md, not from those finite experiments.

The numerical checks use floating-point eigenvalues with tolerance. The theorem concerns one-step expected squared-error contraction, not the multistep error exponent. Independent validation has not been performed.
