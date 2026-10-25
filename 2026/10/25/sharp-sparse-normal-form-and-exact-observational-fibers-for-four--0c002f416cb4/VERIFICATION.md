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

# Reproduction and limits

The standalone `checker.py` uses exhaustive enumeration of all binary relations on the labelled chains of \(1\), \(2\), \(3\), and \(4\) worlds. For each relation it evaluates all four primitive modalities directly on every upward-closed subset and separately computes the proposed four-extrema signature. It verifies exact agreement and groups relations by signature. It then compares every observed group size with the multiplicative local-choice formula, not merely the totals.

Execute `python3 checker.py`. The final success line is `ALL_CHECKS_OK 337329`. The exact semantic class totals are \(2\), \(16\), \(279\), and \(7171\). The largest group sizes are \(1\), \(1\), \(8\), and \(324\).

The checker also tests the extremal two-edge family through \(12\) worlds and confirms four separate two-world pairs demonstrating that none of the four primitive operations is determined by the other three.

For arbitrary finite chain sizes the theorem is proved by threshold semantics, independent endpoint choices, and a forced-edge construction. The finite checker is diagnostic support, not an exhaustive proof over unbounded sizes. Independent external auditing has not been performed.
