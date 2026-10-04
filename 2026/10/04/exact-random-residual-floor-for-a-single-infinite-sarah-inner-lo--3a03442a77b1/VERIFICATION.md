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
The proof reconstructs the original scalar SARAH recursion after its full-gradient initialization step.

`verify.py` enumerates finite sample paths in exact rational arithmetic, checks the multiplicative direction formula and its exact second moment, verifies finite perpetuity moments against the recursion used in the proof, and checks that the \(h=1/2,\alpha=1\) approximants form the equally weighted dyadic grids converging to the uniform law.

Finite enumeration is not used as proof of the infinite limit. Almost-sure and \(L^2\) convergence and the residual formula follow from summability of the random products and the exact perpetuity moment equation in `RESULT.md`.
