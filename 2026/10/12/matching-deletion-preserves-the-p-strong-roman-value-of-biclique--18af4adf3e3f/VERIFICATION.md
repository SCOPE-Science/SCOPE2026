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

The analytic proof is self-contained in `RESULT.md`. The bundled `verify.py` independently implements the definition of \(p\)-strong Roman domination and exhaustively minimizes over all labelings for every \(G_{3,3,t}\) and \(G_{3,4,t}\), every matching size \(t\), and \(p\in\{3,4,5\}\). It also checks the closed formula, the explicit two-defender construction, and the key \(H_m\) inequality over a wider finite parameter grid.

Finite enumeration is only a stress test and is not used as an infinite proof. The unproved limit of the computation is explicit: it does not enumerate arbitrary \(r,s,p\). The arbitrary-parameter conclusion rests on the analytic matching-defect argument.
