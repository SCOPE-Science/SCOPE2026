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

# Verification of finite identities

Execute `python3 checker.py` in the same directory. The checker uses only the Python standard library; it enumerates all 8191 attachment words with at most twelve choices and verifies metric identities for every vertex pair. It independently compares a postorder diameter implementation with brute-force lowest-common-ancestor distances. It also checks 75 seeded larger trees. The observed count is 1,797,528 passed assertions.

These finite tests check the deterministic inputs to the analytical proof, not the infinite-index limit, probability-tail estimates or the central limit theorem. Those are established symbolically in the result document. The audit described here is not an independent scientific audit.
