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

The characteristic-independent proof is the displayed ideal intersection and point-count decomposition in RESULT.md. These statements can be checked without trusting any finite experiment.

`python verify_counts.py` exhaustively traverses all active coordinate assignments over fields of sizes 2, 3, 4 and 5, including explicit GF(4) field operations. Output: `VERIFY_OK_FLAGGED_ZERO_PRODUCT_N4` with active counts 26, 129, 388, 905.

`python verify_ideals.py` requires SymPy (tested with version 1.14.0); elimination computations over the rationals and moduli 2, 3 and 5 produce `VERIFY_OK_PRIMARY_INTERSECTION_N4`.

These calculations are checks, not proofs of the all-characteristic statement. The unexamined source noted under limitations remains a historical-priority risk. No independent audit has been carried out.
