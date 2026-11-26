---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-25.md",
      "INDEPENDENT_AUDIT_2026-11-25.json"
    ],
    "status": "passed"
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Reproducibility

Run `python3 verify.py` using the Python standard library. It reconstructs the Petersen cubical cells in the stated order and evaluates the cup-product representative from the two coordinate linear forms. It checks the integral cochain identity witnessing that twice the product vanishes, and a mod-two cycle with odd pairing witnessing that the product is nonzero. The expected marker is `PRODUCT_ORDER_TWO_OK`. The geometric identification of the product is justified in `RESULT.md`, not by the checker alone.
