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

# Reproducibility checks

Run `python3 verify.py` with Python 3 and no external modules. The checked script independently computes joint-leaf probabilities both by exhaustive parent-array enumeration and by a second independent time-step product, comparing each with the analytic finite identity. It also checks negative orthant domination, fixed small-r tuples at larger sizes and approximate first two factorial moments at three macroscopic sample sizes.

The packaged script completed successfully with 17,287 consistency assertions. These checks cover finite test cases only; they cannot replace the conditional telescoping product and dominated Laplace-functional argument that establish the infinite point-process statement. Historical publication priority is not independently established.
