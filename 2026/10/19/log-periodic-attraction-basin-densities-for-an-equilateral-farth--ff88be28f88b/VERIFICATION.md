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

Run `python3 verify_equilateral.py` using Python 3's standard library; the program has no external dependencies or downloaded inputs. It represents the Euclidean plane in exact coordinates \((p,q)\leftrightarrow(p,\sqrt3q)\), and all relevant distances, projections and branch tests use `fractions.Fraction`.

Actual execution passed \(46{,}839\) literal geometric transition comparisons, \(15{,}613\) rational-state basin comparisons, \(4{,}788\) independent exact interval-length tests, as well as periodic-orbit and exceptional-sequence checks. The analytic proof independently establishes the infinite-domain conclusions by piecewise-affine entrance identities, all midpoint preimages, and a geometric-series length calculation. Finite enumeration is a diagnostic, not a replacement for proof of claims quantified over all real initial points.

The manuscript states the precisely constrained geometry, the tie-as-fixed rule, directed cutoff orientation, and residual historical-priority risk. The existence and number of attracting three-cycles were previously established for the broader triangle family; the substantive new assertions concern complete attraction basins and their one-sided scaling behavior.
