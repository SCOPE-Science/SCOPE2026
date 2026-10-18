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

# Reproducible checks and their limits

Run `python3 fano_radius_exact_check.py` using Python 3 and the standard library. Expected successful output begins with `PASS` and reports seven lines, six retained lines, \(128\) cube sign vertices, \(10\) proper two-colourings of the six-line incidence hypergraph, \(118\) norm-attaining vertices, all \(128\) restored, and support value \(3/5\) for the explicit norm-one dual witness. The program checks each of the seven possible deleted lines through binary-linear line transitivity and tests strictly positive rational barycentric weights.

The general upper bound is analytic rather than empirical: a supporting functional of \(\ell_1\)-norm \(1\) loses twice the smaller of the two signed masses on a retained line. Proper colourings are classified by the three perfect matchings on the four points outside the deleted line. One colouring class requires at least three units of base mass and two units of leaf mass per unit of two-sided margin, hence the margin is at most \(1/5\); the other requires six units, hence at most \(1/6\). Equality at \(1/5\) is exhibited explicitly. The exact arithmetic check verifies only the stated finite combinatorics and witness; it does not enumerate the continuum of real coefficients or claim to do so.

The proof uses ordinary support-function separation for finite-dimensional convex bodies and strict positivity of every incidence coefficient. It assumes no numerical optimizer, external validation, or infinite exhaustive computation.
