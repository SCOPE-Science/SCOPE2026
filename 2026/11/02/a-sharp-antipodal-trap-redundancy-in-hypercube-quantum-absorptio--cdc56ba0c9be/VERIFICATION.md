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

The exact analytical proof is included in RESULT.md. To reproduce finite diagnostic checks, run `python3 VERIFY.py` with Python and NumPy installed. The program tests all 20 combinations of dimension and sink separation with \(2\le d\le6\). It builds the binary hypercube adjacency independently from bit operations, computes two-source Krylov ranks, and compares the observed ranks against the all-dimension formula. These finite tests support but do not replace the proof. No independent audit or laboratory validation has been performed.
