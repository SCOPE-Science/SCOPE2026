---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-26.md",
      "INDEPENDENT_AUDIT_2026-11-26.json"
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

The positive-diagonal thin QR gives RᵀR=ZᵀZ and W is an isometry, so the reconstructed basis has norm 1/σ_min(Z); its Frobenius norm is between that norm and √m times it. After diagonalizing BᵀB, the Gaussian bottom-row covariance is (I−BᵀB)/ℓ, so the null-block columns form an iid ℓ-by-k matrix G independent of the remaining Gaussian columns U. For k>0, testing vectors supported on ker B gives σ_min(Z)≤σ_min(G). If r>0 the top block with smallest positive singular value η bounds the anchored part of a vector by η^{-1} times its image norm. Solving the bottom block with the pseudoinverse of G then gives the reverse inverse bound σ_min(Z)^{-1}≤η^{-1}+(1+‖U‖/η)σ_min(G)^{-1}. For r=0 there is equality. Independence and Gaussian moments make the two inverse norms equivalent for moment existence. In Gaussian QR the reciprocal last diagonal has a divergent p-moment precisely for p≥ℓ−k+1. Conversely each inverse triangular entry is a finite sum of products of independent Gaussian entries and reciprocals of distinct chi diagonals; all p-moments exist below that threshold. The Gram norm lies between ‖Q‖²−1 and ‖Q‖²+1, yielding the doubled-order criterion including its endpoint. Full anchoring instead gives the deterministic lower bound σ_min(B). At ℓ=m+1, the stated rank-zero versus rank-one mean-defect example follows directly. A common Gaussian coupling along B tending to zero and Fatou explain why a finite mean may grow without bound despite rank one.

## originality

PASS

The supported distinct result is rank-sensitive inverse-moment integrability for the reconstructed basis of the partially anchored sketch. The construction, the classical unanchored exponent, and Gaussian QR/Wishart laws are not original here. The checked related reconstruction and Krylov laws exhibit the same source of heavy tails but do not classify the effect of a deterministic top block on this basis and its Euclidean Gram defect.

## value

PASS

This classifies a natural conditioning diagnostic for a specific basis construction. In particular, adding one arbitrarily weak but nonzero anchored direction changes whether the mean Gram defect exists in minimal oversampling, although it need not make conditioning typical or the finite mean small. That qualitative rank transition is not answered by an embedding probability bound.

The dated certificate retains the supplied scientific assessment, sources and limitations.
