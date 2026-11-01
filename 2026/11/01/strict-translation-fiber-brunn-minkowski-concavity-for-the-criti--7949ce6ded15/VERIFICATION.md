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

The proof is analytic and self-contained modulo established geometric facts: divergence/Minkowski surface identities, Brunn–Minkowski with equality classification, and the normal-area transformation under invertible affine maps. In particular, strictness follows from a global equality obstruction, not from finite tests.

The companion verifier `verify_transition_centers.py` ran under Python 3. It evaluates polygonal facet-normal measures and midpoint Jensen inequalities, computes areas by convergent radial integration, checks positive volume-root concavity margins for a square and a nonsymmetric triangle, and checks central symmetry inclusion at representative points. It reports `PASS: convexity, strict volume-root concavity examples, center inclusion`.

This verifier is not a formal proof, a numerical exhaustion of origins, or an independent assessment. The mathematically proved scope is all full-dimensional convex bodies in dimension at least two, all interior origins and positive thresholds. Earlier literature priority is provisional. No independent audit has been performed.
