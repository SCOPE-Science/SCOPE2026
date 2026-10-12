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

# Verification notes

The attached `verify.py` constructs the direct-product graph by coordinate inequalities. For each pair of nonadjacent vertices it independently computes the common-neighbor mask; a proposed complement is feasible precisely when it intersects every such mask. It checks inclusion-maximality by deleting each omitted cell in turn and compares all tested results to the proposed three-family structure. It exhaustively covers orders \((3,3)\), \((3,4)\), \((3,5)\), and \((4,4)\), and performs predetermined additional sample tests for \((4,5)\) and \((5,5)\). The exhaustive tests include 102,912 binary configurations, and the two sample groups cover 20,000 checks.

Run `python3 verify.py` from this package directory. `verification_output.txt` records one successful execution; rerun against the packaged script, not a version external to this package. The checker establishes no infinite claim and does not independently audit originality or mathematical value. The general proof is in `RESULT.md`.
