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

The theorem uses the exact binary subsequence relation (order-preserving deletion), not contiguous-factor avoidance. The proof is contained in `RESULT.md`: a shortest-absence recursion, simultaneous induction on a periodic template and its first-symbol-deleted suffix, boundary-count exclusion, and a ternary-digit gap identity.

Run `python3 checker.py` in the same directory. The checker requires only Python 3 and no external datasets or packages. It computes actual shortest absent subsequence sets using suffix dynamic programming, independently compares all candidate strings for smaller complete Cantor iterates, and checks reproducible gap-inflated examples. The finite checks passed in the preparation environment; they do not certify the infinite induction or historical priority.

Self-review is documented separately. Independent audit has not been performed.
