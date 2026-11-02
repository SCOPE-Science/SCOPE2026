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

# Verification instructions

Run `python3 verify.py certificates.json` from the extracted package directory. A successful run prints four verified order lines followed by `VERIFY_OK`. The checks reconstruct all required reversal classes and signed overlap graphs, derive exact alternating shortest-path distances using breadth-first search, verify the integer dual inequalities and the four constructive covering witnesses. The certificates are exhaustive for the four finite orders, not for higher orders. The script uses only Python standard-library modules and does not depend on an optimizer.
