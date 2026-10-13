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

# Verification notes

The proof is an infinite-parameter symbolic argument using second-order recurrence propagation, cyclic Pluecker identities, and a three-coordinate Schur-complement transversality calculation. `CHECKER.py` performs 84 exact-arithmetic examples for sizes four through nine and tests the kernel rank, reconstruction ratios, and normal Hessian span. Run with `python CHECKER.py` using Python 3 and SymPy; `CHECKER_OUTPUT.txt` records the observed output.

The checker does not establish the all-size theorem. The boundary codimension estimate follows from independent path-block determinant equations rather than sampling. No independent expert or machine formal certification is represented.
