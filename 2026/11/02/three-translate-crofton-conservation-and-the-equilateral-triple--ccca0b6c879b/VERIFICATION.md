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

# Reproducibility and verification

The exact theorem is proved in `RESULT.md` from fixed-direction projection intervals, Cauchy's planar perimeter identity, one-dimensional inclusion–exclusion, and an explicit six-sector integral for equilateral centers.

Run `python3 checker.py` from the directory containing these files. The checker uses only Python's standard library. It independently sorts all projection-interval endpoints, calculates the lengths where exactly one, two, or three intervals are active, and integrates those lengths numerically. The tests encompass a noncentrally symmetric triangular body, a rectangle, a polygonal approximation to an ellipse, and eight disk radius/spacing ratios spanning both critical ratios. The checks passed in the final package with the discrepancies stated in `RESULT.md`.

The infinite statements are established by the written proof, **not** by finite sampling. The numerical tests do not establish novelty or independently audit the result. First public availability of the older directly relevant focal source is confirmed as 14 September 2010 for DOI 10.1007/s00454-010-9292-x; a 2002 line-transversal source and an undated classical three-circle exposition are also expressly acknowledged.
