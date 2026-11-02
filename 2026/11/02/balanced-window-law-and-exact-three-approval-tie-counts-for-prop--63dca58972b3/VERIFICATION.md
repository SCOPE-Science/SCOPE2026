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

# Reproducible mathematical checks

The analytical proof in RESULT.md establishes the infinite family. The standalone `verify.py` performs exact independent finite calculations to corroborate critical implications and counts.

Run `python3 verify.py` from a directory containing the file. Only Python 3.9+ standard library is used. PAV harmonic scores are multiplied by a common integer denominator, so no floating-point comparison is used. For all n=3,..,12 and d=1,..,n it enumerates every 0/1 committee, independently computes all cyclic window intersections and their PAV scores, confirms the claimed sharp bound, and checks that equality occurs exactly for balanced windows. For d=3 it also compares winning counts to the binomial formula, and extends the full count check through n=18 using an integer scaling of the first three harmonic weights.

Observed output terminates with `VERIFY_OK enumerated_binary_committees 606200 domain_first 3 domain_last 18`. In particular the n=12,d=3,k=6 winning count is 174 and n=18,d=3,k=9 count is 2570. This verification is exhaustive only in the stated finite ranges and does not independently certify the proof for all n.

Independent audit: not performed.
