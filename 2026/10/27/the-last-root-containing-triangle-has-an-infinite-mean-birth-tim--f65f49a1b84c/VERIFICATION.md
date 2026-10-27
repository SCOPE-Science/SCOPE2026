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

Run `python3 verify.py`. The script uses Python standard-library `fractions`, `itertools`, and `math` only. It performs exact exhaustive enumeration of 14,400 attachment sequences on six vertices and checks 15 first/pair moment equalities. A separate exact root-degree dynamic program checks 36 finite-window Bonferroni comparisons. It also prints deliberately truncated numerical tail-expectation diagnostics, clearly labelled as such; these are not infinite proofs.

The full theorem is justified by the displayed analytic proof in `RESULT.md`. The exact conditional probability, the closed two-arrival identity, and summation with Bonferroni are the critical steps. No infinite numerical enumeration or independent audit is claimed.
