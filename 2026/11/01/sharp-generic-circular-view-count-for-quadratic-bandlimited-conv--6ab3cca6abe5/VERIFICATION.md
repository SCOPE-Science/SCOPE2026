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

# Verification of the stated theorem

The proof of the all-dimensional result uses exact linear-algebraic identities, not numerical extrapolation. Every planar restriction of a quadratic support has two observable second angular Fourier coefficients. The critical separation step is the explicitly calculated nonzero determinant of the two restrictions on the plane spanned by \((e_i+e_j)/\sqrt2\) and \((e_i-e_j+2e_k)/\sqrt6\), whenever the joint eigenvalue points \((a_i,b_i)\), \((a_j,b_j)\), \((a_k,b_k)\) are noncollinear. This follows after eigenvector compression forces simultaneous diagonalization under the hypothetical universal rank defect. The induction therefore lowers any remaining kernel by two dimensions per plane, except its last one-dimensional stage.

The attached checker is executable with the Python standard library: `python verify_quadratic_views.py`. It uses integer-coordinate pairs of linearly independent spanning vectors for each plane. For each tracefree matrix basis element, it computes the two rational-linear compression conditions in exact integers and performs Gaussian elimination in the finite field modulo \(1000003\). A full field rank is a certificate of full rational rank of this particular sample. A deterministic seed gives full ranks in dimensions \(3\) through \(12\); these are diagnostic finite certificates only.

For the lower bound, if the view count is less than the ceiling of half the traceless-symmetric dimension, a nonzero tracefree matrix annihilates every observed second harmonic. The spherical support-curvature matrix of \(1+\varepsilon u^{\mathsf T}Qu\) has smallest eigenvalue at least \(1-3|\varepsilon|\|Q\|_{\mathrm{op}}\), giving a smooth strictly convex nonball witness for sufficiently small nonzero \(\varepsilon\).

Limitations: no computer test proves the all-dimensional quantifier, the generic set need not contain every tuple, and the claimed count does not apply to unbounded harmonic bandwidth. Historical priority has not been independently certified.
