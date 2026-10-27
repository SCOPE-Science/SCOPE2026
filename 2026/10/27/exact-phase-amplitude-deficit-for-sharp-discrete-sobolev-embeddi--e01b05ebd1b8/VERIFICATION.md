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

The derivation reconstructs the zero-extension convention, the Gram entries and their signs, invertibility by injectivity of finite-support differences, entrywise Green positivity using all one-row/one-column Toeplitz minors, and the Hilbert projection and phase-graph equalities.

The included `verify.py` computes rational inverses for orders 1 through 5 and support lengths 2 through 9, checks exact sharp constants, and evaluates the deficit identity for 640 deterministic complex sequences. The numerical replay passed. Separately, a finite implementation checked the collision-free path schedule for all deleted-row/deleted-column choices in orders 1 through 7 and lengths 2 through 9. These tests are not exhaustive for arbitrary orders or lengths; the written combinatorial proof handles the universal quantifiers.

The originality comparison inspected the motivating arXiv HTML primary paper and related indexed records. Historical priority is not independently certified.
