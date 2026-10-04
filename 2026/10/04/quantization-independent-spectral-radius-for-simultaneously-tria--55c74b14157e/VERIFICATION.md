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
# Verification

The similarity characterization was converted to the exact formula \(\rho_{\mathcal E}(X)=\inf_S\|S^{-1}XS\|\) using homogeneity and the ordinary inequality between spectral radius and norm.

For an upper-triangular tuple, conjugation by \(D_t=\operatorname{diag}(1,t,\ldots,t^{n-1})\) multiplies entry \((i,j)\) by \(t^{j-i}\). Thus the tuple converges in matrix norm to its block diagonal as \(t\downarrow0\); Ruan's direct-sum axiom gives exactly the maximum of the level-one norms of the diagonal tuples.

For the reverse inequality, for each diagonal tuple a norming functional was chosen. Scalar-valued operator-space functionals have completely bounded norm equal to their Banach norm, so matrix amplification is contractive. The amplified scalar matrix is similar to an upper-triangular matrix with the norming value on its diagonal, hence its operator norm is at least that value. This proves the lower bound uniformly over all similarities.

Lie's theorem was applied only in finite-dimensional complex matrix form. No computation or finite enumeration is used as proof. The verification does not cover infinite-dimensional triangularizable families, the minimal spectral radius, or a converse from non-solvability to quantization dependence.
