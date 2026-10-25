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

# Reproduction and mathematical boundaries

The exact statement and full proof appear in `RESULT.md`. Run `python verify.py` with NumPy, SciPy and SymPy installed. The script separately constructs the six unit normals, verifies their first and second moments, computes the convex hull of the intersection of six halfspaces, and independently compares the resulting vertex count, surface area and volume with the analytical expressions. The tested twists are \(0\), \(10^{-5}\), \(\pi/12\), \(\pi/6\), \(0.7\), and \(\pi/3\). It also tests the symbolic facet-area reduction, scale-normalization formula, derivative and both exact endpoint values. All tests passed in the execution environment.

The numerical hull checks are finite corroboration only: they do not certify all twists, nor do they test an exhaustive census of arbitrary frame configurations. Universality instead follows from the complementary-projector and self-inversive-polynomial argument together with the closed convex-geometric calculation. The planar root-factorization argument allows coincident roots at the degenerate endpoint. The main proof uses only classical finite-dimensional linear algebra, elementary symmetric-polynomial identities, convex polarity, the divergence theorem and Minkowski uniqueness.

No independent review, external formal certificate or third-party reproducibility attestation has been performed. The priority comparison is best-knowledge only and retains the limitations recorded in `REVIEW.md`.
