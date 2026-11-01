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

Run `python verify.py` from the directory containing the package files (Python 3, standard library only). A recorded execution of the actual candidate verifier returned: `PASS: 48479 checks; cubical Betti ranks through dimension 6; rational skeleton-offset membership grids through dimension 4`. The code constructs cubical cellular boundaries over the two-element field and computes ranks, and also checks three independently implemented membership characterizations on exact rational coordinate grids. This checks finitely many examples; exact all-dimensional persistence and topological conclusions come from the analytic proof in RESULT.md. No independent audit or external certification has been performed.
