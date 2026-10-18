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

# Reproducibility and limits

The published mathematical proof of the all-dimensional criterion is in `RESULT.md`. Its main steps are quadratic reduction, negative-cone far-ray forcing, the spanning argument for null vectors in the indefinite case, and orthogonality to the kernel in the negative-semidefinite case. The strict witness calculations in `verify.py` are rational, with no floating-point tolerances. They verify a concrete obstruction but do not replace the general proof. No data external to this package are needed. Independent audit has not been performed.
