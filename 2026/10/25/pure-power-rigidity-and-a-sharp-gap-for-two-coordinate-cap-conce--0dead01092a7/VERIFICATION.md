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

Run `python verify.py` with Python 3.8 or later. The checker is self-contained and uses exact rational arithmetic. It independently computes the coordinate-cap concentration eigenvalues by finite beta-binomial sums or Dirichlet complement integrations, checks the first and second spectral levels against all monomial branches, and checks the gap integral by a separate polynomial expansion. The captured execution reported: `PASS: 5208 exact-rational eigenvalue, ordering, and gap assertions`.

The tests cover finite grids only. The argument valid for arbitrary dimensions, degrees, and real thresholds is the analytic proof in `RESULT.md`, especially the two conditional beta likelihood-ratio comparisons. There is no formal proof-assistant certificate or independent audit.
