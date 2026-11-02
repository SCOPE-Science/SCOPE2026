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

# Reproduction and boundaries

Run the included `check_matching_multicuts.py` with Python 3 and the standard library; no third-party packages or internet are required. The program independently generates every set partition via canonical restricted-growth labels; for each graph it counts the blocks and crossing edges after directly evaluating whether each vertex has crossing degree at most one.

The program compares these direct counts with the Stirling/chromatic formulas for all paths on 2–9 vertices and cycles on 3–9 vertices, with the factorization formula on eleven small named Cartesian products, and with the product formula for all 43 labeled connected factor graphs on 2–4 vertices times a single edge. It also compares seven explicit multi-axis grid formulas computed two ways. The executed output terminates in `VERIFY_OK`.

These enumerations are exhaustive only for the stated finite graphs; they are not a proof for all graph orders. The general proof is in `RESULT.md`, deriving the square-propagation rigidity and the exact run-partition formulas. The code does not establish novelty, independent validation, or publication priority. The research literature comparison and its limitations are in `REVIEW.md` and `AUDIT.json`.
