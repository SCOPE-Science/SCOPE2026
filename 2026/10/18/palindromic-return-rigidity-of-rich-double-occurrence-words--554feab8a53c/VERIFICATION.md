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

# Verification and reproducibility

The packaged `check_rich_dow.py` is standalone Python 3 code requiring no external libraries. Execute `python3 check_rich_dow.py`. It exhaustively enumerates all \( (2q-1)!! \) first-appearance-canonical length-\(2q\) double-occurrence words for \(q=1,2,3,4,5,6,7\). It independently compares directly computed ordinary palindromic-factor richness, palindromic letter returns, and block parsing. Direct letter-endpoint crossing counts are compared against a separate dynamic recurrence for the bivariate rational series.

Observed results: \(q=1\): 1 total / 1 rich / crossing profile [(0,1)]; \(q=2\): 3 / 3 / [(0,2),(1,1)]; \(q=3\): 15 / 6 / [(0,4),(1,2)]; \(q=4\): 105 / 14 / [(0,8),(1,5),(2,1)]; \(q=5\): 945 / 31 / [(0,16),(1,12),(2,3)]; \(q=6\): 10395 / 70 / [(0,32),(1,28),(2,9),(3,1)]; \(q=7\): 135135 / 157 / [(0,64),(1,64),(2,25),(3,4)]. The check completed with `RICH_DOUBLE_OCCURRENCE_PASS total_normalized_words= 146599`.

The claims for arbitrary \(q\) depend on the combinatorial proof, not on numerical extrapolation. The program is finite and supplies no external independent mathematical audit.
