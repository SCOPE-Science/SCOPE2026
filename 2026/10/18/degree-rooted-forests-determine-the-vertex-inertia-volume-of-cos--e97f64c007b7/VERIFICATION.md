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

# Reproducible mathematical verification

The analytic proof and normalization are in `RESULT.md`. Under Python 3.9+, run `python CHECKER.py`; only the standard library is required. The checker separately creates all three real point-coordinate vertices of every tested graph, computes the centered covariance using the exact integer numerator, and derives the product of its nonzero eigenvalues from a principal cofactor. This direct route is checked against the independent graph expression involving \(\det(2D-A)\).

A second exact implementation enumerates acyclic edge subsets and their degree-rooted forest weights. Every labeled tree through five vertices and every connected simple graph on three and four vertices was checked: **187** graph/tree instances. The star and path formulas were checked for all orders from two through thirteen. Two six-vertex degree-sequence twin trees produced respectively the exact values \(492\) and \(483\), and their covariance pseudodeterminants agreed with independent moment calculations. The executable prints `PASS` on success and stops by assertion on any failed equality.

Finite enumeration is not an exhaustive proof for arbitrary graphs and dimensions. The symbolic block matrix, centering determinant lemma, forest Cauchy–Binet expansion, and path recurrence in `RESULT.md` establish the quantified general claims. Inertia ellipsoids are equal-vertex-mass dispersion ellipsoids and are not certified John or Löwner ellipsoids. No independent audit was performed.
