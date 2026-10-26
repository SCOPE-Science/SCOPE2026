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

The reproducible checker `stable_welfare_boundary_check.py` uses exact integer arithmetic and standard Python only. In direct execution it passed exhaustive tests of 1, 16, and 46,656 labeled strict preference profiles at market sizes 1, 2, and 3; the independently specified strict blocking-pair condition checks every bijection in each profile. It established the full three-by-three frequency counts and validated the four-by-four witness by exhaustive checking of its 24 bijections. An additional separate enumeration implementation reproduced the three-by-three counts. The infinite family of larger markets is not exhaustively checked; only a single explicit n=4 counterexample is required for the sharp-cutoff claim.
