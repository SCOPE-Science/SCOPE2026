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

The exact proof is provided in `RESULT.md` and relies on a facet-sign silhouette lemma and exhaustive enumeration of the edge types of a disjoint vertex truncation. The proof also identifies all fourteen strict sign patterns and determines their exact Haar probabilities for a regular tetrahedron. The numerical/symbolic verification is corroboration, not an infinite proof.

Run `python verify.py` with NumPy, SciPy and SymPy. This was run from the actual embedded script source on 28 October 2026. It passed 28,800 independently computed projected convex hull comparisons across three original tetrahedron shapes and sixteen truncation subsets; all complementary identities; exact symbolic formulas for all five distributions; and 250,000 random viewing directions per distribution. The script prints `PASS:` upon success. These tests do not verify all infinite parameter choices; that guarantee comes from the analytical proof.

All claims apply to generic viewing directions and disjoint truncations by planes parallel to opposite original facets. The first stage's tetrahedral three/four-vertex probability is an acknowledged classical result. Priority is subject to unindexed earlier stereology or projection theorems. No independent audit was performed.
