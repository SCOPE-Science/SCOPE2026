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

Checks performed for this finding:

- Derived the discrete-Laplace convolution identity directly from the kernel coefficients.
- Substituted the principal-eigenvector equation to obtain the three-term recurrence.
- Verified that the mortality assumption makes the recurrence perturbation summable.
- Supplied a backward Volterra construction for the decaying solution and used \(\ell_1\)-summability to exclude the growing branch.
- Derived the two-sided tail, omitted-mass asymptotic, and critical exponential-moment boundary.
- Compared the statement with the recent model paper and semantic published-finding corpus searches; the general Jacobi-asymptotic literature remains a stated residual risk.

Limits: no finite-section eigenvector error bound is claimed; no independent audit or independent validation was performed. The trusted importer initializes absent external channels as unperformed; research never assesses/authors them or resets old evidence.
