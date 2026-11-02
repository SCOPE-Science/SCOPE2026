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

# Verification scope

Run `python3 verify.py` using Python 3.9 or later. The program enumerates integer compositions of total length \(n\), constructs the graph joining two compositions when their coordinatewise-minimum intersection is at most \(k-1\), and recursively counts fixed-size cliques in the upper-triangular graph. It does not assume the symbolic proof or any oracle optimal values when producing counts.

Exact enumerations include the ternary four-survivor lengths \(n=6,7,8,9\), ternary five-survivor lengths \(n=8,10,11,12\), and binary control cases. At the ternary four-survivor upper endpoints it obtains exactly 9 and 1 maximum codebooks; for five survivors, exactly 9 and 1. Constructed endpoints and lower-threshold witnesses are checked over six alphabet/survivor parameter pairs. These finite results corroborate the proof but do not independently prove its universal quantifiers.

The script prints `ALL VERIFICATION CHECKS PASSED` on successful completion. The adjacent output file records all checked counts. Independence of an external mathematical audit is not claimed.
