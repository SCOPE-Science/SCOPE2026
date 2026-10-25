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

# Verification and limits

The proof checks the entire domain analytically: a flag-cell decomposition covers volume almost everywhere; squared-distance differences are affine; the candidate ordered pair minimizes at every cell corner; the edge-normalized gap is one barycentric coordinate; uniform simplex measure gives \(\operatorname{Beta}(1,d)\). Thus the calculation is not restricted to the finite examples below.

`verify.py` can be run using Python with NumPy and SciPy as declared in `requirements.txt`, and tests polygon orders, simplex dimensions, cubes and cross-polytopes, plus the two nontrivial icosahedral and dodecahedral solids. `checks.log` is actual program output. Tests use pseudorandom samples and approximate tolerances; they are diagnostics only, not exhaustive or an independent proof.

The reported result concerns squared Euclidean distances to *distinct* vertex sites and volume-uniform interior points of full-dimensional regular Euclidean convex polytopes. It does not establish corresponding claims for arbitrary polygons/polyhedra, nonuniform sampling, unsquared distances, or data corrupted by measurement error.
