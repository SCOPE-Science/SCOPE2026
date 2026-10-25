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

# Verification of the triangle three-jet reconstruction theorem

The proof in `RESULT.md` reconstructs every ingredient analytically; code is corroborative, not an infinite certificate. Run `python3 verify.py` in a standard Python 3 environment. The script reconstructs intersection polygons by successive half-plane clipping, integrates the resulting covariogram for five triangles, checks the exact coefficient formula, evaluates strict curvature-ratio ordering on 5,000 seeded triples, and checks strict monotonicity on five fixed-invariant arcs. The checked execution printed `VERIFY_OK`.

The curvature-ratio derivative is validated symbolically in the mathematical proof, not from floating-point tests: with \(v=(\pi-x)/2\), it is \(4\cos^2v(v\cos v-\sin v)/\sin^5v<0\). Boundary cases are handled by continuity, and the equilateral case by strict Jensen equality. The finite numerical tests do not establish convergence at arbitrary radii or quantitative inverse stability. No external independent audit has been carried out.
