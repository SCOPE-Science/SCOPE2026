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
# Verification record

The standard-library `check.py` is fully embedded with the result and was run successfully from its actual package path with `python3 check.py`.

It constructs every pair-Kneser graph \(KG(n,2)\) for each integer \(5\le n\le10\), verifies degrees and edge counts, and for every oriented graph edge independently tests the claimed integer-normalized Poisson potential at every graph vertex. The same checks sum every edge-coordinate absolute value in the cut and cycle projection columns and compare the results with exact rational formulas. The run passed 652346 exact assertions, including the indicated endpoint maximizing examples. The package contains no external runtime requirements beyond Python 3.

Finite numerical or exact-rational tests do **not** certify all larger graph orders. The universal proof is the symmetry classification, Laplacian derivation, graph-edge class enumeration, and rational finite-difference argument in RESULT.md. The originality comparisons are bibliographically bounded; no independent third-party scientific validation has been performed.
