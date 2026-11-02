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

# Verification record

The analytical proof is in `RESULT.md`. To reproduce the finite tests, run `python3 verify.py` with Python 3 and its standard library. The test compares the claimed PBH characterization against exact rational Kalman-matrix ranks for 9,126 selected configurations; it checks all vertex subsets for the specified small motif sizes and boundary-weight cases for larger motifs. The expected output is `PASS: 9126 exact rational controllability comparisons`.

Independently from the executable verifier, symbolic polynomial expansion confirms the 3-by-3 common-pair characteristic polynomial and the exact zero-coordinate factor \((b-ma)(ac+b(a+c))\) (and its symmetric counterpart).

No finite number of tests establishes the all-integer/all-positive-real statement, for which the invariant splitting, PBH and nodal calculation constitute the proof. No independent audit has been performed.
