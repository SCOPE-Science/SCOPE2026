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

`check_metric.py` builds the full oriented codimension-one boundary-incidence matrix for the \((n-1)\)-simplex independently of the stated Gram formula. It checks the resulting top down-Laplacian against \(nI-ss^{\mathsf T}\), maps the columns into a computed orthonormal basis for their affine span, forms their convex hull, and independently maximizes the ball radius using its hull facet inequalities and linear programming. The script compares the formula with every computed inradius, all proposed minimum-sphere vertex distances and supporting-vertex counts, and all facet distances from the stated incenter.

Executed successfully for integers \(3\le n\le10\), including both parities. The tests require Python 3, NumPy and SciPy and can be reproduced with `python check_metric.py` from the directory containing the file. Qhull and the LP solver supply independent finite-dimensional numerical comparisons; their tolerances cannot establish results beyond the tested dimensions. The complete analytical proof for every dimension appears in `RESULT.md`. No independent audit was conducted.
