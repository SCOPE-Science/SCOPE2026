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

# Verification

The finite-field Alltop construction and all claimed conclusions have algebraic proofs in `RESULT.md`. The accompanying executable `check_alltop_mub.py` computes actual mutually unbiased Gabor bases in orders 5, 7, 11, and 25, verifies the predicted Hermitian projector-span rank in orders 5, 7, 11, tests the two-coordinate measurement ambiguity and repair with separated weights, and checks the exact sorted-weight maximin formula. See `check_output.txt` for the actual observed outputs.

The critical infinite quantifier is proved by planar exponential-sum orthogonality and a full Hilbert–Schmidt dimension count, not by finite sampling. Any nonzero Hermitian diagonal difference of rank at most two and zero trace has the signed two-site form, which is detected exactly by the squared-modulus condition. Algebraic perturbation/noise stability was not tested or established.
