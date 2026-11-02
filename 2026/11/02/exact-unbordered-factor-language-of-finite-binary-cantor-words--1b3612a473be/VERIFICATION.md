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

The included `checker.py` reconstructs each finite Cantor iterate, independently computes exact unbordered candidate sets via the prefix-function border criterion (no gap shortcut), and compares complete sets against the theorem's parametric construction for ranks 1 through 6. All checks passed, including factor counts 4, 12, 60, 348, 2076, 12444 and maximal lengths 2, 6, 18, 54, 162, 486. The proof's valuation-periodicity argument, not finite testing, covers all ranks.

Run with `python3 checker.py`; no external packages or downloads are required. The check exhausts these finite ranks only. Historical priority was checked against named accessible work but is not guaranteed exhaustive. Independent audit has not been performed.
