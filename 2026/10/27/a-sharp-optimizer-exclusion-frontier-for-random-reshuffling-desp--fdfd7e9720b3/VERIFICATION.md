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
The program `rr_support_check.py` requires only the Python standard library and runs with `python rr_support_check.py` from the directory containing the files. It enumerates exact rational state distributions for five rational step sizes across six epochs, verifies both exact second-moment expressions and their ratio, checks exclusion inequalities when appropriate, reproduces the finite four-gradient small-ball difference, and independently checks all seven finite-TV cases at the half-step. The program executed successfully.

The infinite claims instead follow analytically from the explicit two-update epoch map, uniqueness and support of contractive iterated-function-system invariant measures, two first-level interval overlaps, and the separated-similarity Hausdorff dimension formula; the actual finite checker is not represented as an exhaustive proof over continuous parameters or infinite time. Stationary-law convergence is weak, not claimed to be total variation convergence from discrete finite laws. The self-review examined the proof and listed assumptions. Independent audit is not performed.
