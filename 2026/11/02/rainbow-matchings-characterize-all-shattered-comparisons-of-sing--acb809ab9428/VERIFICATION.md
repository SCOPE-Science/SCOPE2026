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
# Reproduction of the finite checks

Run `python verify_single_peaked.py` with standard Python 3.9 or later. The checker generates every strict single-peaked preference on the known axis for `n=1,...,9` by endpoint removals. It constructs truth tables for all pairwise comparisons, traverses every shattered support using the hereditary two-branch test, and compares the supports themselves (not just counts) to the constructed rainbow matchings. A separate memoized minimax recursion computes the Littlestone dimension from comparison masks.

The recorded standard output is `verification_output.txt`, ending with `SINGLE_PEAKED_SUPPORT_CLASSIFICATION_ALL_CHECKS_PASS`. The tests cover all orders only up to nine axis vertices, whereas the theorem has a self-contained unrestricted proof. No formal-proof or independent scientific validation is asserted.
