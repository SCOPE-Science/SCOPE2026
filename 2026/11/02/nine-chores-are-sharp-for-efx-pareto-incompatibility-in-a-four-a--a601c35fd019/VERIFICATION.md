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

# Reproduction

Run `OPENBLAS_NUM_THREADS=1 python verify_nine_chores.py` under Python 3 with NumPy. It checks 165 nonnegative chore-class multiplicity triples of total at most eight and all 125,970 allocation matrices at each of 13 rational representatives/breakpoints, using integer arithmetic only. Pareto optimality checks all allocations, not just itemwise efficiency. It also verifies incompatibility at every representative for the nine-item (3,3,3) instance. The all-real nine-item obstruction is credited to He–Tao, Theorem 2.

Each EFX inequality removes a chore from the comparing agent's own bundle. An EFX-positive candidate is PO exactly if no complete alternative allocation weakly lowers all four disutilities and strictly lowers one. Source code enumerates each class-column composition and tests these inequalities literally. See the mathematical proof for justification of the finite sign-cell reduction; this is an exact finite proof, not extrapolation from tested sample ratios.

Independent validation has not been performed.
