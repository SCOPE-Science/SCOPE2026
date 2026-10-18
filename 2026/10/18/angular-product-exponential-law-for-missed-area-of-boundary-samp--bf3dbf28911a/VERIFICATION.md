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

# Verification evidence and limits

The proof checks the finite-sample corner-triangle identity on the event of occupied sides, exponential rarity of its complement, joint convergence through disjoint-arc survival functions, all-integer-moment uniform integrability, and the exact product-exponential Laplace/moment computations. The planar angle sum and strict Jensen concavity certify the equality classification.

The standalone standard-library script `checker.py` runs seeded Monte Carlo checks and checks corner triangles against independently computed convex hulls for three nondegenerate polygons. Its recorded run produced 300 exact corner-area identity tests, three scaled-mean simulations, and two product-exponential moment comparisons without assertion failures. The checker does not prove an infinite-sample assertion, a distributional rate, completeness of bibliographic searches, or independent scientific validation.

Independent audit has not been performed.
