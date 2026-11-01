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

# Reproduction and verification

Install the dependencies in `requirements.txt`, then run `python volume_checker.py` with Python 3, NumPy and SciPy. The exact combinatorial checks use only the Python standard library; the numerical polytope cross-check uses `scipy.spatial.ConvexHull` and `scipy.spatial.HalfspaceIntersection`.

Executed output:

`CHECK_OK exact_volume_identities=567 independently_computed_convex_hull_volumes=30 parameter_N=3..40`

The first 456 identities come from separate exact sums over beta-binomial order-chamber volumes and over type-A root-polytope facets, at six rational metric parameters for each of 38 cardinalities. The remaining 111 checks evaluate the unique maximizing parameter, exact ratio, and peak product for cardinalities 4 through 40. Independent numerical convex-hull computations evaluate two actual polytopes at three metric parameters for cardinalities 3 through 7. These results check normalization, dimension and the absence of a mixed tip-volume term.

The unrestricted theorem is proved by the determinant-one chamber decomposition, facet-product staircase triangulation, visible-facet cap addition, and single-variable differentiation in `RESULT.md`. Finite calculations do not prove the infinitely many cases or substitute for the geometric facet argument. Independent external mathematical review was not performed.
