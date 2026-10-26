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

Run `python3 verify.py` with the Python 3 standard library. The script directly forms the incidence poset, enumerates all downsets as bitmasks, computes rowmotion from minimal complement elements, and traces each orbit. It checks every case from \(n=1\) through \(n=8\) against the predicted cycle counts and independently checks the total number of ideals. The larger-\(n\) theorem follows from the proof in `RESULT.md`, not from extrapolation of these computations.

Observed cycle profiles at the eight tested values:

| \(n\) | ideals | count of length \(2\) | length \(3\) | length \(8\) |
| ---: | ---: | ---: | ---: | ---: |
| 1 | 5 | 1 | 1 | 0 |
| 2 | 13 | 1 | 1 | 1 |
| 3 | 35 | 1 | 3 | 3 |
| 4 | 97 | 1 | 13 | 7 |
| 5 | 275 | 1 | 51 | 15 |
| 6 | 793 | 1 | 181 | 31 |
| 7 | 2315 | 1 | 603 | 63 |
| 8 | 6817 | 1 | 1933 | 127 |

All tests passed. Numerical verification is exhaustive only within the stated finite range and is not independent scientific audit.
