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

## Reproduction
Run `python3 verify.py`. The standard-library script performs exhaustive checks of the original multiplication and determinant/rank conditions for all linear transformations at three small parameters, and independent orthogonal-group enumerations at five parameters. Compare exact stdout to `checks.txt`.

## Mathematical limits
These are finite checks. The arbitrary finite-field and leaf-count statements rest on the block-decomposition, characteristic-vector and symplectic-complement proofs in `RESULT.md`. No machine proof or independent mathematical audit is claimed.
