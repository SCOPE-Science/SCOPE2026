---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-30.md",
      "INDEPENDENT_AUDIT_2026-10-30.json"
    ]
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Independent mathematical audit

## correctness

PASS

The canonical genus-two double cover h:C→P1 has K_C=h^*O(1); every bicanonical zero divisor is a sum F_s+F_t of two degree-two canonical fibres with multiplicity. Every effective degree-three sub-divisor includes a full F_s or F_t, even at branch or coincident fibres, and is P+F_t; converse is immediate using F_h(P)+F_t. For any degree-three line bundle L, RR gives h0(L)=2, h1(L)=0, so Abel-Jacobi α3:Sym3 C→Pic3 C is a P1-bundle. The Abel translate T={K_C(P)} is C and its inverse image consists exactly of complete linear systems P+|K_C|; multiplication by the tautological O_C(P) section trivializes the family projectively, giving CxP1 smooth Cartier divisor. Pic3(C) is an abelian surface; adjunction gives normal T/Pic3 is K_T, pulling back gives pr_C^*K_C. Independently checked degrees and RR plus boundary fibre arguments, not relying on a saved code log.

## originality

PASS

Dinh’s arXiv 2406.04224 genus-two extension treats quadratic-differential-special divisors in the broader wobbly-bundle/spectral-curve setting and gives criteria for wobbliness, but the inspected definitions/results do not identify this base-curve sub-divisor locus in Sym³(C) with product C×P1 or compute its normal. Related published Resultary wobbly-divisor normalization P1×Z3 has a genus-17 curve in a different ambient moduli space and does not cover the genus-two base Q3 locus. A textbook-level Abel-Jacobi inference or unindexed symmetric-product source remains a priority risk, despite direct distinctness of checked wobbly results.

## value

PASS

The low-genus quadratic-differential incidence condition has a natural role in wobbly-bundle geometry; specifying the entire smooth subvariety and its normal class is more informative than membership counts, and directly usable in intersection/deformation calculations. It is a short special-geometry structural lemma, not a claim of a new wobbly-divisor classification or unrelated arbitrary isolated computation.

The dated certificate retains the supplied scientific assessment, sources and limitations.
