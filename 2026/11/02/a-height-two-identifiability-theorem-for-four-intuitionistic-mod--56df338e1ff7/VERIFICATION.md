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

# Reproducibility and scientific boundaries

Run `python3 checker.py` from a directory containing the supplied script. The script uses only the Python standard library and evaluates the four modal truth clauses directly for every finite persistent valuation considered. It checks 1-, 2-, and 3-point preorder universes exhaustively, tests all 65,536 accessibility relations on a fixed four-world branching height-two partial order, and verifies the explicit two-world indispensability pairs and universal obstruction patterns on small orders. The expected terminal output ends `ALL_CHECKS_OK`.

No computation on finite carriers establishes the theorem for infinite preorders. The separate symbolic proof directly reconstructs all edges and constructs noninjective relation pairs on every disallowed preorder. The verification does not cover arbitrary accessibility-class restrictions or comparisons of frame-validity logics.

Scientific overlap checks compared the exact claim with primary four-connective semantics, distributive modal operator compatibility, and earlier finite-chain observational results. The latter already covers the finite-chain subcase. The new mathematical contribution concerns the full classification for arbitrary preorders, including branching and non-antisymmetric cases, and the irredundance of all four operations. Historical priority has not been independently validated.
