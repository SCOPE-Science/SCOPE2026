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

# Verification record

The printed dimensional equations were checked against the motivating full text. The proof uses the observable
\[
\Phi=x+\frac{y}{k_1}+\frac{\alpha+d_1}{\alpha k_1}z
\]
and verifies directly that
\[
\dot\Phi=r x\left(1-\frac{x}{k}\right)-\frac{(\alpha+d_1)d_2}{\alpha k_1}z.
\]
No numerical experiment is used to infer an infinite or asymptotic statement.

The bundled `verify.py` performs exact symbolic cancellation, exact completed-square rearrangement, and exact rational evaluation at the source values. It was executed from the packaged file before serialization and again after re-extraction from the final JSONL row.

The proof covers compactly supported invariant probability measures in the nonnegative octant. It does not prove existence of such a measure, existence of a periodic orbit, or stability of a recurrent state. The equality-rigidity argument uses invariance of measure support; equality in the mature-predator ceiling is therefore excluded for every non-equilibrium ergodic recurrent state.
