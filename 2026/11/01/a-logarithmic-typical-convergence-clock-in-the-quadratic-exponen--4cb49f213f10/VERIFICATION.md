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

# Reproducibility checks

Execute `python3 verify.py` from the directory containing this document, the program and `verification_output.txt`. The verifier independently implements the network as a bit-mask update and as a coordinate-wise Boolean recurrence. It enumerates all \(2^n\) binary initial states for every \(3\le n\le14\), checks the gap bounds and exact unique worst-case initializer, checks every singleton entry time, and verifies the Boolean walk-covering inclusion for \(3\le n<90\).

The recorded execution reports `EXHAUSTIVE_STATES_OK 32760`, `BOOL_WALK_INCLUSION_OK`, and `WIELANDT_OR_ALL_CHECKS_PASSED`. It checks no dimensions above \(89\), does not enumerate every infinite-family state, and does not statistically establish the probabilistic limits. The mathematical proofs for those claims are in `RESULT.md`. The relevant external full texts available for inspection were arXiv:0805.0275v1 and arXiv:2104.04403; the 1998 generalized-exponent article remained unavailable in full.
