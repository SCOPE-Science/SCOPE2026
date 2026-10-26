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

# Reproducibility and limits

Execute `python3 verify.py` in the folder containing this document. The script has no external dependencies. It constructs the rule directly from the two active neighborhoods, enumerates all 32 length-five words, constructs the full de Bruijn graph, and exhaustively counts its elementary directed cycles and all vertex-disjoint selections to produce the determinant coefficients in exact integer arithmetic. It also exhaustively enumerates all binary configurations on rings of lengths 1 through 15 and directly checks both temporal fixed points and exact second-iterate fixed points against the proved recurrence. Expected final line begins with `a_n_1..18=` after `VERIFY_OK`; the actual run printed `VERIFY_OK`.

The proof of the theorem for arbitrary ring length is the finite graph representation together with the formal determinant identity, not an extrapolation of numerical data. The standalone replay proves the finite graph enumeration performed by the script, while the document's mathematical argument explains why that certificate proves the infinite family result. No separate or independent scientific validation has been performed.
