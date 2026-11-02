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

# Reproducible mathematical checks

Run `python3 verify.py` with Python 3 standard library. The test constructs each wheel from its hub and rim edges, computes shortest-path distances by breadth-first search, derives all forbidden three-vertex geodesic subsets directly from the distance equality, and tests every vertex subset for inclusion-maximality. Independently, it computes the predicted two-variable formal-power-series coefficient of the asserted logarithmic determinant by reciprocal-polynomial arithmetic.

For each \(n=5,\ldots,13\), it compares the full polynomial coefficient dictionary, the number and sizes of hub-containing sets, the smallest and largest rim-only maximal cardinalities, and both extremal multiplicity formulas. The packaged `verification_output.txt` records the output and ends `VERIFY_OK`.

These finite checks do not exhaust all values of \(n\). The all-parameter statement requires the combinatorial run characterization and the transfer trace identity proved in RESULT.md. The numerical growth constant derives from the exact reciprocal sextic; it is not inferred from sample counts. This document contains no independent external validation.
