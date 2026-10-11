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

Run `python3 verify.py` with SymPy available. The program checks four symbolic frustum-moment limit pairs and computes the exact affine-normalized triangle convex hull using rational arithmetic. Its expected success marker is `OFFCENTER_CORE_CHECKS_OK`. The analytic proof in `RESULT.md`, especially the all-direction support sandwich and strict-interior frustum admissibility, establishes the theorem independently of these finite checks. No independent audit or external certification is asserted.
