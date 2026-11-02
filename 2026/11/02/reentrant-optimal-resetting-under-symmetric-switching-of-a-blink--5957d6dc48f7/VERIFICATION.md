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

Run `python3 verify.py` with Python 3 standard library only. The saved executable was run and returned `PASS: 1411 finite assertions`. Checks compare two algebraic versions of the previously published mean-first-passage formula, differentiate it numerically on a seeded parameter sample, reconstruct the limiting roots and signs, test uniform compact expansions, and compare candidate optima with finite test grids. All sample counts and tolerances are in the code. These numerical checks are finite and cannot establish the global minimizer claims: the latter follow from the written analytic compactness and implicit-function proof.

The limiting stationary duty fraction of the blinking target remains exactly one half. The optimizer uniqueness proof covers sufficiently small and sufficiently large positive switching speed, not every intermediate speed.
