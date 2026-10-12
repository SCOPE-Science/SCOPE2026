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

# Verification scope and reproducibility

Run `python verify.py` with NumPy installed as specified in `requirements.txt`. The code checks exact rational trace and determinant identities for the split-preconditioned matrix; independently forms symmetric matrices, diagonalizes them, constructs extremizing first-step errors, and tests the actual PCG line search against the theoretical contraction formula. It also compares alternative positive multipliers against the proposed minimax multiplier, verifies equality at the nominal-scaling angular frontier, and checks representative small-curvature limits. A deterministic random seed is used.

Observed output:

```
VERIFY_OK rational_matrix_and_minimax_identities= 15444
VERIFY_OK independent_eigensystem_and_worst_PCG_cases= 2400
VERIFY_OK robust_minimax_sample_cases= 850
VERIFY_OK exact_nominal_safety_threshold_and_small_curvature_limits=1
```

Neither randomized sampling nor finite exact-rational checks establish global minimaxity by themselves. The proof in `RESULT.md` supplies the quantified trace, determinant, Kantorovich equality, unique minimax optimization, and asymptotic arguments. The calculation is exact-arithmetic mathematics; the NumPy checks necessarily introduce floating-point tolerances for corroboration.
