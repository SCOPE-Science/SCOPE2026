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

# Reproduction and proof limits

Run `python verify.py` using Python 3; no third-party packages are required. It constructs the direct product adjacency relation and tests every vertex subset with size at most the claimed minimum for 27 parameter pairs (\(q=2,2\le n\le10\); \(q=3,2\le n\le9\); \(q=4,2\le n\le7\); \(q=5,2\le n\le5\)). It independently computes the minimum size and its multiplicity from a row-state dynamic program for 553 further pairs (\(2\le q\le8, 2\le n\le80\)). Expected output begins with `VERIFIED:`; assertions detect discrepancies.

The full proof is the unconditional combinatorial layer decomposition and inequality (1) in `RESULT.md`, followed by weak-composition counting and the two-path decomposition. Neither finite enumeration nor the finite-state comparison is used to extrapolate to infinitely many parameters. No independent audit or external verification has been conducted.
