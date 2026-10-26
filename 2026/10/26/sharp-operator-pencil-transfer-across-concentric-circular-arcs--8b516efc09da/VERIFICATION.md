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

# Reproducibility and proof checks

The core proof requires no external numerical certificates: the explicit scalar arc maximum, the three monotonicity branches, and Hahn--Banach scalarization are written in RESULT.md. The sharpness witness is the exact pair \(A=-B\ne0\), and the scalar equality classification is proved algebraically. The operator-space claim is verified at every matrix level by applying the operator-pencil inequality with \(A,B\) as complex matrices. The inverse is restriction between nested compact arcs and has exact norm one.

The included `verify_arc_transfer.py` was executed using NumPy with deterministic seed 5321. It reported `FINITE_ARC_PENCIL_CHECKS_OK 405`, covering 400 complex 2-by-2 random pencils and five analytically checked sharpness examples across five angle pairs. Its angular grid has 501 points per arc, so these finite tests cannot certify the all-parameters theorem or originality. The written analytic proof is the necessary evidence. Independent audit or expert checking has not been performed.
