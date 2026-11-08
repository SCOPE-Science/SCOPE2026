---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-04.md",
      "INDEPENDENT_AUDIT_2026-11-04.json"
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

The exact f² coefficient extraction in RESULT.md yields the sparse 4×4 Cartier matrix; the scalar line contributes one stable image dimension iff L=a²+2b≠0 and the complementary alternating 3-block contributes two iff S=b²(1+2a⁵)+4(a⁵+b⁵)≠0. The first Cartier rank is 2+1_{L≠0} on smooth locus bΔ≠0, yielding a-number 2 or 1; Frobenius semilinearity is treated via twists. Over char5, S=(2b²+4)a⁵+b²+4b⁵ is primitive and −B/A not a fifth power because B′A−BA′=3b+4b⁶≠0, proving absolute irreducibility; gradient excludes singularities inside U. Substituting L=0 (b=2a²) gives S=−2a⁴(a+1)(a−2)⁵ and Δ=2a²(a−2)²; after bΔ≠0 only a=−1,b=2 survives, with transverse gradients. Independent symbolic identities and direct small-field ranks corroborate rather than prove geometric assertions.

## originality

PASS

The same normalized C6 hyperelliptic family and general Cartier computation were already studied by Kudo–Nakagawa–Takagi, but their principal published theorems enumerate superspecial models (not the 5-rank 0–3 strata in characteristic five). The rank-drop intersection and geometric statements are not implied by their stated p≥7 superspecial classifications. Older a-number results could cover that auxiliary component; exact p-rank geometry is best-knowledge original.

## value

PASS

A complete stratification by p-rank and a-number of a natural genus-four automorphism family, with a unique transverse rank-zero specialization and geometrically irreducible rank-drop curves, gives actual moduli-slice geometry rather than a small unmotivated finite experiment.

The dated certificate retains the supplied scientific assessment, sources and limitations.
