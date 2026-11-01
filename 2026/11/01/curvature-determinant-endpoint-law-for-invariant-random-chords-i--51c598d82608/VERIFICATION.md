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

The proof in `RESULT.md` establishes the infinite-family result from local boundary expansions, a matrix determinant identity, compactness and Cauchy's projection formula. The standalone `verify.py` provides independent reproducible finite checks and was executed successfully using NumPy, SciPy and SymPy. It exactly checks the determinant for tangent dimensions 1, 2 and 3, including noncommuting endpoint matrices in dimensions 2 and 3. It also computes the exact ellipsoid-tail invariant line mass independently by angular quadrature for semiaxis sets (2,1), (2,1.4,0.9) and (3,2.4,1.2), with deficit levels 0.04, 0.015 and 0.005. After dividing by the predicted deficit power, all final test ratios differ from one by less than 0.002. This is numerical corroboration of the coefficient for examples, not a proof for arbitrary convex bodies.

The curved-boundary conditions, positive matrix condition and finite diameter multiplicity are essential; no inference is made for excluded cases. The prior-paper comparison includes explicitly named inaccessible full texts; independent priority review has not been performed.
