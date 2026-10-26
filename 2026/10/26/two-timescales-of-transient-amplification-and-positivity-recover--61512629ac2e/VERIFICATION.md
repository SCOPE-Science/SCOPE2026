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

The squared-graph-Laplacian kernel is reconstructed analytically from four orthogonal eigenspaces. The exact endpoint norms, uniqueness of the transient peak, positivity recovery and the unbalanced limit all follow from the proof in `RESULT.md`.

Run `python verify.py` with the versions in `requirements.txt` installed. The program independently exponentiates explicit finite graph matrices and verifies kernel entries, endpoint norms and selected parameter-regime bounds. A successful execution returns `CHECKS_OK 3618` (program assertions counted).

Finite computation does not prove the infinitely quantified statements. The numerical check uses standard double precision and tolerances of the order indicated in `verify.py`; it is supplemental, not an interval-arithmetic or symbolic certificate. The analytical argument is self-contained and independent of those numerical checks.

No independent mathematical audit or independent validation has been performed.
