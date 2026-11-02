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

The reproducibility command is `python3 verify.py` with standard Python 3. It independently implements the three-variable integer denumerant dynamic program; tests the \(84\)-period coefficient law and six comparable coprime parameter pairs; tests the direct \((6,7,8)\) denumerant against the parity formulas; and exhaustively checks all \(p\in\{0,\dots,180\}\). The exact finite exception sets in the manuscript are the asserted outputs. The proof for infinitely many larger \(p\) is mathematical, not experimental. This check is not an independent audit.
