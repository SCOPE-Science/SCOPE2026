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

# Reproducibility

Run `python3 checker.py` in the same directory as this document. The script uses only the Python standard library and is self-contained.

The direct check constructs each nonzero partial translation on \(\{1,\dots,n\}\) for \(1\le n\le9\), then computes the nonzero-product indicator by image membership under genuine partial-map composition. Independent length-based summation and the two closed formulas are compared through \(n=100\). The expected output is `CHECKER_OK: direct maps n=1..9, length sums n=1..100`.

The infinite-parameter proof is the interval bijection plus the bounded-degree polynomial identity in `RESULT.md`. Finite computations independently test those steps but do not substitute for the degree bound or the disjointness argument. Mathematical record and source comparisons are detailed separately in `AUDIT.json`; no independent audit has been performed.
