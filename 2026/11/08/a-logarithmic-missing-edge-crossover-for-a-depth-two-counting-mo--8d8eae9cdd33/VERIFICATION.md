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

# Verification details

The standalone `checker.py` enumerates all unary colorings and all labelled directed loop-allowing adjacency matrices for \(1\le n\le4\). For each color split it verifies that the root count difference without the self-successor follows the exact conditional trivalent convolution derived in the proof. It also verifies direct binomial convolution probabilities for each color split through \(n=11\) against explicit row enumeration. Execution ends with `NEAR_COMPLETE_MODAL_BALANCE_EXACT_CHECKS_OK` on success.

These are finite checks of definitions and conditional distribution identities only. The moving-parameter asymptotic claim depends on the self-contained exponential-tilting and local-limit argument, conditional central limit theorem, Bernstein inequality, and subsequence proof in `RESULT.md`. No separate independent mathematical assessment was performed. The checker deliberately does not purport to certify an infinite theorem or its historical priority.
