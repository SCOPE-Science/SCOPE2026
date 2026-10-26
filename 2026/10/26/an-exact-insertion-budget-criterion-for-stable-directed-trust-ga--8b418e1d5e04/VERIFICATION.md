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

# Reproducibility and logical boundaries

Run `python checks/verify.py` using Python 3.10+ with the standard library. The checker produced `PASS 6228 exact finite graph/aggregator cases and sharpness witness`.

For two and three vertices the graph-weight sweep covers all arc statuses absent or integer weight one or two, with all possible directed edges allowed except loops; for four and five vertices it uses 150 pseudorandom instances per size with a fixed seed. Each instance is tested against the six aggregators, every nonempty restricted vertex set, and every coalition of each restriction. The code uses `fractions.Fraction` arithmetic throughout, including arithmetic means and order-statistic tests.

The check does not enumerate all real weights, larger networks, or every multiset function. The universal result is derived symbolically from the insertion inequality in the written proof. Its necessity is certified by direct formulas for the two-player in-star restriction; the provided nonlinear operator additionally gives a three-vertex empty full core. An independent audit has not been performed.
