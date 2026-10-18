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

# Reproduction

Run `python paired_support_checker.py` and `python convex_boundary_checker.py` with a standard Python 3 installation. The first enumerates all nonempty sets of positive predicate footprints on world sets of sizes \(1\) through \(4\), takes the two generated support downsets, keeps the minimum individual count per pair, and verifies the exact extremal-footprint formula. The second enumerates **every** subset of each corresponding Boolean lattice, tests convexity directly using all three-way inclusion intervals, and counts distinct boundary extremes. Both assert identical known exact count totals and four-world histogram.

The finite check does not by itself prove the all-\(n\) theorem; the general proof is in `RESULT.md`, including the construction and a two-Sperner chain-counting argument. The programs do not address historical priority, independent reproducibility by third parties, or the full monadic logic.
