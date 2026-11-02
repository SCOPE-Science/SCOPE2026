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

The standalone checker enumerates binary-subset encodings through size seven; validates that the permutation count is exactly \(2^n-n\); confirms that a unique descent decodes every nonidentity permutation; tests all proper prefix-suffix overlaps for code families of sizes one through eight; and compares finite first-hit event counts for the feasible cases. The observed output was `ALL_CHECKS_OK`. This computation does not establish infinite-model probability statements; the finite-state and first-hit bijection proofs are supplied in RESULT.md.
