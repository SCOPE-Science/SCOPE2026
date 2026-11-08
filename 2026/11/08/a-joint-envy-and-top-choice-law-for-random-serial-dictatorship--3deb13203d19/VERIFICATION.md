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

# Mathematical verification

The standalone `verify_joint.py` has no nonstandard dependencies and is intended to run as `python3 verify_joint.py`. It derives an exact rational bivariate transition table and tests all probability masses and identities for \(n=1,\ldots,7\). Independently, for \(n=1,\ldots,4\), it exhausts all \((n!)^n\) labeled strict preference profiles, constructs RSD assignments, and directly counts both envy statistics and their joint table. The exhaustive check also computes the number of agents in both categories; its exact expectation equals one for all four exhaustively tested market sizes. The computed tables agree with the recurrence.

The general proof is the conditional-uniform-rank argument followed by telescoping survival factors, presented in RESULT.md. These analytic steps, and not the bounded enumeration, establish the quantifiers for every integer \(n\ge1\).

**Scope:** No independent audit has been performed. The checker provides finite diagnostic support, not an infinite-machine certificate or independent scientific validation.
