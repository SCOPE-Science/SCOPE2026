---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-27.md",
      "INDEPENDENT_AUDIT_2026-10-27.json"
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

For all integer n≥5 and r≥1, the graph is connected, has nr vertices, nr² oriented edges and degree 2r. The Laplacian splitting L=rL_n⊗P+2r I⊗P^⊥ and its pseudoinverse on the orthogonal constant-fiber/mean-zero-fiber decomposition are exact. A unit source edge at layers 0→1 induces base-cycle gradient (n−1)/n at the source boundary and −1/n elsewhere; subtracting its full potential yields the complete signed current table. Its eight disjoint conditions exhaust all nr² edges (including multiplicity-zero classes at r=1); the signs are fixed over n≥5, r≥1, so absolute summation is legitimate. Edge-transitivity gives common column sum and symmetry transfers ℓ1 to ℓ∞; Q_ee=1/r−1/(nr²) gives the complement norm 1+||Q e||_1−2Q_ee. Hence exact norms are Q=4−2/r−4/n+2/(nr²) and C=5−4/r−4/n+4/(nr²), difference 1−2/r+2/(nr²). At r=1 the difference −1+2/n<0, for r=2 it is 1/(2n)>0, and for all r≥2 positive. The uniform upper 4 and 5 bounds are strict and sharp as n,r→∞. Independently constructed grounded exact-rational Laplacian inverses verified full Q matrices, all column norms and BQ=B on n,r=(5,1),(5,2),(6,2),(5,3), totaling 94 columns, and a separate rational transfer-current evaluation checked six parameter pairs totaling 154 columns. These finite tests are corroboration only; the all-parameter proof follows from explicit symbolic decomposition.

## originality

PASS

Best-of-knowledge original specifically as the fully evaluated exact canonical cut/cycle ℓ1/ℓ∞ norms and signed current classes for the infinite cyclic independent-fiber family. Prior general H-join Laplacian (2018) and resistance (2025 abstracts) calculations supply or may supply ingredients, and the complement difference/Foster cutoff is elementary once diagonal resistance is known. No inspected prior paper states or demonstrably implies the complete sharp absolute-sum evaluation without doing the new signed class analysis. Significant risk remains because 2025 general resistance full texts were unavailable. The claim is not presented as new general pseudoinverse theory.

## value

PASS

The vertex-independent blowup of a cycle is a standard natural graph substitution, while the canonical Euclidean cut/circulation projections have intrinsic ℓ1/ℓ∞ Banach-space operator norms. A two-parameter exact evaluation and complete eight-class signed current profile supply a reusable reference family distinct from Cartesian Hamming products, with a sharp parity-independent reversal in cut/cycle norm ordering already at minimal nontrivial fiber width and optimal asymptotic upper constants. Though the scalar difference follows from Foster and symmetry, the absolute norm requires nontrivial local sign classification; this is a motivated exact invariant, not an arbitrary tiny graph census. No claim about all projections or intermediate p.

The dated certificate retains the supplied scientific assessment, sources and limitations.
