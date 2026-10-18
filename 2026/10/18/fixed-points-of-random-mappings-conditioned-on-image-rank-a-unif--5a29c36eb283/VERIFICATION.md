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

The standalone `verify_rank_fixedpoint.py` uses only the Python standard library. Running `python3 verify_rank_fixedpoint.py` completed and printed `PASS 8633 exact finite-size assertions`. It exhaustively enumerated every self-map on sets of cardinality 2, 3, 4, 5 and 6; aggregated exact fixed-point factorial moments at each image rank, checked the conditional variance and inclusion–exclusion formulas, and checked associated degree-sequence moments.

The enumerations confirm these finite cases only. The all-size theorem, asymptotic statements, and total-variation inequality follow from the mathematical proof in `RESULT.md`, not from the script. Independent audit and independent validation have not occurred.
