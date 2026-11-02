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

# Reproducibility

Run `python3 checker.py` with the standard Python library. The included program checks the exact rational Möbius inversion identities, the dispersal involution, both threshold equalities, the root polynomial identity, and branch image inequalities for a grid of rational admissible parameters. It also checks square-root endpoints to numerical tolerance. The replay reported 2,383 assertions passed.

The universally quantified classification is proved in `RESULT.md`; numerical testing is not a proof of convergence or a substitute for the topological contraction argument. No finite enumeration is claimed exhaustive over all real parameters. No external independent audit was performed.
