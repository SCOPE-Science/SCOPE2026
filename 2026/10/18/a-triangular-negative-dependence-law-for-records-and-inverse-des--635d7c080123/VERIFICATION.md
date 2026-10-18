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

The theorem is proved symbolically by a value-transposition coupling, independence of selected high-label positions and their relative order, and an exact hypergeometric order-statistic formula. To independently check finite cases, run `python3 verify.py` with Python 3 and no third-party dependencies. The script exhaustively enumerates every permutation of sizes \(2\) through \(8\), checks each entry of the cross-covariance matrix with exact fractions, and checks the claimed monotone one-coordinate coupling for each paired permutation. It also checks the telescoping covariance totals. In the completed run, all \(168\) exact matrix entries and all conditional value-transposition comparisons passed. Full enumeration is not a proof beyond size eight; the algebraic coupling argument covers all sizes. No independent audit has been conducted.
