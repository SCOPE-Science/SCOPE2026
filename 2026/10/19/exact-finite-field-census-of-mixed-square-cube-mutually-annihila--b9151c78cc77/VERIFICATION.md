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

The theorem was checked by a direct structural proof and by the packaged standalone Python 3 program `check.py` (standard library only).

The checker independently enumerates each ambient matrix \(B\) over small prime fields, filters by \(AB=BA=0\) and \(B^3=0\) with \(A\) in each square-zero rank normal form, then compares each resulting fixed-rank fiber against an independently computed Jordan-type/finite-group formula. The exact tests passed for \((n,q)\in\{(0,2),(1,2),(2,2),(3,2),(4,2),(2,3),(3,3),(2,5)\}\). Expected pair totals respectively are \(1,1,10,232,15856,33,3537,145\). The program prints `ALL_EXACT_CHECKS_PASSED` when successful.

The checker does not enumerate all \(q\) and \(n\), and has no extension-field arithmetic implementation. The proof's matrix-block and Jordan arguments apply to every finite field irrespective of characteristic. No independent mathematical audit has been performed.
