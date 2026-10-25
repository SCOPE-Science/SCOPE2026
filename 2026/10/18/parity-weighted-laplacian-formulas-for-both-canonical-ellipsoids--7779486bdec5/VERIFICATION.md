---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-22.md",
      "INDEPENDENT_AUDIT_2026-10-22.json"
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

Incidence edge space of a cactus has exactly one disjoint support relation per cycle, so its P_G=conv±b_e is a linear image of the free sum of each centered cycle-vertex configuration u_i=e_i−1/ℓ and independent bridge segments. Polar is product Q_ℓ={y∈Hℓ:|y_i|≤1}×bridge intervals. Every Qℓ vertex has norm² kℓ=ℓ for even ℓ, or ℓ−1 for odd ℓ; the exact facet count follows. Symmetry and uniqueness force block-scalar extremal shapes. John determinant optimization under single budget Σkℓ aℓ+Σt_bridge≤1 yields aℓ=(ℓ−1)/(d kℓ), t=1/d, transporting to Σ_J weighted Laplacian. Löwner independent outer-vertex constraints yield aℓ=(ℓ−1)/ℓ, t=1, transporting to Σ_L. All polar vertices attain John support equality; all signed generating edge roots meet Löwner boundary, and strict convexity excludes other points. Block determinant ratio gives d^{d/2}∏(kℓ/ℓ)^((ℓ−1)/2); matching block ratios gives precise homothety classification. Weighted matrix-tree identity gives individual volumes. Finite 61-cactus checker explicitly confirms 26,006 facet contacts and 998 signed vertex contacts; it cannot prove all cacti. Proof valid even single-bridge graph and multiple articulation cycles.

## originality

PASS

Known symmetric edge polytope regular-matroid/facet structural results and general John–Löwner theorem supply ingredients but not the explicit paired ellipsoid matrices, universal all-contact property and mixed odd/even cactus homothety dichotomy. A related published *cographic* complete-graph orthogonal cycle-space John/Löwner result uses a distinct polytope realization and does not imply this *graphic* cactus incidence result. Facet count is not claimed as new; best-of-knowledge ellipsoid novelty subject to more general optimal-design formulations.

## value

PASS

Two canonical extremal ellipsoids are natural geometric invariants of all connected cactus graph root polytopes. Closed Laplacian coefficients, absolute/relative volumes, contacts and an exact homothety classification detect parity, bridge structure, and odd cycle lengths, allowing structural computation without exponentially enumerating faces. This is a complete natural family classification beyond a textbook bound.

The dated certificate retains the supplied scientific assessment, sources and limitations.
