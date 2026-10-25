---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-19.md",
      "INDEPENDENT_AUDIT_2026-10-19.json"
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

For finite n≥1 and a real hereditary facet family containing every singleton, reconstructed the full proof for norm max_F(∑_{i∈F}x_i²)^{1/2}. Each facet quadratic q_F is the strict unique maximum near 1_F; the finite polynomial-zero-set argument forces any onto linear isometry U to bijectively conjugate the facet quadratic forms, UᵀD_GU=D_F. Summing matched facet projections yields invertible positive diagonal R_F,R_G and orthogonal Q=R_G^{1/2} U R_F^{-1/2}. Conjugated diagonal incidence operators have joint eigenspaces precisely the twin coordinate blocks (identical incidence in every maximal facet), with equal positive degree and block dimensions under Q. The R factors cancel on corresponding blocks, showing U is Euclidean orthogonal, and induces a facet-preserving coordinate permutation between families followed by independent O(|B|) maps within target twin blocks. Weighted quotient hypergraph automorphisms split by coordinate permutation matrices, giving (∏_B O(|B|)) ⋊ Aut(weighted facet-quotient), identity component ∏SO(|B|), and dimension ∑_B |B|(|B|−1)/2. Checked n=1 and one-facet ℓ₂ⁿ boundaries and the {1,2,3}/{1,2,4} example; real rather than complex, onto linear rather than into-isometries. Finite exact rational sample checks in source corroborate only small cases and are not the proof.

## originality

PASS

Best-of-knowledge PASS only for the explicit complete *real finite quadratic* group classification and between-family criterion, not the already-known criterion for complete signed-permutation rigidity. Fakhoury arXiv:2305.13125 Proposition 4.1 and remark credit Brech–Tcaciuc with exactly the singleton-twin test for when rotations do not occur. Example 1.2 shows a 2D rotating twin block. The present result classifies every nontrivial block, the semidirect product, and all between-family maps. General Kalton–Wood Hilbert-component machinery is powerful and could yield an alternative proof; the missing original Brech–Tcaciuc 'Notes on isometries of X_F^p' and possible general Hilbert-component full classification remain meaningful novelty risks.

## value

PASS

For quadratic combinatorial norms, the non-signed-permutation case is a structurally natural exception to a major existing p≠2 rigidity theorem. Identifying the precise continuous O(|B|) blocks and weighted quotient action, including between-family isometry classification and Lie dimension, is a meaningful closed classification that resolves actual functional-analytic geometry rather than renaming the rigid case. Its motivation precedes the proof; value does not rely on a broad infinite-dimensional theorem.

The dated certificate retains the supplied scientific assessment, sources and limitations.
